#tuples are like list but we can not modify them they are immutable.
my_tuple = (1,2,3,4,5)
# my_tuple[1] = "z"  #this gives an error as they immutable we can not modify them.
print(my_tuple) 

print(5 in my_tuple)
#if we dont need to change the list, we can use tuple.
#Tuples are less flexible, they are faster than the list 
#we can use geographic locations in tuple which dont change easily.

new_tuple = my_tuple[1:2]
print(new_tuple)  #we get (2,) which is still a tuple
x = my_tuple[0]
y = my_tuple[1]

x,y,z, *other = (1,2,3,4,5)

new_tuple = my_tuple[1:2]
print(x)
print(y)
print(z)
print(other)


#tuple methods

#a tuple has only two methods
#count & index
my_tuple = (1,2,3,4,5)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))