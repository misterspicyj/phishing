# Evilginx2 Automated Setup Script

This Python script automates downloading, extracting, and configuring [Evilginx2](https://github.com/kgretzky/evilginx2) with a custom WordPress phishlet.

---

## Features

- Automatically fetches the latest Evilginx2 Linux 64-bit release from GitHub
- Downloads and extracts the Evilginx2 binary
- Creates a WordPress phishlet YAML configuration file based on user input
- Launches Evilginx2 and configures it with your domain, IP, and phishlet
- Creates a lure and outputs the phishing URL for immediate use

---

## Phishlet Template

The current phishlet template is tailored specifically for WordPress hosts, targeting typical WordPress login flows and cookies. However, the YAML content can be easily modified to support other login pages or platforms by adjusting the domains, credential keys, and URL paths in the script. You have full control to customize this as needed.

---

## Inspiration

This script and phishlet design were inspired by a course from Tyler — check out his work at [https://github.com/TeneBrae93](https://github.com/TeneBrae93).

---

## Requirements

- Python 3.6+
- `requests` library (`pip install requests`)
- `pexpect` library (`pip install pexpect`)
- Linux environment with `wget` and `unzip` installed
- Executable permissions to run the `evilginx` binary

---

## Usage

1. Clone or download this script to your Linux machine.

2. Run the script:

   ```bash
   python3 evilginx_setup.py
