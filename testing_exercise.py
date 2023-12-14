#we know the random guessing number game
import random
import unittest


def run_guess(guess,answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a genius!')
            return True
    else:
        print('Hey I said 1~10')
        return False


#how to test this code, we dont really have a function?
#to break up our code in small bits of functions

#so here now we test the run_test
if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError as err:
            print('please enter a number ')
            continue

