#what are instance has as methods using dir()
#__ are spcial methods
#dunder methods allows us to use python specific function on objects created through our class.

class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
action_figure = Toy("Red",0)
print(action_figure.__str__)   #this is same as  print(str(action_figure))
# __ are special methods allows us to use actions methods

# lets modify str
class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict ={
            "name":"yoyo",
            "pet_name":"yo"
        }
    def __str__(self):
        return f"{self.color}"
    #we can change meaning of length
    def __len__(self):
        return 5
    # def __del__(self):
    #     print("deleted")
    def __call__(self):
        print("Yes???")  
    def __getitem__(self,i):
        return self.my_dict['name'] 
        
action_figure = Toy("Red",0)
print(action_figure.__str__) 
print(str(action_figure))  #mostly do not modify dunder methods
print(len(action_figure))
# del action_figure  #we get deleted 
print(action_figure())
print(action_figure["name"]) #we get yoyo

#we can customize the classes



