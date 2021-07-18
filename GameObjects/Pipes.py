import pygame
import random


class Pipe(pygame.sprite.Sprite):

    GAP = 150
    VEL = 2

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.image = pygame.transform.scale(
            pygame.image.load('GameObjects/sprites/pipe.png').convert_alpha(), (70, 400)
        )

        self.top_pipe = pygame.transform.flip(
            self.image, False, True
        )
        self.bottom_pipe = self.image

        self.height = random.randint(50, 370)
        self.top = self.height - self.top_pipe.get_height()
        self.bottom = self.height + self.GAP
        self.rect = self.image.get_rect()
        self.top_mask = pygame.mask.from_surface(self.top_pipe)
        self.bottom_mask = pygame.mask.from_surface(self.bottom_pipe)

    def draw(self, window):
        window.blit(self.top_pipe, (self.x, self.top))
        window.blit(self.bottom_pipe, (self.x, self.bottom))

    def move(self):
        self.x -= self.VEL

    def collide(self, bird):
        bird_mask = bird.get_mask()

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        return bird_mask.overlap(self.top_mask, top_offset) or bird_mask.overlap(self.bottom_mask, bottom_offset)
