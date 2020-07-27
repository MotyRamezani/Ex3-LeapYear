def fib_list(arg):
    if arg <= 0:
        raise Exception("Please choose a number greater than 0.")
    elif arg == 1:
        return [0]
    elif arg == 2:
        return [0, 1]
    List = fib_list(arg - 1)
    List.append(List[-2] + List[-1])
    return List