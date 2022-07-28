from posixpath import split
import sys
from FilerReader import FileReader
from HoursChecker import HourChecker
from LaborHour import LaborHour

# appending the directory of person
sys.path.append('App/Models')
from Person import Person

class WorkHoursController:
   
    def __init__(self):
        self.persons = []
        fr = FileReader()
        self.persons = fr.getPersons()
        del fr

    def hoursCoincided(self, p1, p2): #compare hours coincided between 2 persons
        days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
        hoursCoincided = 0
        for day in days:
            #dayIndex = days.index(day)
            #print("index>>"+ dayIndex.__str__())

            if( p1.haveDay(day) and p2.haveDay(day)):       #Compare the hours if they work the same day
                p1WeekIndex = p1.indexDay(day)
                """ print("el indice en el for>")
                print(p1WeekIndex) """
                p2WeekIndex = p2.indexDay(day)

                if (self.compareHours(p1.week[p1WeekIndex][1], p2.week[p2WeekIndex][1])):
                    hoursCoincided+=1
        """ print("HORAS COINCIDIDAS")
        print(hoursCoincided) """
        return hoursCoincided

    def compareHours(self, hoursWorked1, hoursWorked2):
        coincidedHours = False
        laborHour1 = LaborHour(hoursWorked1)
        laborHour2 = LaborHour(hoursWorked2)
        hoChecker = HourChecker()
        
        #if start working at the same time then they coincide
        if( hoChecker.comparate(laborHour1.hourIn, laborHour2.hourIn) == 0):     
            coincidedHours = True
        # if worker 1 start before worker 2 'comparate(laborHour1.hourIn, laborHour2.hourIn)==-1' 
        # and end after worker2 start 'comparate(laborHour1.hourOut, laborHour2.hourIn) == 1' then they  concide
        elif(hoChecker.comparate(laborHour1.hourIn, laborHour2.hourIn) == -1 and hoChecker.comparate(laborHour1.hourOut, laborHour2.hourIn) == 1): 
            coincidedHours = True
        # if worker 1 start after worker 2 start '(comparate(laborHour1.hourIn, laborHour2.hourIn)==1)' and
        # if worker 1 start before worker 2 end '(hour1.comparete(hour2) == -1)' then they  concide
        elif(hoChecker.comparate(laborHour1.hourIn, laborHour2.hourIn) == 1 and hoChecker.comparate(laborHour1.hourIn, laborHour2.hourOut) == -1):
            coincidedHours = True
        return coincidedHours



