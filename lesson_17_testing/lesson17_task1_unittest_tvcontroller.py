# Lesson 17
# Task 1. Test
# Pick your solution to one of the exercises in this module. Design tests
# for this solution and write tests using unittest library.

import unittest
from .lesson17_task1_tvcontroller_for_tests import TVController

class TestTVController(unittest.TestCase):
    def setUp(self):
        self.controller = TVController(["BBC", "Discovery", "TV1000"])

    def test_switching_channels(self):
        self.assertEqual(self.controller.first_channel(), "BBC")
        self.assertEqual(self.controller.last_channel(), "TV1000")
        self.assertEqual(self.controller.turn_channel(1), "BBC")
        self.assertEqual(self.controller.next_channel(), "Discovery")
        self.assertEqual(self.controller.previous_channel(), "BBC")
        self.assertEqual(self.controller.current_channel(), "BBC")

    def test_checking_channels(self):
        self.assertEqual(self.controller.is_exist(4), "No")
        self.assertEqual(self.controller.is_exist("BBC"), "Yes")


if __name__ == '__main__':
    unittest.main()