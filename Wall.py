import pygame


class Wall(object):

    def __init__(self, pos, col):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.color = col

walls = []