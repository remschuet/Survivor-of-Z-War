import pygame
from enemy import Enemy
from player import Player
from position_environment import PositionEnvironment

"""
    REFACTORING
    ajouter les enemy dans une list
    enemy qui ne se touche pas
    collision avec le joueur
    supprimer position_player
    pas tout le temps key press, mais des fois key up
    Il y a une liste et un dictionnaire, problème de destruction et de collision
"""


pygame.init()

# init the constant variable
ROOT_WIDTH = 900
ROOT_HEIGHT = 600
HUMAN_WIDTH = 80
HUMAN_HEIGHT = 80
HUMAN_SPEED = 2

# create a list for the enemy
enemy_list = []
number_of_enemy = 0

# create writing style
arial_font = pygame.font.SysFont("arial", 20)

# create root and the background root
root = pygame.display.set_mode((ROOT_WIDTH, ROOT_HEIGHT))
root_background_image = pygame.image.load("background_game.png")
root_background_image = pygame.transform.scale(root_background_image, (ROOT_WIDTH, ROOT_HEIGHT))
# set the name of the root
pygame.display.set_caption("Game")

# create the clock (timer)
clock = pygame.time.Clock()

# every 2 seconds
pygame.time.set_timer(pygame.USEREVENT, 2000)

# Set up player
position_environment = PositionEnvironment()
player = Player(root, "player", "player", 400, 250, HUMAN_WIDTH, HUMAN_HEIGHT, HUMAN_SPEED, position_environment)

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
            number_of_enemy += 1
            # create just 3 enemy
            if number_of_enemy <= 3:
                enemy_list.append(Enemy(root, "enemy", ("enemy"+str(number_of_enemy)), 50, 400,HUMAN_WIDTH,
                                        HUMAN_HEIGHT, HUMAN_SPEED, position_environment))

    # player mouvement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.position_x > 0:
        player.move_left()
    if keys[pygame.K_RIGHT] and player.position_x < ROOT_WIDTH - HUMAN_WIDTH:
        player.move_right()
    if keys[pygame.K_UP] and player.position_y > 0:
        player.move_up()
    if keys[pygame.K_DOWN] and player.position_y < ROOT_HEIGHT - HUMAN_HEIGHT:
        player.move_down()
    if keys[pygame.K_1]:
        # to can destroy an enemy
        for enemy_item in enemy_list:
            if isinstance(enemy_item, Enemy):
                if enemy_item.name_id == "enemy1":
                    enemy_list.remove(enemy_item)
                    # destroy the position in position environment dict
                    position_environment.destroy_enemy_in_list(enemy_item.name_id)

    # mouvement enemy
    for enemy_item in enemy_list:
        if isinstance(enemy_item, Enemy):
            enemy_item.movement()

    # display the background image to the root
    root.blit(root_background_image, [0, 0])

    # draw enemy
    for enemy_item in enemy_list:
        if isinstance(enemy_item, Enemy):
            enemy_item.draw()

    # draw player
    player.draw()

    # display the fsp in the screen
    fps_text = arial_font.render(f"{int(clock.get_fps())} fps", True, (0, 0, 0))
    root.blit(fps_text, [(ROOT_WIDTH - 70), 20])

    # main loop
    pygame.display.update()

pygame.quit()
