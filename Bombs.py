import globalVariables as gV
import pygame as pg

class Bomb(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.objType = "Bomb"
        self.position = [0, 0]
        self.movementSpeed = 2
        self.image = pg.image.load('images/bomb.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.rect = self.rect.move(0, self.movementSpeed)
        collided = pg.sprite.spritecollide(self, gV.PLAYERS, dokill=False)
        if len(collided) > 0:
            gV.gameRunning = False