from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=5, mode=Timer.PERIODIC, callback=tick)
#tim.init(mode=Timer.ONE_SHOT, period=100)