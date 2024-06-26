import time
from machine import Pin, PWM

#construct PWM object, with LED on Pin(25)
pwm = PWM(Pin(25))

#set the PWM frecuency
pwm.freq(1000)

#fade the LED in and out a few times
duty = 0
direction = 1
for _ in range(8*256):
    duty+= direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction =  1
    pwm.duty_u16(duty * duty)
    time.sleep(0.001)