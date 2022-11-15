from Items import *
import pygame
import pygame as pg
from random import randint

class Missile(pg.sprite.Sprite):
    def __init__(self, damage, image, cooldown, pos):
        pg.sprite.Sprite.__init__(self)
        self.objType = "Missile"
        self.movementSpeed = -10
        self.image = pygame.image.load(image)
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = self.setPosition(pos)
        self.last = pygame.time.get_ticks()
        self.cooldown = cooldown
        self.damage = damage

    def setPosition(self, position):
        if position == "topright":
            return gV.player1.rect.topright
        elif position == "topleft":
            return gV.player1.rect.topleft
        else:
            return gV.player1.rect.midtop

    def subtractHitpoints(self, collided: list):
        for enemy in collided:
            enemy.hitpoints -= 1
            if enemy.hitpoints == 0:
                enemy.kill()
                gV.hits += 1

    def update(self):
        if self.rect.bottom < 0:
            self.kill()
        self.rect = self.rect.move(0, self.movementSpeed)
        collided = pygame.sprite.spritecollide(self, gV.MOBS, dokill=False)
        if len(collided) > 0: # missile collided with an enemy
            self.kill()
            self.subtractHitpoints(collided)
            # Roll drop chance and spawn item based on it
            r = randint(0, 100)
            drop = None
            for itemId in gV.ITEMS.items:
                if r in gV.ITEMS.items[itemId]["roll"]:
                    drop = Item(itemId, gV.ITEMS.items[itemId]["image"])
            if drop is not None:
                drop.rect.center = collided[0].rect.center
                gV.SPRITES.add(drop)