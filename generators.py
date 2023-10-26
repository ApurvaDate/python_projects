#generators allows us to generate a sequence of values over time.

# range()  #this is a generator

# special type of thing in python , it can pause and resume functions
list(range(100))   #this creates giant list in memory

range(100)  #this creates one by one.

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)

print(my_list)  #this list is pointing to a location in memory., which is taking up space

#range is a generator, it is not created in memory.
#it is hectic when the list is too big.


