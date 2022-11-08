import sys
import pygame
from random import randint
import Enemies
import Missiles
import globalVariables as gV

# inits
pygame.init()
pygame.mixer.init()
#sounds
missile_sound = pygame.mixer.Sound("sounds/Blaster-Solo.wav")
# generals
gameWindow = pygame.display.set_mode(gV.WindowSize)
SPRITES = gV.SPRITES
MOBS = gV.MOBS
PLAYERS = gV.PLAYERS
clock = pygame.time.Clock()
#player
player1 = gV.player1
PLAYERS.add(player1)
# Background
bg = pygame.image.load("images/background.png")

def draw_text(text,color):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[gV.WindowSize[0]/2, 20])

while gV.gameRunning:
    gameWindow.blit(bg, (0, 0))
    SPRITES.draw(gameWindow)
    MOBS.draw(gameWindow)
    PLAYERS.draw(gameWindow)
    draw_text(str(gV.hits), (255, 255, 255))
    pygame.display.update()
    pygame.display.flip()

    gV.game_clock = pygame.time.get_ticks()
    r = randint(0,50)
    if r == 50:
        alien = Enemies.Enemy()
        gV.collidables.append(alien)
        gV.MOBS.add(alien)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # TODO: Let player class handle events individually
            if event.key == pygame.K_LEFT:
                player1.movementSpeed = -3
            elif event.key == pygame.K_RIGHT:
                player1.movementSpeed = 3
            elif event.key == pygame.K_SPACE:
                curWeapon = player1.weapon.getWeapon()
                #  cooldown check, missile spawn only every 0.3 seconds
                if gV.game_clock - gV.time_since_last_missile >= curWeapon["cooldown"]:
                    caliber = Missiles.Missile(curWeapon["damage"], curWeapon["image"], curWeapon["cooldown"])
                    pygame.mixer.Sound.play(missile_sound)
                    gV.collidables.append(caliber)
                    SPRITES.add(caliber)
                    caliber.movementSpeed = -4 # TODO in missile class
                    caliber.rect.center = player1.rect.midtop
                    gV.time_since_last_missile = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.movementSpeed = 0
            elif event.key == pygame.K_RIGHT:
                player1.movementSpeed = 0
        if event.type == pygame.QUIT:
            sys.exit()
            #pygame.quit()
    SPRITES.update()
    MOBS.update()
    PLAYERS.update()
    clock.tick_busy_loop(60)
# Game Over
sys.exit()


