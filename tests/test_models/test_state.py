#!/usr/bin/python3
""" Test State """
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """ Test State """
    @classmethod
    def setUpClass(clase):
        """ setup """
        clase.chk_state = State()
        clase.chk_state.name = "Florida"

    @classmethod
    def deleteClase(clase):
        """ delete """
        del clase.chk_state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_StyleCheck(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_SubClass(self):
        """ Test type """
        self.assertTrue(issubclass(self.chk_state.__class__, BaseModel), True)

    def test_Functions(self):
        """ Test functions """
        self.assertIsNotNone(State.__doc__)

    def test_Attr(self):
        """ Test attributes """
        self.assertTrue('name' in self.chk_state.__dict__)

    def test_Strings(self):
        """ Test strings """
        self.assertEqual(type(self.chk_state.name), str)

    def test_Save(self):
        """ Test save """
        self.chk_state.save()
        self.assertNotEqual(self.chk_state.created_at,
                            self.chk_state.updated_at)

    def test_ToDict(self):
        """ Test to_dict """
        self.assertEqual('to_dict' in dir(self.chk_state), True)


if __name__ == "__main__":
    unittest.main()
