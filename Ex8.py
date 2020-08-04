def LeapYear(year=0,month=0,day=0):
 
    List1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    DoM = sum (List1 [:(month-1)])
    if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if (month>=3):
            num = DoM+1
        else:
            num = DoM
    else:
        num = DoM
        
    T = day + num
    N=list(str(T))
    if (int(N[-1])) == 1:
        return ("Today is the {}st day of the year!".format(T))
    elif (int(N[-1])) == 2:
        return ("Today is the {}nd day of the year!".format(T))
    elif (int(N[-1])) == 3:
        return ("Today is the {}rd day of the year!".format(T))
    else:
        return ("Today is the {}th day of the year!".format(T))