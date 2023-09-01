class PlayerCharacter:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def run(self):
        print('run')
    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")
player1 = PlayerCharacter("andrei",100)


player1.speak() 

#using _name or _age means these are private variables which should not be touched.
#hence _variables should not be modified.
#if we want to keep a method or attribute private we should use _ before it.

#__init__ is a dunder method, we never write dunder method of our own.