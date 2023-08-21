#len() which is for length

print(len("hellooooooo"))   #11  #its starts from 1

greet = "hellooooo"

print(greet[:])

print(greet[0:len(greet)])

#Built-in function has a syntax of word that is highlighted to perform an action.
#methods are similar to function but they are owned by something. For python string methods we get automatic tools.

quote = "to be or not to be"

print(quote.upper())

print(quote.capitalize())

print(quote.lower())

print(quote.find("be"))   #it starts at index 3

print(quote.replace("be","not "))
quote2= quote.replace("be","not ")

print(quote)

#strings are immutable, we cannot change them we either create or destory them

#hence any operation done on it must be saved.

print(quote2)  #we have created a new string


