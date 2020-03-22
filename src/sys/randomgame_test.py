import unittest
from randomgame import run_guess


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = run_guess(answer, guess)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = run_guess(5, 0)
        self.assertFalse(result)

    def test_large_num(self):
        result = run_guess(5, 11)
        self.assertFalse(result)

    def test_string_input(self):
        result = run_guess(5, "yo")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
