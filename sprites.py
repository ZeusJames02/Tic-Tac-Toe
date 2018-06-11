import pygame
from settings import *

# Class for x image
class X(pygame.sprite.Sprite):

    # It has x and y parameters
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(X_img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Class for y image
class O(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(O_img)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Class for the areas
class Area(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width/3, height/3))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
