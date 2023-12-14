import unittest
import testing_exercise

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = testing_exercise.run_guess(answer,guess)
        self.assertTrue(result)
    
    def test_input_wrong_guess(self):
        result = testing_exercise.run_guess(0,5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = testing_exercise.run_guess(5,11)
        self.assertFalse(result)
    def test_input_string(self):
        result = testing_exercise.run_guess(5,'11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()