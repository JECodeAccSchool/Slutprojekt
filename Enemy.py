import random
import math
import pygame
import Wall
import Particle

class Enemy(object):
    def __init__(self, typ, pos_x, pos_y, index):
        enemies.append(self)
        self.type = typ
        if self.type == "normal":
            self.rect = pygame.rect.Rect(pos_x, pos_y, 16, 16)
            self.rect_dam = pygame.rect.Rect(pos_x + 8, pos_y + 8, 12, 12)
            self.health = 100
            self.speed = 3
            self.damage = 5
            self.mom_v = 0
            self.index = index
            self.color = (255, 100, 100)
            self.timer = 0

        if self.type == "large":
            self.rect = pygame.rect.Rect(pos_x, pos_y, 32, 32)
            self.rect_dam = pygame.rect.Rect(pos_x + 16, pos_y + 16, 24, 24)
            self.health = 150
            self.speed = 2
            self.damage = 10
            self.mom_v = 0
            self.index = index
            self.color = (255, 150, 100)
            self.timer = 0

        if self.type == "flying":
            self.rect = pygame.rect.Rect(pos_x, pos_y, 16, 16)
            self.rect_dam = pygame.rect.Rect(pos_x + 8, pos_y + 8, 16, 16)
            self.health = 50
            self.speed = 1
            self.damage = 4
            self.mom_v = 0
            self.index = index
            self.color = (0, 100, 200)
            self.timer = 0

        if self.type == "ranged":
            self.rect = pygame.rect.Rect(pos_x, pos_y, 16, 16)
            self.rect_dam = pygame.rect.Rect(pos_x + 8, pos_y + 8, 16, 16)
            self.health = 70
            self.speed = 4
            self.damage = 5
            self.mom_v = 0
            self.index = index
            self.color = (0, 200, 0)
            self.timer = 0

        if self.type == "boss":
            self.rect = pygame.rect.Rect(pos_x, pos_y, 16, 16)
            self.rect_dam = pygame.rect.Rect(pos_x + 8, pos_y + 8, 16, 16)
            self.health = 500
            self.speed = 4
            self.damage = 20
            self.mom_v = 0
            self.index = index
            self.color = (200, 200, 0)
            self.timer = 0

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        #kollision med partiklar samt döda rätt fiende vid träff
        for part in Particle.particles:
            if self.timer < 0:
                if self.type == "normal":
                   self.color = (255, 100, 100)
                if self.type == "large":
                   self.color = (255, 150, 100)
                if self.type == "flying":
                   self.color = (0, 100, 200)
                if self.type == "ranged":
                   self.color = (0, 200, 0)
                if self.type == "boss":
                   self.color = (200, 200, 0)
            if self.rect.colliderect(part.rect) and self.timer < 0:
                self.health -= 30
                self.color = (255, 255, 255)
                self.timer = 25
            if self.health < 0:
                p = 0
                for n in range(len(enemies)):
                    if enemies[n - p].index == self.index:
                        del enemies[n]
                        p += 1
        self.timer -= 1


    def track(self, p_pos_x, p_pos_y):
        if self.rect.x < p_pos_x:
            saved_pos = self.rect.x
            self.move(self.speed, 0)
            if saved_pos == self.rect.x and self.move_single_axis(0, self.mom_v):
                self.mom_v = -5
        if self.rect.x > p_pos_x:
            saved_pos = self.rect.x
            self.move(-self.speed, 0)
            if saved_pos == self.rect.x and self.move_single_axis(0, self.mom_v):
                self.mom_v = -5

        if self.type == "flying":
            if self.rect.y < p_pos_y:
                self.move(0, self.speed)
            if self.rect.y > p_pos_y:
                self.move(0, -self.speed)



    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        #kollision med väggar
        for wall in Wall.walls:
            if self.rect.colliderect(wall.rect) and wall.collide_on:
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
        for enem in enemies:
            if self.rect.colliderect(enem.rect) and self.index != enem.index:
                if dx > 0:
                    self.rect.right = enem.rect.left
                if dx < 0:
                    self.rect.left = enem.rect.right
                if dy < 0:
                    self.rect.top = enem.rect.bottom
                if dy > 0:
                    self.rect.bottom = enem.rect.top
                    self.ground = True
                    return True
                else:
                    return False




enemies = []
