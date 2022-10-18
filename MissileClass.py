from bombs import *
class Missile:
    objType = "Missile"
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        self.color = (0,0,255,255)
        self.position = [0,0]
        self.movementSpeed = 0
        self.sprite = pygame.image.load('images/missile.png')
        self.size = (self.sprite.get_width(), self.sprite.get_height())

    def move(self):
        self.position[1] += self.movementSpeed
        if self.position[1] < 0:
            gV.collidables.remove(self)
        else:
            for obj in gV.collidables:
                if obj.objType == "Enemy":
                    if collisionCheck(self,obj):
                        bomb1 = bomb()
                        gV.collidables.append(bomb1)
                        bomb1.position[0] = obj.position[0]
                        bomb1.position[1] = obj.position[1]
                        gV.collidables.remove(self)
                        gV.collidables.remove(obj)
                        gV.hits += 1
                        break