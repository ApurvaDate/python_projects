#__init__ 

class PlayerCharacter:
    membership = True
    def __init__(self,name= "anonymous",age=0):
        if (age>18):
            self.name = name
            self.age = age
    def shout(self):
        print(f"my name is {self.name}")

player1 = PlayerCharacter('Tom',20)
player2 = PlayerCharacter() #if we do not pass any parameter we get an error as default age is 0
#so we never going to instantiate the property.


print(player1.shout())
 