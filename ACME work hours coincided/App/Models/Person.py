class Person:
    def __init__(self, name, week):
        self.name = name
        self.week = week

    def haveDay(self, day):
        band = False
        for dayPerson in self.week:
            try:
                dayPerson.index(day)
            except:
                continue #controlled exception
            else:
                band = True
                break   
        return band

    def indexDay(self, day):
        i = 0
        for dayPerson in self.week:
            try:
                var = dayPerson.index(day) 
            except:
                var = -1
            else:
                return i
            i+=1
        return -1
