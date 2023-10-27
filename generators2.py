# # def make_list(num):
# #     result = []
# #     for i in range(num):
# #         result.append(i*2)
# #     return result

# # my_list = make_list(100)

# # print(my_list)


# #a list is an iterable, is any object in python, which we can able to loop though.
# #generators are iterable, everything that is generator is always iterable, but an iterable is not always generator.

# # generator is subset of iterable

# #general way to create generator

# def generator_function():#they are functions
#     for i in range(1000):
#         #instead of returning we are going to use yield
#         yield i   #yield pauses the function, and comes back to it when next is called.


# # for item in generator_function():
# #     print(item)
    

# def generator_function(num):#they are functions
#     for i in range(num):
#         return i*2
# g = generator_function(100)
# # print(g)  # we just get a value
# next(g)
# # print(next(g))   # getting an error here. check again 
# #     next(g)
# # TypeError: 'int' object is not an iterator


#but by using yield we turn this into a generator function.
#yield pauses the function, the first item in range 100 was 0, then 1*2 = 2, 2*2 = 4 and so on.

#it keeps the most recent data in memory.

#next will be called till the range expires, when we exceed we get stop iteration error.




############ generators performance #################


#consider the example of decorator performance, we have two functions long_time() and long_time2() creates a list, created in memory

from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i  in range(10000000):
        i*5

@performance
def long_time2():
    print("2")
    for i in list(range(10000000)):
        i*5
#range is generator, one by one , removes odd numbers from the memory.


long_time()
long_time2()

#output
# 1
# took 0.3297131061553955 s
# 2
# took 0.5004856586456299 s
#so long_time() is faster than long_time2()

#geneartors are useful when calculating large sets of data, we dont store much
#a lot of libraries in python use generator than list as they are faster

# steps to use generator
# create generator function
# loop over some Value
# yield the result