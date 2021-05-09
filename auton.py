# VEX IQ Python-Project
import sys
import vexiq

#region config
claw        = vexiq.Motor(1)
left_drive  = vexiq.Motor(3)
right_drive = vexiq.Motor(4, True) # Reverse Polarity
left_lift   = vexiq.Motor(5)
right_lift  = vexiq.Motor(6)

import drivetrain
dt          = drivetrain.Drivetrain(left_drive, right_drive, 200, 225)
joystick    = vexiq.Joystick()
#endregion config

import drivetrain
dt          = drivetrain.Drivetrain(left_drive, right_drive, 200, 185)

#deadzone =10
#auton code 
left_lift.run_until_time(100,0.1)
right_lift.run_until_time(-100,0.1)
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
