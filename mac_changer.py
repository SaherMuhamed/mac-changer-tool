import subprocess
from optparse import OptionParser


def change_mac(interface_name, new_mac_address):
    # TODO: Secure version of mac changer.
    subprocess.call(["ifconfig", interface_name, "down"])
    subprocess.call(["ifconfig", interface_name, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface_name, "up"])
    print("")

    # TODO: Non-secure version of mac changer.
    # subprocess.call(f"ifconfig {interface_name} down", shell=True)
    # subprocess.call(f"ifconfig {interface_name} hw ether {new_mac_address}", shell=True)
    # subprocess.call(f"ifconfig {interface_name} up", shell=True)
    print(f"[+] Mac Address Successfully Changed to {new_mac_address} :-)\n")


def get_argument():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    # print(parser.parse_args())
    # interface_name = input("[+] Please, specify your interface name: ")
    # new_mac_address = input("[+] Please, enter a new Mac address: ")
    (option, argument) = parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not option.new_mac:
        parser.error("[-] Please specify a new Mac address, use --help for more info")
    else:
        return option


option = get_argument()
change_mac(option.interface, option.new_mac)
