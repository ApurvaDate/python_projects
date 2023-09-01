# while condtion:
#     #do something


# while 0 <50:
#     print("yes")

# i = 0
# while i<50:
#     print(i)   # this will create an infinite loop

#we can use break to stop the program
i = 0
while i<50:
    print(i) 
    break  # this will create an infinite loop

i=0
while i<50:
    print(i)
    i+=1

while i<50:
    print(i)
    i+=1
else:
    print("Done with all the work")
#if we add a break statement, the else will does not print
#else will only work if there is no break


#when to use for loop and when to use while loop?

my_list = [1,2,3]
for item in my_list:
    print(item)

i=0
while i < len(my_list):
    print(my_list[i])
    i+=1

#both gives the same result.

#while loops are very flexible, but for loops are simpler.
#(for iterating over iterable objects, for loops are best)

while True:
    response = input("Say something : ")
    if response =="bye":
        break

#this will create an infinite loop,
#but after we get by as an input, we break the statement.