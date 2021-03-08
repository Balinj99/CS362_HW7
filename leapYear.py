def ly(x):
    if(x % 4 == 0 and x % 100 != 0):
        msg = "Input year is a leap year."
        print(msg)
        return(msg)
    else:
        msg = "Input year is not a leap year."
        print(msg)
        return(msg)