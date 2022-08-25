import subprocess
from optparse import OptionParser
import re


def change_mac(interface_name, new_mac_address):
    # TODO: Secure version of mac changer.
    subprocess.call(["ifconfig", interface_name, "down"])
    subprocess.call(["ifconfig", interface_name, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface_name, "up"])

    # TODO: Non-secure version of mac changer.
    # subprocess.call(f"ifconfig {interface_name} down", shell=True)
    # subprocess.call(f"ifconfig {interface_name} hw ether {new_mac_address}", shell=True)
    # subprocess.call(f"ifconfig {interface_name} up", shell=True)
    # print(f"[+] Mac Address Successfully Changed to {new_mac_address} :-)\n")


def get_argument():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    # print(parser.parse_args())
    # interface_name = input("[+] Please, specify your interface name: ")
    # new_mac_address = input("[+] Please, enter a new Mac address: ")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("Please specify a new Mac address, use --help for more info")
    else:
        return options


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # print(ifconfig_result)
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address:
        return mac_address.group(0)
    else:
        print("[*] Could not find Mac address")


option = get_argument()
current_mac_address = get_current_mac(option.interface)
print("")
print(f"[+] Current Mac Address: {current_mac_address}")
change_mac(option.interface, option.new_mac)
current_mac_address = get_current_mac(option.interface)
if current_mac_address == option.new_mac:
    print(f"[+] Mac address successfully changed to {current_mac_address} :-)")
    print("")
else:
    print("[*] Sorry, could not change Mac address, try again")
    print("")
