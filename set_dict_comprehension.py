#set comprehension, dictionary comprehension

#set
my_list = {char for char in "hello"}  #change the notation from list to set [] to {}
print(my_list)  #here we get a set  {'l', 'e', 'o', 'h'}

my_list2 = {num for num in range (0,100)}
print(my_list2)

my_list3 = {num**2 for num in range(0,100)}
print(my_list3)

my_list4  = {num**2 for num in range(0,100) if num%2 == 0}
print(my_list4)

#set allows items which are not duplicate, only unique items.

#dictionary

# my_dict = {key:value**2} #multiply the value by 2
#we create a key value pair and the value gets acted upon.
simple_dict = {"a": 1, "b": 2}
my_dict = {key: value**2 for key, value in simple_dict.items() if value%2 ==0} #only if we write for even value we add if statement
#to create a dictionary we need both a key and a value, for that we need to pass an iterable, for that we pass simple_dict
print(my_dict) 

### what we want to do with data - k,v , do the power of 2 v**2 - extract the key , values by dict.items() and then value power 2
#e.g.
my_dict = {num: num*2 for num in [1,2,3]}
print(my_dict)


