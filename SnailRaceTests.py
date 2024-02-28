import unittest
from unittest.mock import patch
from parameterized import parameterized

from Snail import Snail
from main import *


class MyTestCase(unittest.TestCase):

    def test_snail_progression_increment_1(self):
        snail = Snail()
        snail.progression()
        self.assertEqual(1, snail.progress)

    @patch('builtins.input', side_effect=['', '', 'ValidName'])
    def test_name_snail(self, mock_input):
        # It shouldn't let you have names that 0 characters long.
        snail = Snail()
        snail.name_snail(1)
        self.assertEqual(snail.name, 'ValidName')

    @patch('builtins.input', side_effect=['-1', '11', '10'])  # Mocking user input
    def test_get_number_of_racing_snails(self, mock_input):
        # Test will run and input -1, 11, and 10 in the user input when asked how many players there will be
        # The function doesnt allow input less than 1 or greater than the MAX_NUM_SNAILS input, so
        # verifying that racing_snails = 10 means it went through the first 2 inputs first.
        racing_snails = get_number_of_racing_snails(10)
        self.assertEqual(racing_snails, 10)


if __name__ == '__main__':
    unittest.main()
