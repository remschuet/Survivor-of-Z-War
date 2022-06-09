import pygame
from management_canvas import ManagementCanvas


pygame.init()

# variable for dimension screen
ROOT_WIDTH = 900
ROOT_HEIGHT = 600

# create root
root = pygame.display.set_mode((ROOT_WIDTH, ROOT_HEIGHT))
pygame.display.set_caption("Game")

# create the clock (timer)
clock = pygame.time.Clock()

launched = True
# create management canvas to display information
management_canvas = ManagementCanvas(root, clock, launched, ROOT_WIDTH, ROOT_HEIGHT)
management_canvas.create_management_menu_environment()

while launched:
    # reset the screen to black
    root.fill((0, 0, 0))

    # fps
    clock.tick(120)

    # verify if the game is launch
    launched = management_canvas.launched

    # check the event in management canvas
    management_canvas.call_every_frame()

    # main loop
    pygame.display.update()

pygame.quit()
