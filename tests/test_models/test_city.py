#!/usr/bin/python3

"""Unittest for the class City"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUpClass(self):
        """setup  a instantiation for test"""

        self.inst = City()

    @classmethod
    def tearDownClass(self):
        """Delete created instantiation after test"""

        del self.inst

    def test_state_id(self):
        """Test state_id is a string"""

        self.assertTrue(isinstance(self.inst.state_id, str))

    def test_state_name(self):
        """Test whether state name is a string"""

        self.assertTrue(isinstance(self.inst.name, str))
