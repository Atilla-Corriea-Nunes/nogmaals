from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for w in range (1, 5):
    for z in range (0, w):
        robotArm.grab()
        for x in range (0, 5):
         robotArm.moveRight()
        robotArm.drop()
        for y in range (0, 5):
         robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()