# I/O means input and output from the outside world
#we use I /O through reading files

#reading and writing files in very important

#python has a built in function open
my_file = open(r"C:\Users\Apurv\projects\python\tuple.py")

print(my_file.read()) #read this file

#we can only read the file once, and it returns a file object

print(my_file.seek(0))


#we have to manuaaly close the file , so that we can use it somewhere else.

my_file.close()


#this is correct way to read a file
with open(r"C:\Users\Apurv\projects\Underwriting\text.txt") as my_file:  #here we dont have to worry about closing the file
    print(my_file.readlines())

#open has a default parameter mode = 'r' which stands for read
with open(r"C:\Users\Apurv\projects\Underwriting\text.txt",mode='r+') as my_file:  #here we use r+ then we can read and write
    text = my_file.write(" Hey, its me! writing a new code to understand")
    print(text)  #we get 46
#when we write something to a file, it resets,and we might overwrite the file if it already has something

#to not change whatever is already present in the file and new text we use append
#the append mode is "a"
with open(r"C:\Users\Apurv\projects\Underwriting\text.txt",mode='a') as my_file:  #here we use r+ then we can read and write
    text = my_file.write(" Hey, its me! writing a new code to understand")
    print(text)
#we can use "w" to write it.

    

