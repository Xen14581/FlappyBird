import pygame


class Ground(pygame.sprite.Sprite):

    VEL = 2

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('GameObjects/sprites/ground.png').convert_alpha()
        self.y = y
        self.x1 = 0
        self.x2 = 450
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(pygame.transform.scale(self.image, (450, 150)), (self.x1, self.y))
        window.blit(pygame.transform.scale(self.image, (450, 150)), (self.x2, self.y))

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + 450 <= 0:
            self.x1 = self.x2 + 450

        if self.x2 + 450 <= 0:
            self.x2 = self.x1 + 450

    def collide(self, bird):
        bird_mask = bird.get_mask()

        offset = (self.x1 - bird.x, self.y - round(bird.y))

        return bird_mask.overlap(self.mask, offset)
