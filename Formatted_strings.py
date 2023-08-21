# #Formatted string

# #the format method formats the specified value(s) and insert them inside the strings placeholder.
# #the placeholder is defined using curly brackets {}

# text1= "my name is {fname} , I live in {fcity}".format(fname="Adam", fcity="Mumbai")
# print(text1)

# text2 = "values less than 5 are {fval}".format(fval="<5")
# print(text2)


#ordered piece of characaters

#string indexes 

selfish = "me me me"   #this will be stored in a order
          #01234567

#we can access different part of string using indexes

print(selfish[0])

print(selfish[7])

selfish = "01234567" 

#[start:stop]

print(selfish[0:2])

#[start:stop:srepover]
print(selfish[0:8:2])

print(selfish[:5])

print(selfish[::1])

print(selfish[-1])

#to get the reverse of a string

print(selfish[::-1])
print(selfish[::-2])


#### immutability #####

# selfish[start:stop:stepover]  #this is known as slicing

#immutability - strings in python are immutable , that is we cannot change them.

selfish = 100
print(selfish)

selfish[0] = "8"
print(selfish)    #here we get an error 'int' object does not support item assigment

# we cannot change the string, only thing we can do it by redefining it.





