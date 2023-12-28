# MAC Address Changer

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)  ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

This script allows you to change the MAC address of a specified network interface on your system providing a secure way to modify the MAC address. It is written in Python and uses the subprocess module to interact with the operating system's command-line interface.

## Prerequisites
- Python 3.x

## Usage
- To use this script, follow these steps:

  1. Open a terminal or command prompt.
  2. Run the script using the following command:
    ```commandline
    python3 mac_changer.py -i interface -m new_mac_address
  ```
    Replace <interface> with the name of the network interface you want to modify (e.g., wlan0) and <new_mac_address> with the desired MAC address you want to set (e.g., 70:00:00:00:00:08).

## Options
The script supports the following command-line options:

- `-i`, `--interface`: Specifies the network interface to change its MAC address. This option is mandatory.
- `-m`, `--mac`: Specifies the new MAC address to assign to the network interface. This option is mandatory.

## Example
To change the MAC address of the interface `wlan0` to `70:00:00:00:00:08`, run the following command:
```commandline
python3 mac_changer.py -i wlan0 -m 70:00:00:00:00:08
```

## Screenshot
![](https://github.com/SaherMuhamed/mac-changer-tool/blob/master/screenshots/Screenshot%202023-12-28%20021841.png)

## Notes
- This script uses the `subprocess` module to execute shell commands. Make sure to run it with appropriate permissions or as an administrator, depending on your operating system and network configuration.
- Changing the MAC address of a network interface may have legal and ethical implications. Ensure that you have proper authorization and adhere to applicable laws and regulations.
- This script is provided as-is without any warranty. Use it at your own risk.

### Updates
`v1.0.1 - 28/12/2023` adding ethtool command to fetch permanent MAC of network card
