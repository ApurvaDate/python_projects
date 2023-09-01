#game and users
#users
    # -wizards
    # -Archers
    # -ogres
#e.g 1
class User:
    def sign_in(self):
        print("logged in")
    #if we dont have any attributes or variables to assign we dont need any init method
class Wizard(User):
    pass
class Archer(User):
    pass
#all these wizards and archers are users
#how we can give access to wizard and archer to sign in? for that we use inheritance
#we just pass the parent class name in the wizard class 

#to instantiate a class
wizard1 = Wizard()
print(wizard1.sign_in())  #we get "logged in"

#e.g 2 
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
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f"attacking with arrows : arrows left - {self.num_arrows}")
    
wizard1 = Wizard("Merlin",50)
archer1 = Archer("Robin",100)
#so the wizard and archer will have sign in and attack unique to their individual classes as defined above and different properties
wizard1.attack() #attacking with power of 50
archer1.attack()
#and both of these have sign_in function with them as well inherited from User class.
#here User is parent class and Wizard and Archer are child classes/ subclasses/ derived classes


#inheritance2

#python gives us a tool to check whether something is an instance of a class
#isinstance - built in function in python
# isinstance(instance,class)
wizard1 = Wizard("Merlin",60)
print(isinstance(wizard1,Wizard))  #we get true as wizard1 is an instance of wizard
print(isinstance(wizard1,User))  #we get True as Wizard is a subclass of User

#we also can use other properties of base class defined in python.
