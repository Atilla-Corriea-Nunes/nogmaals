from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for z in range (0, 7):
    robotArm.grab()
    for x in range(0, 8):
        robotArm.moveRight()
    robotArm.drop()
    for y in range(0, 8):
        robotArm.moveLeft()
robotArm.wait()