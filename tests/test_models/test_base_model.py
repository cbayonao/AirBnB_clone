#!/usr/bin/python3
"""
Test Module
"""
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Class"""
    def setUp(self):
        """setup"""
        self.bm_test1 = BaseModel()
        self.bm_test2 = BaseModel()

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

    def test_save(self):
        """test save"""
        save_a = self.bm_test1.updated_at
        self.bm_test1.save()
        save_b = self.bm_test2.updated_at
        self.assertFalse(save_a == save_b)
        
#    def test_to_dict(self):
#        bm_dict = self.basem.to_dict()
#        self.assertTrue(bm_dict.get("__class__"))
#        self.assertTrue(type(bm_dict) is dict)
#        self.assertTrue("to_dict" in dir(self.basem))

    def test_to_dict(self):
        """test to_dict"""
        self.assertEqual('to_dict' in dir(self.bm_test1), True)


if __name__ == "__main__":
    unittest.main()
