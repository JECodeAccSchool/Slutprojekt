import pygame

#kan säkert bunta in detta i Wall, men är ej högsta prioritet
class Detail_front(object):

    def __init__(self, pos):
        det_fronts.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

det_fronts = []
