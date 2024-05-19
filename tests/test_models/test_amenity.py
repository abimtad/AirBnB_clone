#!/usr/bin/python3
"""Unittest for amenity class"""

import unittest
import models
from datetime import datetime
from models.amenity import Amenity
from time import sleep


class TestAmenity_instantiation(unittest.TestCase):
    """Unit test for verifying the instantiation of Amenity class."""

    def test_no_args_instantiates(self):
        """Test for instances with no args"""

        self.assertEqual(Amenity, type(Amenity()))

    def test_instance_stored_in_object(self):
        """Test for instances stored in object"""

        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_public_str(self):
        """Test if id is a public string"""

        self.assertEqual(str, type(Amenity().id))

    def test_created_is_public_datetime(self):
        """created is public date time"""

        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_is_public_datetime(self):
        """updated is public timestamp"""

        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_public_class_attribute(self):
        """Test name is public string attribute"""

        amn = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amn.__dict__)

    def test_two_amenities_unique_id(self):
        """Test if instances are unique"""

        amn1 = Amenity()
        amn2 = Amenity()
        self.assertNotEqual(amn1.id, amn2.id)

    def test_two_amenities_different_created(self):
        """different instances have different creation timestamp """
        amn1 = Amenity()
        sleep(0.05)
        amn2 = Amenity()
        self.assertLess(amn1.created_at, amn2.created_at)

    def test_two_amenities_different_updated_at(self):
        """Two instances have different update timestamp """

        amn1 = Amenity()
        sleep(0.05)
        amn2 = Amenity()
        self.assertLess(amn1.updated_at, amn2.updated_at)

    def test_args_unused(self):
        """Test if args are unused"""

        amn = Amenity(None)
        self.assertNotIn(None, amn.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwarg test methods"""

        dat = datetime.today()
        dt_iso = dt.isoformat()
        amn = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amn.id, "345")
        self.assertEqual(amn.created_at, dat)
        self.assertEqual(amn.updated_at, dat)

    def test_instantiation_None_kwarg(self):
        """Init with none kwarg"""

        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)
