import numpy as np

ROT_SPEED = 0


rotate = 0
vec = 0

for i in range(10):
    rotate = np.array([[np.cos(ROT_SPEED), np.sin(-ROT_SPEED)],
                    [np.sin(ROT_SPEED), np.cos( ROT_SPEED)]])

    vec = np.array([[1],
                    [0]])
    # test = np.sin(ROT_SPEED)
    # print(test)
    rotated_vec = rotate @ vec
    print((rotated_vec))
    ROT_SPEED +=1