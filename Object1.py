import pygame as py 

class Object(py.sprite.Sprite): 
    def __init__(self, screen, color, x, y, width, height, mass):
        super().__init__()
        self.image = py.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.mass = mass
        self.dy = 0  # Vertical velocity

    def gravity(self):
        gravity = 0.5  
        acceleration = gravity / self.mass  
        self.dy += acceleration
        self.rect.y += self.dy

    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)
