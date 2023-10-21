def hello ():  #simple function
    print("helloooooooooo")


def my_decorator(func):
    def wrap_func():
        print("*****************")
        func()
        print("*****************")
    return wrap_func

@my_decorator
def hello():
    print("helloooooo")
hello()

#what happens when a decorator takes a parameter?
# @my_decorator
# def hello(greeting):
#     print(greeting)

# hello()  #this gives an error- hello() missing 1 required positional argument: 'greeting' 

# so if we add x as a parameter in func() for above wrapper function

def my_decorator(func):
    def wrap_func(x):
        print("*****************")
        func(x)
        print("*****************")
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)

hello("hiiiiiiiiii")

hello("hiiiiiii")  # now we get the greeting

#the function hello gets passed then we receive as argument the x,  here we are saying
#a = my_decorator(hello)
# so when we use wrap function a , we give it an argument, which accepts the parameter and runs the function hello.

#what if greeting also had an emoji? for that we again to create anothe parameter, also while calling the function pass two parameters like below
def my_decorator(func):
    def wrap_func(x, y):
        print("*****************")
        func(x, y)
        print("*****************")
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

hello("hiiiiiiiiii", ":)")

#if we have keyword arguments or another parameters, it becomes hectic. There is a pattern over here

#we write * args which takes all positional arguments and then **kwargs which takes all the keyword arguments,
#  and we call the function by *args to unpack positional arguments and **kwargs to unpack keyword arguments

#decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrap_func

#so this is just a pattern which we can copy and paste.

#with the help of this decorator pattern we can decorate our functions. which is very powerful concept.


################################ why do we need decorators ###############################

#some of the practical applications of decorators
#to build our own decorator from scratch

from time import time  #check for module section
def performance(fn):
    def wrap_func(*args, **kwargs):
        t1 = time() #we are running this time function #this time will check what time is now  
        result = fn(*args, **kwargs) #run the function 
        t2 = time() #this function will again check the time 
        #so difference between these two times, is how long result part is.
        print(f"it took {t2-t1} s")
        return  result
    return wrap_func


@performance
def long_time():
    for i in range(100000000):
        i*5
long_time()


#we want to check how well it performs'
#so now we have this performance decorator which we can use, to measure performance of my function 
#wwe can also optimize functions

#this performance decorator depends on your machine, 
