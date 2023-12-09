#!/usr/bin/python3

""" This module defines a command-line
 interface for interacting with a hypothetical Airbnb-like application.
 The interface allows users to create,
  read, update, and delete instances of various classes, such as User,
  State, City, Place, Amenity, and Review.

The module uses the cmd module to create a command interpreter,
 and defines several methods to handle different commands.
  The do_create method creates
   a new instance of a specified class and prints its ID.
   The do_show method displays information about a
    specific instance of a class,
    and the do_destroy method deletes a specific instance.
     The do_all method displays information about all instances of
      a specified class.
 The do_update method updates an instance of a
  class by adding or updating an attribute. """

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
import re


class HBNBCommand(cmd.Cmd):
    """ This class will be the entry point of the
    command interpreter
    it contains methods like count, create, and so on
    """

    prompt = "(hbnb) "
    __classes_list = {"BaseModel", "User", "State",
                      "City", "Place", "Amenity", "Review"}

    def default(self, line):
        """this is a method where it
        Handle default case for the command and support
         <class name>.<action>()."""
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.match(
            r"(\w+)\.(all|count|show|destroy|update)\((.*)\)$", line)

        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            args = match.group(3)

            if class_name in HBNBCommand.__classes_list:
                method = methods.get(method_name)

                if method_name in ["show", "destroy"]:
                    # Remove quotes from the ID if present
                    instance_id = args.strip("\"'")
                    method(f"{class_name} {instance_id}")

                elif method_name == "update":

                    # Check if the argument is a dictionary
                    if args.endswith("}"):

                        instance_id, dict_string = args.split(",", 1)
                        instance_id = instance_id.strip("\"'")
                        try:

                            attr_dict = eval(dict_string.strip())
                            if isinstance(attr_dict, dict):
                                for key, value in attr_dict.items():
                                    method(
                                        f"{class_name} \
                                            {instance_id} {key} {value}")
                        except (SyntaxError, NameError):
                            print("** invalid dictionary representation **")
                    else:

                        # Individual attribute/value pair
                        update_args = args.split(",", 2)
                        if len(update_args) == 3:
                            instance_id, attr_name, attr_value = update_args
                            instance_id = instance_id.strip("\"'")
                            attr_name = attr_name.strip("\"'")
                            attr_value = attr_value.strip("\"'")
                            method(
                                f"{class_name} {instance_id} \
                                    {attr_name} {attr_value}")

                else:
                    method(class_name)
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """this is a method where it handles
        Counts the number of instances of a class."""
        class_name = arg
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)

    def do_quit(self, arg):
        """ this is a method where it handles
        Quit is a command to quit the console """
        return True

    def do_EOF(self, arg):
        """ this is a method where it handles
        What to do in the end of the file """
        print()
        return True

    def emptyline(self):
        """ this is a method where it handles
        do nothing when press enter on empty line """
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
        """ method is used to display information about a specific instance
         of a class that has been stored in the storage object.
         The method takes a single argument, arg,"""

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
        """  method is used to delete a specific instance
         of a class that has been stored in the storage object.  """

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
        """  method is used to display information about all
         instances of a specific class that
          have been stored in the storage object.
         The method takes a single argument, """

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
        """Updates an instance based on the
        class name and id by adding or updating attribute."""

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
            attr_name = args[2].strip("\"'")
            attr_value = args[3].strip("\"'")
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
