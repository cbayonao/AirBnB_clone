#!/usr/bin/python3
""" test FileStorage """
import unittest
import os
import pep8
import json
from models.base_model import BaseModel
from models.engine import file_storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """ test class """
    @classmethod
    def setUpClass(class_test):
        """ setup """
        class_test.usr = User()
        class_test.usr.first_name = "Joe"
        class_test.usr.last_name = "Black"
        class_test.usr.email = "joeblack2020@gmail.com"
        class_test.storage = file_storage.FileStorage()

    @classmethod
    def deleteclass(class_test):
        """ delete """
        del class_test.usr

    def deleteclass_test(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_All(self):
        """ test all """
        fstorage = file_storage.FileStorage()
        dic = fstorage.all()
        self.assertIsNotNone(dic)
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, fstorage._FileStorage__objects)

    def test_New(self):
        """ test new """
        fstorage = file_storage.FileStorage()
        dic = fstorage.all()
        check = User()
        check.id = 2112
        check.name = "Bob"
        fstorage.new(check)
        key = check.__class__.__name__ + "." + str(check.id)
        self.assertIsNotNone(dic[key])

    def test_Reload(self):
        """ test reload """
        self.storage.save()
        path_inf = os.path.dirname(os.path.abspath("console.py"))
        path_f = os.path.join(path_inf, "file.json")
        with open(path_f, "r") as f:
            ln = f.readlines()
        try:
            os.remove(path_f)
        except BaseException:
            pass
        self.storage.save()
        with open(path_f, "r") as f:
            ln2 = f.readlines()
        self.assertEqual(ln, ln2)
        try:
            os.remove(pt)
        except BaseException:
            pass
        with open(path_f, "w") as f:
            f.write("{}")
        with open(path_f, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
