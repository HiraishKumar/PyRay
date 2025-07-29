import numpy as np
from numpy import ndarray
from Config import *

class Player:
    def __init__(self, InitCordX:float = INIT_PLAYER_X,
                InitCordY:float = INIT_PLAYER_Y,
                InitDirX:float = INIT_DIR_X,
                InitDirY:float = INIT_DIR_Y,
                InitPlanX:float = INIT_PLAN_X, 
                InitPlanY:float = INIT_PLAN_Y 
            ):
        self.Xcord:float = InitCordX
        self.Ycord:float = InitCordY
        self.DirVec:ndarray = np.array([[InitDirX] ,[InitDirY]])
        self.PlaVec:ndarray = np.array([[InitPlanX],[InitPlanY]])

    @property
    def dirX(self) -> float:
        return self.DirVec[0,0]

    @dirX.setter
    def dirX(self, value: float):
        self.DirVec[0,0] = value

    @property
    def dirY(self) -> float:
        return self.DirVec[1,0]

    @dirY.setter
    def dirY(self, value: float):
        self.DirVec[1,0] = value

    @property
    def planX(self) -> float:
        return self.PlaVec[0,0]

    @planX.setter
    def planX(self, value: float):
        self.PlaVec[0,0] = value

    @property
    def planY(self) -> float:
        return self.PlaVec[1,0]

    @planY.setter
    def planY(self, value: float):
        self.PlaVec[1,0] = value

    def Move(self, deltaX:float = 0.0, deltaY:float = 0.0):
        self.Xcord += deltaX
        self.Ycord += deltaY

    def MoveTo(self, Xcord:float, Ycord:float):
        self.Xcord += Xcord
        self.Ycord += Ycord
