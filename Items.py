from Collidables import Instance
import globalVariables as gV
from collisionCheck import collisionCheck

# Item/Missile ideas: https://opengameart.org/content/bullet-collection-1-m484
class Ray(Instance):
    def __init__(self):
        self.itemId = 1
        super().__init__("Item", [0,0], 2, "images/bomb_powerup.png")

    def move(self):
        self.position[1] += self.movementSpeed
        if self.position[1] == gV.WindowSize[1]:
            gV.collidables.remove(self)
        else:
            for obj in gV.collidables:
                if obj.objType == "Player":
                    if collisionCheck(self, obj):
                        gV.collidables.remove(self)
                        obj.itemCollect(self.itemId)
