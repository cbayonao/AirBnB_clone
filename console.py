#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
from models.base_model import BaseModel
from models import storage, classes
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from datetime import datetime
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb) "
    dict_classes = classes
    __flag = 0

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
        obj_list = []
        if not args:
            if HBNBCommand.__flag == 0:
                print("[\"" + "\", \"".join(["{}".format(val) for val in
                                            storage.all()
                                            .values()]), end="\"]\n")
            else:
                print("[" + ", ".join(["{}".format(val) for val in
                                       storage.all().values()]), end="]\n")
        elif args not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
        else:
            if HBNBCommand.__flag == 0:
                print("[\"" + "\", \"".join(["{}".format(val) for key, val in
                                            storage.all().items() if args
                                            in key]), end="\"]\n")
            else:
                print("[" + ", ".join(["{}".format(val) for key, val in
                                      storage.all().items() if args
                                      in key]), end="]\n")
                HBNBCommand.__flag = 0

    def update_from_dict(self, dprm, tokens, msk, objects):
        obj_dic = self.build_dict(dprm)
        classes = self.up_clases
        if tokens[0] in classes:
            if msk in objects:
                obj = objects[msk]
                for k, v in obj_dic.items():
                    setattr(obj, k, v)
                obj.updated_at = datetime.now()
                storage.save()

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
or updating attribute (save the change into the JSON file)

Usage: update <classname> <uuid> <attribute> <value>
        """
        args = (args.replace('"', ""))
        args = [txt.strip() for txt in args.split()]
        print(len(args))
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
        elif "{}.{}".format(args[0], args[1]) in storage.all():
            setattr(storage.all()["{}.{}".format(args[0], args[1])],
                    args[2], args[3])
            storage.all()[args[0]+"."+args[1]].updated_at = datetime.now()
            storage.save()
        else:
            print("** no instance found **")

    def default(self, args):
        """
            Catches all the function names that are not expicitly defined.
        """
        functions = {"all": self.do_all, "show": self.do_show,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").replace("{", "")
                .replace("}", "").replace("'", "").replace(":", "")
                .split("."))
        print(args)
        try:
            if args[1].startswith("count"):
                sum = 0
                milist = storage.all()
                for keys in milist.keys():
                    if keys.split('.')[0] == args[0]:
                        sum += 1
                print(sum)
            elif args[2]:
                command_args = args[0] + " " + args[2]
                func = functions[args[1]]
                func(command_args)
            else:
                HBNBCommand.__flag = 1
                command_args = args[0]
                func = functions[args[1]]
                func(command_args)
        except:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
