#!/usr/bin/python3
"""A unittest for baseModal class."""

import unittest
from models import storage
from models.base_model import BaseModel
from datetime import datetime

_b1 = BaseModel()
_b2 = BaseModel(**_b1.to_dict())
_b3 = BaseModel("hello", "wait", "in")


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_params(self):
        """Test method for class attribute"""

        k = f"{type(_b1).__name__}.{_b1.id}"

        self.assertIn(k, storage.all())
        self.assertIsInstance(_b1.id, str)
        self.assertIsInstance(_b1.created_at, datetime)
        self.assertEqual(_b1.cr_eated_at, _b2.created_at)
        self.assertEqual(_b1.id, _b2.id)
        self.assertIsInstance(_b1.created_at, datetime)

    def test_dict(self):
        """Test method for dict"""

        b1_dict = _b1.to_dict()

        self.assertIsInstance(_b1.to_dict(), dict)
        self.assertEqual(b1_dict['__class__'], type(_b1).__name__)
        self.assertIn('updated_at', b1_dict.keys())
        self.assertNotEqual(_b1, _b2)
        self.assertIn('created_at', b1_dict.keys())

    def test_save(self):
        """Test method for the save method"""

        old_update = _b1.updated_at
        _b1.save()
        self.assertNotEqual(_b1.updated_at, old_update)

    def test_str(self):
        """Test method for str"""

        string = f"[{type(_b1).__name__}] ({_b1.id}) {_b1.__dict__}"
        self.assertEqual(_b1.__str__(), string)


if __name__ == "__main__":
    unittest.main()
