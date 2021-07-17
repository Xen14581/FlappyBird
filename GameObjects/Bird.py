import pygame


class Bird(pygame.sprite.Sprite):

    clock = pygame.time.Clock()

    def __init__(self, y, x=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load('GameObjects/sprites/bird.png').convert_alpha(),
            (50, 40)
        )
        self.x = x
        self.y = y
        self.gravity = 0.25
        self.bird_movement = 0
        self.rect = self.image.get_rect(center=(100, 320))
        self.first = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def jump(self):
        self.bird_movement = 0
        self.bird_movement -= 8.5

    def move(self):
        if not self.first:
            self.jump()
            self.first = 1
        self.bird_movement += self.gravity
        self.y += self.bird_movement * 0.6

    def get_mask(self):
        return pygame.mask.from_surface(self.image)