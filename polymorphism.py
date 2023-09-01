#polymorphism - many forms

#methods belongs to objects, we use self keyword to act upon the object

#in polymorphism, object classes can share the same method name,but
#with polymorphism different object classes can share method names.
class User:
    def sign_in(self):
        print("Logged in")
    def attack():
        print("do nothing")

class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f"I am attacking with power of {self.power}")

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")

wizard1 = Wizard("Merlin",60)
print(wizard1.attack())

#wizard and archer have same method "attack" with their use is different, hence output is different

archer1 = Archer("Robin",30)

def player_attack(char):
    char.attack()
player_attack(wizard1)

player_attack(archer1)
#here we are calling the same function but as we pass different object we get different results, this is called polymorphism

for char in [wizard1, archer1]:
    print(char.attack())
#here we are getting two different outputs even after using the same method because of the different objects
#we are able to customize it based on our needs
#even if we define attack() in User class it is going to overwrite, where the attack is called.

#in case if want to have both user and wizard, how can we do that? we can use User.attack(self) on the Wizard class
#  then if we run we get the required attack output from both User and Wizard classes as defined.

#so polymorphism has ability to redefine the methods for the derived classes,
#and object that gets instantiated can be written in different ways based on polymorphism, able to modify classes based 
# on the needs without repeating ourselves



########### super ##################
#we learnt how to call a method from subclass of the parent class
# super() - refers to super class
# class User:
#     def __init__(self,email):
#         self.email = email
#     def sign_in(self):
#         print("Logged in")


# class Wizard(User):
#     def __init__(self,name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power
#     def attack(self):
#         User.attack(self)
#         print(f"I am attacking with power of {self.power}")
# wizard2 = Wizard("merlin",60,"merlin@gamil.com")
# print(wizard2.email)

#super refers to the super class, no need to self, we get answer we dont have to worry about passing self.




