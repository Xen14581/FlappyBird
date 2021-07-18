import pygame


class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font('GameObjects/font/flappy-font.ttf', 50)
        self.score = 0
        self.text = ''

    def show(self, window, size):
        self.text = self.font.render(f'{self.score}', False, (255, 255, 255))
        window.blit(self.text, (size[0]/2 - 10, size[1]/10))

    def increment(self):
        self.score += 1
