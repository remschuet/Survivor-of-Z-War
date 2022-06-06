import pygame
from management_environment import ManagementEnvironment

"""
    REFACTORING
    détruire un enemy avec des balle
    timer pour les balles
    il y a une liste et un dictionnaire, problème de destruction et de collision
    essayer avec une autre fonction qui récupèrent les bullet en mouvement et qui peut les détruire
        ou détruire les bullets sur une distance et non au toucher
    mettre un system de point de vie
    Mettre le fusil ready à chaque seconde
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
pygame.time.set_timer(pygame.USEREVENT, 1000)

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
            management_environment.create_enemy_every_2_sec()
        # to can shoot
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_3:
                management_environment.shoot_bullet()

    # player mouvement
    keys_pressed = pygame.key.get_pressed()

    # keys_up = pygame.key.K_UP()
    if keys_pressed:
        management_environment.key_pressed(keys_pressed)

    # mouvement enemy
    management_environment.enemy_mouvement()
    management_environment.bullet_mouvement()

    # display the background image to the root
    root.blit(root_background_image, [0, 0])

    # draw enemy
    management_environment.draw_human_and_fps(clock)

    # main loop
    pygame.display.update()

pygame.quit()
