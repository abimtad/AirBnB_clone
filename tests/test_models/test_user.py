#!/usr/bin/python3
"""Unittest for 'user' class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    @classmethod
    def setUpClass(self):
        """Setup instantiation for tests"""

        self.inst = User()

    @classmethod
    def tearDownClass(self):
        """Delete tests after test"""

        del self.inst

    def test_first_name(self):
        """Test if User first name is a public string"""

        self.assertTrue(isinstance(self.inst.first_name, str))

    def test_name(self):
        """Test if user last name is a public string"""

        self.assertTrue(isinstance(self.inst.last_name, str))

    def test_password(self):
        """Test if password is public string"""

        self.assertTrue(isinstance(self.inst.password, str))

    def test_email(self):
        """Test if user email is a public string"""

        self.assertTrue(isinstance(self.inst.email, str))
