#In functional programming we separate the data and functions
#instead of combining methods & attributes we separate them up.

# two rules for a function

#1) given the same input it will always return the same output
#2) A function should not produce any side effect
#side effects: function does that affects the outside world.

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

#anything outside the function is outside world, so anything outside the function written affects
#when we have pure function bugs are less.

#it is not possible to have pure functions everywhere.


