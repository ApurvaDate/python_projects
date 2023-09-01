class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print(f'my name is {self.name}')
player1 = PlayerCharacter('cindy',44)
player2 = PlayerCharacter('Tom',21)
player2.attack = 50

print(player1.shout())
print(player1.run())

#class object attributes like membership are not dynamic. Which are not same deynamic as self.name attributes.
# # class object attributes are static
# #all methods defined get "self" as first parameter so that we can get & use it anywhere.
# if we write
    
#     def shout(self):
#         print(f'my name is {PlayerCharacter.name}')
#     #we get an error here as Playercharacter is not a class object attribute.
# #class object attributes does not change across different instances.
