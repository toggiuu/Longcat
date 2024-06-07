import pygame

def handle_input(player, bounds):
    keys = pygame.key.get_pressed()
    player.update(keys, bounds)