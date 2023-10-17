some_list = ['a','b','c','d','b','m','n','n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates) #we get ['b','n']


#create a list comprehension for above example

duplicates = set([value for value in some_list if some_list.count(value) > 1])
print(duplicates)  #we get ['b','n']