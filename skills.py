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
mode =" "
deadzone =10
while True:
#mode selection 
    if(joystick.bEup() and joystick.bFup()):
        vexiq.lcd_write("Tank mode")
        mode = "tank"
    if(joystick.bEdown() and joystick.bFdown()):
        vexiq.lcd_write("Arcade mode")
        mode = "arcade"
#run correct mode 
    if(mode =="tank"):
#tank
        if(abs(joystick.axisA())>deadzone):
            left_drive.run(joystick.axisA())
        else:
            left_drive.off()
        if(abs(joystick.axisD())>deadzone):
            right_drive.run(joystick.axisD())
        else:
            right_drive.off()
    elif(mode =="arcade"):
#arcade 
        if(abs(joystick.axisD())>deadzone or abs(joystick.axisC())>deadzone):
            left_drive.run(joystick.axisD()+joystick.axisC()/2)
            right_drive.run(joystick.axisD()-joystick.axisC()/2)
        else:
            right_drive.off()
            left_drive.off()
    else:
        vexiq.lcd_write("Please select a mode")
#lift 
    if(joystick.bRup()):
        right_lift.run(-100)
        left_lift.run(100)
    elif(joystick.bRdown()):
        right_lift.run(100) 
        left_lift.run(-100)
    else:
        right_lift.off()
        left_lift.off()
        
#claw
    if(joystick.bLup()):
        claw.run(50)
    elif(joystick.bLdown()):
        claw.run(-50)
    else:
        claw.off()
#macro for height
riser_height = 250
# if(joystick.bEup()):
# right_lift_motor.run_until_position(50,riser_height,True)
# left_lift_motor.run_until_position(50,riser_height,True)
