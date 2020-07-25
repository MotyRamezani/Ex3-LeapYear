def fib(arg) :
    if arg <= 0 :
        print("Please choose a number greater than 0.")
    elif arg == 1 :
        return 0
    elif arg == 2 :   
        return 1
    else :
        return fib(arg-1) + fib(arg-2)
