from RobotArm import RobotArm
hasblock = ("")
x = 2
robotArm = RobotArm()
robotArm.randomLevel(1,7)
while True:
    robotArm.grab()
    hasblock = robotArm.scan()
    if (hasblock != ""):
        for x in range (1, x):
         robotArm.moveRight()
         x = x + 1
         print (x)
        robotArm.drop()
        for x in range (1, x):
         robotArm.moveLeft()
         x = x + 2
         print(x)
    else:
        quit()
robotArm.wait()