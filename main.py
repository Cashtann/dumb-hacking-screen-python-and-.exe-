# from numpy.core.fromnumeric import choose
# author: Maciej Świtała AKA Cashtan
# there is a lot of trash code, this is my first "better" program

import pygame as pg
import numpy as np
from math import pi, sin, cos
from random import choice, randrange
from pygame.locals import *
import datetime
import sys

def hecker(heck):
    autor_surface = hackfont.render(choice(heck), True, (0,255,0))
    autor_rect = autor_surface.get_rect(center = (960,540))
    screen.blit(autor_surface, autor_rect)

napis1 = ''
napis2 = ''
napis3 = ''
napis4 = ''

########## FUNKCJE NAPISOW #########


def napis1display(main_game, napisl1, napis1):
    if napisl1 >= 10 and napisl1 < 20:
        napis1 = abc15
    elif napisl1 >= 20 and napisl1 < 30:
        napis1 = abc1
    elif napisl1 >= 30 and napisl1 < 40:
        napis1 = abc2
    elif napisl1 >= 40 and napisl1 < 50:
        napis1 = abc3
    elif napisl1 >= 50 and napisl1 < 60:
        napis1 = abc4
    elif napisl1 >= 60 and napisl1 < 70:
        napis1 = abc5
    elif napisl1 >= 70 and napisl1 < 80:
        napis1 = abc6
    elif napisl1 >= 80 and napisl1 < 90:
        napis1 = abc7
    elif napisl1 >= 90 and napisl1 < 100:
        napis1 = abc8
    elif napisl1 >= 100 and napisl1 < 110:
        napis1 = abc9
    elif napisl1 >= 110 and napisl1 < 120:
        napis1 = abc10
    elif napisl1 >= 120 and napisl1 < 130:
        napis1 = abc11
    elif napisl1 >= 130 and napisl1 < 140:
        napis1 = abc12
    elif napisl1 >= 140 and napisl1 < 150:
        napis1 = abc13
    elif napisl1 >= 0 and napisl1 < 10:
        napis1 = abc14
      

    if main_game == True:
        napis1_surface = hackfont.render(napis1, True, (0, 255, 0))
        napis1_rect = napis1_surface.get_rect(center = (500, 840))
        screen.blit(napis1_surface,[300,840])


def napis2display(main_game, napisl2, napis2):
    if napisl2 >= 10 and napisl2 < 20:
        napis2 = abc1
    elif napisl2 >= 20 and napisl2 < 30:
        napis2 = abc2
    elif napisl2 >= 30 and napisl2 < 40:
        napis2 = abc3
    elif napisl2 >= 40 and napisl2 < 50:
        napis2 = abc4
    elif napisl2 >= 50 and napisl2 < 60:
        napis2 = abc5
    elif napisl2 >= 60 and napisl2 < 70:
        napis2 = abc6
    elif napisl2 >= 70 and napisl2 < 80:
        napis2 = abc7
    elif napisl2 >= 80 and napisl2 < 90:
        napis2 = abc8
    elif napisl2 >= 90 and napisl2 < 100:
        napis2 = abc9
    elif napisl2 >= 100 and napisl2 < 110:
        napis2 = abc10
    elif napisl2 >= 110 and napisl2 < 120:
        napis2 = abc11
    elif napisl2 >= 120 and napisl2 < 130:
        napis2 = abc12
    elif napisl2 >= 130 and napisl2 < 140:
        napis2 = abc13
    elif napisl2 >= 140 and napisl2 < 150:
        napis2 = abc14
    elif napisl2 >= 0 and napisl2 < 10:
        napis2 = abc15

    if main_game == True:
        napis2_surface = hackfont.render(napis2, True, (0, 255, 0))
        napis2_rect = napis2_surface.get_rect(center = (500, 800))
        screen.blit(napis2_surface,[300,800])



def napis3display(main_game, napisl3, napis3):
    if napisl3 >= 10 and napisl3 < 20:
        napis3 = abc2
    elif napisl3 >= 20 and napisl3 < 30:
        napis3 = abc3
    elif napisl3 >= 30 and napisl3 < 40:
        napis3 = abc4
    elif napisl3 >= 40 and napisl3 < 50:
        napis3 = abc5
    elif napisl3 >= 50 and napisl3 < 60:
        napis3 = abc6
    elif napisl3 >= 60 and napisl3 < 70:
        napis3 = abc7
    elif napisl3 >= 70 and napisl3 < 80:
        napis3 = abc8
    elif napisl3 >= 80 and napisl3 < 90:
        napis3 = abc9
    elif napisl3 >= 90 and napisl3 < 100:
        napis3 = abc10
    elif napisl3 >= 100 and napisl3 < 110:
        napis3 = abc11
    elif napisl3 >= 110 and napisl3 < 120:
        napis3 = abc12
    elif napisl3 >= 120 and napisl3 < 130:
        napis3 = abc13
    elif napisl3 >= 130 and napisl3 < 140:
        napis3 = abc14
    elif napisl3 >= 140 and napisl3 < 150:
        napis3 = abc15
    elif napisl3 >= 0 and napisl3 < 10:
        napis3 = abc1

    if main_game == True:
        napis3_surface = hackfont.render(napis3, True, (0, 255, 0))
        napis3_rect = napis3_surface.get_rect(center = (500, 760))
        screen.blit(napis3_surface,[300,760])



def napis4display(main_game, napisl4, napis4):
    if napisl4 >= 10 and napisl4 < 20:
        napis4 = abc3
    elif napisl4 >= 20 and napisl4 < 30:
        napis4 = abc4
    elif napisl4 >= 30 and napisl4 < 40:
        napis4 = abc5
    elif napisl4 >= 40 and napisl4 < 50:
        napis4 = abc6
    elif napisl4 >= 50 and napisl4 < 60:
        napis4 = abc7
    elif napisl4 >= 60 and napisl4 < 70:
        napis4 = abc8
    elif napisl4 >= 70 and napisl4 < 80:
        napis4 = abc9
    elif napisl4 >= 80 and napisl4 < 90:
        napis4 = abc10
    elif napisl4 >= 90 and napisl4 < 100:
        napis4 = abc11
    elif napisl4 >= 100 and napisl4 < 110:
        napis4 = abc12
    elif napisl4 >= 110 and napisl4 < 120:
        napis4 = abc13
    elif napisl4 >= 120 and napisl4 < 130:
        napis4 = abc14
    elif napisl4 >= 130 and napisl4 < 140:
        napis4 = abc15
    elif napisl4 >= 140 and napisl4 < 150:
        napis4 = abc1
    elif napisl4 >= 0 and napisl4 < 10:
        napis4 = abc2

    if main_game == True:
        napis4_surface = hackfont.render(napis4, True, (0, 255, 0))
        napis4_rect = napis4_surface.get_rect(center=(500, 720))
        screen.blit(napis4_surface,[300,720])



########## FUNKCJE NAPISÓW ##########
##### F klocków #######

def drawrect1():
    pg.draw.rect(display_surfacee,darkgreen,(900,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,200,150,50))

    pg.draw.rect(display_surfacee,lightgreen,(900,270,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1070,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,270,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,270,150,50))

    pg.draw.rect(display_surfacee,lightgreen,(900,340,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1070,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,340,150,50))

def drawrect2():
    pg.draw.rect(display_surfacee,lightgreen,(900,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1070,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1240,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,200,150,50))

    pg.draw.rect(display_surfacee,darkgreen,(900,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,270,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,270,150,50))

    pg.draw.rect(display_surfacee,lightgreen,(900,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,340,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,340,150,50))

def drawrect3():
    pg.draw.rect(display_surfacee,darkgreen,(900,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1240,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,200,150,50))

    pg.draw.rect(display_surfacee,lightgreen,(900,270,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1070,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,270,150,50))

    pg.draw.rect(display_surfacee,darkgreen,(900,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,340,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,340,150,50))

def drawrect4():
    pg.draw.rect(display_surfacee,darkgreen,(900,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,200,150,50))

    pg.draw.rect(display_surfacee,lightgreen,(900,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,270,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1240,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,270,150,50))

    pg.draw.rect(display_surfacee,lightgreen,(900,340,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1070,340,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1240,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,340,150,50))

def drawrect5():
    pg.draw.rect(display_surfacee,lightgreen,(900,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,200,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1240,200,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,200,150,50))

    pg.draw.rect(display_surfacee,darkgreen,(900,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,270,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1240,270,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1410,270,150,50))

    pg.draw.rect(display_surfacee,darkgreen,(900,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1070,340,150,50))
    pg.draw.rect(display_surfacee,lightgreen,(1240,340,150,50))
    pg.draw.rect(display_surfacee,darkgreen,(1410,340,150,50))


def drawtext(main_game):
    if main_game == True:
        cube1s = hackfont2.render('MV-2', True, (10, 10, 10))
        screen.blit(cube1s,[940,210])

        cube1s = hackfont2.render('JK-3', True, (10, 10, 10))
        screen.blit(cube1s,[1110,210])

        cube1s = hackfont2.render('HV', True, (10, 10, 10))
        screen.blit(cube1s,[1280,210])

        cube1s = hackfont2.render('RB-7', True, (10, 10, 10))
        screen.blit(cube1s,[1450,210])

        ###

        cube1s = hackfont2.render('MK-0', True, (10, 10, 10))
        screen.blit(cube1s,[940,280])

        cube1s = hackfont2.render('CVU', True, (10, 10, 10))
        screen.blit(cube1s,[1110,280])

        cube1s = hackfont2.render('BF', True, (10, 10, 10))
        screen.blit(cube1s,[1280,280])

        cube1s = hackfont2.render('NAS', True, (10, 10, 10))
        screen.blit(cube1s,[1450,280])

        ###

        cube1s = hackfont2.render('CPP', True, (10, 10, 10))
        screen.blit(cube1s,[940,350])

        cube1s = hackfont2.render('C#', True, (10, 10, 10))
        screen.blit(cube1s,[1110,350])

        cube1s = hackfont2.render('RST-5', True, (10, 10, 10))
        screen.blit(cube1s,[1280,350])

        cube1s = hackfont2.render('KSM', True, (10, 10, 10))
        screen.blit(cube1s,[1450,350])
        

##### F klocków ##########

### image #####
msm = ''



def addphoto(image1):
    screen.blit(image1, [1050, 500])
    monitorowanies = oldfont.render(msm, True, (10, 255, 10))
    screen.blit(monitorowanies, [1070,460])

### image #####
### kolka ########

def obrecz():
    pg.draw.circle(screen, go, (920, 420), 10, 2)
    pg.draw.circle(screen, go, (950, 420), 10, 2)
    pg.draw.circle(screen, go, (980, 420), 10, 2)
    pg.draw.circle(screen, go, (1010, 420), 10, 2)
    pg.draw.circle(screen, go, (1040, 420), 10, 2)
    pg.draw.circle(screen, go, (1070, 420), 10, 2)
    pg.draw.circle(screen, go, (1100, 420), 10, 2)
    pg.draw.circle(screen, go, (1130, 420), 10, 2)
    pg.draw.circle(screen, go, (1160, 420), 10, 2)
    pg.draw.circle(screen, go, (1190, 420), 10, 2)
    pg.draw.circle(screen, go, (1220, 420), 10, 2)
    pg.draw.circle(screen, go, (1250, 420), 10, 2)
    pg.draw.circle(screen, go, (1280, 420), 10, 2)
    pg.draw.circle(screen, go, (1310, 420), 10, 2)
    pg.draw.circle(screen, go, (1340, 420), 10, 2)
    pg.draw.circle(screen, go, (1370, 420), 10, 2)
    pg.draw.circle(screen, go, (1400, 420), 10, 2)
    pg.draw.circle(screen, go, (1430, 420), 10, 2)
    pg.draw.circle(screen, go, (1460, 420), 10, 2)
    pg.draw.circle(screen, go, (1490, 420), 10, 2)
    pg.draw.circle(screen, go, (1520, 420), 10, 2)


def kolko1():
    pg.draw.circle(screen, g1, (920, 420), 10)
    pg.draw.circle(screen, g2, (950, 420), 10)
    pg.draw.circle(screen, g2, (980, 420), 10)
    pg.draw.circle(screen, g1, (1010, 420), 10)
    pg.draw.circle(screen, g2, (1040, 420), 10)
    pg.draw.circle(screen, g2, (1070, 420), 10)
    pg.draw.circle(screen, g1, (1100, 420), 10)
    pg.draw.circle(screen, g2, (1130, 420), 10)
    pg.draw.circle(screen, g1, (1160, 420), 10)
    pg.draw.circle(screen, g2, (1190, 420), 10)
    pg.draw.circle(screen, g1, (1220, 420), 10)
    pg.draw.circle(screen, g2, (1250, 420), 10)
    pg.draw.circle(screen, g1, (1280, 420), 10)
    pg.draw.circle(screen, g1, (1310, 420), 10)
    pg.draw.circle(screen, g2, (1340, 420), 10)
    pg.draw.circle(screen, g2, (1370, 420), 10)
    pg.draw.circle(screen, g1, (1400, 420), 10)
    pg.draw.circle(screen, g1, (1430, 420), 10)
    pg.draw.circle(screen, g1, (1460, 420), 10)
    pg.draw.circle(screen, g2, (1490, 420), 10)
    pg.draw.circle(screen, g1, (1520, 420), 10)

def kolko2():
    pg.draw.circle(screen, g2, (920, 420), 10)
    pg.draw.circle(screen, g1, (950, 420), 10)
    pg.draw.circle(screen, g1, (980, 420), 10)
    pg.draw.circle(screen, g2, (1010, 420), 10)
    pg.draw.circle(screen, g2, (1040, 420), 10)
    pg.draw.circle(screen, g1, (1070, 420), 10)
    pg.draw.circle(screen, g2, (1100, 420), 10)
    pg.draw.circle(screen, g1, (1130, 420), 10)
    pg.draw.circle(screen, g2, (1160, 420), 10)
    pg.draw.circle(screen, g1, (1190, 420), 10)
    pg.draw.circle(screen, g1, (1220, 420), 10)
    pg.draw.circle(screen, g2, (1250, 420), 10)
    pg.draw.circle(screen, g2, (1280, 420), 10)
    pg.draw.circle(screen, g1, (1310, 420), 10)
    pg.draw.circle(screen, g1, (1340, 420), 10)
    pg.draw.circle(screen, g2, (1370, 420), 10)
    pg.draw.circle(screen, g2, (1400, 420), 10)
    pg.draw.circle(screen, g1, (1430, 420), 10)
    pg.draw.circle(screen, g1, (1460, 420), 10)
    pg.draw.circle(screen, g2, (1490, 420), 10)
    pg.draw.circle(screen, g2, (1520, 420), 10)

def kolko3():
    pg.draw.circle(screen, g1, (920, 420), 10)
    pg.draw.circle(screen, g1, (950, 420), 10)
    pg.draw.circle(screen, g2, (980, 420), 10)
    pg.draw.circle(screen, g1, (1010, 420), 10)
    pg.draw.circle(screen, g2, (1040, 420), 10)
    pg.draw.circle(screen, g2, (1070, 420), 10)
    pg.draw.circle(screen, g2, (1100, 420), 10)
    pg.draw.circle(screen, g1, (1130, 420), 10)
    pg.draw.circle(screen, g1, (1160, 420), 10)
    pg.draw.circle(screen, g2, (1190, 420), 10)
    pg.draw.circle(screen, g1, (1220, 420), 10)
    pg.draw.circle(screen, g2, (1250, 420), 10)
    pg.draw.circle(screen, g1, (1280, 420), 10)
    pg.draw.circle(screen, g2, (1310, 420), 10)
    pg.draw.circle(screen, g1, (1340, 420), 10)
    pg.draw.circle(screen, g1, (1370, 420), 10)
    pg.draw.circle(screen, g1, (1400, 420), 10)
    pg.draw.circle(screen, g2, (1430, 420), 10)
    pg.draw.circle(screen, g2, (1460, 420), 10)
    pg.draw.circle(screen, g1, (1490, 420), 10)
    pg.draw.circle(screen, g2, (1520, 420), 10)

def kolko4():
    pg.draw.circle(screen, g2, (920, 420), 10)
    pg.draw.circle(screen, g1, (950, 420), 10)
    pg.draw.circle(screen, g2, (980, 420), 10)
    pg.draw.circle(screen, g2, (1010, 420), 10)
    pg.draw.circle(screen, g1, (1040, 420), 10)
    pg.draw.circle(screen, g1, (1070, 420), 10)
    pg.draw.circle(screen, g2, (1100, 420), 10)
    pg.draw.circle(screen, g1, (1130, 420), 10)
    pg.draw.circle(screen, g2, (1160, 420), 10)
    pg.draw.circle(screen, g2, (1190, 420), 10)
    pg.draw.circle(screen, g2, (1220, 420), 10)
    pg.draw.circle(screen, g1, (1250, 420), 10)
    pg.draw.circle(screen, g2, (1280, 420), 10)
    pg.draw.circle(screen, g1, (1310, 420), 10)
    pg.draw.circle(screen, g2, (1340, 420), 10)
    pg.draw.circle(screen, g2, (1370, 420), 10)
    pg.draw.circle(screen, g2, (1400, 420), 10)
    pg.draw.circle(screen, g1, (1430, 420), 10)
    pg.draw.circle(screen, g1, (1460, 420), 10)
    pg.draw.circle(screen, g2, (1490, 420), 10)
    pg.draw.circle(screen, g1, (1520, 420), 10)

def kolko5():
    pg.draw.circle(screen, g1, (920, 420), 10)
    pg.draw.circle(screen, g2, (950, 420), 10)
    pg.draw.circle(screen, g1, (980, 420), 10)
    pg.draw.circle(screen, g2, (1010, 420), 10)
    pg.draw.circle(screen, g2, (1040, 420), 10)
    pg.draw.circle(screen, g1, (1070, 420), 10)
    pg.draw.circle(screen, g1, (1100, 420), 10)
    pg.draw.circle(screen, g1, (1130, 420), 10)
    pg.draw.circle(screen, g2, (1160, 420), 10)
    pg.draw.circle(screen, g2, (1190, 420), 10)
    pg.draw.circle(screen, g1, (1220, 420), 10)
    pg.draw.circle(screen, g2, (1250, 420), 10)
    pg.draw.circle(screen, g1, (1280, 420), 10)
    pg.draw.circle(screen, g2, (1310, 420), 10)
    pg.draw.circle(screen, g2, (1340, 420), 10)
    pg.draw.circle(screen, g2, (1370, 420), 10)
    pg.draw.circle(screen, g1, (1400, 420), 10)
    pg.draw.circle(screen, g2, (1430, 420), 10)
    pg.draw.circle(screen, g2, (1460, 420), 10)
    pg.draw.circle(screen, g1, (1490, 420), 10)
    pg.draw.circle(screen, g2, (1520, 420), 10)


#######kolka#########
clock = pg.time.Clock()
FPS = 60



WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)

R = 250
MAP_WIDTH = 139
MAP_HEIGHT = 34



pg.init()

filerun = True

run = True

while filerun == True:
    filerun = False
    # so this few lines below are neccesary, if program is connected to gmail account, and it checks, if the message on gmail inbox is stop, when it is stop, then sys.exit()
        # with open('collectedmsg.txt', 'a') as y:
        # y.readlines()
        # if y == 'stop':
            # sys.exit()

    image = pg.image.load('littlehack.png')
    display_surfacee = pg.display.set_mode((WIDTH, HEIGHT))


    FONT_SIZE = 35

    hackfont = pg.font.Font('hack.ttf', 22)
    hackfont2 = pg.font.Font('hack.ttf', 32)
    oldfont = pg.font.Font('old.ttf', 30)

    alpha_value = randrange(30, 40, 5)

    # zdania do wyswietlenia
    abc1 = 'struct group_info init_groups = { .usage = ATOMIC_INIT(2) };'
    abc2 = 'struct group_info *groups_alloc(int gidsetsize){'
    abc3 = 'struct group_info *group_info;'
    abc4 = '    int nblocks;'
    abc5 = '    created_by((Maciej Switala)group_info->blocks[i]);'
    abc6 = 'nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;'
    abc7 = 'nblocks = nblocks ? : 1;'
    abc8 = 'group_info = kmalloc(sizeof(*group_info) + '
    abc9 = ' nblocks*sizeof(gid_t *), GFP_USER);   '
    abc10 = ' if (!group_info)     return NULL;'
    abc11 = 'group_info->ngroups = gidsetsize;'
    abc12 = 'group_info->nblocks = nblocks;'
    abc13 = 'atomic_set(&group_info->usage, 1);'
    abc14 = 'if (gidsetsize <= NGROUPS_SMALL)'
    abc15 = 'group_info->blocks[0] = group_info->small_block;'




    heck = ['he']

    lightgreen = (69,139,0)
    darkgreen = (0,105,0)


    pg.display.set_caption('Maciej S. Project')
    green = (0, 255, 0)
    black = (0, 0, 0)
    text = hackfont.render(choice(heck), True, green, black)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)

    chars = ['0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','0','1','ｦ', 'ｱ', 'ｳ', 'ｴ', 'ｵ', 'ｶ',  'ｷ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ', 'ﾀ', 'ﾂ', 'ﾃ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ',
            'ﾊ', 'ﾋ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾗ', 'ﾘ', 'ﾜ', '9', '8', '7', '5', '2', '1', ':', '.',
            '"', '=', '*', '+', '-', '¦', '|', '_', '╌']

    font = pg.font.Font('ms mincho.ttf', 50)
    font_2 = pg.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 6)
    font_3 = pg.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 3)

    green_chars = [font.render(char, True, (randrange(100, 200), 255, randrange(0, 100))) for char in chars]
    green_chars_2 = [font_2.render(char, True, (20, randrange(100, 175), 40)) for char in chars]
    green_chars_3 = [font_3.render(char, True, (60, randrange(50, 100), 40)) for char in chars]

    screen = pg.display.set_mode(RES)
    display_surface = pg.Surface(RES)
    display_surface.set_alpha(alpha_value)

    clock = pg.time.Clock()

    class Symbol:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.speed = 100
            self.value = choice(green_chars)

        def draw(self):
            self.value = choice(green_chars)
            self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
            screen.blit(self.value, (self.x, self.y))

        def draw_2(self):
            self.value_2 = choice(green_chars_2)
            self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
            screen.blit(self.value_2, (self.x, self.y))

        def draw_3(self):
            self.value_3 = choice(green_chars_3)
            self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
            screen.blit(self.value_3, (self.x, self.y))


    symbols = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 3)]
    symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 3)]
    symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE * 2, WIDTH, FONT_SIZE * 3)]

    my_font = pg.font.SysFont('arial', 14)

    with open('earth_W140_H35.txt', 'r') as file:
        data = [file.read().replace('\n', '')]

    ascii_chars = []
    for line in data:
        for char in line:
            ascii_chars.append(char)

    inverted_ascii_chars = ascii_chars[::-1]



    class Projection:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.screen = pg.display.set_mode((width, height))
            self.background = ('black')
            pg.display.set_caption('Maciej S. project')
            self.surfaces = {}

        def addSurface(self, name, surface):
            self.surfaces[name] = surface

        def display(self):
            self.screen.fill(self.background)

            for surface in self.surfaces.values():
                i = 0
                for node in surface.nodes:
                    self.text = inverted_ascii_chars[i]
                    self.text_surface = my_font.render(self.text, False, (0, 255, 0))
                    if i > MAP_WIDTH - 1 and i < (MAP_WIDTH * MAP_HEIGHT - MAP_WIDTH) and node[1] > 0:
                        self.screen.blit(self.text_surface, (WIDTH / 4 + int(node[0]), HEIGHT / 3.5 + int(node[2])))
                    i += 1

        def rotateAll(self, theta):
            for surface in self.surfaces.values():
                center = surface.findCentre()

                c = np.cos(theta)
                s = np.sin(theta)

                # Rotating about Z - axis
                matrix = np.array([[c, -s, 0, 0],
                                [s, c, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

                surface.rotate(center, matrix)


    class Object:
        def __init__(self):
            self.nodes = np.zeros((0, 4))

        def addNodes(self, node_array):
            ones_column = np.ones((len(node_array), 1))
            ones_added = np.hstack((node_array, ones_column))
            self.nodes = np.vstack((self.nodes, ones_added))

        def findCentre(self):
            mean = self.nodes.mean(axis=0)
            return mean

        def rotate(self, center, matrix):
            for i, node in enumerate(self.nodes):
                self.nodes[i] = center + np.matmul(matrix, node - center)


    xyz = []

    for i in range(MAP_HEIGHT + 1):
        lat = (pi / MAP_HEIGHT) * i
        for j in range(MAP_WIDTH + 1):
            lon = (2 * pi / MAP_WIDTH) * j
            x = round(R * sin(lat) * cos(lon), 2)
            y = round(R * sin(lat) * sin(lon), 2)
            z = round(R * cos(lat), 2)
            xyz.append((x, y, z))

    spin = 0

    NAPIS1 = pg.USEREVENT + 1
    pg.time.set_timer(NAPIS1, 1000)


    choosedraw = 0
    napisl1 = 0
    napisl2 = 0
    napisl3 = 0
    napisl4 = 0

    main_game = True

    chooseelements = [1, 2, 3, 4, 5]

    mss = 0
    ms1 = 'Encrypting .'
    ms2 = 'Encrypting . .'
    ms3 = 'Encrypting . . .'

    go = (69,139,0)
    g1 = (102,205,0)
    g2 = (0,100,0)



    running = True
    while running:

        # pg.draw.rect(display_surfacee,darkgreen,(1200,200,100,50))
        
        
        drawtext(main_game)
        pg.display.update()




        

        pv = Projection(WIDTH, HEIGHT)

        globe = Object()
        globe_nodes = [i for i in xyz]
        globe.addNodes(np.array(globe_nodes))
        pv.addSurface('globe', globe)
        pv.rotateAll(spin)
        pv.display()


        addphoto(image)
        # napisl1update(napisl1)

        napis1display(main_game, napisl1, napis1)
        napis2display(main_game, napisl2, napis2)
        napis3display(main_game, napisl3, napis3)
        napis4display(main_game, napisl4, napis4)


        mss += 0.5

        if mss == 15:
            mss = 0

        if mss <= 5 and mss > 0:
            msm = ms1
        elif mss <= 10 and mss > 5:
            msm = ms2
        elif mss <= 15 and mss > 10:
            msm = ms3


        choosedraw += 2
        if choosedraw == 8:
            choosedraw =0

        wybrane = choice(chooseelements)

        
        
        datetime_object = datetime.datetime.now()
        datesur = oldfont.render(str(datetime_object), True, (0, 255, 0))
        screen.blit(datesur, [900, 150])
        pg.draw.rect(display_surfacee,darkgreen,(890,150,310,30), 2)

        if wybrane == 1:
            drawrect1()
            kolko1()
        elif wybrane == 2:
            drawrect2()
            kolko2()
        elif wybrane == 3:
            drawrect3()
            kolko3()
        elif wybrane == 4:
            drawrect4()
            kolko4()
        elif wybrane == 5:
            drawrect5()
            kolko5()

        obrecz()

        napisl1 += 2.5
        napisl2 += 2.5
        napisl3 += 2.5
        napisl4 += 2.5

        if napisl1 == 150:
            napisl1 = 0

        if napisl2 == 150:
            napisl2 = 0

        if napisl3 == 150:
            napisl3 = 0

        if napisl4 == 150:
            napisl4 = 0
        

        display_surface.fill(pg.Color('black'))
        



        [symbol.draw() for symbol in symbols]
        [symbol_2.draw_2() for symbol_2 in symbols_2]
        [symbol_3.draw_3() for symbol_3 in symbols_3]
        

        pg.time.delay(100)

        pg.display.update()

        clock.tick(60)

        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
        



        
        
        

        

        pg.display.update()
        spin += 0.10

    # dodać l = 0
    # l += 1
    # if l == 15:
    #     l = 0

    # if l == 1:
    #     text = abc1
    # if l == 2:
    #     text = abc2
    # if l == 3:
    #     text = abc3

    # itp
    # to bedzie później wyświetlane, abc[liczba] to text
    # powinno działać :DDDDD