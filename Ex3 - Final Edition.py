year = int(input ('Please add a year: '))
while (year<=0):
    year = int(input('Please add a number greater than 0: '))
month = int(input('Please add a month: '))
while (month>=13 or month<=0):
    month = int(input('Please add a number between 0 to 12: '))
day = int(input('Please add a day: '))

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
    print ('Today is the',T,'st day of the year!')
elif (int(N[-1])) == 2:
    print ('Today is the',T,'nd day of the year!')
elif (int(N[-1])) == 3:
    print ('Today is the',T,'rd day of the year!')
else:
    print ('Today is the',T,'th day of the year!')