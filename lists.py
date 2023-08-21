#observed sequence of objects of any data type are called lists
#it can be considered as strings but having different objects

li = [1,2,3,4,5 ]

li2 = ['a','b','c']

li3 = [1,2,'a']

#all of the above are lists

#these are very important, they are a form of arrays. But there is difference in that.

#first data stucture - list

#way of organizing information in data into a folder or a box, so these data structures can be used afterwards for operations.
#container around your data, having move, read and write data

amazon_cart = ["notebooks","sunglasses"]

#we can access the amazon cart in different ways.
print(amazon_cart[0])

print(amazon_cart[1])


#List slicing

amazon_cart = [
    "notebooks",
    "toys",
    "sunglasses",
    "grapes"]
print(amazon_cart[0::2])

#lists are mutable

# instead of notebook we can write a new laptop

amazon_cart[0] = "Laptop"

print(amazon_cart)

print(amazon_cart[1:3])

new_cart = amazon_cart[1:3]

print(new_cart)

#if we say 
new_cart = amazon_cart

new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

#here we see that the amazon cart has also been changed, as we are saying the new cart is eqaul to the amazon cart,
#we are changing the amazon cart as well.
#hence if we want to copy the list we should use [:]

amazon_cart = [
    "notebooks",
    "toys",
    "sunglasses",
    "grapes"]
print(amazon_cart[0::2])

#lists are mutable

# instead of notebook we can write a new laptop
print("*****************")
amazon_cart[0] = "Laptop"

new_cart = amazon_cart[:]   #here we are creating a copy of the list

new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)


#################### Matrix #############################

#a matrix is a way to describe 2-D or multidimensional list

matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
print(matrix[0][1])  #2


################## List Methods ###########################

#we can calculate the length of a list

basket = [1,2,3,4,5,6]
# print(len(basket))

#to add something in the list

# new_list = basket.append(100)  
# print(new_list)  #we get None

#as append changes in place, it doesnt produce a new result
#it doesnt create new copy of the list

print(basket)


#insert
basket.insert(4,100)
print(basket)

#extend

# new_list = basket.extend([100,101])
#new_list is None
print(basket)  #this extends the list


#removing

basket.pop()
print(basket)

#if we specify something in pop the value is returned

#or we can use remove

basket.remove(4)
print(basket)

#clear removes everything from the list
basket.clear()
print(basket)  

################# List methods 2 ####################

basket = ["a","b","c","d","e"]
print(basket.index("d"))


#python keyword  which has a meaning

print( "d" in basket)
print("x" in basket)  #in keyword to check whether a given letter exists in the list

print(basket.count('d')) #to check how many times the value occurs in our list

################ List method 3 #######################


basket = ["a","b","c","d","e","f","a"]

#sort 
print(basket.sort())  #we get None here
basket.sort()
print(basket)  #we get sorted list
#we can use built-in function sorted 

basket = ["a","b","c","d","e","f","a"]
print(sorted(basket))  #it produces a new array

new_basket = basket.copy()
print(new_basket)

#reverse
basket.reverse()
print(basket)


############# common list patterns #################

#len()
#reverse()

print(basket[::-1])   #reverse based on list slicing which will create a list

#range
print(list(range(1,101)))

print(list(range(100)))

#.join

#this works on strings
sentence = '!'
new_sentence = sentence.join(['hi','my', 'name','is','JOJO'])
print(new_sentence)

#joins this list by ! 
#similarly we can write
sentence = ' '
new_sentence = sentence.join(['hi','my', 'name','is','JOJO'])
print(new_sentence)

#list unpacking

a,b,c = [1,2,3]

print(a,b,c)

a,b,c, *other = [1,2,3,4,5,6,7,8]
print(other)


#None is a special data type in python










