def fb(x):
    for i in range(1, 101):
        if(i % 3 == 0):
            print("Fizz")
        else:
            print(i)
    
    if(x % 3 == 0):
        return("Fizz")
    else:
        return x