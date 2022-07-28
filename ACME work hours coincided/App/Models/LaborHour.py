from Hour import Hour

class LaborHour:
    def __init__(self, strHours):
        strHours = strHours.split('-')
        self.hourIn = Hour(strHours[0])
        self.hourOut = Hour(strHours[1])


