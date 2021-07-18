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

clock = pygame.time.Clock()

bird = Bird(SCREEN_SIZE[1] * 0.4)
base = Ground(575)
pipes = [Pipe(400)]
scoreboard = Scoreboard()

bg = pygame.image.load('GameObjects/sprites/bg.png').convert_alpha()

# Game Loop
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE and game_start:
            bird.jump()
        if event.type == KEYDOWN and event.key == K_SPACE and not game_start:
            game_start = True
            bird.jump()

    screen.blit(pygame.transform.scale(bg, SCREEN_SIZE), (0, 0))
    # print(clock.get_fps())

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

    for pipe in pipes:
        if pipe.x <= -100:
            pipes.remove(pipe)
        if pipe.collide(bird) or base.collide(bird):
            game_start = False
            bird = Bird(SCREEN_SIZE[1] * 0.4)
            base = Ground(575)
            pipes = [Pipe(400)]
            scoreboard = Scoreboard()

    pygame.display.update()

pygame.quit()
