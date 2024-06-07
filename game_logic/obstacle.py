import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/obstacle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position