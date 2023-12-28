#!/usr/bin/env python3

import re
import sys
import subprocess
from optparse import OptionParser

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write(
        "Please update and make sure you use the command python3 mac_changer.py -i <interface> -m <mac>\n\n")
    sys.exit(0)


def args():
    parser = OptionParser(description="------- Tool for Changing MAC Address of Any Network Adapter -------")
    parser.add_option("-i", "--interface", dest="interface", help="Specify an interface to change its MAC. Example: "
                                                                  "--interface wlan0")
    parser.add_option("-m", "--mac", dest="mac_address", help="Enter a new MAC Address to your NAT interface. Example: "
                                                              "--mac 70:00:00:00:00:08")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(msg="[-] Please specify your NAT card, or type it correctly, ex: --interface wlan0")
    elif not options.mac_address:
        parser.error(msg="[-] Please enter your new MAC Address, or type it correctly, ex: --mac 70:00:00:00:00:08")
    return options


def get_ethtool_mac(interface):
    try:
        # run the ethtool command and capture the output
        result = subprocess.check_output(["ethtool", "-P", interface], stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        # handle the case where the command returns a non-zero exit code
        return f"Error: {e.output.strip()}"
    

def change_mac(iface, mac):
    print("[+] Changing MAC address for " + iface + " to " + mac)
    # subprocess.call("ifconfig " + iface + " down", shell=True)
    # subprocess.call("ifconfig " + iface + " hw ether " + mac, shell=True)
    # subprocess.call("ifconfig " + iface + " up", shell=True)

    # these 3 commands are much more secure version than above to prevent the misuse of the tool
    subprocess.call(["ifconfig", iface, "down"])  # execute the command in foreground
    subprocess.call(["ifconfig", iface, "hw", "ether", mac])
    subprocess.call(["ifconfig", iface, "up"])


def search_mac_regex(iface):
    ifconfig_result = subprocess.check_output(["ifconfig", iface])  # execute the command and return the output in bytes
    mac_address_search_result = re.search(pattern=r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", string=str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Couldn't find MAC address, try another NAT card.\n")


try:
    option = args()
    current_mac_before = search_mac_regex(iface=option.interface)
    print("\n[+] " + get_ethtool_mac(interface=option.interface))
    print("[+] Current MAC: " + str(current_mac_before))

    change_mac(iface=option.interface, mac=option.mac_address)
    current_mac_after = search_mac_regex(iface=option.interface)
    if current_mac_after == option.mac_address:
        print("[+] MAC address was successfully changed to " + current_mac_after + "\n")
except subprocess.CalledProcessError:
    sys.stderr.write("[-] Couldn't find " + option.interface + ", try another NAT card.\n")
