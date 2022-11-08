from Bombs import *
from Items import *
import pygame
import pygame as pg
from random import randint

class Missile(pg.sprite.Sprite):
    def __init__(self, damage, image, cooldown):
        pg.sprite.Sprite.__init__(self)
        self.objType = "Missile"
        self.position = [0,0]
        self.movementSpeed = 0
        self.image = pygame.image.load(image)
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.last = pygame.time.get_ticks()
        self.cooldown = cooldown
        self.damage = damage

    def update(self):
        if self.position[1] < 0:
            self.kill()
        self.rect = self.rect.move(0, self.movementSpeed)
        collided = pygame.sprite.spritecollide(self, gV.MOBS, dokill=True)
        if len(collided) > 0: # missile collided with an enemy
            self.kill()
            gV.hits += 1
            # Roll drop chance
            r = randint(0, 2)
            if r == 2:
                drop = Item(1)  # TODO: Add id to constructor, determines item dropped
            else:
                drop = Bomb()
            drop.rect.center = collided[0].rect.center
            gV.SPRITES.add(drop)