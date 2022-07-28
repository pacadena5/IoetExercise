import sys

# Appending the directory of controllers
sys.path.append('App/Controllers')
from WorkHoursController import WorkHoursController

wk= WorkHoursController()

#Output
for i in range(0,len(wk.persons)):
    for j in range(i+1, len(wk.persons)):
        hoursCoincided = wk.hoursCoincided(wk.persons[i],wk.persons[j])
        print(wk.persons[i].name + ' - ' + wk.persons[j].name + " : " + str(hoursCoincided))