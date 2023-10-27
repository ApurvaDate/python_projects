#to understand how things work under the hood of generators

#implementing for loop and range function

#for
def special_for(iterable):
    iterator = iter(iterable) #this function is going to allows us the next function
    while True:
        try:
            print(iterator)
            next(iterator) #going to output the item
            print(next(iterator))
        except StopIteration:
            break
special_for([1,2,3])  #we loop through some iterable objects using next

#this is how for loops work. they create an iterable and loop through it.

#range
class MyGen():  #this class will work like list
    current = 0 #class object attribute
    def __init__(self, first, last):
        self.first = first
        self.last = last

       #dunder
    def __iter__(self):
        return self 
    def __next__(self):
        #how next we want to work
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        #thats how next works, we increment the number
        raise StopIteration


gen = MyGen(0,100)

for i in gen:
    print(i)

#we are able to loop through generator and get values from 0 to 99

#we want init function have the option of first and last
#itearte through the object created
#and use next   





