# Evilginx Automated Setup Script

This Python script automates the process of downloading, extracting, and configuring Evilginx with a custom phishlet. It simplifies the setup for phishing campaigns by handling the technical details, allowing you to focus on crafting effective lures.

---

## Disclaimer

This script is intended for educational and authorized use only.  
**Do NOT use this tool for any malicious or illegal activities.**  
The author is not responsible for any misuse or damage caused by this script.
Use at your own risk.

---

## Features

- **Automated Download**: Fetches the latest Evilginx release for Linux (64-bit).
- **Phishlet Generation**: Creates a customizable phishlet template for WordPress login pages.
- **Interactive Configuration**: Prompts for user input to configure Evilginx settings.
- **Lure Creation**: Generates a lure and provides the URL for immediate use.

---

## Configuration Prompts

Upon execution, the script will ask for the following inputs:

1. **Phishlet Name**: A unique identifier for your phishlet (e.g., `hackingwithj`).
2. **Phishlet Domain**: The domain associated with the phishlet (e.g., `hackingwithj.com`).
3. **Your Domain**: The domain you control for hosting the phishing page (e.g., `hackingwithj.cam`).
4. **External IP Address**: Your public IP address (e.g., `146.190.237.243`).

These inputs are used to configure Evilginx automatically.

---

## Phishlet Template

The included phishlet template is designed for **WordPress login pages**, targeting cookies like `wordpress_sec_.*` and `wordpress_logged_in_.*`. To adapt it for other login pages:

- Modify the `auth_tokens` keys.
- Adjust the `auth_urls` to match the target login page.
- Update the `credentials` extraction rules.
- Change the `login` domain and path accordingly.

This flexibility allows the phishlet to be customized for various platforms.

---

## Inspiration

This project was inspired by the **Hands-On Phishing** course by Tyler Ramsbey on Simply Cyber Academy. The course provides practical training on setting up phishing campaigns using tools like GoPhish and Evilginx2. For more information, visit the course page: [Hands-On Phishing](https://academy.simplycyber.io/p/hands-on-phishing).

---

## Requirements

- Python 3.x
- `requests` and `pexpect` Python modules
- `wget` and `unzip` command-line tools
- Linux 64-bit system

---

## Usage

1. Clone or download this repository.
2. Run the script:

   ```bash
   python3 evilginx_setup.py
3. Follow the prompts to input the necessary configuration details.
4. Upon completion, the script will output the lure URL for immediate use.