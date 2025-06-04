import Wall
import Enemy
import pygame
import Particle

class Player(object):

    def __init__(self):
        self.rect = pygame.rect.Rect(800, 400, 16, 32)
        self.crouch = False
        self.mom_v = 0
        self.health = 100
        self.i_frames = 0
        self.saved_vars = pygame.Vector2(0, 0)
        players.append(self)
    def collide(self):
        dy = self.saved_vars.y
        for wall in Wall.walls:
            if self.rect.colliderect(wall.rect) and wall.collide_on:
                if dy < 0 or dy > 0:
                    return True
                else:
                    return False

    #flytta på spelaren
    def move(self, dx, dy, i_tick):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        if i_tick:
            self.i_frames -= 1
            if self.i_frames < 0:
                self.i_frames = 0

    #kolla efter kollision
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.saved_vars = pygame.Vector2(dx, dy)

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
                    return True
                else:
                    return False



    #funktioner som jag vill ta bort, men som redan används i specifika områden för att få information om spelaren
    #vill egentligen sätta ihop dessa funktioner till en enda som i partikelklassen
    def player_pos_x(self):
        return self.rect.x
    def player_pos_y(self):
        return self.rect.y
    def player_health(self):
        dx = self.saved_vars.x
        dy = self.saved_vars.y
        if self.i_frames <= 0:
            for enem in Enemy.enemies:
                if self.rect.colliderect(enem.rect) and self.i_frames <= 0:
                    if dx > 0:
                        self.health -= enem.damage
                        self.i_frames += 10
                    if dx < 0:
                        self.health -= enem.damage
                        self.i_frames += 10
                    if dy < 0:
                        self.health -= enem.damage
                        self.i_frames += 10
                    if dy > 0:
                        self.health -= enem.damage
                        self.i_frames += 10
            for part in Particle.enemy_bul:
                if self.rect.colliderect(part.rect) and self.i_frames <= 0:
                    if dx > 0:
                        self.health -= 10
                        self.i_frames += 10
                    if dx < 0:
                        self.health -= 10
                        self.i_frames += 10
                    if dy < 0:
                        self.health -= 10
                        self.i_frames += 10
                    if dy > 0:
                        self.health -= 10
                        self.i_frames += 10

        return self.health




    #minskar spelarens storlek och hastighet

players = []