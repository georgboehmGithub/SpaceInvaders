import sys
import pygame
from random import randint
import Enemies
import Missiles
import globalVariables as gV

# inits
pygame.init()
pygame.mixer.init()
gameWindow = pygame.display.set_mode(gV.WindowSize)
# sounds
missile_sound = pygame.mixer.Sound("sounds/Blaster-Solo.wav")
# generals
SPRITES = gV.SPRITES
MOBS = gV.MOBS
PLAYERS = gV.PLAYERS
clock = pygame.time.Clock()
# player
player1 = gV.player1
PLAYERS.add(player1)
# Background
bg = pygame.image.load("images/background.png")

def draw_text(text: str, color: tuple, size: int, position: list):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    text_rect = screen_text.get_rect(center=(position[0], position[1]))
    gameWindow.blit(screen_text, text_rect)

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

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if self.startButton.collidepoint(mousePos):
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

    def intro(self):
        gameWindow.blit(bg, (0, 0))
        pygame.draw.rect(gameWindow, color="grey", rect=self.startButton)
        draw_text("Start", (255, 255, 255), 25, list(self.startButton.center))
        pygame.display.update()
        pygame.display.flip()
        gV.game_clock = pygame.time.get_ticks()

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
        gameWindow.blit(bg, (0, 0))
        SPRITES.draw(gameWindow)
        MOBS.draw(gameWindow)
        PLAYERS.draw(gameWindow)
        draw_text(str(gV.hits), (255, 255, 255), 25, [gV.WindowSize[0] / 2, 20])
        pygame.display.update()
        pygame.display.flip()

        gV.game_clock = pygame.time.get_ticks()
        r = randint(0, 50)
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
                        caliber.movementSpeed = -4  # TODO in missile class
                        caliber.rect.center = player1.rect.midtop
                        gV.time_since_last_missile = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.movementSpeed = 0
                elif event.key == pygame.K_RIGHT:
                    player1.movementSpeed = 0
            if event.type == pygame.QUIT:
                sys.exit()
                # pygame.quit()
        SPRITES.update()
        MOBS.update()
        PLAYERS.update()
        
# main procedure
gameState = GameState()
while True:
    gameState.manageState()
    clock.tick_busy_loop(60)
