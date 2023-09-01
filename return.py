def sum(num1,num2):
    return num1 + num2 

# print(sum(4,5) ) #here we get None
total = sum(10,5)
print(sum(10,total))



#they always have to return something, if there is no return then it gives None

#return is exit of the function
#we can return something like None or value
#we can have a function which returns nothing, but modifies something

#a function either modifies the program or returns something.

#a function should do one thing really well
#a function should return something.


def sum(num1,num2):
    def another_func(num1,num2):
        return num1 + num2
#here we are defining a function but calling a function

def sum(num1,num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func(num1, num2)
total = sum(10,20)
print(total)

#function must be easy to understand
