def fib(arg) :
    if arg <= 0 :
        print("Please choose a number grater than 0.")
    elif arg == 1 or arg == 2 :
        return 1
    elif arg > 2 :
        return fib(arg-1) + fib(arg-2)