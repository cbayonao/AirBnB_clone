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
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

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
        """ test __init__ """
        self.assertTrue(isinstance(self.base_mod, BaseModel))

    def test_save(self):
        """ test save """
        self.bm1 = self.base_mod.updated_at
        self.base_mod.save()
        self.bm2 = self.base_mod.updated_at
        self.assertNotEqual(self.bm1, self.bm2)
        self.assertNotEqual(self.base_mod.created_at, self.base_mod.updated_at)
        check = BaseModel()
        new_id = check.id
        check.name = "Bean"
        check.save()
        storage.reload()
        my_objs = storage.all()["BaseModel.{}".format(new_id)]
        self.assertTrue(hasattr(my_objs, "name"))
        self.assertTrue(my_objs.name == "Bean")
        self.assertTrue(os.path.exists('file.json'))

    def test_ToDict(self):
        """ Test to_dict """
        test_dict = self.base_mod.to_dict()
        self.assertTrue(test_dict.get("__class__"))
        self.assertTrue(type(test_dict) is dict)
        self.assertTrue("to_dict" in dir(self.base_mod))


if __name__ == "__main__":
    unittest.main()
