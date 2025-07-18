from contextlib import nullcontext
import pygame
import random
import math

class Particle(object):
    def __init__(self, pos_x, pos_y, ang, type, decay, index):
        self.index = index
        self.rect = pygame.rect.Rect(pos_x, pos_y, 4, 4)
        self.angle = ang
        self.type = type
        self.decay = decay #timer tills partikeln försvinner för att spara resurser
        if type == "blast": #används istället för en lista
            self.prev_pos = pygame.Vector2(0, 0)

        if type == "trail":
            part_trail.append(self)
        else:
            if type == "danger":
                enemy_bul.append(self)
            else:
                particles.append(self)




    #flytta på partikeln
    def move(self, spe, ang, d_on):
        if self.type == "blast" and d_on:
            self.prev_pos = pygame.Vector2(self.rect.x, self.rect.y)
        self.rect.x += spe * math.sin(ang)
        self.rect.y += spe * math.cos(ang)
        rand = random.Random()
        if self.type == "trail":
            self.rect.y += 0.03 * rand.random() * math.pow(100 - (self.decay - 200) / 3, 2)
        if self.decay <= 0 and d_on and not (self.type == "trail" or self.type == "danger"):
            p = 0
            for n in range(len(particles)):
                if particles[n - p].index == self.index:
                    del particles[n]
                    p += 1
        else:
            if d_on:
                self.decay -= 1
        if self.decay <= 0 and d_on:
            if self.type == "trail":
                part_trail.pop()
            if self.type == "danger":
                enemy_bul.pop()
        if self.type == "blast":
            deriv = 1
            deriv *= rand.randint(-1, 1)

            self.rect.x += deriv * rand.randint(-1, 1)
            self.rect.y += deriv * rand.randint(-1, 1)

    def reval(self, val): #ge partikelns specifierade värde
        if val == "ang":
            return self.angle
        if val == "type":
            return self.type
        if val == "decay":
            return self.decay
        if self.type == "blast" and val == "prepos":
            return self.prev_pos



particles = []
part_trail = []
enemy_bul = []