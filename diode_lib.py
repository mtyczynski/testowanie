import mraa

class Diodes():
    diodeRed = mraa.Gpio(6)
    diodeGreen = mraa.Gpio(5)
    diodeBlue = mraa.Gpio(4)

def setupTempDiodes(diodes):
    diodes.diodeBlue.dir(mraa.DIR_IN)
    diodes.diodeGreen.dir(mraa.DIR_IN)
    diodes.diodeRed.dir(mraa.DIR_IN)

def getTempDiodesGlow():
    red = diodeRed.read()
    blue = diodeBlue.read()
    green = diodeGreen.read()
    diodesGlow = {"blue": blue, "green": green, "red": red}

    return diodesGlow







