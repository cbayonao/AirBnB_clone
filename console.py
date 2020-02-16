#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb) "
    dict_classes = {"BaseModel": BaseModel}

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Command to exit the program
        """
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        args = [txt.strip() for txt in args.split()]
        if args == '' or args in None:
            print('** class name missing **')
        elif args[0] in my_list:
            new = eval(args[0])(args[1:])
            print(new.id)
            new.save()
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        """
        args = [txt.strip() for txt in args.split()]

        """If the class name is missing"""
        if not args:
            print("** class name missing **")

        """ If the class doesnt exist"""
        elif args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")

        """If the id is missing"""
        elif len(args) == 1:
            print("** instance id missing **")

        """If the instance of the class name doesn’t exist for the id"""
        elif len(args) == 2:
            """If the instance of the class name doesn’t exist for the id"""
            if "{}.{}".format(args[0], args[1]):
                print("** no instance found **")
            """If the attribute name is missing"""
            else:
                print("** attribute name missing **")

        """If the value for the attribute name doesn’t exist"""
        elif len(args) == 3:
            print("** value missing **")

        else:
            if "{}.{}".format(args[0], args[1]) in storage.all():
                setattr(storage.all()["{}.{}".format(args[0], args[1])], args[2], args[3])
                storage.save()

        #All other arguments should not be used
        #id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
        #Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
#Let’s add some rules:

#You can assume arguments are always in the right order
###Each arguments are separated by a space
###A string argument with a space must be between double quote
###The error management starts from the first argument to the last one

if __name__ == "__main__":
    HBNBCommand().cmdloop()
