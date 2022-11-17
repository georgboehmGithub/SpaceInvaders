import pygame


class Weapon:
    def __init__(self, specs: dict):
        self.specs = specs
        self.name = specs["name"]
        self.damage = specs["damage"]
        self.image = specs["image"]
        self.display = specs["display"]
        self.cooldown = specs["cooldown"]
        self.amount = specs["amount"]
        self.position = specs["position"]
        self.ammo = specs["ammo"]


    def decreaseAmmo(self):
        self.ammo[0] -= 1

    def resetAmmo(self):
        self.ammo[0] = self.ammo[1]


class Armory:
    def __init__(self):
        self.modes = \
            {"Basic": {"damage": 1, "image": "images/missile.png", "display": "images/missile.png",
                       "cooldown": 300, "amount": 1, "position": "midtop", "ammo": [1000, 1000],
                       "name": "Basic"},
             "Weapon2": {"damage": 2, "image": "images/missile.png", "display": "images/bomb_powerup.png",
                         "cooldown": 300, "amount": 2, "position": ["topleft", "topright"], "ammo": [30, 30],
                         "name": "Weapon2"},
             "AlienCannon": {"damage": 2, "image": "images/alienCannon.png", "display": "images/alienCannon.png",
                 "cooldown": 1000, "amount": 1, "position": ["midtop"], "ammo": [10, 10], "name": "AlienCannon",
                 "rects": [pygame.Rect(278, 307, 20, 20),
                          pygame.Rect((297, 307, 20, 20)),
                          pygame.Rect((317, 307, 20, 20)),
                          pygame.Rect((336, 307, 20, 20))]
             }
             }