from datetime import datetime, time
from time import sleep
from led import Led
from weather import WeatherAPI
import pigpio
import atexit

PI = pigpio.pi()

# Example usage of the PI
# PI.set_PWM_dutycycle(PIN, BRIGHTNESS)

RED = Led(17)
GREEN = Led(22)
BLUE = Led(24)
WEATHER = WeatherAPI

def day_time():

    # gets the current time
    now = datetime.now()
    now_time = now.time()

    # if the time is greater than 7:00AM and less than 9:30AM
    print "The time is", now_time
    if now_time < time(22,30) and now_time > time(8,00):
        return True
    else:
        return False

def set_pwm_cycle():
    PI.set_PWM_dutycycle(RED.get_pin(), RED.get_brightness())
    PI.set_PWM_dutycycle(GREEN.get_pin(), GREEN.get_brightness())
    PI.set_PWM_dutycycle(BLUE.get_pin(), BLUE.get_brightness())

def turn_lights_on(speed):
    if WEATHER.hot:
        RED.set_brightness(200)
        GREEN.set_brightness(55)
        BLE.set_brightness(55)
    elif WEATHER.warm:
        RED.set_brightness(200)
        GREEN.set_brightness(100)
        BLE.set_brightness(100)
    elif WEATHER.cold:
        RED.set_brightness(55)
        GREEN.set_brightness(55)
        BLE.set_brightness(200)
    elif WEATHER.freezing:
        RED.set_brightness(100)
        GREEN.set_brightness(100)
        BLE.set_brightness(255)
    else:
        RED.set_brightness(0)
        GREEN.set_brightness(0)
        BLE.set_brightness(255)

    set_pwm_cycle()

def turn_lights_off(speed):
    RED.set_brightness(0); 
    GREEN.set_brightness(0); 
    BLUE.set_brightness(0); 
    set_pwm_cycle()

def exit_handler():
    PI.set_PWM_dutycycle(RED.get_pin(), 0)
    PI.set_PWM_dutycycle(GREEN.get_pin(), 0)
    PI.set_PWM_dutycycle(BLUE.get_pin(), 0)

def run():
    while True:
        if day_time():
            print "Turning the lights on..."
            turn_lights_on(0.05)
        else:
            print "Turning the lights off..."
            turn_lights_off(0.05)

        sleep(10)

# handles a exit signal
atexit.register(exit_handler)

# executes the program
run()

