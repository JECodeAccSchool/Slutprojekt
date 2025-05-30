import random
import math

import Enemy

import Detail_back
import pygame

import Detail_front
import Particle
import Wall
import Player

def load_room(rx, ry): #ritar alla kvadrater enligt rum-arrayerna
    Wall.walls = []
    Detail_back.det_backs = []
    Detail_front.det_fronts = []
    x = y = 0
    for row in rooms[rx + 5 * ry]:
        for col in row:
            if col == "W":
                Wall.Wall((x, y), "mid")
            if col == "V":
                Wall.Wall((x, y), "front")
            if col == "F":
                Detail_front.Detail_front((x, y))
            if col == "B":
                Detail_back.Detail_back((x, y))
            if col == "n":
                load_enemy("normal", x, y)
            if col == "l":
                load_enemy("large", x, y)
            if col == "f":
                load_enemy("flying", x, y)
            if col == "r":
                load_enemy("ranged", x, y)
            if col == "b":
                load_enemy("boss", x, y)
            x += 16
        y += 16
        x = 0

def load_enemy(type, pos_x, pos_y):
    Enemy.Enemy(type, pos_x, pos_y, len(Enemy.enemies))

pygame.init()


#variabler
screen = pygame.display.set_mode((1280, 660))
clock = pygame.time.Clock()
running = True
dt = 0
rx = 5
ry = 4
grounded = False
grounded1 = False
crouchval = False
checkground1 = 0
checkground2 = 0
gravity = 20
shot_timer = 0
screen = pygame.display.set_mode((screen.get_width(), screen.get_height()))
player = Player.Player()
player_mom_vert = 0
rand = random.Random()
mouse_ang = 0
cursor_pos = (0, 0)
rect = pygame.Rect(50, 50, 0, 20)
saved_pos_1 = pygame.Vector2(0, 0)
color_var = 0
weapon_mode = "normal"



#alla rum
roomTEST = [
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWWWWWWW                 WWWWW   WWWWW   WWWWW   WWWWW   WWWWW           WWWWW",
"WWWWWWWWWW                 W   W   W   W   W   W   W   W   W   W           WWWWW",
"WWWWWWWWWW                 W n W   W l W   W f W   W r W   W b W           WWWWW",
"WWWWWWWWWW                 W   W   W   W   W   W   W   W   W   W           WWWWW",
"WWWWWWWWWW                 WWWWW   WWWWW   WWWWW   WWWWW   WWWWW           WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWWWWWWWWWWWW                                                            WWWWW",
"WWWWWWWWWWWWWWW                                                            WWWWW",
"WWWWWWWWWWWWWWW                                                            WWWWW",
"WWWWWWWWWWWWWWW                                                            WWWWW",
"WWWWWWWWWWWWWWW                                                            WWWWW",
"WWWWWWWWWWWWWWW                                                            WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWW                                                                      WWWWW",
"WWWWWWWWWWWWWWWWWWWWW                                                      WWWWW",
"WWWWWWWWWWWWWWWWWWWWW                                                      WWWWW",
"WWWWWWWWWWWWWWWWWWWWW                                                      WWWWW",
"WWWWW      WWWWWWWWWW                                                      WWWWW",
"WWWWW      WWWWWWWWWW                                                      WWWWW",
"WWWWW      WWWWWWWWWW                                                      WWWWW",
"WWWWW      WWWWWWWWWW                                                      WWWWW",
"WWWWW      WWWWWWWWWW                                                      WWWWW",
"WWWWW                                    WWWW                              WWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

room40 = [
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"WWWWWWWWWWWWWWWWWWWWWWW                                                         ",
"WWWWWWWWWWWWWWWWWWWWWWW                                                         ",
"WWWWWWWWWWWWWWWWWWWWWWW                                                         ",
"WWWWWWWWWWWWWWWWWWWWWWW                                                         ",
"WWWWWWWWWWWWWWWWWWWWWWWW                                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWW                                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWW                                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWW                                                        ",
"WWWWWWWWWWWWWWWWWWWWWWWWW                                                       ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWW                                                     ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                                                  ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       WWW                                    ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       WWWWWWW                                ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       WWWWWWW                               ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      WWWWWWWWWWW                            ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                         ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                      ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                    ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                    ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                  ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW              ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW    F"
]

room41 = [
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                           BB                                   ",
"                                           BBB                                  ",
"                                           BBB                                  ",
"                                          WWBB                                  ",
"                                           BBBB                                 ",
"                                          BBBBBB                                ",
"                                          BBBBBB                                ",
"                                          BBBBBB                                ",
"                                          BBBBBB                                ",
"                                          BBBBBB                                ",
"                                          BBBBBB                                ",
"                                          BBBBBB                                ",
"                                         BBBBBBB                                ",
"                                         BBBBBWWW                               ",
"                                         BBBBBBB                                ",
"                                         BBBBBBB                                ",
"                                         BBBBBBB                                ",
"                                         BBBBBBB                                ",
"                                         BBBBBBB                                ",
"                                         BBBBBBB                                ",
"                                 WWWWW   BBBBBBB                                ",
"                               WWWWWWWWWWBBBBBBB                                ",
"                              WWWWWWWWWWWWWWBBBB                                ",
"                              WWWWWWWWWWWWWWWBBB                                ",
"                             WWWWWWWWWWWWWWWWBBB                                ",
"                     BBBB  WWWWWWWWWWWWWWWWWWBBB                                ",
"                  BBBBBBBBWWWWWWWWWWWWWWWWWWWWBBB                               ",
"              BBBBBBBBBBBWWWWWWWWWWWWWWWWWWWWWWBB                               ",
"            BBBBBBBBBBBBBWWWWWWWWWWWWWWWWWWWWWWWB                               ",
"           BBBBBBBBBBBBWWWWWWWWWWWWWWWWWWWWWWWWWW                               ",
"        BBBBBBBBBBBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                               ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                             ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                  ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW    F"
]

room42 = [
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"      VVVVVVV                                                                   ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                   n                                              ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVVV                                                                 ",
"      FFFFFFVVBB                                                                ",
"      FFFFFFVBB                                                                 ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVB                                                                  ",
"      FFFFFFVVVB                                                                ",
"      FFFFFFVVB                        WW                                       ",
"      FFFFFFVB                WW      B   B                                     ",
"      FFFFFFVB                  B    B BBB                                      ",
"      FFFFFFVB                   B  B B                                         ",
"      FFFFFFVB                   B  BB                             BBBBB        ",
"      FFFFFFVB                   B  B                     BBBB     BVVVVV       ",
"      FFFFFFVBBB                  B B                    WWW BBB   BFFFFF       ",
"      FFFFFFVVV                    B         BBBBBBB    FFF    BBBBBFFFFF       ",
"      FFFFFFFV               WWB   B         VVVVVVV    FFBBBBBBBBBBFFFFFBBBBBB ",
"      FFFFFFFB                  BB B         FFFFFFF  BFFBBBBBBBBBBBFFFFFBBBBBBB",
"      FFFFFFFB                    B          FFFFFFF BBFFBBBBBBBBBBBFFFFFBBBBBBB",
"      FFFFFFFB                    B BB       FFFFFFFBBBFFFBBBBBBBBBBFFFFFBBBBBBB",
"      FFFFFFFB                    BB         FFFFFFFBBBBFFFBBBBBBBBBFFFFFBBBBBBB",
"      FFFFFFFB                   B        BBBFFFFFFFBBBBFFFBBBBBBBBBFFFFFBBBBBBB",
"BBBBBBFFFFFFFB                   B      BBBBBFFFFFFFBBBBFFBBBBBBBBBBFFFFFBBBBBBB",
"BBBBBBFFFFFFFBBBBB              BBBBBBWWWWBBBFFFFFFFBBBBFFFBBBBBBBBBFFFFFBBBBBBB",
"WWWWWWVVVVVVFBBBBBBBBBBBBBBWWWWWWWWWWWWWWWWWWVVVVVVVWWWWWVFFBBBBBBBWVVVVVWWWWWWW",
"WWWWWWVVVVVVVWWWWWBBBBBWWWWWWWWWWWWWWWWWWWWWWVVVVVVVWWWWWWWVWWWWWWWWVVVVVWWWWWWW",
"WWWWWWVVVVVVVWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWVVVVVVVWWWWWWVVWWWWWWWWVVVVVWWWWWWW",
"WWWWWWVVVVVVVWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWVVVVVVVWWWWWVVWWWWWWWWWVVVVVWWWWWWW"
]

room43 = [
"                                        B                                       ",
"                                        B                                       ",
"                                        B                                       ",
"                                       B                                        ",
"                                       B                                        ",
"                                       B                                        ",
"                                       B                                        ",
"                                       B                                        ",
"                                      B                                         ",
"                                      B                                         ",
"                                      B                                         ",
"                                      B                                         ",
"                                      B                                         ",
"                                     B                                          ",
"                                     B                                          ",
"                                     B                                          ",
"                                     B                                          ",
"                                     B                                          ",
"                                    B                                           ",
"                                    B                                           ",
"                                    B                                           ",
"                                    B                                           ",
"                                    B                                           ",
"                                   B                                            ",
"                                   B                                            ",
"                                   B                                            ",
"    BBBBBB                         B                                            ",
"   VVVVVVB                         B                                            ",
"   FFFFFFB                        B                                             ",
"   FFFFFFB                        B                                             ",
"   FFFFFFB                        B                                             ",
"   FFFFFFB                       B                                              ",
"   FFFFFFB                       B                                   WWWWWWWWWWW",
"   FFFFFFB                       B                       WWWWWWWWWWWWWWWWWWWWWWW",
"   FFFFFFB                      B                WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"   FFFFFFB                      B            WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"   FFFFFFB               WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

room44 = [
"                                                                     WWWWWWWWWWW",
"                                                                     WWWWWWWWWWW",
"                                                                        WWWWWWWW",
"                                                     WWWBBBBBBBWWWWWWWWWWWWWWWWW",
"                                                      B B              WWWWWWWWW",
"                                                      B  B             WWWWWWWWW",
"                                                      B   B            WWWWWWWWW",
"                                                      B    W            WWWWWWWW",
"                                                      B     B           WWWWWWWW",
"                                                      B      B          WWWWWWWW",
"                                                      B       B         WWWWWWWW",
"                                                     WWWWWWWWWWBBBBBBWWWWWWWWWWW",
"                                                                    B   WWWWWWWW",
"                                                                   B    WWWWWWWW",
"                                                                  B     WWWWWWWW",
"                                                                 W      WWWWWWWW",
"                                                                B       WWWWWWWW",
"                                                                B       WWWWWWWW",
"                                                                        WWWWWWWW",
"                                                                 WWWWWWWWWWWWWWW",
"                                                                       WWWWWWWWW",
"                                                                       WWWWWWWWW",
"                                                               WWB    WWWWWWWWWW",
"                                                             WBB    WWWWWWWWWWWW",
"                                                      B   WWB   WWWWWWWWWWWWWWWW",
"                                                      B  WBB  WWWWWWWWWWWWWWWWWW",
"                                                      B WBWWWWWWWWWWWWWWWWWWWWWW",
"                                                      WWWWWWWWWWWWWWWWWWWWWWWWWW",
"                                           WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"                                       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"                     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"        WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]


#rummen i ett koordinatsystem
rooms = ["room00", "room01", "room02", "room03", "room04",
         "room10", "room11", "room12", "room13", "room14",
         "room20", "room21", "room22", "room23", "room24",
         "room30", "room31", "room32", "room33", "room34",
         "room40", "room41", "room42", "room43", "room44", roomTEST]

load_room(rx, ry)

while running:
    #töm skärmen
    screen.fill("black")

    #byt rum vid kanter och ladda rum samt ta bort saker
    if player.rect.x < 10:
        player.rect.x = 1260
        rx -= 1
        Particle.particles = []
        Particle.part_trail = []
        Enemy.enemies = []
        load_room(rx, ry)
    if player.rect.x > 1270:
        player.rect.x = 20
        rx += 1
        Particle.particles = []
        Particle.part_trail = []
        Enemy.enemies = []
        load_room(rx, ry)
    if player.rect.y < 10:
        player.rect.y = 640
        ry -= 1
        Particle.particles = []
        Particle.part_trail = []
        Enemy.enemies = []
        load_room(rx, ry)
    if player.rect.y > 650:
        player.rect.y = 20
        ry += 1
        Particle.particles = []
        Particle.part_trail = []
        Enemy.enemies = []
        load_room(rx, ry)


    #första check för att man står stilla på marken,
    #för att ens momentum inte ska sparas tills när man går av en kant igen


    #lämna spel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #hitta vinkel till musen från spelaren
    cursor_pos = pygame.Vector2(pygame.mouse.get_pos())
    if (cursor_pos.x - (player.player_pos_x() + 8)) != 0:

        mouse_ang = -(math.atan((cursor_pos.y - (player.player_pos_y() + 16)) / (cursor_pos.x - (player.player_pos_x() + 8))) + math.pi / 2)
        if (cursor_pos.x - player.player_pos_x()) > 0:
            mouse_ang = (math.atan(((player.player_pos_y() + 16) - cursor_pos.y) / (cursor_pos.x - (player.player_pos_x() + 8))) + math.pi / 2)
    else:
        mouse_ang = 3 * math.pi / 2

    #gravitation och luftmotstånd
    player.move(0, player_mom_vert)
    player_mom_vert *= 0.98 #luftmotstånd
    player_mom_vert += 0.7 #gravitation
    if player.move_single_axis(0, player_mom_vert):
        player_mom_vert = 3

    for enem in Enemy.enemies:
        if enem.type != "flying":
            enem.move(0, enem.mom_v)
            enem.mom_v *= 0.98
            enem.mom_v += 0.7
            if enem.move_single_axis(0, enem.mom_v):
                enem.mom_v = 3
        enem.track(player.player_pos_x(), player.player_pos_y())





    #timer för att skjuta
    shot_timer -= 1

    #kontroller
    keys = pygame.key.get_pressed()
    #krypläge
    if keys[pygame.K_s]:
        player.hold_s(player.player_pos_x(), player.player_pos_y(), crouchval)
        crouchval = True
    else:
        player.nhold_s(player.player_pos_x(), player.player_pos_y(), crouchval)
        crouchval = False

    #skicka en partikel mot musen
    if keys[pygame.K_f]:
        if weapon_mode == "normal":
            if shot_timer < 0:
                Particle.Particle(player.player_pos_x() + 8, player.player_pos_y() + 16, mouse_ang, "bullet", 50)
                shot_timer = 120

    if keys[pygame.K_a]:
        if crouchval == False:
            player.move(-10, 0)
        else:
            player.move(-3, 0)

    if keys[pygame.K_d]:
        if crouchval == False:
            player.move(10, 0)
        else:
            player.move(3, 0)
    #hoppa
    if keys[pygame.K_w] and (player.move_single_axis(0, player_mom_vert) == True):
        player_mom_vert = -10

    #utseenden och ordning på objekt: längre ner --> överst på skärmen
    for det_b in Detail_back.det_backs:
        pygame.draw.rect(screen, (150, 150, 150), det_b.rect)

    #spelar-sprajten
    pygame.draw.rect(screen, (255, 255, 255), player.rect)

    #fiender
    for enem in Enemy.enemies:
        pygame.draw.rect(screen, enem.color, enem.rect)

    for part in Particle.particles:
        Particle.Particle.move(part, 10, Particle.Particle.reval(part, "ang"), True)
        for enem in Enemy.enemies:
            enem.move(0, 0)
        Particle.Particle.move(part, 10, Particle.Particle.reval(part, "ang"), False)
        for enem in Enemy.enemies:
            enem.move(0, 0)
        Particle.Particle.move(part, 10, Particle.Particle.reval(part, "ang"), False)
        pygame.draw.circle(screen, (255, 255, 255), (part.rect.x, part.rect.y), 4)
        if Particle.Particle.reval(part, "type") == "bullet":
            Particle.Particle(part.rect.x, part.rect.y, mouse_ang, "trail", 500)
            for n in range(5):
                end_pos_bul_1 = pygame.Vector2(part.rect.x + rand.randint(-5, 5) * 2, part.rect.y + rand.randint(-5, 5) * 2)
                end_pos_bul_2 = pygame.Vector2(end_pos_bul_1.x + rand.randint(-5, 5) * 2, end_pos_bul_1.y + rand.randint(-5, 5) * 2)
                pygame.draw.line(screen, (255, 255, 0), (part.rect.x, part.rect.y), end_pos_bul_1, 2)
                pygame.draw.line(screen, (255, 255, 0), end_pos_bul_1, end_pos_bul_2, 1)


    for part in Particle.part_trail:
        pygame.draw.circle(screen, (255, 255, 0), (part.rect.x, part.rect.y), 0)
        if saved_pos_1 != (0, 0) and not (math.sqrt(math.pow(saved_pos_1.x - part.rect.x, 2) + math.pow(saved_pos_1.y - part.rect.y, 2))) > 100:
            if not Particle.Particle.reval(part, "decay") < 0:
                trail_var = Particle.Particle.reval(part, "decay") - 200

            else:
                trail_var = 0
            color_r = 255 - math.pow((300 - trail_var), 2)
            if color_r < 105:
                color_r = 105
            color_g = 255 - math.pow((300 - trail_var), 2)
            if color_g < 105:
                color_g = 105
            color_b = math.pow((300 - trail_var), 2)
            if color_b > 105:
                color_b = 105
            pygame.draw.line(screen, (color_r, color_g, color_b), saved_pos_1, (part.rect.x, part.rect.y), (int(5 * (trail_var / 100)) - 6))
        saved_pos_1 = pygame.Vector2(part.rect.x, part.rect.y)
        Particle.Particle.move(part, 0, 0, True)

    #vapen samt rotation av vapnet
    pygame.draw.polygon(screen, (120, 120, 120), ((player.player_pos_x() + 8 + 12 * math.sin(mouse_ang), player.player_pos_y() + 16 + 12 * math.cos(mouse_ang - math.pi / 12)),
                                                                (player.player_pos_x() + 8 - 12 * math.sin(mouse_ang + math.pi / 8), player.player_pos_y() + 16 - 12 * math.cos(mouse_ang + math.pi / 12)),
                                                                (player.player_pos_x() + 8 - 12 * math.sin(mouse_ang), player.player_pos_y() + 16 - 12 * math.cos(mouse_ang - math.pi / 12)),
                                                                (player.player_pos_x() + 8 + 12 * math.sin(mouse_ang + math.pi / 8), player.player_pos_y() + 16 + 12 * math.cos(mouse_ang + math.pi / 12))))

    for wall in Wall.walls:
        if wall.color == "mid":
            pygame.draw.rect(screen, (200, 200, 200), wall.rect)
        if wall.color == "front":
            pygame.draw.rect(screen, (220, 220, 220), wall.rect)

    for det_f in Detail_front.det_fronts:
        pygame.draw.rect(screen, (220, 220, 220), det_f.rect)


    print(mouse_ang)
    #visa omladdning av skott
    if shot_timer >= 0:
        rect = pygame.Rect(50, 50, shot_timer, 20)
    cd_rect = pygame.draw.rect(screen, (255, 255, 255), rect)

    pygame.display.flip()

    #fps samt tickspeed
    dt = clock.tick(60) / 1000





pygame.quit()