#!/usr/bin/python3

""" The Control Unit Module """

import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class will be the entry point of the
    command interpreter
    """

    prompt = "(hbnb) "
    __classes_list = {"BaseModel", "User", "State",
                      "City", "Place", "Amenity", "Review"}

    def do_quit(self, arg):
        """ Quit is a command to quit the console """
        return True

    def do_EOF(self, arg):
        """ What to do in the end of the file """
        print()
        return True

    def emptyline(self):
        """ do nothing when press enter on empty line """
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """ TO BE ADDED """

        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                sotred_data = storage.all()
                print(sotred_data["{}.{}".format(args[0], args[1])])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ TO BE ADDED """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                sotred_data = storage.all()
                del sotred_data["{}.{}".format(args[0], args[1])]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """ TO BE ADDED """

        args = arg.split()
        obj_list = []
        if len(args) == 1:
            if args[0] not in HBNBCommand.__classes_list:
                print("** class doesn't exist **")
                return
            else:
                for i in storage.all().values():
                    if i.__class__.__name__ == args[0]:
                        obj_list.append(str(i))

        elif len(args) == 0:
            for i in storage.all().values():
                obj_list.append(str(i))

        print(obj_list)

    def do_update(self, arg):
        """ TO BE ADDED """

        args = arg.split()
        data = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args[0], args[1]) not in data.keys():
            print("** no instance found **")

        elif len(args) == 2:
            print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")

        else:
            class_name = args[0]
            instance_id = args[1]
            attr_name = args[2]
            attr_value = args[3].strip('"')
            key = "{}.{}".format(args[0], args[1])
            obj = data[key]

            if hasattr(obj, attr_name):
                vtype = type(getattr(obj, attr_name))
                obj.__dict__[attr_name] = vtype(attr_value)
            else:
                obj.__dict__[attr_name] = attr_value
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
