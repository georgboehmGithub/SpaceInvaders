import globalVariables as gV
from collisionCheck import collisionCheck
from Collidables import Instance

class Bomb(Instance):
    def __init__(self):
        super().__init__("Bomb", [0, 0], 2, 'images/bomb.png')

    def move(self):
        self.position[1] += self.movementSpeed
        if self.position[1] == gV.WindowSize[1]:
            gV.collidables.remove(self)
        else:
            for obj in gV.collidables:
                if obj.objType == "Player":
                    if collisionCheck(self,obj):
                        gV.gameOver = True