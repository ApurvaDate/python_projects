# # Error Handling


# #an error that crashes or program is called an exception.
# #error handling allows us to run the code, even if there are multiple errors.


# ### syntax error ####
# def hoooohoo()  #this gives us syntax error as we forgot to write :
#     pass

# #### NameError ####

# def hoohoo():
#     return 1+ name   #name is not defined

# #### IndexError ####
# li = [1,2,3]
# print(li[5])  #we get an indexError 


# #### KeyError ####
# di = {"a":1,"b":2}
# print(di['c'])  #here we get a KeyError


# print(5/0)  #which gives us zerodivision error

# #there are many built in exception is python



#create a program that takes users input 

age = int(input("what is your age"))
print(age)  #if we give a string as an input we get an error

try:
    age = int(input("what is ypur age"))
    print(age)  #if we give a string as an input we get an error
except: 
    print("please enter a number") 
# #we are handling errors by wrapping our code in try and except 

#how can we keep running the above program, until user actually enters valid response?

while True:
    try:
        age = int(input("what is your age "))
        print(age)  #if we give a string as an input we get an error
        10/age  
    except: 
        print("please enter a number") 

    else:
        print("thank you")
        break  #to break out of the loop
#if we enter 0 as our age, it gives an error even when 0 is a number
#one is value error and other is zerodivision error

#we can mention which type of error we want to handle.

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

