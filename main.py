from Object1 import *
import pygame as py

py.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Physics Simulator")
running = True 

clock = py.time.Clock()

while running: 
    
    clock.tick(60)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill((255,255,255))
    py.display.flip()
    py.display.update()

py.QUIT()

