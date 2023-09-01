is_magician = True
is_expert = False

#check if magician and expert : "You are a master magician"
#check if magician but not expert: "At least you are getting there"
#check if you are not a magician : "You need magic powers"

#create conditional logic

if is_expert and is_magician:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("at least you are getting there")
elif not is_magician:
    print("You need magic powers")




############# is vs == ################
print(True == 1)  #True
print('' == 1)    # False
print([] == 1)    # False
print(10 == 10.0) # True
print([] == [])   #True



#is keyword

print(True is 1)  #False
print('' is 1)    # False
print([] is 1)    # False
print(10 is 10.0) # False
print([] is [])   #False   #these are two different lists and are in different location

#equals check for the equality in value
#is checks whether location in memory this value is stored is same
#but "is" works well for numbers and strings as these are data types

a = [1,2,3]
b= [1,2,3]

print(a is b)  #as they are stored in different locations

#is and == are not same
#equality checks the value.


