import pygame
import Player

WindowSize = [512,512]
hits = 0
gameRunning = True
time_since_last_missile = 0
game_clock = 0
SPRITES = pygame.sprite.Group()
MOBS = pygame.sprite.Group()
PLAYERS = pygame.sprite.Group()
player1 = Player.Player()
