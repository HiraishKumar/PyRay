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
RAY_COUNT = 10
FOV = 1

directionX = 1.0
directionY = 0.0
planeX = 0.0
planeY = FOV

RotateCW = np.array([[np.cos(ROTATIONSPEED), np.sin(-ROTATIONSPEED)],
                     [np.sin(ROTATIONSPEED), np.cos( ROTATIONSPEED)]])
RotateACW= np.array([[np.cos(-ROTATIONSPEED), np.sin(ROTATIONSPEED)],
                     [np.sin(-ROTATIONSPEED), np.cos(-ROTATIONSPEED)]])
DirVec = np.array([[directionX],[directionY]])
PlaVec = np.array([[planeX]    ,[planeY]])

map = np.array([[1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1]])

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
    
    pygame.display.set_caption("Expermental Image Draw Test")
    dispObj = pygame.Rect((0,0),(WIDTH, HIEGHT))
    screen.fill("black", dispObj)
    SPRINT = 1

    if keys.get(K_UP, False):
        print("Up Key is Pressed!")
        # directionX,directionY = DirVec.flatten()
        CIRCLE_CORD_X -= directionX * SPEED
        if CIRCLE_CORD_X < 0:
            CIRCLE_CORD_X = 0
        if CIRCLE_CORD_X > WIDTH:
            CIRCLE_CORD_X = WIDTH

        CIRCLE_CORD_Y -= directionY * SPEED
        if CIRCLE_CORD_Y < 0:
            CIRCLE_CORD_Y = 0
        if CIRCLE_CORD_Y > HIEGHT:
            CIRCLE_CORD_Y = HIEGHT
    
    if keys.get(K_DOWN, False):
        print("Down Key is Pressed!")
        # directionX,directionY = DirVec.flatten()

        CIRCLE_CORD_X += directionX * SPEED
        if CIRCLE_CORD_X < 0:
            CIRCLE_CORD_X = 0
        if CIRCLE_CORD_X > WIDTH:
            CIRCLE_CORD_X = WIDTH

        CIRCLE_CORD_Y += directionY * SPEED
        if CIRCLE_CORD_Y < 0:
            CIRCLE_CORD_Y = 0
        if CIRCLE_CORD_Y > HIEGHT:
            CIRCLE_CORD_Y = HIEGHT

    
    
    if keys.get(K_LEFT, False):
        DirVec = RotateACW @ DirVec
        PlaVec = RotateACW @ PlaVec
        print("Left Key is Pressed!")

    
    if keys.get(K_RIGHT, False):
        DirVec = RotateCW @ DirVec
        PlaVec = RotateCW @ PlaVec
        print("Right Key is Pressed!")

    #Draw BackGround
    rows,   colums   = len(map), len(map[0])
    DBackX, DBackY   = 0,0

    MapBlkWid = WIDTH/colums
    MapBlkHie = HIEGHT/rows

    pygame.draw.rect(screen,"red",[0,0,400,300])
    for row in range(rows):
        for col in range(colums):
            # print(f"current Cord {col},{row}")
            if map[row,col]:
                # print("Block HIT!")
                pygame.draw.rect(screen,"Blue",[DBackX,DBackY,MapBlkWid,MapBlkHie])
                
            DBackX += MapBlkWid
        DBackX = 0
        DBackY += MapBlkHie

    #Draw Player
    cameraX = -1
    for i in range(1,RAY_COUNT+1):
        #sweeps from -1 to 1 for cameraX value
        RayDir = DirVec + (cameraX * PlaVec)
        cameraX += (2/RAY_COUNT)
        
        # Normalize RayDir Vector
        RayDir = RayDir/np.linalg.norm(RayDir)
        
        RayDirectionX, RayDirectionY = RayDir.flatten()
        pygame.draw.line(screen,"purple", (CIRCLE_CORD_X,CIRCLE_CORD_Y),(CIRCLE_CORD_X - RayDirectionX*200, CIRCLE_CORD_Y - RayDirectionY*200),2)

    planeX,planeY = PlaVec.flatten()
    directionX,directionY = DirVec.flatten()
            
        
    pygame.draw.circle(screen,"red", (CIRCLE_CORD_X, CIRCLE_CORD_Y), 10.0,10)
    pygame.draw.line(screen,"red", (CIRCLE_CORD_X,CIRCLE_CORD_Y),(CIRCLE_CORD_X - directionX*SPEED, CIRCLE_CORD_Y - directionY*SPEED),5)
    pygame.display.flip()
    clock.tick(60.0)

pygame.quit()