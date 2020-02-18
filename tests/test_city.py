#!/usr/bin/python3
import unittest
import pep8


class TestBaseModel(unittest.TestCase):
    """Test clase"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8check = pep8.StyleGuide(quiet=True)
        result = pep8check.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings)PEP8.")
