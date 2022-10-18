import sys
import pygame
from enemy import enemy as E
from collisionCheck import collisionCheck
import globalVariables as gV

class player():
    objType = "Player"

    def __init__(self):
        self.playerSpeed = 0
        self.sprite = pygame.image.load('images/player.png')
        self.size = (self.sprite.get_width(),self.sprite.get_height())
        self.position = [gV.WindowSize[0]/2,gV.WindowSize[1]-self.size[1]]

    def move(self):
        self.position[0] += self.playerSpeed
        for obj in gV.collidables:
            if obj.objType == "Enemy":
                if collisionCheck(self,obj):
                    gV.gameOver = True
        if self.position[0] <= 0 or self.position[0] + self.size[0] >= gV.WindowSize[0]:
            self.playerSpeed = 0 
                    
        

        
        
        
