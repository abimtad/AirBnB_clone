#!/usr/bin/python3

"""Defines the HBnB console."""

import ast
import cmd
import re
from models.base_model import BaseModel
import models
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


def convert(lin):
    """Splits input from tty using whitespace as a delimiter.

    Args:
        lin: tty input stream
    """

    if len(lin) == 0:
        return []
    lin_2 = lin.split(" ")
    return lin_2


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter for HolbertonBnB."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review}

    def do_quit(self, lin):
        """Quit command to exit the program."""

        return True

    def do_EOF(self, lin):
        """EOF signal to exit the program."""

        print("")

        return True

    def emptyline(self):
        """Do nothing if no command is provided."""


    def do_create(self, lin):
        """Create a new class instance and print its ID."""

        lin_2 = convert(lin)

        if len(lin_2) == 0:
            print("** class name missing **")

            return

        elif lin_2[0] not in self.__classes:
            print("** class doesn't exit **")

            return

        print(self.__classes[lin_2[0]]().id)
        models.storage.save()


    def do_destroy(self, lin):
        """Delete a class instance with a given ID."""

        lin_2 = convert(lin)
        if len(lin_2) > 1:
            lin_2[-1] = lin_2[-1].strip('"')
        objj = models.storage.all()

        if len(lin_2) == 0:
            print("** class name missing **")
            return

        elif lin_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(lin_2) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(lin_2[0], lin_2[1]) not in objj.keys():
            print("** no instance found **")

        else:
            del objj["{}.{}".format(lin_2[0], lin_2[1])]
            models.storage.save()
        
    def do_show(self, lin):
        """Display the string representation of a class instance with a given ID."""

        lin_2 = convert(lin)
        if len(lin_2) > 1:
            lin_2[-1] = lin_2[-1].strip('"')
        objj = models.storage.all()

        if len(lin_2) == 0:
            print("** class name missing **")
            return

        elif lin_2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif len(lin_2) == 1:
            print("** instance id missing **")
            return

        elif "{}.{}".format(lin_2[0], lin_2[1]) not in objj.keys():
            print("** no instance found **")
            return
        print(objj["{}.{}".format(lin_2[0], lin_2[1])])

    def do_all(self, lin):
        """Display string representations of all instances of a given class."""

        lin_2 = convert(lin) if len(lin) > 0 else None
        objjl = []
        if lin_2 is None:
            for ob in models.storage.all().values():
                objjl.append(ob.__str__())
        elif lin_2[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for ob in models.storage.all().values():
                if lin_2[0] == ob.__class__.__name__:
                    objjl.append(ob.__str__())
                elif len(lin_2) == 0:
                    objjl.append(ob.__str__())
        if len(objjl) != 0:
            print(objjl)

    def do_update(self, lin):
        """Update a class instance with a given ID by adding or updating
        a given attribute key/value pair or dictionary."""

        lin_2 = convert(lin)
        index = 0

        if len(lin_2) >= 4 and lin_2[3].startswith('"'):
            for argg in lin_2:
                if argg.endswith('"'):
                    index = lin_2.index(argg)
            if len(lin_2) > index:
                lin_2[3] = " ".join(lin_2[3:index + 1])

        objj = models.storage.all()

        if len(lin_2) == 0:
            print("** class name missing **")
            return False

        if lin_2[0] not in self.__classes:
            print("** class doesn't exist **")
            return False

        if len(lin_2) == 1:
            print("** instance id missing **")
            return False

        if "{}.{}".format(lin_2[0], lin_2[1]) not in objj.keys():
            print("** no instance found **")
            return False

        if len(lin_2) == 2:
            print("** attribute name missing **")
            return False

        if len(lin_2) == 3:
            try:
                type(eval(lin_2[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(lin_2) >= 4:
            lin_2[3] = lin_2[3].strip('"')
            ob = objj["{}.{}".format(lin_2[0], lin_2[1])]
            if lin[2] in ob.__class__.__dict__.keys():
                value_type = type(ob.__class__.__dict__[lin_2[2]])
                ob.__dict__[lin_2[2]] = value_type(lin_2[3])
            else:
                ob.__dict__[lin_2[2]] = lin_2[3]

        models.storage.save()

    def default(self, lin):
        lin_split = lin.split(".", maxsplit=1)

        if len(lin_split) != 2:
            super().default(lin)
            return

        class_nam, command = lin_split
        match = re.search(r"\((.*?)\)", command)

        if match:
            command = [command[:match.span()[0]], match.group()[1: -1]]
            if hasattr(self, 'do_' + command[0]):
                method = getattr(self, 'do_' + command[0])
                call = class_nam
                if command[0] == "update":
                    id_dict = command[1].split(", ", maxsplit=1)
                    if (len(id_dict) > 1 and id_dict[1][0] == "{"):
                        inst_id, dict = id_dict
                        inst_id = inst_id.strip('"')
                        dict = dict.strip('"')
                        dict = ast.literal_eval(dict)
                        for key, value in dict.items():
                            args = inst_id + " " + key + " " + str(value)
                            method(f"{call} {args}")
                        return
                    else:
                        args = ""
                        args = ''.join(char for char in command[1] if
                                       char not in [',', '"'])
                        if args != command[1]:
                            call = f"{call} {args}"
                            method(call)
                        else:
                            method(call)
                    return

                if len(command[1]) != 0:
                    command[1] = command[1].strip('"')
                    call = f"{call} {command[1]}"
                method(call)

            elif command[0] == "count" and class_nam in self.__classes:
                count = 0
                for obj in models.storage.all().values():
                    if obj.__class__.__name__ == class_nam:
                        count += 1
                print(count)
        else:
            super().default(lin)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
