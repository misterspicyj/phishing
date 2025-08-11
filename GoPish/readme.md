# GoPhish Auto-Deploy Script

Automates downloading, installing, configuring, and running [GoPhish](https://getgophish.com/) on a Linux server.

---

## Disclaimer

This script is intended for educational and authorized use only.  
**Do NOT use this tool for any malicious or illegal activities.**  
The author is not responsible for any misuse or damage caused by this script.  
Always ensure you have explicit permission before deploying or testing GoPhish or any phishing frameworks on any network or domain.  
Use at your own risk.

---

## Features

- Downloads latest GoPhish Linux 64-bit release automatically  
- Installs GoPhish into a subfolder `gophish` in the current directory  
- Configures TLS certificates using Let's Encrypt via Certbot with manual DNS verification  
- Updates GoPhish `config.json` to enable TLS and listen on all interfaces on port 3333  
- Starts GoPhish with the configured settings  

---

## Requirements

- Linux (tested on Ubuntu/Debian)  
- Python 3.x  
- `wget`, `unzip`, `certbot`, `chmod` commands available  
- Internet access to download GoPhish and interact with LetsEncrypt  

---

## Usage

1. Clone or download this script to your desired folder  
2. Run the script as root or with sudo:  
   ```bash
   sudo python3 gophish_autodeploy.py
3. Enter your domain name when prompted (e.g. example.com)
4. Follow the Certbot instructions to add DNS TXT records for your domain
5. Confirm DNS changes when ready
6. The script will finish configuration and start GoPhish
7. Access the GoPhish admin panel at: `https://<your-domain>:3333`

---

## Notes

- Make sure your DNS is properly configured to allow Certbot DNS verification
- The script uses manual DNS verification, so you need to add TXT records yourself
- GoPhish listens on port 3333 by default — ensure it is open in your firewall
- The script must be run with permissions to install software and write to /etc/letsencrypt

---

## Inspiration

This project was inspired by the **Hands-On Phishing** course by Tyler Ramsbey on Simply Cyber Academy. The course provides practical training on setting up phishing campaigns using tools like GoPhish and Evilginx2. For more information, visit the course page: [Hands-On Phishing](https://academy.simplycyber.io/p/hands-on-phishing).

---

## Troubleshooting
- If certbot is not found, install it manually:
  ```bash
  sudo apt-get install certbot
- If you get permission errors, ensure you run the script with sudo or as root
- Check config.json inside the gophish folder for manual adjustments if needed