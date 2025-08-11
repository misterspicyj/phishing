import os
import subprocess
import requests
import json

def get_latest_gopish_release():
    print("[+] Downloading the latest GoPhish instance...")
    url = "https://api.github.com/repos/gophish/gophish/releases/latest"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    for asset in data['assets']:
        if "linux" in asset['name'] and asset['name'].endswith("linux-64bit.zip"):
            return asset['browser_download_url'], asset['name']
    raise Exception("No suitable GoPhish release found.")

def cert_bot_setup(domain):
    print("[+] Setting up Let's Encrypt with Certbot...")
    subprocess.run(["sudo", "apt-get", "install", "-y", "certbot"], check=True)
    subprocess.run(["sudo", "certbot", "certonly", "-d", domain, "--manual", "--preferred-challenges", "dns", "--register-unsafely-without-email"])
    dns_changed = input("[+] Did you change your DNS records? (yes/no): ").strip().lower()
    if dns_changed != 'yes':
        print("Please change your DNS records and run this script again.")
        exit(1)

def install_gophish():
    print("[+] Installing GoPhish...")
    os.makedirs("gophish", exist_ok=True)
    os.chdir("gophish")

    subprocess.run(["wget", get_latest_gopish_release()[0], "-O", "gophish.zip"], check=True)
    subprocess.run(["unzip", "-o", "gophish.zip"], check=True)
    subprocess.run(["chmod", "+x", "gophish"], check=True)

def configure_gophish(domain):
    print("[+] Configuring Gophish...")

    cert_path = f"/etc/letsencrypt/live/{domain}/fullchain.pem"
    key_path = f"/etc/letsencrypt/live/{domain}/privkey.pem"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    gophish_dir = os.path.join(script_dir, "gophish")
    config_path = os.path.join(gophish_dir, "config.json")

    with open(config_path, 'r') as f:
        config = json.load(f)

    config["admin_server"]["listen_url"] = "0.0.0.0:3333"
    config["admin_server"]["use_tls"] = True
    config["admin_server"]["cert_path"] = cert_path
    config["admin_server"]["key_path"] = key_path

    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)

    print(f"[+] Updated config.json at {config_path}")

def main():
    # Prompt user for config
    domain = input("Enter your domain (e.g. example.com): ").strip()

    install_gophish()
    cert_bot_setup(domain)
    configure_gophish(domain)

    print("[+] GoPhish installation and configuration complete.")
    print("[+] Starting GoPhish...")

    subprocess.run(["pwd"])
    subprocess.run(["./gophish"])

    print(f"[+] GoPhish is now running. Access the admin interface at https://{domain}:3333")

if __name__ == "__main__":
    main()