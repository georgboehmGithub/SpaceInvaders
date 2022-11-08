import pygame
import globalVariables as gV
from Weapon import Weapon
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.weapon = Weapon()
        self.image = pygame.image.load('images/player.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.position = [gV.WindowSize[0] / 2, gV.WindowSize[1] - self.size[1]]
        self.objType = "Player"
        self.movementSpeed = 0
        self.image = pygame.image.load('images/player.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.rect = self.rect.move(self.movementSpeed, 0)
        collided = pg.sprite.spritecollide(self, gV.MOBS, dokill=False)
        if len(collided) > 0:
            gV.gameRunning = False
        # Window boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= gV.WindowSize[0]:
            self.rect.right = gV.WindowSize[0]

    # TODO: Interaction between player and items collected
    # TODO: Change weapon value and check per press of spacebar what the ammunition is and update accordingly
    def itemCollect(self, itemId: int):
        self.weapon.active = "Advanced"

