from Bombs import *
from Collidables import Instance
import pygame

class Missile(Instance):
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        self.color = (0,0,255,255)
        super().__init__("Missile", [0,0], 0, "images/missile.png")

    def move(self):
        self.position[1] += self.movementSpeed
        if self.position[1] < 0:
            gV.collidables.remove(self)
        else:
            for obj in gV.collidables:
                if obj.objType == "Enemy":
                    if collisionCheck(self, obj):
                        bomb1 = Bomb()
                        gV.collidables.append(bomb1)
                        bomb1.position[0] = obj.position[0]
                        bomb1.position[1] = obj.position[1]
                        gV.collidables.remove(self)
                        gV.collidables.remove(obj)
                        gV.hits += 1
                        break
