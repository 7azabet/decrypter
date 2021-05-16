#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]  # that means user is NOT has root privileges.
  then
    echo "Please run as root"
  exit
fi
echo -e "\e[32mWelcome r00t!\e[0m"

sudo mv hashd mymodule.py /usr/local/bin
sudo mkdir /usr/share/hashd
sudo mv banner db.txt /usr/share/hashd
sudo chmod 777 /usr/share/hashd

echo -e "\e[32m\nhashd installed successfully\ntype 'hashd' in your terminal.\e[0m"





