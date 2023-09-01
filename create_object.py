#gaming company

#wizard game

#player

class PlayerCharacter: #must be singular
    #class object attribute
    membership = True
    def __init__(self, name, age):
        self.name = name   #attributes these objects have which are not methods but to have access
        self.age = age     
    
    def run(self):
        print(run) #each player can run
        return done

player1 = PlayerCharacter("adam",44)
print(player1) #if we run it we get an error that __init__() missing 1 required positional argument 'name' if we dont give name

#__init__ is a dunder method or magic method
#whenever we instantiate- calling the class to create an object it automatically runs whatever written in init code block.
#whatever written after self is a parameter.

#we get an object with it memory location
#this is where the PlayerCharacter - player1 is located

print(player1.name) #we get adam
#(self,name) is self refers to the created class
#self.name = refer to parameter name which we give.
#the default parameter is self when we define a method
player2 = PlayerCharacter("James",26)
print(player2.name)

print(player1.age)
print(player2.age)
#self refers to . , to have a reference to something that has not been created yet.
#so when player1 is created , when we instantiate it has name attribute.
#so we can create different players with different attributes.
#each object has different memory location.


# if we use help(player1) we get the blueprint of the object
help(player1)

