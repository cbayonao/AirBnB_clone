#!/usr/bin/python3
"""
Test Module
"""
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8check = pep8.StyleGuide(quiet=True)
        result = pep8check.check_files(['models/base_model.py',
                                        'models/user.py',
                                        'models/state.py',
                                        'models/city.py',
                                        'models/place.py',
                                        'models/amenity.py',
                                        'models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
