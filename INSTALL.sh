#!/bin/bash

clear

chmod +x ~/diamond/diamond
chmod +x ~/diamond/*.sh
chmod +x ~/diamond/*.py

DPASS=$(zenity --password --title="Authenticate to Install..") && echo $DPASS | sudo -S chmod 755 ~/diamond/diamond && echo $DPASS | sudo -S cp ~/diamond/diamond /usr/local/bin/diamond && zenity --info --title="Diamond Code Translater" --text="Install Complete! To use diamond code translater, open a new Terminal Window and type: diamond"

clear
