#!/usr/bin/python3
"""
This module defines a simple command interpreter that
manage (create, update, destroy, etc) objects via console
"""
from models.base_model import BaseModel
from models import storage
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Interpreter class """
    prompt = "(hbnb) "
    classes = ['BaseModel', 'State', 'City', 'Amenity', 'Place', 'Review']

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
            new_instance = BaseModel()
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
            key = f"{self.classes[0]}.{cmds[1]}"
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
            key = f"{self.classes[0]}.{cmds[1]}"
            if key in dict_obj:
                del dict_obj[key]
                storage.__objects = dict_obj
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instance """
        cmds = arg.split()
        val_list = []
        if len(cmds) == 0 or cmds[0] in self.classes:
            for value in storage.all().values():
                val_list.append(str(value))
            print(val_list)
        else:
            print("** class doesn't exist **")

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
            key = f"{self.classes[0]}.{cmds[1]}"
            if key not in dict_obj:
                print("** no instance found **")
                return
        if len(cmds) == 2:
            print("** attribute name missing **")
        elif len(cmds) == 3:
            print("** value missing **")
        else:
            setattr(storage.all()[key], cmds[2], cmds[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
