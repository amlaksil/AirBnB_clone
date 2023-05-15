#!/usr/bin/python3
"""
This module defines a simple command interpreter that
manage (create, update, destroy, etc) objects via console
"""
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Interpreter class """
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def parseline(self, line):
        """Adds support for the '.' syntax
        """
        if '.' in line:
            line = line.replace('.', ' ', 1).replace('(', ' ', 1)
            line = line.replace(')', '')
            line = line.split()
            if len(line) == 3:
                line[2] = line[2].replace('"', '')
                line = " ".join([line[1], line[0], line[2]])
            else:
                line = " ".join([line[1], line[0]])

        return super().parseline(line)

    def do_quit(self, arg):
        """Type\n`quit` to exit the console"""
        return True

    def do_EOF(self, arg):
        """Press\n`Ctr + D` to exit the console"""
        print()
        return True

    def emptyline(self):
        """Overidding `emptyline` base class method """
        pass

    def do_create(self, arg):
        """Creates a new instance for BaseModel class """
        cmds = arg.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(cmds[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance """
        cmds = arg.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            dict_obj = storage.all()
            key = f"{cmds[0]}.{cmds[1]}"
            if key in dict_obj:
                print(dict_obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the name and id """
        cmds = arg.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            dict_obj = storage.all()
            key = f"{cmds[0]}.{cmds[1]}"
            if key in dict_obj:
                del dict_obj[key]
                storage.__objects = dict_obj
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances or all instances
        of a specified class
        """
        if not arg:
            for value in storage.all().values():
                print(value)
        
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg in key:
                    print(value)

    def do_update(self, arg):
        """Update an instance based on the class name and id """
        cmds = arg.split()
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            dict_obj = storage.all()
            key = f"{cmds[0]}.{cmds[1]}"
            if key not in dict_obj:
                print("** no instance found **")
            elif len(cmds) == 2:
                print("** attribute name missing **")
            elif len(cmds) == 3:
                print("** value missing **")
            else:
                a = []
                if '"' in cmds[3]:
                    a = cmds[3]
                    cmds[3] = a[1:-1]
                elif cmds[3].isdigit():
                    cmds[3] = int(cmds[3])
                elif cmds[3].replace('.', "").isdigit():
                    cmds[3] = float(cmds[3])
                setattr(storage.all()[key], cmds[2], cmds[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
