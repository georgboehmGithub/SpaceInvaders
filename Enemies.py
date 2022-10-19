import globalVariables as gV
from Collidables import Instance

class Enemy(Instance):
    def __init__(self):
        super().__init__("Enemy", [0,0], 4, 'images/enemy.png')

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
            

        


