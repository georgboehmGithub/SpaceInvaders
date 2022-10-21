import sys
import pygame
from random import randint
import Missiles
import globalVariables as gV
import Player
import Enemies
import Background

pygame.init()
pygame.mixer.init()
#sounds
missile_sound = pygame.mixer.Sound("sounds/Blaster-Solo.wav")

WHITE = (255,255,255)
gameWindow = pygame.display.set_mode(gV.WindowSize)
#player
player1 = Player.Player()
gV.collidables.append(player1)
#clock
clock = pygame.time.Clock()
#background
group = pygame.sprite.LayeredUpdates()
Background.Background(0,group)
Background.Background(1,group)

def draw_text(text,color):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[gV.WindowSize[0]/2, 20])

def drawGame():
    if gV.gameOver:         # TODO: These 3 lines are currently not working!
        gV.gameRunning = False
        GameOverScreen("Game Over!",WHITE)

    group.draw(gameWindow)
    group.update()
    draw_text(str(gV.hits),WHITE)
    for col in gV.collidables:
        gameWindow.blit(col.sprite, (col.position[0],col.position[1]))
    pygame.display.flip()
    clock.tick(60)

# TODO: Not Working yet, will be conducted in the future
def GameOverScreen(text,color):
    font = pygame.font.Font(None, 50)
    screen_text = font.render(text,True,color)
    screen_text_rect = screen_text.get_rect(center=(gV.WindowSize[0]/2,gV.WindowSize[1]/2))
    gameWindow.blit(screen_text, screen_text_rect)

while gV.gameRunning:
    gV.game_clock = pygame.time.get_ticks()
    drawGame()
    r = randint(0,50)
    if r == 50:
        alien = Enemies.Enemy()
        gV.collidables.append(alien)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
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
                    caliber.movementSpeed = -4
                    caliber.position[0] = player1.position[0] + player1.size[0] / 2 - caliber.size[0] / 2
                    caliber.position[1] = player1.position[1] - caliber.size[1]
                    gV.time_since_last_missile = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.movementSpeed = 0
            elif event.key == pygame.K_RIGHT:
                player1.movementSpeed = 0
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
    for col in gV.collidables:
        col.move()