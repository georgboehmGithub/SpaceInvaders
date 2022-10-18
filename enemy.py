import pygame
import globalVariables as gV

class enemy:
    objType = "Enemy"
    def __init__(self):
        self.position = [0,0]
        self.movementSpeed = 4
        self.sprite = pygame.image.load('images/enemy.png')
        self.size = (self.sprite.get_width(),self.sprite.get_height())

    def move(self):
        self.position[0] += self.movementSpeed
        if self.position[0] + self.size[0] > gV.WindowSize[0]:
            self.movementSpeed = self.movementSpeed * (-1)
            self.position[1] += self.size[1]
            self.position[0] = gV.WindowSize[0] - self.size[0]
        elif self.position[0] < 0:
            self.movementSpeed = self.movementSpeed * (-1)
            self.position[1] += self.size[1]
            self.position[0] = 0
            

        


