import pygame
import random

class Wall(object):

    def __init__(self, pos, type):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        rand = random.Random()
        color_val = 15 * rand.random()
        if type == "wall":
            self.type = "wall"
            self.color = (200 + color_val, 200 + color_val, 200 + color_val)
            self.collide_on = True
        if type == "back_wall":
            self.type = "back_wall"
            self.color = (150 + color_val / 3, 150 + color_val / 3, 150 + color_val / 3)
            self.collide_on = False
        if type == "front_wall":
            self.type = "front_wall"
            self.color = (220 + color_val / 3, 220 + color_val / 3, 220 + color_val / 3)
            self.collide_on = False
        if type == "solid_front_wall":
            self.type = "solid_front_wall"
            self.color = (220 + color_val / 3, 220 + color_val / 3, 220 + color_val / 3)
            self.collide_on = True
        if type == "back_wall_2":
            self.type = "back_wall_2"
            self.color = (80 + color_val / 3, 80 + color_val / 3, 80 + color_val / 3)
            self.collide_on = False
        if type == "back_wall_3":
            self.type = "back_wall_3"
            self.color = (40 + color_val / 3, 40 + color_val / 3, 40 + color_val / 3)
            self.collide_on = False


walls = []