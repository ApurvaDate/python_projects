#create a lambda expression that will square a list

#square
my_list = [5,4,3]
new_list = list(map(lambda x : x**2, my_list))
print(new_list)


#List sorting
a = [(0,2),(4,3),(9,9),(10,-1)]
#sort this based on the second value
# print(a.sort())
# print(a)
print(a.sort(key= lambda x : x[1]))  #we are able to sort by second item
print(a)