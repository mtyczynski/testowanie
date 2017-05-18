import unittest

from constants import DARK, LIGHT
from light_lib import Light, setupLight, setLight, getLightStatus


class MyTestCase(unittest.TestCase):
    light = Light()

    def test_light(self):
        setupLight(light=self.light)
        setLight(value=LIGHT)
        status = getLightStatus()
        self.assertFalse(status["light"])
        self.assertFalse(status["diode"])

    def test_dark(self):
        setupLight(light=self.light)
        setLight(value=DARK)
        status = getLightStatus()
        self.assertTrue(status["light"])
        self.assertTrue(status["diode"])



if __name__ == '__main__':
    unittest.main()
