#multiple inheritance
class User:
    def sign_in(self):
        print("logged in")
class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} arrows remaining")

    def run(self):
        print("ran really fast")
        
#here we define a new class
# we want HybridBorg to have all the methods which Wizard and Archer has
class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,arrows):
        Archer.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)
#we can give many parameters as we want as multiple inheritances

hb1= HybridBorg('borgie',80,100)  #instantiated

print(hb1.attack())
print(hb1.run())
# print(hb1.check_arrows())  #we get an error as we inherited first from Wizard class which does not have any check_arrows method
#this is tricky multiple inheritances as we have to know how classes are implemented
#to solve it we write
# class HybridBorg(Wizard,Archer):
#     def __init__(self,name,power,arrows):
#         Archer.__init__(self,name,arrows) #we also using Archer
#         Wizard.__init__(self,name,power) #to use power we have to define the same for Wizard class as well
hb1= HybridBorg('borgie',80,100)  #instantiated
print(hb1.attack())
print(hb1.run())
print(hb1.check_arrows()) 
print(hb1.sign_in()) 
#with multiple inheritances it becomes complex