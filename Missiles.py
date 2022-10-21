from Bombs import *
from Items import *
from Collidables import Instance
import pygame
from random import randint
import globalVariables as gV


class Missile(Instance):
    def __init__(self, damage, image, cooldown):
        self.last = pygame.time.get_ticks()
        self.cooldown = cooldown
        self.damage = damage
        super().__init__("Missile", [0,0], 0, image)

    def move(self):
        self.position[1] += self.movementSpeed
        if self.position[1] < 0:
            gV.collidables.remove(self)
        else:
            for obj in gV.collidables:
                if obj.objType == "Enemy":
                    if collisionCheck(self, obj):
                        r = randint(0, 2)
                        if r == 2:
                            drop = Ray()
                        else:
                            drop = Bomb()
                        gV.collidables.append(drop)
                        drop.position[0] = obj.position[0]
                        drop.position[1] = obj.position[1]
                        gV.collidables.remove(self)
                        gV.collidables.remove(obj)
                        gV.hits += 1
                        break
