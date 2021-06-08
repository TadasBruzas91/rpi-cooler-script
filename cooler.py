import threading
from time import sleep
import lgpio as sbc

on = False

OUTPUT_PIN = 21
HighTemp = 65
LowTemp = 50

h = sbc.gpiochip_open(0)
sbc.gpio_claim_output(h, OUTPUT_PIN)


def getCpuTemp():
    tempFile = open("/sys/devices/virtual/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp) / 1000


def fanSwitch(temp):
    global on, off
    if not(on) and temp >= HighTemp:
        sbc.gpio_write(h, OUTPUT_PIN, 1)
        on = True

    elif on and temp < LowTemp:
        sbc.gpio_write(h, OUTPUT_PIN, 0)
        on = False


try:
    event = threading.Event()
    while True:
        cpuTemp = int(getCpuTemp())
        fanSwitch(cpuTemp)
        event.wait(5)


except KeyboardInterrupt:
    sbc.gpiochip_close(h)
    print("Off")
