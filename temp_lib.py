from pins_setup import TEMPERATURE
from constants import SUCCESS
from commonFunctions import translate
import time

def setTemperature(value=0):
    val = translate(value, 0, 50, 0.0, 1.0)
    val = 0.37
    TEMPERATURE.period_us(700)
    TEMPERATURE.enable(True)
    print TEMPERATURE.read()
    if TEMPERATURE.write(val) == SUCCESS:
        time.sleep(1)
        print "Tak jest!"
        return True

    print "Bagno."
    return False

def getTemperature():
    return translate(TEMPERATURE.read(), 0.0, 1.0, 0, 50)

