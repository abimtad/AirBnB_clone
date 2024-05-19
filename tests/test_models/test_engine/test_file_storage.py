#!/usr/bin/python3

"""Define unittest for models/engine/file_storage.py"""

import unittest

import models
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of the 'FileStorage' class."""

    def test_FileStorage_instantiation_no_args(self):
        """Test FileStorage initialization with no args"""

        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test init with args = None"""

        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test file_path is a private string"""

        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Test object is a private dictionary"""

        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test if the class initializes"""

        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
