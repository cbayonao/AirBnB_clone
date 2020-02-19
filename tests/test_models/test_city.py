#!/usr/bin/python3
""" Test City """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ Test City """
    @classmethod
    def setUpClass(clase):
        """ setup """
        clase.chk_city = City()
        clase.chk_city.name = "Orlando"
        clase.chk_city.state_id = "FL"

    @classmethod
    def deleteClase(clase):
        """ delete """
        del clase.chk_city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        """ test type """
        self.assertTrue(issubclass(self.chk_city.__class__, BaseModel), True)

    def test_Functions(self):
        """ test functions """
        self.assertIsNotNone(City.__doc__)

    def test_Attr(self):
        """ test attributes """
        self.assertTrue('name' in self.chk_city.__dict__)
        self.assertTrue('id' in self.chk_city.__dict__)

    def test_Strings(self):
        """ test strings """
        self.assertEqual(type(self.chk_city.name), str)
        self.assertEqual(type(self.chk_city.state_id), str)

    def test_Save(self):
        """ test save """
        self.chk_city.save()
        self.assertNotEqual(self.chk_city.created_at, self.chk_city.updated_at)

    def test_ToDict(self):
        """ test to dict """
        self.assertEqual('to_dict' in dir(self.chk_city), True)


if __name__ == "__main__":
    unittest.main()
