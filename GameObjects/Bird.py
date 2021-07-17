import pygame


class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('GameObjects/sprites/bird.png')

    def move(self):
        pass

    def draw(self, window, SCREEN_SIZE):
        window.blit(
            pygame.transform.scale(
                self.image.convert_alpha(), (50, 40)
            ), (SCREEN_SIZE[0]/4, SCREEN_SIZE[1]*0.4)
        )

    def jump(self):
        pass
