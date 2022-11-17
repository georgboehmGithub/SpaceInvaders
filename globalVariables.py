import pygame
import Player
import Items

WindowSize = [512, 512]
hits = 0
gameRunning = True
frame = 0
spriteSheet = pygame.image.load("images/M484BulletCollection2.png")
time_since_last_missile = 0
game_clock = 0
SPRITES = pygame.sprite.Group()
MOBS = pygame.sprite.Group()
PLAYERS = pygame.sprite.Group()
player1 = Player.Player()
ITEMS = Items.ItemList()
