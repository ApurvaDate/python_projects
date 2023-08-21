#Dictionaries

#dictionary has a key and a value

dictionary = {
    "a" :1,
    "b" : 2
}

print(dictionary)  #key value pair 

#key is string with the help of which we grab a value.
print(dictionary['a'])

dict1 = {
    "a" : [1,2,3],
    "b" : "Hello",
    "c" : True
}

print(dict1['a'][2])


##################### developer fundamentals #########################
#understanding data strctures

#when to use list & dictionary?
#- a dictionary is not sorted, a list is ordered
#- dictionaries can hold more information than list.

####################

#dictionary keys

#dictionary keys need to have a special property that they should be immutable, that is they cannot be changed.

# dict2 ={
#     123 :[1,2,3],
#     True : "hello",
#     [100] : True
# }

# print( dict2[123])

# print(dict2[True])

# print(dict2[100])  # this will give an error

#a key in a dictionary has to be unique.

############ dictionary methods ####################


# suppose we dont know the dictionary name and whether a certain
# key exists in that dictionary or not, then we use .get method

#.get method on object or dictionary

user = {
    'a': 1,
    'b': [1,2,3]
}

print(user.get('age'))   #it returns none as "age" key doesnt exists

print(user.get("age",55))  #grab a age from dictionary if it doesnt exists use 55


user2 = dict(name= "JohnJohn")  #use variable as key
print(user2)


#another dictionary method
print('a' in user)
print('size' in user) #similar to lists we can use keywords for dictionaries

print("a" in user.keys())


#items grab the entire item

print(user.items())

#clear()

# print(user.clear())


#copy
user2 = user.copy()
print(user2)

#pop

user.pop('a')
print(user)  #it removes the key and value

#update

user.update({"age":55})
print(user)
