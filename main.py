import pygame
from management_environment import ManagementEnvironment
from management_canvas import ManagementCanvas

"""
    REFACTORING
    timer pour les balles, avec un temps en seconde
    mettre un maximum de balle dans le fusil
    mettre un system de point de vie visuel
    Mettre le fusil ready à chaque seconde
    dessin de carte avec des murs et des entrées pour les enemy
    MANAGEMENT CANVAS
"""

pygame.init()

# init the constant variable
ROOT_WIDTH = 900
ROOT_HEIGHT = 600
# HUMAN_WIDTH = 80
# HUMAN_HEIGHT = 80
# HUMAN_SPEED = 2

# create root and the background root
root = pygame.display.set_mode((ROOT_WIDTH, ROOT_HEIGHT))
# root_background_image = pygame.image.load("background_game.png")
# root_background_image = pygame.transform.scale(root_background_image, (ROOT_WIDTH, ROOT_HEIGHT))
# set the name of the root
pygame.display.set_caption("Game")

# create the clock (timer)
clock = pygame.time.Clock()

# every 2 seconds
pygame.time.set_timer(pygame.USEREVENT, 1000)

canvas_menu = False

canvas_gameplay = True

launched = True
management_canvas = ManagementCanvas(root, clock, launched)
while launched:
    # reset the screen to black
    root.fill((0, 0, 0))

    # (fps) speed of the mouvement
    clock.tick(120)

    if canvas_gameplay:
        # verify if the game is launch
        launched = management_canvas.launched
        # check the event in management canvas
        management_canvas.check_event_key()
    elif canvas_menu:
        print("We are in the menu")

    # main loop
    pygame.display.update()

pygame.quit()
