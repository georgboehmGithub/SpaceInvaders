
class Weapon():
    def __init__(self):
        self.modes = \
            {"Basic": {"damage": 1, "image": "images/missile.png", "cooldown": 300},
             "Advanced": {"damage": 2, "image": "images/bomb_powerup.png", "cooldown": 100}
             }
        self.active = "Basic"

    def getWeapon(self):
        return self.modes[self.active]




