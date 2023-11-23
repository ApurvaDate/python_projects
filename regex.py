#There is regular expression module
import re
string = 'search inside of this  this text please! And'

print('search' in string) #we get true here

#regular expression are powerful

print(re.search('this',string)) # we get a match object, <re.Match object; span=(17, 21), match='this'>
a = re.search('this',string)
#with match object we can check what we have
print(a.span())
print(a.start())
print(a.end())
print(a.group())  #piece of the string

#we can create a pattern that we want to check for, the compile will help to get the pattern

pattern = re.compile('this')
a = pattern.search(string)
b=pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)  #this has to be the exact string and not a part of it

d= pattern.match(string)
print(d)


#we can use regex101.com and from code generator we can copy and use it in compile above

# '/([a-zA-Z]).(\W)/m'

pattern = re.compile(r'/([a-zA-Z]).(\W)/m')
a = pattern.search(string)
b=pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)  #this has to be the exact string and not a part of it

d= pattern.match(string)
print(d)