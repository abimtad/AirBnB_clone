#!/usr/bin/python3

"""Unittest for place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    @classmethod
    def setUpClass(self):
        """Setup instantiation for test cases"""

        self.inst = Place()

    @classmethod
    def tearDownClass(self):
        """Delete inst after tests"""

        del self.inst

    def test_string_values(self):
        """Test string type attribute"""

        self.assertTrue(isinstance(self.inst.name, str))
        self.assertTrue(isinstance(self.inst.city_id, str))
        self.assertTrue(isinstance(self.inst.description, str))
        self.assertTrue(isinstance(self.inst.user_id, str))

    def test_number_values(self):
        """Test numeric attribute"""

        self.assertTrue(isinstance(self.inst.number_rooms, int))
        self.assertTrue(isinstance(self.inst.max_guest, int))
        self.assertTrue(isinstance(self.inst.price_by_night, int))
        self.assertTrue(isinstance(self.inst.latitude, float))
        self.assertTrue(isinstance(self.inst.number_bathrooms, int))
        self.assertTrue(isinstance(self.inst.longitude, float))

    def test_amenities_id(self):
        """Test amenities id is  a  list"""

        self.assertTrue(isinstance(self.inst.amenity_ids, list))
