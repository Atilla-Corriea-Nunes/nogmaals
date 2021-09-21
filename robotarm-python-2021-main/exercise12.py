w = 0
from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for y in range(0 ,9):
    robotArm.moveRight()
for x in range (0, 100):
    robotArm.grab()
    color = robotArm.scan()
    if (color == "red"):
        for z in range (0, 10):
            robotArm.moveRight()
        robotArm.drop()
        for v in range (0, w):
            robotArm.moveLeft()
        w = 0
    else:
        robotArm.drop()
    robotArm.moveLeft()
    w = w + 1
robotArm.wait()