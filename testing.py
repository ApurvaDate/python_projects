#Unit testing in python

def do_stuff(number):
    try:
        return int(number) + 5
    except ValueError as err:
        return err

#lets say this code built our app


#the way unit tests works