#!/bin/bash
sudo apt update
sudo apt-get install python3-pip python3-dev libssl-dev libffi-dev curl

sudo -H pip3 install setuptools==33.1.1
sudo -H pip3 install pyopenssl
sudo -H pip3 install --upgrade oauth2client
sudo -H pip3 install --upgrade gspread
sudo -H pip3 install --upgrade dateutils
sudo -H pip3 install oauth2client==1.5.2

sudo mkdir /logging
sudo touch /logging/log.txt
sudo chmod 777 /logging/log.txt


sudo cp log.py /bin/log

