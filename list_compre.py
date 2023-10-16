#there is a way to create list or sets or dictionary in python , instead of looping or appending to bunch of items to lists

my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

#with list comprehension we can do this easily, short form

# my_list = [param for param in iterable]

my_list = [char for char in "hello"]  #this is a list comprehension
print(my_list)

my_list2 = [num for num in range(0,100)]  #num ranging from 0 to 99
print(my_list2)

#multiply by 2, we can expand this

my_list3 = [num*2 for num in range(0,100)]
print(my_list3)

#to keep only even numbers

my_list4 = [num for num in range(0,100) if num%2 == 0]   #expresssion - loop - condition  
print(my_list4)