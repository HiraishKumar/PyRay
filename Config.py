import numpy as np
from numpy import ndarray 

WIDTH:int= 800
HEIGHT:int = 600


SPEED:int = 2 
SPRINT:int = 1
ROTATION_SPEED:float   = 0.08
RAY_COUNT:int = 30
FOV:float = 1.0
'''Y component of the planer vector Perpendicular to INIT_DIR_VEC,
See Config.py to change FOV '''

INIT_DIR_X:float = 1.0
INIT_DIR_Y:float = 0.0

COLUMN_WIDTH:int = 4

INIT_PLAYER_X:float = 400.0
INIT_PLAYER_Y:float = 300.0

MAP: ndarray = np.array([
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

ROWS :int
COLUMNS:int
ROWS ,  COLUMNS = MAP.shape
MAP_BLK_WID:int = WIDTH / COLUMNS

MAP_BLK_HIE:int = HEIGHT / ROWS

HUD_HEIGHT:int = HEIGHT / ROWS
HUD_WIDTH:int = WIDTH

ROTATE_CW: ndarray = np.array([[np.cos(ROTATION_SPEED), np.sin(-ROTATION_SPEED)],
                     [np.sin(ROTATION_SPEED), np.cos( ROTATION_SPEED)]])
ROTATE_ACW: ndarray = np.array([[np.cos(-ROTATION_SPEED), np.sin(ROTATION_SPEED)],
                     [np.sin(-ROTATION_SPEED), np.cos(-ROTATION_SPEED)]])