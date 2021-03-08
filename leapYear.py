def ly(x):
    if(x % 4 == 0 and x % 100 != 0):
        msg = "Input year is a leap year."
        print(msg)
    elif(x % 100 == 0 and x % 400 == 0):
        msg = "Input year is a leap year."
        print(msg)
    else:
        msg = "Input year is not a leap year."
        print(msg)

    return(msg)