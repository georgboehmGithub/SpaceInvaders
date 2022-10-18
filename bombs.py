import pygame
import globalVariables as gV
from collisionCheck import collisionCheck

class bomb:
    objType = "Bomb"
    def __init__(self):
        self.position = [0,0]
        self.movementSpeed = 2
        self.sprite = pygame.image.load('images/bomb.png')
        self.size = (self.sprite.get_width(),self.sprite.get_height())
    def move(self):
        self.position[1] += self.movementSpeed
        if self.position[1] == gV.WindowSize[1]:
            gV.collidables.remove(self)
        else:
            for obj in gV.collidables:
                if obj.objType == "Player":
                    if collisionCheck(self,obj):
                        gV.gameOver = True