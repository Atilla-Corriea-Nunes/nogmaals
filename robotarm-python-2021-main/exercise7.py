from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for y in range (0, 5):
    for x in range (0,6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()  
    robotArm.moveRight()     
robotArm.wait()