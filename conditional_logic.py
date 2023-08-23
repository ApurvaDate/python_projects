is_old = True
is_licenced = True

if is_old:
    print("You are old enough to drive")
elif is_licenced:
    print("you can drive now")
else:
    print("You are not of age")
print("okokok")

#else will only run if condition is not satisfied.

if is_old & is_licenced:
    print("you are old enough to drive and you have licence")
else:
    print("you are not of age!")
print("okok")



################# truthy and Falsy ####################

# is_old = "hello"
# is_licenced = 5

# while using if these "hello" & 5 gets converted to boolean
#if we apply bool() on both then we get True value which we call as truthy
#if we pass an empty string for is_old and 0 for is_licenced and their boolean value , those are Falsy

############ Ternary Operator /conditional expressions ##################

#condition_if_true if condition else condition_if_false

is_friend = True
can_message = "message allowed " if is_friend else "not allowed to message"

print(can_message)


############### short circuiting ####################

is_friend =True
is_user = True
print(is_friend and is_user)  #we get True here

#short circuiting is something where we can use "or" 
if is_friend or is_user:
    print("best friends forever")

#or - either of the condition is True
#and - both the conditions are True



