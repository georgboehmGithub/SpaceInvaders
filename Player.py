import globalVariables as gV
from Weapon import Weapon
import pygame as pg
import Missiles
import sys


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('images/player.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.objType = "Player"
        self.movementSpeed = 0
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = [gV.WindowSize[0] / 2, gV.WindowSize[1] - self.size[1]]

    def setMissileSound(self, sound: pg.mixer.Sound):
        self.missileSound = sound

    def setWeapon(self):
        self.weapon = Weapon()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.movementSpeed = -3
                elif event.key == pg.K_RIGHT:
                    self.movementSpeed = 3
                elif event.key == pg.K_SPACE:
                    curWeapon = self.weapon.getWeapon()
                    #  missile cooldown check
                    if gV.game_clock - gV.time_since_last_missile >= curWeapon["cooldown"]:
                        # spawn missiles
                        pg.mixer.Sound.play(self.missileSound)
                        for m in range(curWeapon["amount"]):
                            caliber = Missiles.Missile(curWeapon["damage"], curWeapon["image"],
                                                       curWeapon["cooldown"], curWeapon["position"][m])
                            gV.SPRITES.add(caliber)
                            gV.time_since_last_missile = pg.time.get_ticks()
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.movementSpeed = 0
                elif event.key == pg.K_RIGHT:
                    self.movementSpeed = 0
            if event.type == pg.QUIT:
                sys.exit()

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
        item = gV.ITEMS.items[itemId]
        if item["type"] == "threat":
            gV.gameRunning = False
        if item["type"] == "weapon":
            self.weapon.active = item["name"]
