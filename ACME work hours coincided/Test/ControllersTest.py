import unittest
import sys

# appending the directory of dependencys
sys.path.append('App/Models')
sys.path.append('App/Controllers')
from Person import Person
from WorkHoursController import WorkHoursController

class ControllersTest(unittest.TestCase):

    #Example from Ioet #1
    def test_Example2Coincided(self):
        per1 = Person("pepe",[['MO','10:15-12:00'],['TU','10:00-12:00'],['TH','13:00-13:15'],['SA','14:00-18:00'],['SU','20:00-21:00']])
        per2 = Person("juan",[['MO','10:00-12:00'],['TH','12:00-14:00'],['SU','20:00-21:00']])
        wk= WorkHoursController()
        EXPECTED = 3
        self.assertEqual(EXPECTED, wk.hoursCoincided(per1,per2))
    
    # 0 coincidences, values in lower limit #2
    def test_zeroLowerLimit(self):
        per1 = Person("pepe",[['MO','10:15-12:00'],['TH','13:00-13:15'],['SA','14:00-18:00'],['SU','20:00-21:00']])
        per2 = Person("juan",[['MO','09:00-10:15'],['TH','12:00-13:00'],['SU','19:00-20:00']])
        wk= WorkHoursController()
        EXPECTED = 0
        self.assertEqual(EXPECTED, wk.hoursCoincided(per1,per2))

    # 0 coincidences, values in upper limit #3
    def test_zeroUpperLimit(self):
        per1 = Person("pepe",[['MO','10:15-12:00'],['TH','13:00-13:15'],['SA','14:00-18:00'],['SU','20:00-21:00']])
        per2 = Person("juan",[['MO','12:00-12:15'],['TH','13:15-15:00'],['SU','21:00-22:00']])
        wk= WorkHoursController()
        EXPECTED = 0
        self.assertEqual(EXPECTED, wk.hoursCoincided(per1,per2))
    
    # full coincidences, values in lower limit #4
    def test_fullLowerLimit(self):
        per1 = Person("pepe",[['MO','10:15-12:00'],['TH','13:00-13:15'],['SA','14:00-18:00'],['SU','20:00-21:00']])
        per2 = Person("juan",[['MO','09:00-10:16'],['TH','12:00-13:01'],['SU','19:00-20:01']])
        wk= WorkHoursController()
        EXPECTED = 3
        self.assertEqual(EXPECTED, wk.hoursCoincided(per1,per2))

    # full coincidences, values in upper limit #5
    def test_fullUpperLimit(self):
        per1 = Person("pepe",[['MO','10:15-12:00'],['TH','13:00-13:15'],['SA','14:00-18:00'],['SU','20:00-21:00']])
        per2 = Person("juan",[['MO','11:59-12:15'],['TH','13:14-15:00'],['SU','20:59-22:00']])
        wk= WorkHoursController()
        EXPECTED = 3
        self.assertEqual(EXPECTED, wk.hoursCoincided(per1,per2))

    # some normal value #6
    def test_NormalValues1(self):
        per1 = Person("pepe",[['MO','10:15-12:00'],['TH','13:00-15:15']])
        per2 = Person("juan",[['MO','10:00-12:15'],['TH','13:15-15:00'],['SU','20:59-22:00']])
        wk= WorkHoursController()
        EXPECTED = 2
        self.assertEqual(EXPECTED, wk.hoursCoincided(per1,per2))
    
if __name__ == '__main__':
    unittest.main()