import math


class Weapon():
    def __init__(self):
        self.modes = \
            {"Basic": {"damage": 1, "image": "images/missile.png", "display": "images/missile.png",
                       "cooldown": 300, "amount": 1, "position": "midtop", "ammo": [1000, 1000],
                       "name": "Basic"},
             "Weapon2": {"damage": 2, "image": "images/missile.png", "display": "images/bomb_powerup.png",
                         "cooldown": 100, "amount": 2, "position": ["topleft", "topright"], "ammo": [30, 30],
                         "name": "Weapon2"}
             }
        self.active = "Basic"

    def getWeapon(self):
        return self.modes[self.active]

    def decreaseAmmo(self, weapon):
        self.modes[weapon]["ammo"][0] -= 1

    def resetAmmo(self, weapon):
        self.modes[weapon]["ammo"][0] = self.modes[weapon]["ammo"][1]






