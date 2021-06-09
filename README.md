# Raspberry pi 4 cooler controll

**GPIO OUTPUT 21**\
**On Off controll**\
**( When hit 65°c temperature => Fan ON if(Fan OFF))**\
**( When hit 50°c temperature => Fan OFF if(Fan ON))**\

## Run script

1. cd $HOME && git clone https://github.com/TadasBruzas91/rpi-cooler-script.git && cd rpi-cooler-script && bash ./install-cooler-service.sh

## OR Instal Manualy

## Install tested on Ubuntu server 20.04

1. sudo apt install swig python3 python3-pip python-dev python3-dev

2. sudo apt install python-setuptools python3-setuptools

3. sudo apt install wget

4. wget https://github.com/joan2937/lg/archive/master.zip

5. sudo apt install unzip

6. unzip master.zip

7. cd lg-master

8. sudo apt install make

9. sudo apt install gcc

10. make

11. sudo make install

12. cd ..

13. sudo rm -rf master.zip && sudo rm -rf lg-master

14. sudo apt install git

15. git clone https://github.com/TadasBruzas91/rpi-cooler-script.git

16. cd rpi-cooler-script

17. sudo apt-get install -y systemd

18. sudo mkdir ~/services && sudo mv cooler.py ~/services

19. sudo mv cooler.service /etc/systemd/system

20. sudo systemctl daemon-reload

21. sudo systemctl enable cooler.service

22. sudo systemctl start cooler.service

23. sudo systemctl status cooler.service

    <-------------systemctl status output--------------------->

    cooler.service - Fan controller
    Loaded: loaded (/etc/systemd/system/cooler.service; enabled; vendor preset: enabled)
    Active: active (running) since Sun 2021-05-30 08:23:45 UTC; 1 weeks 2 days ago
    Main PID: 1927 (python3)
    Tasks: 4 (limit: 4435)
    CGroup: /system.slice/cooler.service
    └─1927 /usr/bin/python3 /home/documents/script/cooler.py

    May 30 08:23:45 ubuntu systemd[1]: Started Fan controller.

    <--------------------------------------------------------->
