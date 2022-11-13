class Weapon():
    def __init__(self):
        self.modes = \
            {"Basic": {"damage": 1, "image": "images/missile.png", "cooldown": 300, "amount": 1,
                       "position": "midtop"},
             "Weapon2": {"damage": 2, "image": "images/missile.png", "cooldown": 100, "amount": 2,
                         "position": ["topleft", "topright"]}
             }
        self.active = "Basic"

    def getWeapon(self):
        return self.modes[self.active]






