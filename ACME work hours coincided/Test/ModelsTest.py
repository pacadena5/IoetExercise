import unittest
import sys

# appending the directory of person
sys.path.append('App/Models')
from Person import Person
from LaborHour import LaborHour

class ModelsTest(unittest.TestCase):
    
    def test_indexDayInRange(self):
        per = Person("pepe",[['MO', '10:00-12:00'], ['TU', '10:00-12:00'], ['TH', '01:00-03:00'], ['SA', '14:00-18:00'], ['SU', '20:00-21:00']])
        self.assertEqual(2, per.indexDay('TH'))
    
    def test_getHours(self):
        per = Person("pepe",[['MO', '10:00-12:00'], ['TU', '10:00-12:00'], ['TH', '01:00-03:00'], ['SA', '14:00-18:00'], ['SU', '20:00-21:00']])
        self.assertEqual('01:00-03:00', per.week[per.indexDay('TH')][1])

    def test_readingHours(self):
        h = LaborHour('10:00-12:25')
        self.assertEqual(h.hourIn.hour, 10) #Reading start hour
        self.assertEqual(h.hourIn.min, 00) #Reading start min
        self.assertEqual(h.hourOut.hour, 12) #Reading end hour
        self.assertEqual(h.hourOut.min, 25) #Reading end min


if __name__ == '__main__':
    unittest.main()