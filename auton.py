# nope
import sys
import vexiq

#region config
claw        = vexiq.Motor(1)
left_drive  = vexiq.Motor(3)
right_drive = vexiq.Motor(4, True) # Reverse Polarity
left_lift   = vexiq.Motor(5)
right_lift  = vexiq.Motor(6, True)

import drivetrain
dt          = drivetrain.Drivetrain(left_drive, right_drive, 200, 225)
#endregion config

class liftTrain:
    def __init__(self,l,r):
        this.left = l;
        this.right = r;
    def lift_up(distance):
        this.left.run(100,distance)
        this.right.run(100,distance)
        sys.sleep(1)
    def lift_down(distance):
        this.left.run(-100,distance)
        this.right.run(-100,distance)
        sys.sleep(1)

lt          = liftTrain(left_lift,right_lift)

#Main function
lt.lift_down(40)

dt.drive_until(100,50)#forward
dt.turn_until(100,-85)#turn to riser
dt.drive_until(100,490)#drives forward and push it forward
dt.drive_until(-100,235)#drives back
dt.turn_until(100,88)#turns to the left
dt.drive_until(100,700)#foward
dt.turn_until(100,-85)#turns to the right and faces pickel
dt.drive_until(100,340)#push pickel into holy goaly
dt.drive_until(-100,290)#run away from pickel in holy goaly
dt.turn_until(100,85)#turn to the left
dt.drive_until(100,630)#drive foward
dt.turn_until(100,-85)#turn to riser
dt.drive_until(100,315)#push in riser
