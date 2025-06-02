import Wall
import Enemy
import pygame

class Player(object):

    def __init__(self):
        self.rect = pygame.rect.Rect(800, 400, 16, 32)
        self.crouch = False
        self.mom_v = 0
        self.health = 100
        self.i_frames = 0
        self.saved_vars = pygame.Vector2(0, 0)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        self.i_frames -= 1
        if self.i_frames < 0:
            self.i_frames = 0


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
                        self.health -= 5
                        self.i_frames += 10
                    if dx < 0:
                        self.health -= 5
                        self.i_frames += 10
                    if dy < 0:
                        self.health -= 5
                        self.i_frames += 10
                    if dy > 0:
                        self.health -= 5
                        self.i_frames += 10
        return self.health


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

