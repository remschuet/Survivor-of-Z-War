import pygame
from management_canvas import ManagementCanvas

"""
    REFACTORING
    timer pour les balles, avec un temps en seconde
    mettre un maximum de balle dans le fusil
    mettre un system de point de vie visuel
    Mettre le fusil ready à chaque seconde
    dessin de carte avec des murs et des entrées pour les enemy
    bouger les enemy sur le menu
    
    Timer dans management canvas
    
"""

pygame.init()

# init the constant variable
ROOT_WIDTH = 900
ROOT_HEIGHT = 600

# timer_create_enemy = 1000

# create root and the background root
root = pygame.display.set_mode((ROOT_WIDTH, ROOT_HEIGHT))
pygame.display.set_caption("Game")

# create the clock (timer)
clock = pygame.time.Clock()

# call every in milliseconds
# pygame.time.set_timer(pygame.USEREVENT, timer_create_enemy)

launched = True
management_canvas = ManagementCanvas(root, clock, launched, ROOT_WIDTH, ROOT_HEIGHT)
while launched:
    # reset the screen to black
    root.fill((0, 0, 0))

    # (fps) speed of the mouvement
    clock.tick(120)

    # verify if the game is launch
    launched = management_canvas.launched

    # check the event in management canvas
    management_canvas.call_every_frame()

    # main loop
    pygame.display.update()

pygame.quit()
