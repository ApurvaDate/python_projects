#print the username , the password in ***** and how many letters it has.

username = input("Enter the username : ")
password = input("Enter your password: ")

password_length = len(password)

hidden_password = "*"*password_length

print(f"{username} your password {hidden_password} is {password_length} letters long")

