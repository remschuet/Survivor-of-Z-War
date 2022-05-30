import pygame
from enemy import Enemy
from player import Player
from position_player import PositionPlayer
from position_environment import PositionEnvironment

"""
for enemi in list
"""


pygame.init()

ROOT_WIDTH = 900
ROOT_HEIGHT = 600

PLAYER_WIDTH = 80
PLAYER_HEIGHT = 80
PLAYER_SPEED = 2

arial_font = pygame.font.SysFont("arial", 20)

root = pygame.display.set_mode((ROOT_WIDTH, ROOT_HEIGHT))
background_image = pygame.image.load("background_game.png")
background_image = pygame.transform.scale(background_image, (ROOT_WIDTH, ROOT_HEIGHT))

pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Toute les 2 secondes
pygame.time.set_timer(pygame.USEREVENT, 2000)

# Set up player
position_environment = PositionEnvironment()
position_player = PositionPlayer(400, 250)
player = Player(root, "player", "player", 400, 250, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, position_player, position_environment)
enemy = Enemy(root, "enemy", "enemy01", 100, 100, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, position_player, position_environment)
enemy02 = Enemy(root, "enemy", "enemy02", 400, 400, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, position_player, position_environment)

launched = True
while launched:
    # reset the screen to black
    root.fill((0, 0, 0))

    # (fps) speed of the mouvement
    clock.tick(120)

    for event in pygame.event.get():
        # quit the game
        if event.type == pygame.QUIT:
            launched = False
        # for event every 2 sec
        elif event.type == pygame.USEREVENT:
            print("New enemy")

    # player mouvement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.position_x > 0:
        player.move_left()

    if keys[pygame.K_RIGHT] and player.position_x < ROOT_WIDTH - PLAYER_WIDTH:
        player.move_right()

    if keys[pygame.K_UP] and player.position_y > 0:
        player.move_up()

    if keys[pygame.K_DOWN] and player.position_y < ROOT_HEIGHT - PLAYER_HEIGHT:
        player.move_down()

    # enemy mouvement
    enemy.movement()
    enemy02.movement()

    # display the background image to the root
    root.blit(background_image, [0, 0])

    # display by draw players
    enemy.draw()
    enemy02.draw()
    player.draw()

    # display the fsp in the screen
    fps_text = arial_font.render(f"{int(clock.get_fps())} fps", True, (255, 255, 255))
    root.blit(fps_text, [(ROOT_WIDTH - 70), 20])

    # main loop
    pygame.display.update()

pygame.quit()
