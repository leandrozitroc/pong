import pygame
yellow = (255,190,0)
blue= (255,190,210)

class Paddle(pygame.sprite.Sprite):
    speed = 0

    def __init__(self, color, width, height):

       pygame.sprite.Sprite.__init__(self)


       self.image = pygame.Surface([width, height])
       self.image.fill(color)


       self.rect = self.image.get_rect()

    def moveup(self, speed):
        self.rect.y -= speed
        if self.rect.y < 0 :
            self.rect.y = 0

    def movedown(self, speed):
        self.rect.y += speed
        if self.rect.y > 300:
            self.rect.y = 300