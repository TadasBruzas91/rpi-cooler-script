#!/bin/bash
#!/usr/bin/bash

echo "Install Started"

sudo apt install swig python3 python3-pip python-dev python3-dev -y

sudo apt install python-setuptools python3-setuptools -y

wget https://github.com/joan2937/lg/archive/master.zip || sudo apt install wget -y

unzip master.zip || sudo apt install unzip -y

cd lg-master

sudo apt install make -y

sudo apt install gcc -y

make

sudo make install

cd ..

sudo rm -rf master.zip && sudo rm -rf lg-master

sudo apt-get install -y systemd

sudo mkdir /usr/services
 
sudo mv cooler.py /usr/services

sudo mv cooler.service /etc/systemd/system

sudo systemctl daemon-reload && echo "Daemon reloaded"

sleep 2 

sudo systemctl enable cooler.service && echo "Enabled cooler.service"

sleep 2

sudo systemctl start cooler.service && echo "Started cooler.service"

sleep 3

sudo systemctl status cooler.service 

echo "Install Done"