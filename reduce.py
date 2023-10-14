#advanced function
#reduce

#reduce is not a python built in function
from functools import reduce

#functools is a toolbox we can use for functional tools with the python installation
my_list = [1,2,3]

def multiplyBy2(item):
    return item*2

def  only_odd(item):
    return item % 2 !=0

def accumulator(acc,item):
    print(acc, item)
#it will default to 0 if we dont give anything
    return acc + item


print(reduce(accumulator,my_list, 0 ))  #for reduce we need the function and the data, here we give three arguments
print(my_list)

#reduce allows us to reduce something value from the iterable that we give.
# we apply my_list to accumulator through reduce
# accumulator is going to take my_list and the first thing in the first pass through is
# the acc will be 0, and item is going to be 1, and then we add it (0+1) ,
# in the second passthrough is going to be what we have returned which is equal to 1, 0+1 = 1
# 1+2 = 3 , so acc will be equal to 3 and what we pass through is going to be 3 as well.
# print(3+3)

# we accumulates all these values and return a single value which is 6

# we reduce our list in sort of a data that we manipulate using accumulator

print(reduce(accumulator,my_list, 10 )) #if we change initial value to 10 we get 16

#when we first pass my_list from reduce we will get the first item, which will be in the item(first parameter in accumulator)
#acc is the initial