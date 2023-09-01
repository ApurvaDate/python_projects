def say_hello():
    print("Hellooo")

#in order to use a function we have to call it
say_hello()  #to take an action intepreter should know.

#functions are powrful
#we can reuse the functions over and over


########### parameters and arguments #########

# we can define parameters inside a function.
def say_hello(name,emoji):
    print(f"hellooo {name}{emoji}")

say_hello("adam",':)')

#parameters are given when we define the function.
#arguments are given when we call the function.

#these above we call it positional arguments or positional parameters.
#these arguments or parameters are required to be in a proper position.



#keyword arguments- allows us we dont need to worry about the position
say_hello(emoji=":/",name="adam")
#but mostly stick to positional arguments and not keyword agruments to avoid confusion for other developers.

###default parameters
#allow us to give what we want as default

def say_hello(name="Adam",emoji=";"):
    print(f"hellooo {name} {emoji}")
say_hello()

#here when we call the function we get deafult values in the print statement in case we forget to give the input


