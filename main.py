import pygame
from pygame.locals import *
from Config import *
from Player import Player
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

keys = {}

player = Player()

SpeedModifier = 1.0 
state = NOT_DASHING
DashDuration = DASH_DURATION
CanDash = True

fov = FOV
Speed = SPEED
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock  = pygame.time.Clock()

FOVslider = Slider(screen, 25, 25, 200, 10, min=0.1, max=5.0, step=0.1, initial = 0.8)
FOVsliderOut = TextBox(screen, 250, 15, 50, 30, fontSize=15)
SPEEDslider = Slider(screen, 25, 45, 200, 10, min=0.1, max=5.0, step=0.1, initial = SPEED)
SPEEDsliderOut = TextBox(screen, 250, 40, 50, 30, fontSize=15)

def close():
    pygame.display.quit()
    pygame.quit()
#Lower HUD_TEXT
scene = 1
font = pygame.font.SysFont("Times New Roman", 20)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        match event.type:
            case pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    close()
                    print("ESC Pressed: Running Stopped!")
                    
                keys[event.key] = True

                if event.key == K_F1:
                    if scene == 1:
                        scene = 2
                    else:
                        scene = 1 

            case pygame.KEYUP:
                keys[event.key] = False
                if event.key == K_SPACE:
                    CanDash = True

            case pygame.QUIT:
                running = False
                close()
                print("Running Stopped!")

    if not running:
        break

    HUD_TEXT = font.render(f"Currently On Scene {scene}, To change Scene Press F1", True, (255,255,255)) 
    FOV_SLIDER_TEXT = font.render("FOV", True, (255,255,255)) 
    SPEED_SLIDER_TEXT = font.render("SPEED", True, (255,255,255)) 
    pygame.display.set_caption("Pyray V 0.1.0")
    dispObj = pygame.Rect((0,0),(WIDTH, HEIGHT))

    screen.fill("black", dispObj)

    #Calculate player Grid Corrdinates

    PlayerXGridFloat:float = player.Xcord / MAP_BLK_WID
    """Player X Grid Coordinates as float"""
    
    PlayerYGridFloat:float = player.Ycord / MAP_BLK_HIE
    '''Player Y Grid Coordinates as float'''

    PlayerXGridindex:int = min(int(PlayerXGridFloat), COLUMNS - 1)
    '''Player X Grid Coordinates as int (index)'''

    PlayerYGridindex:int = min(int(PlayerYGridFloat), ROWS - 1)
    '''Player Y Grid Coordinates as int (index)'''


    # Draw BackGround
    # Draw 2D MAP
    WallColors_s1 = [[],[150,0,0],[0,150,0],[0,0,150]]
    WallColors_s2 = [[150,0,150],[150,0,0],[0,150,0],[0,0,150]]
    if scene == 1:
        for row in range(ROWS):
            for col in range(COLUMNS):
                BlockType = MAP[row, col] 
                if BlockType: # If MAP value is not 0 (a wall)
                    pygame.draw.rect(screen, WallColors_s1[BlockType], [col * MAP_BLK_WID, row * MAP_BLK_HIE, MAP_BLK_WID, MAP_BLK_HIE])

    #Draw Rays
    player.PlaVec *= fov
    for wall_column in range(0,WIDTH,COLUMN_WIDTH):
        #sweeps from -1 to 1 for cameraX value
        cameraX = 2 * wall_column / WIDTH - 1 

        RayStartX = PlayerXGridFloat
        RayStartY = PlayerYGridFloat

        RayDir = player.DirVec + (cameraX * player.PlaVec)

        RayDirectionX, RayDirectionY = RayDir.flatten()

        deltaDistanceX = abs(1.0 / (RayDirectionX + 0.0000001))
        deltaDistanceY = abs(1.0 / (RayDirectionY + 0.0000001))

        RayEndX = PlayerXGridindex
        RayEndY = PlayerYGridindex

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

            if (MAP[RayEndY, RayEndX] > 0): 
                hit = 1
                break

        if side == 0: # X-side hit
            perpWallDist = (RayEndX - RayStartX + (1.0 - stepX) / 2.0) / RayDirectionX
        else: # Y-side hit
            perpWallDist = (RayEndY - RayStartY + (1.0 - stepY) / 2.0) / RayDirectionY
        
        # Calculate the actual end point for drawing the ray
        # These are in MAP units
        HitWallX = RayStartX + RayDirectionX * perpWallDist
        HitWallY = RayStartY + RayDirectionY * perpWallDist

        # Calculate the delta in MAP units from player to wall hit point
        RayDeltaX = HitWallX - PlayerXGridFloat
        RayDeltaY = HitWallY - PlayerYGridFloat

        endX = player.Xcord + RayDeltaX * MAP_BLK_WID
        endY = player.Ycord + RayDeltaY * MAP_BLK_HIE
        if scene == 1:
            # Draw Rays
            pygame.draw.line(screen, "purple", (player.Xcord, player.Ycord), (endX, endY), 1)
        if scene == 2:
            WallHeight:int = abs(HEIGHT//(perpWallDist + 0.0000001))
            DrawStart = HEIGHT/2 - WallHeight/2  
            if DrawStart < 0:
                DrawStart = 0
            
            DrawEnd = HEIGHT/2 + WallHeight/2 
            if DrawEnd > HEIGHT:
                DrawEnd = HEIGHT - 1
            color_index = MAP[RayEndY,RayEndX]
            pygame.draw.line(screen, WallColors_s2[color_index], (wall_column, DrawStart), (wall_column, DrawEnd), COLUMN_WIDTH)
    player.PlaVec /= fov
#--------------------------------DRAW RAY LOOP END-------------------------------

    # reset values if DeltaX and DeltaY from prior Tick for current Tick
    DeltaX = 0
    DeltaY = 0
    SpeedModifier = 1.0

    if keys.get(K_LSHIFT, False):
        SpeedModifier = SPRINT_SPEED
    
    if keys.get(K_SPACE, False) and state == NOT_DASHING and CanDash:
        state = DASHING
        DashDuration = DASH_DURATION
        CanDash = False
        
    if state == DASHING:
        SpeedModifier = DASH_SPEED
        DashDuration -= 1
        if DashDuration <= 0:
            state = NOT_DASHING

    if keys.get(K_UP, False):
        ProbX = player.Xcord + player.dirX * Speed * SpeedModifier
        ProbY = player.Ycord + player.dirY * Speed * SpeedModifier


        nextCol = int(ProbX / MAP_BLK_WID)
        nextCol =  min(nextCol, COLUMNS - 1)

        if not MAP[PlayerYGridindex, nextCol] :
            DeltaX = player.dirX * Speed * SpeedModifier

        nextRow = int(ProbY / MAP_BLK_HIE)
        nextRow = max(0, min(nextRow, ROWS - 1))

        if not MAP[nextRow, PlayerXGridindex] :
            DeltaY = player.dirY * Speed * SpeedModifier

    if keys.get(K_DOWN, False):
        ProbX = player.Xcord - player.dirX * Speed * SpeedModifier
        ProbY = player.Ycord - player.dirY * Speed * SpeedModifier

        nextCol = int(ProbX / MAP_BLK_WID)
        nextCol = max(0, min(nextCol, COLUMNS - 1))
        if MAP[PlayerYGridindex, nextCol] == 0:
            DeltaX = -player.dirX * Speed * SpeedModifier

        nextRow = int(ProbY / MAP_BLK_HIE)
        nextRow = max(0, min(nextRow, ROWS - 1))
        if MAP[nextRow, PlayerXGridindex] == 0:
            DeltaY = -player.dirY * Speed * SpeedModifier

    player.Move(DeltaX, DeltaY)

    if keys.get(K_LEFT, False):
        player.DirVec = ROTATE_ACW @ player.DirVec
        player.PlaVec = ROTATE_ACW @ player.PlaVec

    if keys.get(K_RIGHT, False):
        player.DirVec = ROTATE_CW @ player.DirVec
        player.PlaVec = ROTATE_CW @ player.PlaVec

    if scene == 1:
        pygame.draw.circle(screen,"red",  (player.Xcord, player.Ycord), 2.5,1)
    
    screen.blit(HUD_TEXT, (20, HEIGHT - 30))
    screen.blit(FOV_SLIDER_TEXT, (310,18))
    screen.blit(SPEED_SLIDER_TEXT, (310,45))
    FOVSliderVal = FOVslider.getValue()
    SPEEDSliderVal = SPEEDslider.getValue()
    FOVsliderOut.setText(" "+str(FOVSliderVal))
    SPEEDsliderOut.setText(" "+str(SPEEDSliderVal))
    fov = FOVSliderVal
    Speed = SPEEDSliderVal
    pygame_widgets.update(events)
    pygame.display.flip()
    clock.tick(60.0)

pygame.quit()
