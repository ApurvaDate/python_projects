print(str(100))
print(type(str(100)))

print(type(int(str(100))))

a =str(100)
b = int(a)
c = type(b)

print(c)

#this is what type conversion is.

#######################Escape Sequence############################

# weather = "It's "kind of" sunny"   #how to solve this?
#we can use escape sequence here.
weather = "It\"s \"kind of\" sunny"    #whatever comes after \ is a string.

print(weather)

print("\t It\"s \"kind of\" sunny")    #\ t to add tab in the given string at the start


print("\t It\"s \"kind of\" sunny\n hope you have a new day!" )    #\ t to add tab in the given string at the start & \n for new college

