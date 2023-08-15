import pygame as py
from Object1 import Object 
py.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Physics Simulator")
running = True 

clock = py.time.Clock()


blue = (0, 0, 255)
filled_rect = Object(screen, blue, 100, 100, 100, 100, mass=50)

while running: 
    clock.tick(60)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    filled_rect.gravity()  
    if filled_rect.rect.bottom >= SCREEN_HEIGHT:
        filled_rect.rect.bottom = SCREEN_HEIGHT  

    screen.fill((255, 255, 255))
    filled_rect.draw()
    py.display.flip()

py.quit()
