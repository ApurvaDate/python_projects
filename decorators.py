#to understand decorators we have to know about functions 
#functions are nothing but first clas citizens , they can be passed as variables, or as an argument

def hello():
    print("helllooooo")

#functions are similar as variables in python 

greet = hello  #greet is going to point to hello
del hello   #delete the function, thats in memory, 
# however because greet is another variable still pointing to this function , we are deleting hello, but greet is still pointing in that memory
#so hello deleted but because of greet , we have not deleted the hello funcion
print(greet())


def hello(func):
    func

def greet():
    print("still here!")

a = hello(greet)  #call the function hello with argument greet, hello function calls it for us

print(a)

#decorators are only possible because of these features, the ability of functions to act like variables, 
# @decorators supercharge our functions and add extra functionality to it.



##################### Higher order functions  (HOC) ######################

#it could be a function that accepts function like below

def greet(func):
    func

# or it could be a function that returns a function 
def greet2():
    def func():
        return 5
    return func

#a higher order function is a function that accepts a function as parameter , or it returns a function
#map is a higher order function



