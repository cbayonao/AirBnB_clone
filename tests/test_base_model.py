#!/usr/bin/python3
""" Test clase """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import unittest
import pep8


class Test_Base(unittest.TestCase):
    """ Test clase """

    @classmethod
    def setUpClass(cls):
        """ setup """
        cls.base_mod = BaseModel()
        cls.base_mod.name = "Joe"
        cls.base_mod.my_num = 16

    @classmethod
    def deleteclass(cls):
        """ delete """
        del cls.base_mod
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 style """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_functions(self):
        """ test functions """
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """ test attributes """
        self.assertEqual(hasattr(self.base_mod, "id"), True)
        self.assertEqual(hasattr(self.base_mod, "created_at"), True)
        self.assertEqual(hasattr(self.base_mod, "updated_at"), True)

    def test_init(self):
        self.assertTrue(isinstance(self.base_mod, BaseModel))

    def test_save(self):
        """test save"""
        self.base_mod.save()
        self.assertNotEqual(self.base_mod.created_at, self.base_mod.updated_at)

    def test_to_dict(self):
        """test to_dict"""
        self.assertEqual('to_dict' in dir(self.base_mod), True)


if __name__ == "__main__":
    unittest.main()
