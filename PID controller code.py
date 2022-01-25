#PID Controler Code 

from controller import Robot


robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

time_step=30
max_speed = 6.28

#Motor
left_motor1 = robot.getDevice('wheel1')
left_motor2 = robot.getDevice('wheel3')
right_motor1 = robot.getDevice('wheel2')
right_motor2 = robot.getDevice('wheel4')
left_motor1.setPosition(float('inf'))
right_motor1.setPosition(float('inf'))
left_motor2.setPosition(float('inf'))
right_motor2.setPosition(float('inf'))
left_motor1.setVelocity(0.0)
right_motor1.setVelocity(0.0)
left_motor2.setVelocity(0.0)
right_motor2.setVelocity(0.0)

#Ir Sensor
right_ir= robot.getDevice('ir_right')
right_ir.enable(time_step)
mid_ir= robot.getDevice('ir_mid')
mid_ir.enable(time_step)
left_ir= robot.getDevice('ir_left')
left_ir.enable(time_step)



#simulation
# Main loop:
# - perform simulation steps until Webots is stopping the controller

while robot.step(timestep) != -1:
# Read the sensors
# Enter here functions to read sensor data, like:
#val = ds.getValue()
      right_ir_val = right_ir.getValue()
      mid_ir_val = mid_ir.getValue()
      left_ir_val = left_ir.getValue()
      print (" left: {} mid: {} right: {}".format(left_ir_val,mid_ir_val,right_ir_val))
      left_speed = -(max_speed*0.75)
      right_speed = -(max_speed*0.75)
      if left_ir_val<1000 and right_ir_val<1000 and mid_ir_val>=1000:
          left_motor1.setVelocity( -left_speed )
          right_motor1.setVelocity(- right_speed )
          left_motor2.setVelocity( -left_speed )
          right_motor2.setVelocity(- right_speed )
          
  
      if left_ir_val<1000 and right_ir_val>=1000 and mid_ir_val>=1000:
          left_motor1.setVelocity(-left_speed)
          right_motor1.setVelocity(0)
          left_motor2.setVelocity(-left_speed)
          right_motor2.setVelocity(0)
          
      if left_ir_val>=1000 and right_ir_val<1000 and mid_ir_val>=1000:
          left_motor1.setVelocity(0)
          right_motor1.setVelocity(-right_speed)
          left_motor2.setVelocity(0)
          right_motor2.setVelocity(-right_speed)
          
      if left_ir_val>=1000 and right_ir_val<1000 and mid_ir_val<1000:
          left_motor1.setVelocity(0)
          right_motor1.setVelocity(- right_speed )
          left_motor2.setVelocity(0)
          right_motor2.setVelocity(- right_speed )
          
      if left_ir_val<1000 and right_ir_val>=1000 and mid_ir_val<1000:
          left_motor1.setVelocity(-left_speed)
          right_motor1.setVelocity(0)
          left_motor2.setVelocity(-left_speed)
          right_motor2.setVelocity(0)
          
      if left_ir_val<1000 and right_ir_val<1000 and mid_ir_val<1000:
          left_motor1.setVelocity(-left_speed)
          right_motor1.setVelocity(-right_speed)
          left_motor2.setVelocity(-left_speed)
          right_motor2.setVelocity(-right_speed)
          
# Enter here functionsto send actuator commands, like:
#motor.setPosition(10.0)
pass
#Enter here exit cleanup code
