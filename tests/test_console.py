#!/usr/bin/python3

"""Defines unittests for console.py."""

from io import StringIO
from unittest.mock import patch
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test for the console module"""

    def tearDown(self) -> None:
        return super().tearDown()

    def setUp(self) -> None:
        return super().setUp()

    def test_simple(self):
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help show")