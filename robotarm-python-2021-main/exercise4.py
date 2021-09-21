from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for ch in range(1,4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.moveRight()
robotArm.moveRight()

for ch in range(1,4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()