import pygame

class Instance():
    def __init__(self, objType:str, position:list, movementSpeed:int, sprite:str):
        self.objType = objType
        self.position = position
        self.movementSpeed = movementSpeed
        self.sprite = pygame.image.load(sprite)
        self.size = (self.sprite.get_width(), self.sprite.get_height())


