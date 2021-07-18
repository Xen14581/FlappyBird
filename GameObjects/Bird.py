import pygame


class Bird(pygame.sprite.Sprite):

    def __init__(self, y, x=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load('GameObjects/sprites/bird.png').convert_alpha(),
            (50, 40)
        )
        self.x = x
        self.y = y
        self.height = self.y
        self.gravity = 0.3
        self.bird_movement = 0
        self.tilt = 0
        self.rect = self.image.get_rect(center=(100, 320))

    def draw(self, window):
        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotated_image, new_rect)

    def jump(self):
        self.bird_movement = 0
        self.bird_movement -= 9.5

    def move(self):
        self.bird_movement += self.gravity
        self.y += self.bird_movement * 0.6

        if self.bird_movement < 0 :
            if self.tilt < 25:
                self.tilt = 25
        else:
            if self.tilt > -90:
                self.tilt -= 2

    def get_mask(self):
        return pygame.mask.from_surface(self.image)