import pygame
from pygame.locals import *
from GameObjects.Bird import Bird
from GameObjects.Ground import Ground
from GameObjects.Pipes import Pipe
from GameObjects.Scoreboard import Scoreboard

SCREEN_SIZE = (450, 640)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
game_start = False

bird = Bird(SCREEN_SIZE[1] * 0.4)
base = Ground(575)
pipes = [Pipe(400)]
scoreboard = Scoreboard()

# Game Loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE and game_start:
            bird.jump()
        if event.type == KEYDOWN and event.key == K_SPACE and not game_start:
            game_start = True

    screen.blit(
        pygame.transform.scale(
            pygame.image.load('GameObjects/sprites/bg.png').convert_alpha(), SCREEN_SIZE
        ), (0, 0)
    )

    for pipe in pipes:
        pipe.draw(screen)
    base.draw(screen)
    bird.draw(screen)
    scoreboard.show(screen, SCREEN_SIZE)

    if game_start:
        bird.move()
        base.move()
        for pipe in pipes:
            pipe.move()

    if pipes[-1].x <= 200:
        pipes.append(Pipe(500))
    if pipes[0].x == 50:
        scoreboard.increment()
        scoreboard.show(screen, SCREEN_SIZE)

    for pipe in pipes:
        if pipe.x <= -100:
            pipes.remove(pipe)
        if pipe.collide(bird):
            game_start = False
            bird = Bird(SCREEN_SIZE[1] * 0.4)
            base = Ground(575)
            pipes = [Pipe(400)]
            scoreboard = Scoreboard()

    pygame.display.flip()

pygame.quit()
