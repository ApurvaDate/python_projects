# to build a counter which will count items in our list
#list
my_list = [1,2,3,4,5,6,7,8,9,10]
#iterate over list and print sum up to the list
counter = 0  #we needed somthing outside the loop that doesnt change
for item in my_list:
    counter = counter+item
print(counter)



################ range ##################

for number in range(0,100):
    print(number)
for number in range(0,10,2):
    print(number)
for number in range(10,0,-1):  #which will give numbers in descending order
    print(number)
    
for _ in range(2):
    print(list(range(10)))

############### enumerate #################

for i,char in enumerate("Hellooo"):
    print(i,char) 
#we get hellooo iterated over we get the index of each item and the item

for i, char in enumerate([1,2,3,4]):
    print(i,char)
for i, char in enumerate((1,2,3,4)):
    print(i,char)


#create a script that enumerate range 100, find the index of number 50 is.
#only print index value of 50

for i,char in enumerate(list(range(100))):
    print(i,char)
    if char ==50:
        print('index of 50 is ',i)

