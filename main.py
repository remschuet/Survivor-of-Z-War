import pygame
from object_scene import ObjectScene

pygame.init()

WIDTH = 700
HEIGHT = 500

position_x = 200
position_y = 200
player_width = 40
player_height = 40
speed = 2

arial_font = pygame.font.SysFont("arial", 20)

root = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.image.load("background_game.png")
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Toute les 2 secondes
pygame.time.set_timer(pygame.USEREVENT, 2000)

# Set up player
player = ObjectScene(root, 20, 20, player_width, player_height, speed)

launched = True
while launched:
    root.fill((0, 0, 0))

    # (fps)
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.USEREVENT:
            print("New enemy")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.position_x > 0:
        position_x -= speed
        player.move_left()
    if keys[pygame.K_RIGHT] and player.position_x < WIDTH - player_width:
        position_x += speed
        player.move_right()
    if keys[pygame.K_UP] and player.position_y > 0:
        position_y -= speed
        player.move_up()
    if keys[pygame.K_DOWN] and player.position_y < HEIGHT - player_height:
        position_y += speed
        player.move_down()

    root.blit(background_image, [0, 0])

    player.draw()

    fps_text = arial_font.render(f"{int(clock.get_fps())} fps", True, (255, 255, 255))
    root.blit(fps_text, [(WIDTH-70), 20])

    pygame.display.update()

pygame.quit()
