import pygame
import globalVariables as gV
class Background(pygame.sprite.Sprite):
    def __init__(self, number, *args):
        self.image = pygame.image.load("images/back.jpg").convert()
        self.image = pygame.transform.scale(self.image,gV.WindowSize)   # background adapts to different window sizes
        self._layer = -10
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self, *args)
        self.pix_moved = 0
        self.number = number
        self.rect.bottomleft = (0,self.rect.height * number)

    def update(self):
        if self.pix_moved >= self.rect.height:
            self.rect.bottomleft = (0,self.rect.height * self.number)
            self.pix_moved = 0
        else:
            self.rect.move_ip(0,1)
            self.pix_moved += 1