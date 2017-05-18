from pins_setup import alarmArm, alarmBuzzer, diodeAlarm, alarmDoor
import mraa

class Alarm():
    alarmArm = mraa.Gpio(3)
    alarmBuzzer = mraa.Gpio(8)
    diodeAlarm = mraa.Gpio(7)
    alarmDoor = mraa.Gpio(2)

def setupAlarm(alarm):
    alarm.alarmArm.dir(mraa.DIR_IN)
    alarm.alarmBuzzer.dir(mraa.DIR_IN)
    alarm.diodeAlarm.dir(mraa.DIR_IN)
    alarm.alarmDoor.dir(mraa.DIR_IN)

def getAlarmStatus():
    alarm = alarmArm.read()
    buzzer = alarmBuzzer.read()
    diode = diodeAlarm.read()
    door = alarmDoor.read()

    alarmStatus = {"alarm": alarm, "buzzer": buzzer, "diode": diode, "door": door}

    return alarmStatus