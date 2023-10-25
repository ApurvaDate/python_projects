
#in case of severe errors, we need to stop our programs, in that case we dont use the except block, or raise a value error.
#with this we are able to throw our own error.

while True:
    try:
        age = int(input("what is your age "))
        print(age)  #if we give a string as an input we get an error
        10/age  
        raise ValueError ("hey cut it out")   #With this we can through our own errors.
    except ZeroDivisionError: 
        print("please enter a number higher than 0") 
        break


    