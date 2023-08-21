#sets

#unordered unique collection of objects

my_set = {1,2,3,4,5}
print(my_set)

my_set.add(100)

my_set.add(2)  #this does not get added, as 2 was already present
print(my_set)

my_list = [1,2,3,4,5,5]
#return a list that has only unique items

my_unique_list = set(my_list)

print(my_unique_list)

#usernames, or email address and we dont want duplicate emails we can use sets

my_set = {1,2,3,4,5,6}
# print(my_set[0])  #this gives an error as it doesnt support index

#we have to use the value directly to check whether it is set or not
print(1 in my_set)
print(len(my_set))

#we can convert it to a list
print(list(my_set))

new_set = my_set.copy()
print(new_set)

print(my_set.clear())

print(my_set)


####### set methods ############

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

#difference()

print(my_set.difference(your_set)) 
#what is different between my_set and your_set when viewd from my_set is 1,2,3 
#it ignores duplicate values which are in both the sets

# #discard

# print(my_set.discard(5))  #to remove an element from the set
# print(my_set)

# #difference_update
# my_set.difference_update(your_set)
# print(my_set)   #4 , 5 are removed


#intersection (&)

print(my_set.intersection(your_set))  #common elements which are 4,5

#isdisjoint()

print(my_set.isdisjoint(your_set))  #we get False here as there are common elements present
#isdisjoint means there is no common value present then we get True

#union (|)

my_set1 = {4,5}
print(my_set.union(your_set))

#issubset()
print(my_set1.issubset(your_set))

#issuperset

print(your_set.issuperset(my_set1))  

