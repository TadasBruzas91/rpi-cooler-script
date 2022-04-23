from threading import Thread
import sys
from time import sleep
from py_console import console
import psutil
try:
    import lgpio as sbc
except:
    console.error("lgpio not found!!!")
    console.warn("To install library run 'sudo apt install python3-lgpio'")
    sys.exit()


class FanController(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lgpio_started = False
        self.__gpio_state = None
        self.__fan_on = False
        self.__fan_output_pin = None
        self.__cpu_temp = 0
        self.__hightempthreshold = 60
        self.__lowtempthreshold = 50

    def start_lgpio(self):
        try:
            self.__gpio_state = sbc.gpiochip_open(0)
            self.lgpio_started = True
        except:
            self.lgpio_started = False

    def close_lgpio(self):
        try:
            sbc.gpiochip_close(self.__gpio_state)
            console.success("Succesfuly closed lgpio.")
        except:
            console.error("Can't close lgpio!!!")

    def set_fan_output_pin(self, pin):
        if(self.lgpio_started):
            sbc.gpio_claim_output(self.__gpio_state, pin)
            self.__fan_output_pin = pin
        else:
            console.warn("lgpio not started please run 'start_lgpio'")

    def set_high_temp_threshold(self, temp):
        if(temp > self.__lowtempthreshold):
            self.__hightempthreshold = temp
        else:
            console.warn(
                "High tempt threshold can,t be lower or eaqual to Low temp threshold!")

    def set_low_temp_threshold(self, temp):
        if(temp < self.__hightempthreshold):
            self.__lowtempthreshold = temp
        else:
            console.warn(
                "Low tempt threshold can,t be higher or eaqual to High temp threshold!")

    def __get_cpu_temp(self):
        self.__cpu_temp = int(psutil.sensors_temperatures()[
                              "cpu_thermal"][0][1])

    def __fan_switch(self, swtch):
        if(self.lgpio_started and self.__fan_output_pin):
            sbc.gpio_write(self.__gpio_state, self.__fan_output_pin, swtch)

    def __chech_if_cooling_rquired(self):
        if not self.__fan_on and self.__cpu_temp >= self.__hightempthreshold:
            self.__fan_switch(1)
            self.__fan_on = True
        if self.__fan_on and self.__cpu_temp <= self.__lowtempthreshold:
            self.__fan_switch(0)
            self.__fan_on = False

    def run(self):
        while True:
            self.__get_cpu_temp()
            self.__chech_if_cooling_rquired()
            print(f"CPU_temp: {self.__cpu_temp}\tFAN_on: {self.__fan_on}")
            sleep(1)
