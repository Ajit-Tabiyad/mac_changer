#!usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("i", "--interface", dest="interface", help="Interface To change its MAC Address")
    parser.add_option("m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, Use --help fore more info.")

    elif not options.new_mac
        parser.error("[-]Please specify A new mac, Use --help fore more info.")
    return  options

def change_mac(interface, new_mac):
    print("[+]Changing MAC Address For" + interface + "To" + new_mac)

    subprocess.call("[ifconfig", interface, "down"])
    subprocess.call("[ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call("[ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)

