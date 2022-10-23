#!/bin/bash
sudo apt-get update 
sudo apt-get install python3 python3-pip idle3 git 
pip3 install numpy 
pip3 install pygame 

#import pygame
# pygame.init()
# pygame.display.list_modes()
# import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"
sudo apt-get install libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
sdl-config --cflags --libs
python config.py
python config.py
sudo python setup.py install
sudo python setup.py

cd ./source && python3 main.py 
exit;
