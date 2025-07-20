
import numpy as np
import pygame


map = np.array([[1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,1],
                [1,0,0,1,0,0,0,1],
                [1,0,0,0,1,0,0,1],
                [1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1]])

print("number of rows is",len(map))
print("number of colm is",len(map[0]))

WIDTH = 800
HIEGHT = 600
pygame.init()

running = True

screen = pygame.display.set_mode((WIDTH,HIEGHT))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            pygame.quit()

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
    pygame.display.flip()