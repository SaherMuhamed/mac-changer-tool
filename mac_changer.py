#!/usr/bin/python3

import re
import subprocess
from optparse import OptionParser


def get_argument():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Specify an interface to change its MAC. Example: --interface wlan0")
    parser.add_option("-m", "--mac", dest="mac_address",
                      help="enter a new MAC Address to your NAT interface. Example: --mac 70:00:00:00:00:08")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify your NAT card, or type it correctly, ex: --interface wlan0")
    elif not options.mac_address:
        parser.error("[-] Please enter your new MAC Address, or type it correctly, ex: --mac 70:00:00:00:00:08")
    return options


def change_mac(interface, new_mac):
    # subprocess.call(f"ifconfig {interface} down", shell=True)
    # subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    # subprocess.call(f"ifconfig {interface} up", shell=True)

    # TODO: These 3 commands are a much more secure version of the 3 command above.
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(f"[+] Changing MAC Address for {interface} to {new_mac}\n")


def get_current_mac(interface):
    ifconfig_command_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_command_result.decode("UTF-8"))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Couldn't find MAC address, try another NAT card.\n")


option = get_argument()

current_mac = get_current_mac(option.interface)
print(f"[+] Current MAC: {current_mac}")

change_mac(interface=option.interface, new_mac=option.mac_address)

current_mac = get_current_mac(option.interface)
if current_mac == option.mac_address:
    print(f"[+] MAC Address was successfully changed to {current_mac}\n")
else:
    print("[-] Couldn't change MAC Address\n")
