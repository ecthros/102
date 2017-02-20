#!/bin/bash
sudo apt update
sudo apt-get install python-pip python-dev libssl-dev libffi-dev curl

sudo -H pip install --upgrade pyopenssl
sudo -H pip install --upgrade oauth2client
sudo -H pip install --upgrade gspread
sudo -H pip install --upgrade dateutils
sudo -H pip install oauth2client==1.5.2

sudo mkdir /logging
sudo touch /logging/log.txt
sudo chmod 777 /logging/log.txt


sudo cp log.py /bin/log

