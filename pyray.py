

try:
    import math
    import time
    import pygame
    from pygame.locals import *
    import numpy as np
except ImportError:
    print("PyRay could not import necessary modules")
    raise ImportError

# Use a dictionary instead of a fixed-size array for keys
keys = {}

# A map over the world
worldMap = np.array([
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

# Closes the program
def close():
    pygame.display.quit()
    pygame.quit()

def main():
    pygame.init()

    # Head Up Display information (HUD)
    font = pygame.font.SysFont("Verdana", 20)
    HUD = font.render("F1 / F2 - Screenshot JPEG/BMP   F5/F6 - Shadows on/off   F7/F8 - HUD Show/Hide", True, (0, 0, 0))

    # Creates window
    WIDTH = 1000
    HEIGHT = 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyRay - Python Raycasting Engine (v0.03)")

    showShadow = True
    showHUD = True

    # Defines starting position and direction
    positionX = 3.0
    positionY = 7.0

    directionX = 1.0
    directionY = 0.0

    planeX = 0.0
    planeY = 0.5  #change this quantity to change FOV
    # FOV is the ratio between the leanth direction vector and the leanth of the plane vector  

    # Movement constants
    ROTATIONSPEED   = 0.02
    MOVESPEED       = 0.03

    # Graphic Constants
    COLUMNWIDTH     = 4

    RotateCW = np.array([[np.cos(ROTATIONSPEED), np.sin(-ROTATIONSPEED)],
                         [np.sin(ROTATIONSPEED), np.cos( ROTATIONSPEED)]])
    RotateACW= np.array([[np.cos(-ROTATIONSPEED), np.sin(ROTATIONSPEED)],
                         [np.sin(-ROTATIONSPEED), np.cos(-ROTATIONSPEED)]])
    DirVec = np.array([[directionX],[directionY]])
    PlaVec = np.array([[planeX]    ,[planeY]])
    PosVec = np.array([[positionX],[positionY]])


    clock = pygame.time.Clock()  # Add clock for better frame rate control

    while True:
        # Catches user input
        # Sets keys[key] to True or False
        for event in pygame.event.get():
            if event.type == QUIT:
                close()
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    close()
                    return
                keys[event.key] = True
            elif event.type == KEYUP:
                keys[event.key] = False

        # Checks which keys are pressed by the user
        # Uses if so that more than one button at a time can be pressed.
        if keys.get(K_ESCAPE, False):
            close()
            return

        if keys.get(K_LEFT, False):
            DirVec = RotateACW @ DirVec
            PlaVec = RotateACW @ PlaVec

            directionX,directionY = DirVec
            planeX,planeY = PlaVec

        if keys.get(K_RIGHT, False):
            DirVec = RotateCW @ DirVec
            PlaVec = RotateCW @ PlaVec

            directionX,directionY = DirVec.flatten()
            planeX,planeY = PlaVec.flatten()

        if keys.get(K_UP, False):
            nPosVec = PosVec + DirVec * MOVESPEED
            if not worldMap[int(nPosVec[0,0]), int(PosVec[1,0])]:
                PosVec[0,0] = nPosVec[0,0]
            if not worldMap[int( PosVec[0,0]), int(nPosVec[1,0])]:
                PosVec[1,0] = nPosVec[1,0]
            positionX, positionY = PosVec.flatten()

        if keys.get(K_DOWN, False):
            nPosVec = PosVec - DirVec * MOVESPEED
            if not worldMap[int(nPosVec[0,0]), int(PosVec[1,0])]:
                PosVec[0,0] = nPosVec[0,0]
            if not worldMap[int( PosVec[0,0]), int(nPosVec[1,0])]:
                PosVec[1,0] = nPosVec[1,0]
            positionX, positionY = PosVec.flatten()

        if keys.get(K_F1, False):
            try:
                pygame.image.save(screen, ('PyRay' + time.strftime('%Y%m%d%H%M%S') + '.jpeg'))
            except:
                print("Couldn't save jpeg screenshot")

        if keys.get(K_F2, False):
            try:
                pygame.image.save(screen, ('PyRay' + time.strftime('%Y%m%d%H%M%S') + '.bmp'))
            except:
                print("Couldn't save bmp screenshot")

        # showShadows - On / Off
        if keys.get(K_F5, False):
            showShadow = True
        if keys.get(K_F6, False):
            showShadow = False

        # showHUD - Show / Hide
        if keys.get(K_F7, False):
            showHUD = True
        if keys.get(K_F8, False):
            showHUD = False

        # Draws roof and floor
        # screen.fill((25, 25, 25))
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

        # Starts drawing level from 0 to < WIDTH
        # column = 0
        for column in range(0,WIDTH,COLUMNWIDTH):
            cameraX = 2 * column / WIDTH - 1.0
            rayPositionX = positionX
            rayPositionY = positionY
            rayDirectionX = directionX + planeX * cameraX
            rayDirectionY = directionY + planeY * cameraX + .000000000000001  # avoiding ZDE

            # In what square is the ray?
            mapX = int(positionX)
            mapY = int(positionY)

            # Delta distance calculation
            deltaDistanceX = abs(1.0 / rayDirectionX)
            deltaDistanceY = abs(1.0 / rayDirectionY)

            # We need sideDistanceX and Y for distance calculation. Checks quadrant
            if (rayDirectionX < 0):
                stepX = -1
                sideDistanceX = (rayPositionX - mapX) * deltaDistanceX
            else:
                stepX = 1
                sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

            if (rayDirectionY < 0):
                stepY = -1
                sideDistanceY = (rayPositionY - mapY) * deltaDistanceY
            else:
                stepY = 1
                sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

            # Finding distance to a wall
            hit = 0
            while (hit == 0):
                if (sideDistanceX < sideDistanceY):
                    sideDistanceX += deltaDistanceX
                    mapX += stepX
                    side = 0
                else:
                    sideDistanceY += deltaDistanceY
                    mapY += stepY
                    side = 1

                if (worldMap[mapX, mapY] > 0):
                    hit = 1

            # Correction against fish eye effect
            if (side == 0):
                perpWallDistance = abs((mapX - rayPositionX + (1.0 - stepX) / 2.0) / rayDirectionX)
            else:
                perpWallDistance = abs((mapY - rayPositionY + (1.0 - stepY) / 2.0) / rayDirectionY)

            # Calculating HEIGHT of the line to draw
            lineHEIGHT = abs(int(HEIGHT / (perpWallDistance + .0000001)))
            drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0

            # if drawStart < 0 it would draw outside the screen
            if (drawStart < 0):
                drawStart = 0

            drawEnd = lineHEIGHT / 2.0 + HEIGHT / 2.0

            if (drawEnd >= HEIGHT):
                drawEnd = HEIGHT - 1

            # Wall colors 0 to 3
            wallcolors = [[], [150, 0, 0], [0, 150, 0], [0, 0, 150]]
            color = wallcolors[worldMap[mapX, mapY]][:]  # Make a copy to avoid modifying original

            # If side == 1 then tone the color down. Gives a "shadow" on the wall.
            # Draws shadow if showShadow is True
            if showShadow:
                if side == 1:
                    for i, v in enumerate(color):
                        color[i] = int(v / 1.2)

            # Drawing the graphics
            pygame.draw.line(screen, color, (column, drawStart), (column, drawEnd), COLUMNWIDTH)
            # column += 2

        # Drawing HUD if showHUD is True
        if showHUD:
            pygame.draw.rect(screen, (100, 100, 200), (0, HEIGHT - 40, WIDTH, 40))
            screen.blit(HUD, (20, HEIGHT - 30))

        # Updating display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

if __name__ == "__main__":
    main()