
import unittest
import testing #testing.py file
############## writing unit tests #################
# assertIsInstance(a,b)

#create a class
class TestMain(unittest.TestCase): #we are inheriting what unit test test cases gives, now we have that functionality with us in TestMain
    def test_do_stuff(self):
        test_param = 10
        result = testing.do_stuff(test_param)
        self.assertEqual(result,15) # these two params must be same, check testing.py to understand do_stuff function
        #this is just one test
    def test_do_stuff4(self):
        test_param = 'fbfdjd'
        result = testing.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
    #everything is working good till now

    def test_do_stuff5(self):
        test_param = None
        result = testing.do_stuff(test_param)
        self.assertEqual(result,'_please enter a number')
         #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType' how to fix thsi error?
         #if we check for number and change do_stuff function, and run these test again we get4
         #----------------------------------------------------------------------
         # Ran 3 tests in 0.001s
         # OK
    
    def test_do_stuff6(self):
        test_param = ''
        result = testing.do_stuff(test_param)
        self.assertEqual(result,'_please enter a number')
#### all the four tests are running fine



#tests allows us to check if we have made any mistakes
#This is how we write unit tests

#we can use python -m unittest to run the test or 
#python -m unittest -v
#we can also add comments to our tests.

#setup allows us to run a piece of code

class TestMain(unittest.TestCase):
     #we are inheriting what unit test test cases gives, now we have that functionality with us in TestMain
    def setUp(self):
        print('about to test a function')
    def test_do_stuff(self):
        test_param = 10
        result = testing.do_stuff(test_param)
        self.assertEqual(result,15) # these two params must be same, check testing.py to understand do_stuff function
        #this is just one test
    def test_do_stuff4(self):
        test_param = 'fbfdjd'
        result = testing.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
    #everything is working good till now

    def test_do_stuff5(self):
        test_param = None
        result = testing.do_stuff(test_param)
        self.assertEqual(result,'_please enter a number')
    
    def tearDown(self):
        print('clean up')
        
if __name__ == '__main__':
    unittest.main()