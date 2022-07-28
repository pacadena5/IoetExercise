class HourChecker:
    #Compare 2 hours and return: 0 if equals, -1 if (hour1<hour2) and 1 if (hour1>hour2)
    def comparate(self, hour1, hour2):                            
        if (hour1.hour == hour2.hour and hour1.min == hour2.min):   #Hours and min equals -> 0
            return 0
        elif (hour1.hour == hour2.hour):                            #Hours equals compare mins
            if (hour1.min < hour2.min):
                return -1
            else: 
                return 1
        else:
            if (hour1.hour < hour2.hour):                           #Not equal hours compare hours
                return -1
            else:
                return 1