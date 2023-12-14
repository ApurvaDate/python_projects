import unittest
import testing #testing.py file
#we want to import the file which we want to test

#create a class
class TestMain(unittest.TestCase): #we are inheriting what unit test test cases gives, now we have that functionality with us in TestMain
    def test_do_stuff(self):
        test_param = 10
        result = testing.do_stuff(test_param)
        self.assertEqual(result,15) # these two params must be same, check testing.py to understand do_stuff function
        #this is just one test
    def test_do_stuff2(self):
        test_param = 'shbfdhgf'
        result = testing.do_stuff(test_param)
        self.assertEqual(result,ValueError) # these two params must be same, check testing.py to understand do_stuff function
        #here we failed, and we get a TypeError #TypeError: can only concatenate str (not "int") to str

#in this case actually the test file fails.
#because we are returning an error, its actually an instance of the ValueError

#we have write self.assertEqual(result,ValueError) as self.assertEqual(isinstance (result,ValueError)), 
# but the problem is assertequal requires two parameters
#besides assertEqual we have other methods, for asserting and testing the code
    def test_do_stuff3(self):
        test_param = 'dgdks'
        result = testing.do_stuff(test_param)
        self.assertTrue(isinstance(result,ValueError))
#we are running the test file
#we are trying to improve our function, by simply breaking it

    



unittest.main()
#when we run this we get

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK





