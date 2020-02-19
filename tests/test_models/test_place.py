#!/usr/bin/python3
""" Test Place """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Test Place """
    @classmethod
    def setUpClass(clase):
        """ setup """
        clase.chk_place = Place()
        clase.chk_place.name = "FiveStarts"
        clase.chk_place.description = "Luxury"

    @classmethod
    def deleteClase(clase):
        """ delete """
        del clase.chk_place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        """ test type """
        self.assertTrue(issubclass(self.chk_place.__class__, BaseModel), True)

    def test_Functions(self):
        """ test functions """
        self.assertIsNotNone(Place.__doc__)

    def test_Attr(self):
        """ test attributes """
        self.assertTrue('name' in self.chk_place.__dict__)
        self.assertTrue('description' in self.chk_place.__dict__)

    def test_Strings(self):
        """ test string """
        self.assertEqual(type(self.chk_place.name), str)
        self.assertEqual(type(self.chk_place.description), str)

    def test_Save(self):
        """ test save """
        self.chk_place.save()
        self.assertNotEqual(self.chk_place.created_at, self.chk_place.updated_at)

    def test_ToDict(self):
        """ test to_dict """
        self.assertEqual('to_dict' in dir(self.chk_place), True)


if __name__ == "__main__":
    unittest.main()
