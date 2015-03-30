#!/bin/bash

clear

gnome-terminal --title="INSTALL" -x sh -c "sudo apt-get install python-scapy tcpdump isc-dhcp-server hostapd"

gnome-terminal --title="INSTALL" -x sh -c "cd ~/ && git clone https://github.com/sophron/wifiphisher.git"

clear

INDONE=$(zenity --info --title="INSTALL" --text="Installation Complete!")

clear
