import pygame
from pygame.locals import *
import numpy as np
from math import sqrt


keys = {}
WIDTH = 800
HEIGHT = 600


SPEED = 5 # Reduced speed for better control during testing
SPRINT = 1
ROTATIONSPEED   = 0.08
RAY_COUNT = 100
FOV = 1

directionX = 1.0
directionY = 0.0
DeltaX = 0
DeltaY = 0
planeX = 0.0
planeY = FOV

HUD_HEIGHT = 40
HUD_WIDTH = WIDTH

DIRVEC_SCALAR = 1

CIRCLE_CORD_X = 400
CIRCLE_CORD_Y = 300

RotateCW = np.array([[np.cos(ROTATIONSPEED), np.sin(-ROTATIONSPEED)],
                     [np.sin(ROTATIONSPEED), np.cos( ROTATIONSPEED)]])
RotateACW= np.array([[np.cos(-ROTATIONSPEED), np.sin(ROTATIONSPEED)],
                     [np.sin(-ROTATIONSPEED), np.cos(-ROTATIONSPEED)]])
DirVec = np.array([[directionX],[directionY]])
PlaVec = np.array([[planeX]    ,[planeY]])

map = np.array([
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2],
    [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 3, 1, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 2, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 3, 1, 0, 0, 2, 0, 0, 2, 1, 3, 2, 0, 2, 0, 0, 3, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 1, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
])

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
def close():
    pygame.display.quit()
    pygame.quit()

#Lower Hud
scene = 1
font = pygame.font.SysFont("Times New Roman", 20)

running = True
while running:
    for event in pygame.event.get():
        match event.type:
            case pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    close()
                    print("ESC Pressed: Running Stopped!")
                    
                keys[event.key] = True

            case pygame.KEYUP:
                keys[event.key] = False

            case pygame.QUIT:
                running = False
                close()
                print("Running Stopped!")

    if not running:
        break

    HUD = font.render(f"Currently On Scene {scene}, To change Scene Press F1/F2", True, (0, 0, 0)) 
    pygame.display.set_caption("Experimental Image Draw Test")
    dispObj = pygame.Rect((0,0),(WIDTH, HEIGHT))

    planeX,planeY = PlaVec.flatten()
    directionX,directionY = DirVec.flatten()

    screen.fill("black", dispObj)

    #Draw BackGround
    rows,   columns   = map.shape
    MapBlkWid = WIDTH / columns
    MapBlkHie = HEIGHT / rows

    # Draw Map
    for row in range(rows):
        for col in range(columns):
            if map[row, col]: # If map value is not 0 (a wall)
                pygame.draw.rect(screen, "Blue", [col * MapBlkWid, row * MapBlkHie, MapBlkWid, MapBlkHie])



    #Calculate player Grid Corrdinates

    PlayerXfloat = CIRCLE_CORD_X / MapBlkWid
    PlayerYfloat = CIRCLE_CORD_Y / MapBlkHie

    PlayerX = int(PlayerXfloat)
    PlayerY = int(PlayerYfloat)

    PlayerX = min(PlayerX, columns - 1)
    PlayerY = min(PlayerY, rows - 1)

    DeltaX = 0
    DeltaY = 0

    #Draw Rays
    cameraX = -1
    for RayCnt in range(1,RAY_COUNT+1):
        #sweeps from -1 to 1 for cameraX value
        cameraX += (2/RAY_COUNT)

        RayStartX = PlayerXfloat
        RayStartY = PlayerYfloat

        RayDir = DirVec + (cameraX * PlaVec)

        RayDirectionX, RayDirectionY = RayDir.flatten()

        deltaDistanceX = abs(1.0 / RayDirectionX)
        deltaDistanceY = abs(1.0 / RayDirectionY)

        RayEndX = PlayerX
        RayEndY = PlayerY

        if (RayDirectionX < 0):
            stepX = -1
            sideDistanceX = (RayStartX - RayEndX) * deltaDistanceX
        else:
            stepX = 1
            sideDistanceX = (RayEndX + 1.0 - RayStartX) * deltaDistanceX

        if (RayDirectionY < 0):
            stepY = -1
            sideDistanceY = (RayStartY - RayEndY) * deltaDistanceY
        else:
            stepY = 1
            sideDistanceY = (RayEndY + 1.0 - RayStartY) * deltaDistanceY
        
                    # Finding distance to a wall
        hit = 0
        while hit == 0:
            if (sideDistanceX < sideDistanceY):
                sideDistanceX += deltaDistanceX
                RayEndX += stepX
                side = 0
            else:
                sideDistanceY += deltaDistanceY
                RayEndY += stepY
                side = 1

            if (map[RayEndY, RayEndX] > 0): 
                hit = 1
                break

        if side == 0: # X-side hit
            perpWallDist = (RayEndX - RayStartX + (1.0 - stepX) / 2.0) / RayDirectionX
        else: # Y-side hit
            perpWallDist = (RayEndY - RayStartY + (1.0 - stepY) / 2.0) / RayDirectionY

        # perpWallDist = sqrt((RayEndX - RayStartX)**2 + (RayEndY - RayStartY )**2 )
        
        # Calculate the actual end point for drawing the ray
        # These are in map units
        HitWallX = RayStartX + RayDirectionX * perpWallDist
        HitWallY = RayStartY + RayDirectionY * perpWallDist

        # Calculate the delta in map units from player to wall hit point
        RayDeltaX = HitWallX - PlayerXfloat
        RayDeltaY = HitWallY - PlayerYfloat

        endX = CIRCLE_CORD_X + RayDeltaX * MapBlkWid
        endY = CIRCLE_CORD_Y + RayDeltaY * MapBlkHie

        pygame.draw.line(screen, "purple", (CIRCLE_CORD_X, CIRCLE_CORD_Y), (endX, endY), 1)
  
#--------------------------------DRAW RAY LOOP END-------------------------------
    if keys.get(K_F1, False):
        scene = 1

    if keys.get(K_F2, False):
        scene = 2


    if keys.get(K_UP, False):
        ProbX = CIRCLE_CORD_X + directionX * SPEED
        ProbY = CIRCLE_CORD_Y + directionY * SPEED


        nextCol = int(ProbX / MapBlkWid)
        nextCol =  min(nextCol, columns - 1)

        if not map[PlayerY, nextCol] :
            DeltaX = directionX * SPEED

        nextRow = int(ProbY / MapBlkHie)
        nextRow = max(0, min(nextRow, rows - 1))

        if not map[nextRow, PlayerX] :
            DeltaY = directionY * SPEED

    if keys.get(K_DOWN, False):
        ProbX = CIRCLE_CORD_X - directionX * SPEED
        ProbY = CIRCLE_CORD_Y - directionY * SPEED

        nextCol = int(ProbX / MapBlkWid)
        nextCol = max(0, min(nextCol, columns - 1))
        if map[PlayerY, nextCol] == 0:
            DeltaX = -directionX * SPEED

        nextRow = int(ProbY / MapBlkHie)
        nextRow = max(0, min(nextRow, rows - 1))
        if map[nextRow, PlayerX] == 0:
            DeltaY = -directionY * SPEED

    CIRCLE_CORD_X += DeltaX
    CIRCLE_CORD_Y += DeltaY

    # Boundary checks for screen edges
    CIRCLE_CORD_X = max(0, min(CIRCLE_CORD_X, WIDTH))
    CIRCLE_CORD_Y = max(0, min(CIRCLE_CORD_Y, HEIGHT))


    if keys.get(K_LEFT, False):
        DirVec = RotateACW @ DirVec
        PlaVec = RotateACW @ PlaVec

    if keys.get(K_RIGHT, False):
        DirVec = RotateCW @ DirVec
        PlaVec = RotateCW @ PlaVec

    pygame.draw.line(screen,"purple", (CIRCLE_CORD_X,CIRCLE_CORD_Y),(CIRCLE_CORD_X + directionX*SPEED*5, CIRCLE_CORD_Y + directionY*SPEED*5),2)

    pygame.draw.circle(screen,"red", (CIRCLE_CORD_X, CIRCLE_CORD_Y), 2.5,1)

    pygame.draw.rect(screen, (100, 100, 200), (0, HEIGHT - HUD_HEIGHT, HUD_WIDTH, HUD_WIDTH))
    screen.blit(HUD, (20, HEIGHT - 30))
    pygame.display.flip()
    clock.tick(60.0)

pygame.quit()