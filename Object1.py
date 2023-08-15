from main import *

class Object1(py.sprite.Sprite): 
    def __init__ (self, x, y):
        body = py.Rect(100,100,100,100)
        self.rect = self.body.get_rect()
        self.width = 50
        self.height = 50

    def draw(self):
        screen.blit()
