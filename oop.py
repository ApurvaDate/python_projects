#everything in python is an object

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

#<class 'NoneType'>
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

#everything is build by class keyword in python as given above.
#objects have methods and attributes which we can access by .
#this oop allows us to go beyond what python gives us.


#we will be able to create our own datatypes with different atributes and methods
#a way to define structure our code



######### what is OOP #################

#In python we can create our own datatype/ class

class BigObject:  #we have created a class here
    pass
obj1 = BigObject()  #here we are instanciating the class and create a new object
print(type(obj1))   #we get class '__main__.BigObject'>




#blueprint of what we want to create
#create different objects over and over again considering the blueprint as building block
#bluerprint is a class and class can be instantiated that is the action by creating instances.
#instanciated as class means created a new instance object


#Blueprint (class) will be stored in the memory.
#Go in BigObject code and run it while we define an instance.
