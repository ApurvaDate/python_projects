#lambda expressions
#lambda are one time anonymous functions, 
#lambda expressions are used only for functions which are used only once
#we dont need to have name for them, we dont need to store them as we are using them only once.
from functools import reduce
# lambda parameter : function (parameter) / manipulation(parameter) / action we wanna take one a parameter

def multiplyBy2(item):
    return item*2

my_list = [1,2,3]

print(list(map(multiplyBy2, my_list)))

#we can write the above using lambda 
print(list(map(lambda item : item*2 , my_list)))  #take item from my_list and multiply it by 2 
print(my_list)

# lambda parameter : action

print(list(filter(lambda item : item %2 !=0, my_list)))  #for odd_only function, here we can filter as well

print(reduce(lambda acc, item: acc+ item , my_list))  #for reduce function we can write lambda function 

