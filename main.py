import pygame as py 

py.init()
screen = py.display.set_mode((1280, 720))

running = True 

while running: 

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    py.display.flip()
    py.display.update()

py.QUIT()

