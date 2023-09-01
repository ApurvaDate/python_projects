#loops allows us to run a code over and over again

########### for loop #############

for item in "zero to mastery":  #string
    print(item)
#a variable is created for item for zero to mastery
#iterable is something which gets looped over.

for item in [1,2,3,4,5]:   #list
    print(item)

for item in {1,2,3,4,5}: #set
    print(item)

for item in (1,2,3,4,5): #tuple
    print(item)
#for loop allows us to iterate over anything that has collection of items

#we can also nest things in python
#nested loops

for item in [1,2,3,4,5]:
    for x in ['a','b','c']:
        print(item,x)


#iterable - it is an object or a collection that can be iterated over.
#it can be  list, dictionary, tuple, set, string
#iterate -> one by one check each item in the collection.

#to iterate over a dictionary

user ={
    "name":"Golen",
    "age": 30,
    "can_swim" : False
}

for item in user:
    print(item)
    #here we get the keys of dictionary

for item in user.items():
    print(item) #we get key value pair in tuple

for item in user.values():
    print(item) #here we get values

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key,value)     #we can separate the items in a dictionary in key and value and print them