#!/bin/bash
sudo apt-get update 
sudo apt-get install python3 python3-pip idle3 git 
pip3 install numpy 
pip3 install pygame 

cd ./source && python3 main.py 
exit;
