import re
#email could be anything it could be letters or numbers
#'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+

#$re = '/(^[a-z]*+@[a-z].[a-z]*)/m';
# $str = 'djssdmnscdsja@a.com';
pattern = re.compile(r'(^[a-z]*+@[a-z].[a-z]*)')
string = 'djssdmnscdsja@a.com'

a = pattern.search(string)
print(a)

#we get a ,atch for the above string

# <re.Match object; span=(0, 19), match='djssdmnscdsja@a.com'>


############ password validation #################
#8 char long
#contain any sort of letters, numbers, #$ special char
#has to and with a number

# $re = '/[a-zA-Z0-9#$%@]{8,}\d/m';
# $str = 'supersec$#8';

pattern = re.compile(r'[a-zA-Z0-9#$%@]{8,}\d')
string1 = 'supersec$#8'
b = pattern.search(string1)
print(b)


# password = 'supersec$#8'
# pattern2 = re.compile(r'[a-zA-Z0-9#$%@]{8,}\d')
# a = pattern
# check = pattern2.fullmatch(password)
# print(check)

