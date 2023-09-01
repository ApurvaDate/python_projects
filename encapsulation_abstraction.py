#encapsulation means binding of data into one object which can be used further
#it is nothing but binding of data and functions into (attributes and methods)
#because of encapsulation we have all the functionality available.
#we pacakage the data into functions and attributes to use it more efficiently.

class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print('run')
    def speak(self):
        print(f"my name is {self.name}, and I am {self.age} years old")
player1 = PlayerCharacter("andrei",100)


player1.speak()   #so here we have access to speak but we are not focusing on how it is implemented which is abstraction.

#similar we see in a tuple if we use count() we are interested in the count but not how it is implemented.

#if we write
player1.name = '!!!'
player1.age = 'BOOOOO'

#here we see all the code written in class is changed to a string, which is bad as 
# the work we have done can overwriteen by someone else

