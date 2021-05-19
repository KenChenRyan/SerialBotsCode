# nope
import sys
import vexiq

#region config
claw        = vexiq.Motor(1)
left_drive  = vexiq.Motor(3)
right_drive = vexiq.Motor(4, True) # Reverse Polarity
left_lift   = vexiq.Motor(5)
right_lift  = vexiq.Motor(6, True)
touch_led   = vexiq.TouchLed(9)

import drivetrain
dt          = drivetrain.Drivetrain(left_drive, right_drive, 200, 225)
#endregion config

class liftTrain:
    def __init__(self,l,r):
        self.left = l;
        self.right = r;
    def lift_up(distance):
        self.left.run(100,distance)
        self.right.run(100,distance)
        sys.sleep(1)
    def lift_down(distance):
        self.left.run(-100,distance)
        self.right.run(-100,distance)
        sys.sleep(1)

lt          = liftTrain(left_lift,right_lift)

#Main function
lt.lift_down(370);
touch_led.brightness(80)
while not touch_led.is_touch():
    vexiq.lcd_write("Waiting for touch")
touch_led.brightness(0)
vexiq.lcd_write("")
dt.drive_until(100,50)#robot a little forward
dt.turn_until(100,-60)#turn right to riser
dt.drive_until(100,335)#drives forward and push it forward
dt.drive_until(-100,235)#drives back
dt.turn_until(100,56)#turns to the left
dt.drive_until(100,450)#foward
dt.turn_until(100,-38)#turns to the right and faces pickel
dt.drive_until(100,220)#push pickel into holy goaly
dt.drive_until(-100,240)#run away from pickel in holy goaly rolly polly
dt.turn_until(100,30)#turn to the left
dt.drive_until(100,450)#drive foward
dt.turn_until(100,-85)#turn to rise
dt.drive_until(100,315)#push in ri
