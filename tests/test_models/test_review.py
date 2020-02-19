#!/usr/bin/python3
""" Test Review """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Test Review """
    @classmethod
    def setUpClass(clase):
        """ setup """
        clase.chk_review = Review()
        clase.chk_review.text = "Luxury"

    @classmethod
    def deleteClase(clase):
        """ delete """
        del clase.chk_review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        """ Test type """
        self.assertTrue(issubclass(self.chk_review.__class__, BaseModel), True)

    def test_Functions(self):
        """ Test functions """
        self.assertIsNotNone(Review.__doc__)

    def test_Attr(self):
        """ Test attributes """
        self.assertTrue('text' in self.chk_review.__dict__)

    def test_Strings(self):
        """ Test string """
        self.assertEqual(type(self.chk_review.text), str)

    def test_Save(self):
        """ Test save """
        self.chk_review.save()
        self.assertNotEqual(self.chk_review.created_at,
                            self.chk_review.updated_at)

    def test_ToDict(self):
        """ Test to_dict """
        self.assertEqual('to_dict' in dir(self.chk_review), True)


if __name__ == "__main__":
    unittest.main()
