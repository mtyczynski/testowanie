import unittest

import mraa

from diode_lib import getTempDiodesGlow, Diodes, setupTempDiodes
from pins_setup import setupDiodePins
from temp_lib import setTemperature, getTemperature

class MyTestCase(unittest.TestCase):
    diodes = Diodes()

    def setUp(self):
        # setupPins()
        setupTempDiodes(self.diodes)
        # diodeBlue = mraa.Gpio(4)
        # diodeGreen = mraa.Gpio(5)
        # diodeRed = mraa.Gpio(6)
        # diodeBlue.dir(mraa.DIR_IN)
        # diodeGreen.dir(mraa.DIR_IN)
        # diodeRed.dir(mraa.DIR_IN)

    def test_something(self):
        setTemperature(50)
        a = getTempDiodesGlow()
        print a
        print getTemperature()

        self.assertTrue(a["blue"])


if __name__ == '__main__':
    unittest.main()
