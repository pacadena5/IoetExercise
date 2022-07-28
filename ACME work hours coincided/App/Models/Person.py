class Person:
    def __init__(self, name, week):
        self.name = name
        self.week = week

    def haveDay(self, day):
        bool = False
        for dayPerson in self.week:
            try:
                var = dayPerson.index(day)
            except:
                var = -1
            else:
                bool = True
        
        return bool

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
