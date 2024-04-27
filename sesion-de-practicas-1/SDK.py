import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.on()
    utime.sleep(0.2)
    led.off()
    utime.sleep(0.2)