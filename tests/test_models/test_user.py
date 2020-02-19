#!/usr/bin/python3
""" Test User """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """ Test User """
    @classmethod
    def setUpClass(clase):
        clase.chk_usr = User()
        clase.chk_usr.first_name = "Joe"
        clase.chk_usr.last_name = "Black"
        clase.chk_usr.email = "joeblack2020@gmail.com"
        clase.chk_usr.password = "test0192"

    @classmethod
    def deleteClase(clase):
        """ delete """
        del clase.chk_usr
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        """ Test type """
        self.assertTrue(issubclass(self.chk_usr.__class__, BaseModel), True)

    def test_Functions(self):
        """ Test functions """
        self.assertIsNotNone(User.__doc__)

    def test_Attr(self):
        """ Test attributes """
        self.assertTrue('email' in self.chk_usr.__dict__)
        self.assertTrue('id' in self.chk_usr.__dict__)
        self.assertTrue('created_at' in self.chk_usr.__dict__)
        self.assertTrue('updated_at' in self.chk_usr.__dict__)
        self.assertTrue('password' in self.chk_usr.__dict__)
        self.assertTrue('first_name' in self.chk_usr.__dict__)
        self.assertTrue('last_name' in self.chk_usr.__dict__)

    def test_Strings(self):
        """ Test string """
        self.assertEqual(type(self.chk_usr.email), str)
        self.assertEqual(type(self.chk_usr.password), str)
        self.assertEqual(type(self.chk_usr.first_name), str)
        self.assertEqual(type(self.chk_usr.first_name), str)

    def test_Save(self):
        """ Test save """
        self.chk_usr.save()
        self.assertNotEqual(self.chk_usr.created_at, self.chk_usr.updated_at)

    def test_ToDict(self):
        """ Test to_dic """
        self.assertEqual('to_dict' in dir(self.chk_usr), True)


if __name__ == "__main__":
    unittest.main()
