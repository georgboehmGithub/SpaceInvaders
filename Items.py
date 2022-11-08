import pygame as pg
import globalVariables as gV

# Item/Missile ideas: https://opengameart.org/content/bullet-collection-1-m484
class Item(pg.sprite.Sprite):
    def __init__(self, id):
        pg.sprite.Sprite.__init__(self)
        self.id = id
        self.objType = "Item"
        self.position = [0,0]
        self.movementSpeed = 2
        self.image = pg.image.load("images/bomb_powerup.png")
        self.size = (self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.rect = self.rect.move(0, self.movementSpeed)
        collided = pg.sprite.spritecollide(self, gV.PLAYERS, dokill=False)
        if len(collided) > 0:
            self.kill()
            gV.player1.itemCollect(1)
        # TODO: DESPAWNING
        if self.rect == gV.WindowSize[1]:
            gV.collidables.remove(self)

