import mraa

TEMPERATURE = mraa.Pwm(10)
LIGHT = mraa.Pwm(11)
alarmDoor = mraa.Gpio(2)
alarmArm = mraa.Gpio(3)
alarmBuzzer = mraa.Gpio(8)
diodeAlarm = mraa.Gpio(7)
diodeBlue = mraa.Gpio(4)
diodeGreen = mraa.Gpio(5)
diodeRed = mraa.Gpio(6)
diodeLight = mraa.Gpio(17)
lightBulb = mraa.Gpio(16)

def setupDiodePins():
    diodeBlue.dir(mraa.DIR_IN)
    diodeGreen.dir(mraa.DIR_IN)
    diodeRed.dir(mraa.DIR_IN)
