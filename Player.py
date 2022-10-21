import pygame
from collisionCheck import collisionCheck
import globalVariables as gV
from Collidables import Instance
from Weapon import Weapon

class Player(Instance):
    def __init__(self):
        self.weapon = Weapon()
        self.sprite = pygame.image.load('images/player.png')
        self.size = (self.sprite.get_width(), self.sprite.get_height())
        self.position = [gV.WindowSize[0] / 2, gV.WindowSize[1] - self.size[1]]
        super().__init__("Player", self.position, 0, 'images/player.png')

    def move(self):
        self.position[0] += self.movementSpeed
        for obj in gV.collidables:
            if obj.objType == "Enemy":
                if collisionCheck(self,obj):
                    gV.gameOver = True
        if self.position[0] <= 0 or self.position[0] + self.size[0] >= gV.WindowSize[0]:
            self.movementSpeed = 0

    # TODO: Interaction between player and items collected
    # TODO: Change weapon value and check per press of spacebar what the ammunition is and update accordingly
    def itemCollect(self, itemId: int):
        self.weapon.active = "Advanced"

