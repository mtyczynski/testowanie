import time

from constants import SUCCESS
from pins_setup import lightBulb, diodeLight, LIGHT
import mraa


LIGHT.period_us(700)
LIGHT.enable(True)

class Light():
    lightBulb = mraa.Gpio(16)
    diodeLight = mraa.Gpio(17)

def setupLight(light):
    light.lightBulb.dir(mraa.DIR_IN)
    light.diodeLight.dir(mraa.DIR_IN)

def getLightStatus():
    light = lightBulb.read()
    diode = diodeLight.read()

    lightStatus = {"light": light, "diode": diode}

    return lightStatus

class LightSensor():
    lightSensor = mraa.Pwm(11)

def getLightSensorStatus(sensor):
    return sensor.read()

def setLight(value=0):
    print LIGHT.read()
    if LIGHT.write(value) == SUCCESS:
        time.sleep(1)
        print "Tak jest!"
        return True

    print "Bagno."
    return False
