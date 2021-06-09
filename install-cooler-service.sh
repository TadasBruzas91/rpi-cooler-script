#!/bin/bash
#!/usr/bin/bash

echo "Install Started"

#Preparing install

sudo apt update

sudo apt upgrade

sudo apt install swig python3 python3-pip python-dev python3-dev

sudo apt install python-setuptools python3-setuptools

sudo apt install wget

sudo apt install make

sudo apt install gcc

sudo apt install unzip

sudo apt-get install systemd

wget https://github.com/joan2937/lg/archive/master.zip

unzip master.zip

cd lg-master && echo "Current dir => $(pwd)"

make

sudo make install

cd .. && echo "Current dir => $(pwd)"

rm -rf master.zip && sudo rm -rf lg-master && echo "Files deleted successfuly"

mkdir $HOME/services && echo "Created services dir"
 
mv cooler.py $HOME/services && echo "services dir => $(ls services)"

sudo chmod go-wx $HOME/services

printf "[Unit]\nDescription=Fan controller\nAfter=multi-user.target\n\n[Service]\nType=simple\nRestart=always\nExecStart=/usr/bin/python3 $(echo $HOME)/services/cooler.py\n\n[Install]\nWantedBy=multi-user.target\n" > cooler.service

sudo mv cooler.service /etc/systemd/system && echo "system dir => $(ls /etc/systemd/system | grep cooler)"

cd ..

rm -rf rpi-cooler-script && echo "Files deleted successfuly"

sudo systemctl daemon-reload && echo "Daemon reloaded"

sleep 2 

sudo systemctl enable cooler.service && echo "Enabled cooler.service"

sleep 2

sudo systemctl start cooler.service && echo "Started cooler.service"

sleep 3

sudo systemctl status cooler.service 

echo "Install Done"