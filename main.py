import random
import math
import time

import Enemy
import pygame
import Particle
import Wall
import Player

def load_room(rx, ry): #ritar alla kvadrater enligt rum-arrayerna
    Wall.walls = []
    x = y = 0
    for row in rooms[rx + 5 * ry]:
        for col in row:
            if col == "5":
                Wall.Wall((x, y), "wall")
            if col == "6":
                Wall.Wall((x, y), "solid_front_wall", )
            if col == "7":
                Wall.Wall((x, y), "front_wall", )
            if col == "4":
                Wall.Wall((x, y), "back_wall", )
            if col == "3":
                Wall.Wall((x, y), "back_wall_2", )
            if col == "2":
                Wall.Wall((x, y), "back_wall_3", )
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
rx = 2
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
switch_timer = 0



#alla rum
roomTEST = [
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"55555                                                                      55555",
"5555555555                 55555   55555   55555   55555   55555           55555",
"5555555555                 5   5   5   5   5   5   5   5   5   5           55555",
"5555555555                 5 n 5   5 l 5   5 f 5   5 r 5   5 b 5           55555",
"5555555555                 5   5   5   5   5   5   5   5   5   5           55555",
"5555555555                 55555   55555   55555   55555   55555           55555",
"55555                                                                      55555",
"55555                                                                      55555",
"555555555555555                                                            55555",
"555555555555555                                                            55555",
"555555555555555                                                            55555",
"555555555555555                                                            55555",
"555555555555555                                                            55555",
"555555555555555                                                            55555",
"55555                                                                      55555",
"55555                                                                      55555",
"555555555555555555555                                                      55555",
"555555555555555555555                                                      55555",
"555555555555555555555                                                      55555",
"55555      5555555555                                                      55555",
"55555      5555555555                                                      55555",
"55555      5555555555                                                      55555",
"55555      5555555555                                                      55555",
"55555      5555555555                                                      55555",
"55555                                    5555                              55555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555"
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
"55555555555555555555555                                                         ",
"55555555555555555555555                                                         ",
"55555555555555555555555                                                         ",
"55555555555555555555555                                                         ",
"555555555555555555555555                                                        ",
"555555555555555555555555                                                        ",
"555555555555555555555555                                                        ",
"555555555555555555555555                                                        ",
"5555555555555555555555555                                                       ",
"555555555555555555555555555                                                     ",
"555555555555555555555555555555                                                  ",
"5555555555555555555555555555555555       555                                    ",
"5555555555555555555555555555555555       5555555                                ",
"55555555555555555555555555555555555       5555555                               ",
"55555555555555555555555555555555555      55555555555                            ",
"5555555555555555555555555555555555555555555555555555555                         ",
"5555555555555555555555555555555555555555555555555555555555                      ",
"555555555555555555555555555555555555555555555555555555555555                    ",
"555555555555555555555555555555555555555555555555555555555555                    ",
"55555555555555555555555555555555555555555555555555555555555555                  ",
"555555555555555555555555555555555555555555555555555555555555555555              ",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555"
]

room41 = [
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                           44                                   ",
"                                           444                                  ",
"                                           444                                  ",
"                                          5544                                  ",
"                                           4444                                 ",
"                                          444444                                ",
"                                          444444                                ",
"                                          444444                                ",
"                                          444444                                ",
"                                          444444                                ",
"                                          444444                                ",
"                                          444444                                ",
"                                         4444444                                ",
"                                         44444555                               ",
"                                         4444444                                ",
"                                         4444444                                ",
"                                         4444444                                ",
"                                         4444444                                ",
"                                         4444444                                ",
"                                         4444444                                ",
"                                 55555   4444444                                ",
"                               55555555554444444                                ",
"                              555555555555554444                                ",
"                              555555555555555444                                ",
"                             5555555555555555444                                ",
"                     4444  555555555555555555444                                ",
"                  4444444455555555555555555555444                               ",
"              44444444444555555555555555555555544                               ",
"            4444444444444555555555555555555555554                               ",
"           44444444444455555555555555555555555555                               ",
"        44444444444555555555555555555555555555555                               ",
"555555555555555555555555555555555555555555555555555                             ",
"55555555555555555555555555555555555555555555555555555555555555                  ",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555"
]

room42 = [
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"      6666666       2                                                           ",
"      77777764      2                                                           ",
"      777777643    2   2                                                         ",
"      77777764333  2 22                2  2                                     ",
"      777777643333222                 2  22                                     ",
"      77777764333322222      222      2 2 2                                     ",
"      777777643333222222    222222    22  2                                     ",
"      777777666333222222    2222222   2  2                                      ",
"      7777776644332222222   2222222  22 22                                      ",
"      7777776443332222222  222222222 2 2 2                                      ",
"      7777776433332222222  22222222222  2                                       ",
"      7777776433332222222  222222222222 2                                       ",
"      77777764333322222222 22222222222222                                       ",
"      77777764333322222222 22222222222222                                       ",
"      77777764333322222222 22222222222222                                       ",
"      77777766643322222222 222222222222222                                      ",
"      77777766433322222222 222222222222552                                      ",
"      77777764333322222222 2225522222242224                                     ",
"      77777764333322222222 2222242222424442                                     ",
"      7777776433332222222222222224224242222                                     ",
"      7777776433332222222222222224224422222                        44444        ",
"  2   77777764333322222222222222242242222222              4444     466666       ",
"   2 277777764443322222222222222224242222222  b          555 444   477777       ",
"   22 77777776633322222222222222222422222222 4444444    777    4444477777       ",
"    2 77777776333322222222222554222422222222 6666666    77444444444477777444444 ",
"    2 7777777433332222222222222244242222222227777777  47744444444444777774444444",
"     27777777433332222222222222222422222222227777777 447744444444444777774444444",
"     277777774333322222222222222224244222222277777774447774444444444777774444444",
"     277777774333322222222222222224422222222277777774444777444444444777774444444",
"      77777774333322222222222222242222222244477777774444777444444444777774444444",
"44444477777774333322222222222222242222224444477777774444774444444444777774444444",
"44444477777774444422222222222222444444555544477777774444777444444444777774444444",
"55555566666674444444444444455555555555555555566666665555567744444445666665555555",
"55555566666665555544444555555555555555555555566666665555555655555555666665555555",
"55555566666665555555555555555555555555555555566666665555556655555555666665555555",
"55555566666665555555555555555555555555555555566666665555566555555555666665555555"
]

room43 = [
"                                        4                                       ",
"                                        4                                       ",
"                                        4                                       ",
"                                       4                                        ",
"                                       4                                        ",
"                                       4                                        ",
"                                       4                                        ",
"                                       4                                        ",
"                                      4                                         ",
"                                      4                                         ",
"                                      4                                         ",
"                                      4                                         ",
"                                      4                                         ",
"                                     4                                          ",
"                                     4                                          ",
"                                     4                                          ",
"                                     4                                          ",
"                                     4                                          ",
"                                    4                                           ",
"                                    4                                           ",
"                                    4                                           ",
"                                    4                                           ",
"                                    4                                           ",
"                                   4                                            ",
"                                   4                                            ",
"                                   4                                            ",
"    444444                         4                                            ",
"   6666664                         4                                            ",
"   7777774                        4                                             ",
"   7777774                        4                                             ",
"   7777774                        4                                             ",
"   7777774                       4                                              ",
"   7777774                       4                                   55555555555",
"   7777774                       4                       55555555555555555555555",
"   7777774                      4                5555555555555555555555555555555",
"   7777774                      4            55555555555555555555555555555555555",
"   7777774               5555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555"
]

room44 = [
"                                                                     55555555555",
"                                                                     55555555555",
"                                                                        55555555",
"                                                     555444444455555555555555555",
"                                                      4 4              W55555555",
"                                                      4  4             W55555555",
"                                                      4   4            W55555555",
"                                                      4    5            55555555",
"                                                      4     4           55555555",
"                                                      4      4          55555555",
"                                                      4       4         55555555",
"                                                     555555555544444455555555555",
"                                                                    4   55555555",
"                                                                   4    55555555",
"                                                                  4     55555555",
"                                                                 5      55555555",
"                                                                4       55555555",
"                                                                4       55555555",
"                                                                        55555555",
"                                                                 555555555555555",
"                                                                       555555555",
"                                                                       555555555",
"                                                               554    5555555555",
"                                                             544    555555555555",
"                                                      4   554   5555555555555555",
"                                                      4  544  555555555555555555",
"                                                      4 545555555555555555555555",
"                                                      55555555555555555555555555",
"                                           5555555555555555555555555555555555555",
"                                       55555555555555555555555555555555555555555",
"                     55555555555555555555555555555555555555555555555555555555555",
"        555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555",
"55555555555555555555555555555555555555555555555555555555555555555555555555555555"
]


#rummen i ett koordinatsystem
rooms = ["room00", "room01", "room02", "room03", "room04",
         "room10", "room11", "room12", "room13", "room14",
         "room20", "room21", "room22", "room23", "room24",
         "room30", "room31", "room32", "room33", "room34",
         room40, room41, room42, room43, room44, roomTEST]

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
        mouse_ang = 2 * math.pi / 2

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
                Particle.Particle(player.player_pos_x() + 8, player.player_pos_y() + 16, mouse_ang, "bullet", 50, len(Particle.particles))
                shot_timer = 60
        if weapon_mode == "blast":
            if shot_timer < 0:
                for n in range(17):
                    Particle.Particle(player.player_pos_x() + 8, player.player_pos_y() + 16, mouse_ang - (math.pi / 16) + n * math.pi / 128, "blast", 50, len(Particle.particles))
                shot_timer = 120

    if keys[pygame.K_r]:
        if switch_timer < 0:
            if weapon_mode == "normal":
                weapon_mode = "blast"
            else:
                if weapon_mode == "blast":
                    weapon_mode = "normal"
            switch_timer = 10


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

    for wall in Wall.walls:
        if wall.type == "back_wall_3":
            pygame.draw.rect(screen, wall.color, wall.rect)

    for wall in Wall.walls:
        if wall.type == "back_wall_2":
            pygame.draw.rect(screen, wall.color, wall.rect)

    for wall in Wall.walls:
        if wall.type == "back_wall":
            pygame.draw.rect(screen, wall.color, wall.rect)

    #spelar-sprajten
    pygame.draw.rect(screen, (255, 255, 255), player.rect)

    #fiender
    for enem in Enemy.enemies:
        pygame.draw.rect(screen, enem.color, enem.rect)

    for part in Particle.particles:
        if part.type == "bullet":
            Particle.Particle.move(part, 10, Particle.Particle.reval(part, "ang"), True)
            for enem in Enemy.enemies:
                enem.move(0, 0)
            Particle.Particle.move(part, 10, Particle.Particle.reval(part, "ang"), False)
            for enem in Enemy.enemies:
                enem.move(0, 0)
            Particle.Particle.move(part, 10, Particle.Particle.reval(part, "ang"), False)
            pygame.draw.circle(screen, (255, 255, 255), (part.rect.x, part.rect.y), 4)
        if part.type == "blast":
            Particle.Particle.move(part, 5, Particle.Particle.reval(part, "ang"), True)
            for enem in Enemy.enemies:
                enem.move(0, 0)
            Particle.Particle.move(part, 5, Particle.Particle.reval(part, "ang"), False)
            for enem in Enemy.enemies:
                enem.move(0, 0)
            Particle.Particle.move(part, 5, Particle.Particle.reval(part, "ang"), False)
            pygame.draw.circle(screen, (255, 0, 0), (part.rect.x, part.rect.y), 0 + part.decay / 10)

        if Particle.Particle.reval(part, "type") == "bullet":
            Particle.Particle(part.rect.x, part.rect.y, mouse_ang, "trail", 500, len(Particle.particles))
            for n in range(5):
                end_pos_bul_1 = pygame.Vector2(part.rect.x + rand.randint(-5, 5) * 2, part.rect.y + rand.randint(-5, 5) * 2)
                end_pos_bul_2 = pygame.Vector2(end_pos_bul_1.x + rand.randint(-5, 5) * 2, end_pos_bul_1.y + rand.randint(-5, 5) * 2)
                pygame.draw.line(screen, (255, 255, 0), (part.rect.x, part.rect.y), end_pos_bul_1, 2)
                pygame.draw.line(screen, (255, 255, 0), end_pos_bul_1, end_pos_bul_2, 1)

        if Particle.Particle.reval(part, "type") == "blast":
            for n in range(1):
                print(part.angle)
                end_pos_bla_1 = pygame.Vector2(part.rect.x - 10 * math.atan(part.angle), part.rect.y - 10 * math.atan(part.angle))
                pygame.draw.line(screen, (255, 0, 0), (part.rect.x, part.rect.y), end_pos_bla_1, 0 + int(part.decay))

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
        if wall.type == "wall":
            pygame.draw.rect(screen, wall.color, wall.rect)

    for wall in Wall.walls:
        if wall.type == "front_wall":
            pygame.draw.rect(screen, wall.color, wall.rect)

    for wall in Wall.walls:
        if wall.type == "solid_front_wall":
            pygame.draw.rect(screen, wall.color, wall.rect)


    #visa omladdning av shot
    if shot_timer >= 0:
        if weapon_mode == "normal":
            rect = pygame.Rect(50, 50, shot_timer * 2, 20)
            cd_rect = pygame.draw.rect(screen, (255, 255, 255), rect)
        if weapon_mode == "blast":
            rect = pygame.Rect(50, 50, shot_timer, 20)
            cd_rect = pygame.draw.rect(screen, (255, 155, 155), rect)


    switch_timer -= 1

    pygame.display.flip()

    #fps samt tickspeed
    dt = clock.tick(60) / 1000





pygame.quit()