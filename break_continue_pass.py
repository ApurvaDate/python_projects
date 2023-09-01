#break, continue, pass

#why use continue, break, pass
#when we use a break statement we break the loop after certain condition
#when we use continue we again go back to the loop, until the loop ends.
#pass is not that useful, it just passes to the next line it can be placeholder for a loop.

my_list = [1,2,3]
for item in my_list:
    #thinking about it
    pass

i=0
while i<len(my_list):
    print(my_list[i])
    i+=1
    pass
