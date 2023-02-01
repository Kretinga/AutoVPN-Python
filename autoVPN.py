#!/usr/bin/python3
import os
from termcolor import colored

def intro():
    print(colored('''             _     __     ______  _   _ 
  __ _ _   _| |_ __\ \   / /  _ \| \ | |
 / _` | | | | __/ _ \ \ / /| |_) |  \| |
| (_| | |_| | || (_) \ V / |  __/| |\  |
 \__,_|\__,_|\__\___/ \_/  |_|   |_| \_| ''', 'blue'))

intro()
option = input("Choose the VPN:\n" ## If you like you can add more VPNs 
            "[1] - HackTheBox\n"
            "[2] - TryHackMe\n"
            "\n"
            ">> Choose VPN --> ")

if option == "1":
    os.system("openvpn /home/user/Download/") ## Change the route through your VPN route 
elif option == "2":
    os.system("openvpn /home/user/Download/") ## Change the route through your VPN route

else:
    print("[!] Select a valid option\n"
            "[+] Example: 1 or 2")
