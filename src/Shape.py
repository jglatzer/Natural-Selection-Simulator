import pygame
import random

GREEN = (0,100,0)
BLACK = (0,0,0)
TAN = (210,210,210)
class Shape(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width=15, height=15):
        """This function is respnsible for initializing the aspect of the Shape class. It creates the sprites and sets the random location of the sprites on the screen.
Args: self, color, x and y values, width and height for the shape"""
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0,x-width)
        self.rect.y = random.randint(50,y-height)

    def update(self):
        """This function ensures that the dots will be randomly placed in new locations each round.
Args: self
Returns: N/A"""
        xChange = self.rect.x
        yChange = self.rect.y
        xChange = random.randrange(50,750,10)
        yChange = random.randrange(50,550,10)
