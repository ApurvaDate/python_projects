#error handling

#lets create our own function

def sum (num1, num2):
    try: 
        return num1 + num2 
    except:
        print("something is wrong")

print(sum('1','2')) #we get 12 here 

#its imp to know what went wrong
# always catch the errors based on specific exceptions

def sum (num1, num2):
    try: 
        return num1 + num2 
    except TypeError as e:
        print(f"please enter numbers {e}")  #what we get here is an error object.

print(sum('1',2))

#common error handling is ,
# except type error as er:
        # print(er)

#we can also combine two erros togther, and handle them in same way
def sum (num1, num2):
    try: 
        return num1 / num2 
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(sum(1,0))     