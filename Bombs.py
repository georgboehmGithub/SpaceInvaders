import globalVariables as gV
import pygame as pg

class Bomb(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.objType = "Bomb"
        self.movementSpeed = 2
        self.image = pg.image.load('images/bomb.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]

    def update(self):
        if self.rect.top > gV.WindowSize[0]:
            self.kill()
        self.rect = self.rect.move(0, self.movementSpeed)
        collided = pg.sprite.spritecollide(self, gV.PLAYERS, dokill=False)
        if len(collided) > 0:
            gV.gameRunning = False