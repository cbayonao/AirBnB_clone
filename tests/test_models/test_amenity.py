#!/usr/bin/python3
""" Test Amenity """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Test Amenity """
    @classmethod
    def setUpClass(clase):
        """ Test setup """
        clase.chk_amenity = Amenity()
        clase.chk_amenity.name = "Pool"

    @classmethod
    def deleteClase(clase):
        """ Test delete """
        del clase.chk_amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        """ Test type """
        self.assertTrue(issubclass(self.chk_amenity.__class__, BaseModel),
                        True)

    def test_Functions(self):
        """ Test functions """
        self.assertIsNotNone(Amenity.__doc__)

    def test_Attr(self):
        """ Test attributes """
        self.assertTrue('name' in self.chk_amenity.__dict__)

    def test_Strings(self):
        """ Test string """
        self.assertEqual(type(self.chk_amenity.name), str)

    def test_Save(self):
        """ Test save """
        self.chk_amenity.save()
        self.assertNotEqual(self.chk_amenity.created_at,
                            self.chk_amenity.updated_at)

    def test_ToDict(self):
        """ Test to_dict """
        self.assertEqual('to_dict' in dir(self.chk_amenity), True)


if __name__ == "__main__":
    unittest.main()
