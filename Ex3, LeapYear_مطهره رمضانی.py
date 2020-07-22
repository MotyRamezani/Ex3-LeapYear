Year = int(input ('Please add a year: '))

if  Year % 4 == 0 :
    if  Year % 100 == 0 :
        if  Year % 400 == 0 :
            print ('This year is a Leap Year!')
        else :
            print ('This year is NOT a Leap Year!')
    else :
        print ('This year is a Leap Year!')
else :
    print ('This year is NOT a Leap Year!')
