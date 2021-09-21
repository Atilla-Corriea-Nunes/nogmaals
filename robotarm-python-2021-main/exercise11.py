from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
for y in range(0 ,9):
    robotArm.moveRight()
for x in range (0, 10):
    robotArm.grab()
    color = robotArm.scan()
    if (color == "white"):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
robotArm.wait()