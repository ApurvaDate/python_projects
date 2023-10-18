#Decorators

#decorator supercharges our function.

#function that wraps a function & enhances it or changes it
#create our own decorator
def hello ():  #simple function
    print("helloooooooooo")

# def my_decorator(func):
#     def wrap_func(): #wrap a function
#         func()       # returns a function
#     return wrap_func #return wrap function, we are returning the function so that it can be used further. we are not calling it.

#now after defining simple function, we can use my_decorator function as decorator

#@ - this is going to be a decorator

# @my_decorator
#this decorator can be used on top on defining our functions

# @my_decorator
# def hello():
#     print("helloooooo")
# hello()

#with the decorator hasnt changed anything, but it allows us to add extra functinality.
#so with the help of decorator we can enhance it.

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


#output

# *****************
# helloooooo
# *****************

@my_decorator
def bye():
    print("see ya later")
bye()

#it all does 
a = hello #and wraping this hello and calling it with my_decorator , a = my_decorator(hello) a()

#wraping a hello function with decorator and assigning it to a variable

# hello2 = my_decorator(hello) 
# hello2()



