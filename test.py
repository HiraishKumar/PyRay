import pygame 
from pygame.locals import *
import numpy as np


keys = {}
WIDTH = 800
HIEGHT = 600
CIRCLE_CORD_X = 400
CIRCLE_CORD_Y = 300

SPEED = 5
SPRINT = 1
ROTATIONSPEED   = 0.08

directionX = 1.0
directionY = 0.0

RotateCW = np.array([[np.cos(ROTATIONSPEED), np.sin(-ROTATIONSPEED)],
                     [np.sin(ROTATIONSPEED), np.cos( ROTATIONSPEED)]])
RotateACW= np.array([[np.cos(-ROTATIONSPEED), np.sin(ROTATIONSPEED)],
                     [np.sin(-ROTATIONSPEED), np.cos(-ROTATIONSPEED)]])
DirVec = np.array([[directionX],[directionY]])

pygame.init()
screen = pygame.display.set_mode((WIDTH,HIEGHT))
clock = pygame.time.Clock()
def close():
    pygame.display.quit()
    pygame.quit()

running = True
while running:
    #input Capturing
    for event in pygame.event.get():
        match event.type:
            case pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    close()
                    print("ESC Pressed: Running Stopped!")
                keys[event.key] = True
                 
            case pygame.KEYUP:
                keys[event.key] = False

            case pygame.QUIT:
                running = False
                close()
                print("Running Stopped!")
    
    SPRINT = 1
    if keys.get(K_LSHIFT, False):
        print("Shift Key is Pressed!")
        SPRINT = 2

    DELTA_X = SPEED * SPRINT
    DELTA_Y = SPEED * SPRINT
    if keys.get(K_UP, False):
        print("Up Key is Pressed!")
        directionX,directionY = DirVec.flatten()

        CIRCLE_CORD_X -= directionX * SPEED
        if CIRCLE_CORD_X < 0:
            CIRCLE_CORD_X = 0
        if CIRCLE_CORD_X > WIDTH:
            CIRCLE_CORD_X = WIDTH

        CIRCLE_CORD_Y -= directionY * SPEED
        if CIRCLE_CORD_Y < 0:
            CIRCLE_CORD_Y = 0
        if CIRCLE_CORD_Y > HIEGHT:
            CIRCLE_CORD_Y = WIDTH
    
    if keys.get(K_DOWN, False):
        print("Down Key is Pressed!")
        directionX,directionY = DirVec.flatten()

        CIRCLE_CORD_X += directionX * SPEED
        if CIRCLE_CORD_X < 0:
            CIRCLE_CORD_X = 0
        if CIRCLE_CORD_X > WIDTH:
            CIRCLE_CORD_X = WIDTH

        CIRCLE_CORD_Y += directionY * SPEED
        if CIRCLE_CORD_Y < 0:
            CIRCLE_CORD_Y = 0
        if CIRCLE_CORD_Y > HIEGHT:
            CIRCLE_CORD_Y = WIDTH
        # CIRCLE_CORD_Y -= DELTA_Y
        # if CIRCLE_CORD_Y < 0:
        #     CIRCLE_CORD_Y = 0
        # if CIRCLE_CORD_Y > HIEGHT:
        #     CIRCLE_CORD_Y = WIDTH
    
    
    if keys.get(K_LEFT, False):
        DirVec = RotateACW @ DirVec
        directionX,directionY = DirVec.flatten()
        print("Left Key is Pressed!")
        # print(DirVec)
        # CIRCLE_CORD_X -= DELTA_X
        # if CIRCLE_CORD_X < 0:
        #     CIRCLE_CORD_X = 0
        # if CIRCLE_CORD_X > WIDTH:
        #     CIRCLE_CORD_X = WIDTH
    
    if keys.get(K_RIGHT, False):
        DirVec = RotateCW @ DirVec
        directionX,directionY = DirVec.flatten()
        print("Right Key is Pressed!")
        # print(DirVec)
        # CIRCLE_CORD_X += DELTA_X
        # if CIRCLE_CORD_X < 0:
        #     CIRCLE_CORD_X = 0
        # if CIRCLE_CORD_X > WIDTH:
        #     CIRCLE_CORD_X = WIDTH

            
        
    pygame.display.set_caption("Expermental Image Draw Test")
    dispObj = pygame.Rect((0,0),(WIDTH, HIEGHT))
    screen.fill("purple", dispObj)
    pygame.draw.circle(screen,"red", (CIRCLE_CORD_X, CIRCLE_CORD_Y), 30.0,10)
    pygame.draw.line(screen,"red", (CIRCLE_CORD_X,CIRCLE_CORD_Y),(CIRCLE_CORD_X - directionX*SPEED, CIRCLE_CORD_Y - directionY*SPEED),5)
    pygame.display.flip()
    clock.tick(60.0)

pygame.quit()