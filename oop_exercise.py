#create a supelist
# class SuperList():
#     pass
#allows us to access index, anyway a regular way allows us to use it.
#it will have special dunder method
#how to modify the length
#superlist will be a list, we instantiate,it is going to allow us to len, append(), access items

class SuperList(list):
    def __len__(self):
        return 1000

superlist1= SuperList()
print(len(superlist1))
superlist1.append(5)

#as we add list in superlist, it becomes parent class
print(superlist1[0])
#we extended the functionality of list
print(issubclass(SuperList,list))
print(issubclass(list,object))