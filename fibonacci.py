def fib(number): #this number will be index, so if it is 20 it will give value of F20 = 6765
    #we can do it with a list, or generator
    #as with list we are going to run out of resources.
    a = 0 
    b = 1 #start of the numbers

    for i in range(number):
        yield a  #give a and pause the function
        temp = a #temporary variable
        a = b
        b = temp + b

for x in fib(21):
    print(x)

#the above is done by using range generator

#with fib2 we try the same using list

def fib2(number):
    a = 0
    b = 1
    result = []

    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result
print(fib2(21))

print(int(5))