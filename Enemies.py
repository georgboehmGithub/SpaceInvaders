import globalVariables as gV
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.objType = "Enemy"
        self.position = [50,30]
        self.movementSpeed = 4
        self.image = pg.image.load('images/enemy.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.rect = self.rect.move(self.movementSpeed, 0)
        if self.rect.left < 0:
            self.movementSpeed = self.movementSpeed * -1
            self.rect = self.rect.move(0, self.image.get_height())
        if self.rect.right > gV.WindowSize[0]:
            self.movementSpeed = self.movementSpeed * -1
            self.rect = self.rect.move(0, self.image.get_height())