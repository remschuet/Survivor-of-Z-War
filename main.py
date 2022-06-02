import pygame
from management_environment import ManagementEnvironment

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

management_environment = ManagementEnvironment(root, HUMAN_WIDTH, HUMAN_HEIGHT, HUMAN_SPEED, ROOT_WIDTH, ROOT_HEIGHT)

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
            management_environment.call_every_2_sec()

    # player mouvement
    keys = pygame.key.get_pressed() # Pourrait servir à rediriger vers une fonction
    if keys:
        management_environment.key_pressed(keys)


    # mouvement enemy
    management_environment.enemy_mouvement()


    # display the background image to the root
    root.blit(root_background_image, [0, 0])

    # draw enemy
    management_environment.draw_human_and_fps(clock)

    # main loop
    pygame.display.update()

pygame.quit()
