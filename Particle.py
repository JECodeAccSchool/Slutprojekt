from contextlib import nullcontext

import pygame
import random
import math


class Particle(object):
    def __init__(self, spe, pos_x, pos_y, col, ang, type, decay):
        self.rect = pygame.rect.Rect(pos_x, pos_y, 4, 4)
        self.angle = ang
        self.type = type
        self.decay = decay #timer tills partikeln försvinner för att spara resurser
        if type == "trail":
            part_trail.append(self)
        else:
            if type == "bullet":
                particles.append(self)


    def move(self, spe, ang):
        self.rect.x += spe * math.sin(ang)
        self.rect.y += spe * math.cos(ang)
        rand = random.Random()
        if self.type == "trail":
            self.rect.y += 0.03 * rand.random() * math.pow(100 - (self.decay - 200) / 3, 2)
        if self.decay < 0:
            if self.type == "bullet":
                print(particles)
                particles.pop()
            if self.type == "trail":
                part_trail.pop()
        else:
            self.decay -= 1

    def reval(self, val): #ge partikelns specifierade värde
        if val == "ang":
            return self.angle
        if val == "type":
            return self.type
        if val == "decay":
            return self.decay



particles = []
part_trail = []