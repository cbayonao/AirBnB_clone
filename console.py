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
    dict_classes = {"BaseModel": BaseModel,
                    "User": User, "Amenity": Amenity,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State}

    def default(self, args):
        """Function to retrieve all instances of a
        class by using: <class name>.all()"""
        com = args.split(".")
        if len(com) > 1:
            if com[1].startswith('all()'):
                return self.do_all(com[0])
            if com[1].startswith('count()'):
                sum = 0
                milist = storage.all()
                for keys in milist.keys():
                    if keys.split('.')[0] == com[0]:
                        sum += 1
                print(sum)
            if com[1].startswith('show()'):

        else:
            cmd.Cmd.default(self, args)




    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """Exit program at End Of File (EOF)
        """
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
and prints the id."""
        args = [txt.strip() for txt in args.split()]
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
        else:
            new = eval(args[0])(args[1:])
            print(new.id)
            new.save()

    def do_show(self, args):
        """Prints the string representation of an instance
based on the class name and id.

Usage: show <classname> <uuid>
        """
        args = [txt.strip() for txt in args.split()]
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
(save the change into the JSON file)

Usage: destroy <classname> <uuid>
        """
        args = [txt.strip() for txt in args.split()]
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
based or not on the class name

Usage: all <classname>
       or just the command without <classname>: all
"""
        if not args:
            for val in storage.all().values():
                print(val)
        elif args not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
        else:

            for key, val in storage.all().items():
                if args == key.split(".")[0]:
                    print(val)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
or updating attribute (save the change into the JSON file)

Usage: update <classname> <uuid> <attribute> <value>
        """
        args = [txt.strip() for txt in args.split()]
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            if "{}.{}".format(args[0], args[1]) not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if "{}.{}".format(args[0], args[1]) in storage.all():
                setattr(storage.all()["{}.{}".format(args[0], args[1])],
                        args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
