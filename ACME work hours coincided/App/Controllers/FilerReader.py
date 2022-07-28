import sys

# appending the directory of person
sys.path.append('App/Models')
from Person import Person

class FileReader:
    def __init__(self):
        self.persons = []
        self._chargeData()

    def _chargeData(self):
        rows = self._readFile("App/Resources/data.txt")

        for row in rows:
            line = row.split('=')
            name = line[0]
            week = self._reedWeek(line[1])
            print("name > "+name)
            print(week)
            self.persons.append(Person(name,week))
        
    def _reedWeek(self, strWeek):   #separating days('MO') and the hours worked('12:00-15:00')
        days = []
        daysString = strWeek.split(',')
        
        for day in daysString:
            days.append([day[0:2],day[2:]])

        return days

    def _readFile(self, fileName):  #reading file per rows
        rows = []
        file  = open(fileName,'r')
        line = file.readline()
        while not(line==''):
            line  = line.strip('\n')
            rows.append(line)       
            line = file.readline()
        
        file.close()
        return rows

    def getPersons(self):
        return self.persons