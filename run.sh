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

cd ./source && python3 main.py 
exit;
