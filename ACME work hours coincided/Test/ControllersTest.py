import unittest
import sys

# appending the directory of WorkHour
sys.path.append('App/Models')
from LaborHour import LaborHour

class ControllersTest(unittest.TestCase):

    def test_Example2Coincided(self):
        per1 = Person("pepe",[['MO10:15-12:00'],['TU10:00-12:00'],['TH13:00-13:15'],['SA14:00-18:00'],['SU20:00-21:00']])
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()