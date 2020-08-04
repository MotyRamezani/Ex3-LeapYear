class Time:
    
    def __init__(self,Hour_value=00,Minute_value=00,Secound_value=00):
        self.Hour = Hour_value
        self.Minute = Minute_value
        self.Secound = Secound_value
        
    def Show (self):
        return str(self.Hour)  + ":" + str(self.Minute) + ":" + str(self.Secound)
    
    def __str__(self):
        return str(self.Hour)  + ":" + str(self.Minute) + ":" + str(self.Secound)
    
    def __repr__(self):  
        return str(self.Hour)  + ":" + str(self.Minute) + ":" + str(self.Secound)
    
    def __add__(self,other):
        secound = self.Secound + other.Secound
        minute = self.Minute + other.Minute
        hour = self.Hour + other.Hour
        if secound>=60:
            secound = secound-60
            minute+=1
        if minute>=60:
            minute = minute-60
            hour+=1
        return str(hour)  + ":" + str(minute) + ":" + str(secound)
    
    def __sub__(self,other):
        secound = self.Secound - other.Secound
        Sec = secound
        minute = self.Minute - other.Minute
        hour = self.Hour - other.Hour
        if secound<0:
            secound = (self.Secound + 60) - other.Secound
            minute-=1
        if minute<0:
            if Sec<0:
               minute = (self.Minute + 59) - other.Minute
               hour-=1 
            else:
                minute = (self.Minute + 60) - other.Minute
                hour-=1
        return str(hour)  + ":" + str(minute) + ":" + str(secound)  
    
    def __lt__(self,other):
        return (self.Hour, self.Minute, self.Secound) < (other.Hour, other.Minute, other.Secound)
    
    def __eq__(self,other):
        return (self.Hour, self.Minute, self.Secound) == (other.Hour, other.Minute, other.Secound)
    
    def __gt__(self,other):
        return (self.Hour, self.Minute, self.Secound) > (other.Hour, other.Minute, other.Secound)