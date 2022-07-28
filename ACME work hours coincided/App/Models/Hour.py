from locale import atoi

class Hour:
    def __init__(self, str):    #str format ('hh:mm')
        hour = str.split(':')
        self.hour = atoi(hour[0].strip())
        self.min = atoi(hour[1].strip())