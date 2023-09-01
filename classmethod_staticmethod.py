# #@classmethod and @staticmethod

# class PlayerCharacter:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def shout(self):
#         print(f"my name is {self.name}")
#     @classmethod
#     def adding_things(cls, num1, num2):
#         return num1 + num2
    
#     #lets see whether player1 has access to adding things
# player1 = PlayerCharacter("Tom",20)
# print(player1.adding_things(2,3))  
# #here we get an error
# # TypeError: PlayerCharacter.adding_things() takes 2 positional arguments but 3 were given
# #as similar to self classmethod has first parameter cls which stands for class which if we define, we get the answer.

# #we actully use it without instantiating , that means even if we dont define player1 we can use it
# print(PlayerCharacter.adding_things(2,5)) #we get the answer.

# #classmethods are not used often.
#     @staticmethod  #it is similar to classmethod but we do not have access to cls
#     def adding_things( num1, num2):
#         return num1 + num2
# #we use static method , when we do not care about classmethod