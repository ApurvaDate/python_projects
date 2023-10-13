#filter

def check_odd(item):
    return item%2 != 0 #odd

#filter will get a boolean value

print(list(filter(check_odd,[1,2,3])))