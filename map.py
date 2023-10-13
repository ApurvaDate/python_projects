#useful functions for functional programming are : map(), filter(), zip(), reduce

# map(actions, data)

# # map(action, [1,2,3])
# def multiplyBy2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(list(map(multiplyBy2, [1,2,3])) )  #once we run it, we get map object 

#with map object we dont need to do creation of a list, appending the items
#map : give data & data gets acted upon this, 
# so instead of above code we need to write

def multiplyBy2(item):
    return item*2

print(list(map(multiplyBy2,[1,2,3])) ) #map is going to call the function 