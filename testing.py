#Unit testing in python

def do_stuff(number=0):  # we can give default parameter as =0
    try:
        if number:
            return int(number) + 5
        else:
            return '_please enter a number'
    except ValueError as err:
        return err

#lets say this code built our app


#the way unit tests works