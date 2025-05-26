import random
import Wall
import pygame

class Player(object):

    def __init__(self):
        self.rect = pygame.rect.Rect(800, 400, 16, 32)
        self.crouch = False
        self.mom_v = 0

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        #kollision med väggar
        for wall in Wall.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    return True
                else:
                    return False


    def player_pos_x(self):
        return self.rect.x
    def player_pos_y(self):
        return self.rect.y
    def hold_s(self, x, y, crouch):
        if crouch == False:
            self.rect = pygame.rect.Rect(x, y, 16, 16)
            self.rect.y += 16
        else:
            self.rect = pygame.rect.Rect(x, self.rect.y, 16, 16)
        crouch = True
        return crouch

    def nhold_s(self, x, y, crouch): #stoppar krypläge
        crouch = False
        self.rect = pygame.rect.Rect(x, y, 16, 32)
        return crouch

