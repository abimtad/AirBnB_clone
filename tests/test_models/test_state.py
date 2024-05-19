#!/usr/bin/python3

"""Unittest for state class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test case for State class"""

    def test_state_name(self):
        """Test state name is public string"""

        self.assertTrue(isinstance(State().name, str))
