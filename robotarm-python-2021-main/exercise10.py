from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for x in range (9, 0, -2):
    robotArm.grab()
    for d in range (0, x):
        robotArm.moveRight()
    robotArm.drop()
    x = x - 1
    for y in range (0, x):
        robotArm.moveLeft()
robotArm.wait()