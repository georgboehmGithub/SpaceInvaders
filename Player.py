import globalVariables as gV
from Weapon import Weapon, Armory
import pygame as pg
import Missiles
import sys


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('images/player.png')
        self.size = (self.image.get_width(), self.image.get_height())
        self.armory = Armory()
        self.weapons = [Weapon(self.armory.modes["Basic"])]
        self.activeWeapon = self.weapons[0]
        self.objType = "Player"
        self.hitpoints = 3
        self.movementSpeedX = 0
        self.movementSpeedY = 0
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = [gV.WindowSize[0] / 2, gV.WindowSize[1] - self.size[1]]

    def setMissileSound(self, sound: pg.mixer.Sound):
        self.missileSound = sound

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.movementSpeedX = -3
                elif event.key == pg.K_d:
                    self.movementSpeedX = 3
                elif event.key == pg.K_w:
                    self.movementSpeedY = -3
                elif event.key == pg.K_s:
                    self.movementSpeedY = 3
                elif event.key == pg.K_e:
                    weaponIndex = self.weapons.index(self.activeWeapon)
                    if weaponIndex + 1 < len(self.weapons):
                        self.activeWeapon = self.weapons[weaponIndex + 1]
                    else:
                        self.activeWeapon = self.weapons[0]
                elif event.key == pg.K_SPACE:
                    curWeapon = self.activeWeapon
                    #  missile cooldown check
                    if gV.game_clock - gV.time_since_last_missile >= curWeapon.cooldown:
                        pg.mixer.Sound.play(self.missileSound)
                        # update ammo
                        curWeapon.decreaseAmmo()
                        # spawn missiles
                        for m in range(curWeapon.amount):
                            caliber = Missiles.Missile(curWeapon.damage, curWeapon.image,
                                                       curWeapon.cooldown, curWeapon.position[m])
                            gV.SPRITES.add(caliber)
                            gV.time_since_last_missile = pg.time.get_ticks()
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    self.movementSpeedX = 0
                elif event.key == pg.K_d:
                    self.movementSpeedX = 0
                elif event.key == pg.K_w:
                    self.movementSpeedY = 0
                elif event.key == pg.K_s:
                    self.movementSpeedY = 0
            if event.type == pg.QUIT:
                sys.exit()

    def update(self):
        self.rect = self.rect.move(self.movementSpeedX, 0)  # Horizontal movement
        self.rect = self.rect.move(0, self.movementSpeedY)  # Vertical movement
        collided = pg.sprite.spritecollide(self, gV.MOBS, dokill=False)
        if len(collided) > 0:
            gV.gameRunning = False
        # Window boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= gV.WindowSize[0]:
            self.rect.right = gV.WindowSize[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > gV.WindowSize[1]:
            self.rect.bottom = gV.WindowSize[1]
        # Check ammo
        if self.activeWeapon.ammo[0] == 0 and self.activeWeapon.name != "Basic":
            self.activeWeapon.resetAmmo()
            self.activeWeapon = "Basic"

    def itemCollect(self, itemId: int):
        item = gV.ITEMS.items[itemId]
        if item["type"] == "threat":
            if self.hitpoints > 1:
                self.hitpoints = self.hitpoints - 1
            else:
                gV.gameRunning = False
        if item["type"] == "weapon":
            for weapon in self.weapons:
                if weapon.name == item["name"]:
                    weapon.resetAmmo()
                    return
            self.weapons.append(Weapon(self.armory.modes[item["name"]]))
