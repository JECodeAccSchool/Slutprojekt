import pygame
import random
import math
import pygame
import Wall
import Particle

class Enemy(object):
    def __init__(self, typ, pos_x, pos_y, index):
        enemies.append(self)
        self.rect = pygame.rect.Rect(pos_x, pos_y, 16, 16)
        self.rect_dam = pygame.rect.Rect(pos_x + 8, pos_y + 8, 16, 16)
        self.type = typ
        self.health = 100
        self.speed = 10
        self.damage = 1
        self.mom_v = 0
        self.index = index
        self.color = (255, 100, 100)
        self.timer = 0

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        #kollision med partiklar samt döda rätt fiende vid träff
        for part in Particle.particles:
            if self.timer < 0:
                self.color = (255, 100, 100)
            if self.rect.colliderect(part.rect) and self.timer < 0:
                self.health -= 30
                self.color = (255, 255, 255)
                self.timer = 25
            if self.health < 0:
                p = 0
                for n in range(len(enemies)):
                    print(n)
                    if enemies[n - p].index == self.index:
                        del enemies[n]
                        p += 1
        self.timer -= 1


    def track(self, p_pos_x, p_pos_y):
        if self.rect.x < p_pos_x:
            saved_pos = self.rect.x
            self.move(3, 0)
            if saved_pos == self.rect.x and self.move_single_axis(0, self.mom_v):
                self.mom_v = -5
        if self.rect.x > p_pos_x:
            saved_pos = self.rect.x
            self.move(-3, 0)
            if saved_pos == self.rect.x and self.move_single_axis(0, self.mom_v):
                self.mom_v = -5
        saved_pos = " "

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
                    self.ground = True
                    return True
                else:
                    return False
                    self.ground = False




enemies = []
