"""testing

Testing is very important to protecting the integrity of software.
Think of how you write your code with a linter and proper indentation, then test after!
tests should be really descriptive and easy to read
"""

import unittest
from main import do_stuff


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    # we are accounting for a value error to make sure it will be a value error if they don't enter a number
    def test_do_stuff2(self):
        test_param = 'blahblh'
        result = do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        # below is the result of the function when passing the above param
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number higher than 0')

    def test_do_stuff4(self):
        test_param = ''
        # below is the result of the function when passing the above param
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number higher than 0')

    def test_do_stuff5(self):
        test_param = 0
        # below is the result of the function when passing the above param
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number higher than 0')


# run this file if it is the main - the main file being run
if __name__ == "__main__":
    unittest.main()
