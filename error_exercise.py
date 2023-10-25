while True:
    try:
        age = int(input("what is your age "))
        print(age)  #if we give a string as an input we get an error
        10/age  
    except ValueError: 
        print("please enter a number") 
    except ZeroDivisionError: 
        print("please enter a number higher than 0") 
    else:
        print("thank you")
        break  #to break out of the loop
    finally:
        print("ok, I am finally done!")

#there is one more piece 
#finally

#finally runs after everything has been executed successfully

while True:
    try:
        age = int(input("what is your age "))
        print(age)  #if we give a string as an input we get an error
        10/age  
    except ValueError: 
        print("please enter a number")
        continue 
    except ZeroDivisionError: 
        print("please enter a number higher than 0") 
        break
    else:
        print("thank you")
        break  #to break out of the loop  
     #if we remove the break statement here, we will be able to print "can you hear me? " otherwise it wont 
     # get printed as we are either continuing the program or breaking it based on the error we have got
    finally:
        print("ok, I am finally done!")
    print("can you hear me?")


    #in case of severe errors, we need to stop our programs, in that case we dont use the except block, or raise a value error.
    #with this we are able to throw our own error.

    