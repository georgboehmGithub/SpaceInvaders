import sys
import pygame
from random import randint
import Enemies
import globalVariables as gV

# inits
pygame.init()
# sounds
pygame.mixer.init()
missile_sound = pygame.mixer.Sound("sounds/Blaster-Solo.wav")
# Window
gameWindow = pygame.display.set_mode(gV.WindowSize)
clock = pygame.time.Clock()
# player
player1 = gV.player1
player1.setMissileSound(missile_sound)
gV.PLAYERS.add(player1)
# Background
bg = pygame.image.load("images/background.png").convert()
# Hitpoints
hp = pygame.image.load("images/life.png").convert()

def draw_text(text: str, color: tuple, size: int, position: list):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    text_rect = screen_text.get_rect(center=(position[0], position[1]))
    gameWindow.blit(screen_text, text_rect)

def draw_hitpoints(hitpoints):
    x = 10
    for hitpoint in range(hitpoints):
        gameWindow.blit(hp, (x, 10))
        x += 40

def draw_weapon():
    gameWindow.blit(pygame.image.load(
        player1.activeWeapon.display).convert(), (gV.WindowSize[0] - 40, 10)
                    )
    draw_text(str(player1.activeWeapon.ammo[0]), (255, 255, 255), 25, [gV.WindowSize[0] - 70, 20])
# i = 0
class GameState():
    def __init__(self):
        self.state = "intro"
        self.startButton = pygame.rect.Rect(0,0,200,50)
        self.startButton.center = (gV.WindowSize[0] / 2, gV.WindowSize[1] / 2)

    def manageState(self):
        if self.state == "intro":
            self.intro()
        elif self.state == "main_game":
            self.main_game()
        elif self.state == "game_over":
            self.game_over()

    def game_over(self):
        gameWindow.blit(bg, (0, 0))
        pygame.draw.rect(gameWindow, color="grey", rect=self.startButton)
        draw_text("Game Over!", (255, 255, 255), 25, list(self.startButton.center))
        pygame.display.update()
        pygame.display.flip()
        gV.game_clock = pygame.time.get_ticks()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if self.startButton.collidepoint(mousePos):
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

    def intro(self):
        # Draw scene
        gameWindow.blit(bg, (0, 0))
        pygame.draw.rect(gameWindow, color="grey", rect=self.startButton)
        draw_text("Start", (255, 255, 255), 25, list(self.startButton.center))
        pygame.display.update()
        pygame.display.flip()
        gV.game_clock = pygame.time.get_ticks()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if self.startButton.collidepoint(mousePos):
                    self.state = "main_game"
            if event.type == pygame.QUIT:
                sys.exit()

    def main_game(self):
        if not gV.gameRunning:
            self.state = "game_over"
            return
        # Draw scene
        gameWindow.blit(bg, (0, 0))  # Background
        draw_hitpoints(player1.hitpoints)  # Hitpoints
        draw_weapon()  # Active weapons
        gV.SPRITES.draw(gameWindow)
        gV.MOBS.draw(gameWindow)
        gV.PLAYERS.draw(gameWindow)
        draw_text(str(gV.hits), (255, 255, 255), 25, [gV.WindowSize[0] / 2, 20]) # Score
        pygame.display.update()
        pygame.display.flip()
        # Spawn new mobs
        gV.game_clock = pygame.time.get_ticks()
        r = randint(0, 60)
        if r == 1:
            alien = Enemies.Enemy()
            gV.MOBS.add(alien)
        # Handle events
        player1.handleEvents()
        gV.SPRITES.update()
        gV.MOBS.update()
        gV.PLAYERS.update()

# main procedure
gameState = GameState()
while True:
    gV.frame += 1
    gameState.manageState()
    clock.tick_busy_loop(60)
