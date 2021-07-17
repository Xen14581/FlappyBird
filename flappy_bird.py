import pygame
from pygame.locals import *
from GameObjects.Bird import Bird

SCREEN_SIZE = (450, 640)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

running = True

# Game Loop
while running:

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE:
            pass

    # Objects
    screen.blit(
        pygame.transform.scale(
            pygame.image.load('GameObjects/sprites/bg.png').convert_alpha(), SCREEN_SIZE
        ), (0, 0)
    )

    bird = Bird()

    bird.draw(screen, SCREEN_SIZE)

    pygame.display.flip()

pygame.quit()
