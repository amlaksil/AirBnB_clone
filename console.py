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
import ast
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Interpreter class """
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def parseline(self, line):
        """Adds support for the `(` syntax """
        if '(' in line:
            line = line.replace('.', ' ', 1).replace('(', ' ', 1)
            line = line.replace(')', '')
            if '{' in line and ': ' in line and '}' in line:
                #  Update if dictionary is given
                line = line.replace(': ', '##').replace(', ', '%%')
                line = line.replace('%%{', ' {', 1)
                line = line.split(" ", 3)
                line[3] = line[3].replace('##', ': ').replace('%%', ', ')
                line[2] = line[2].replace('"', '').replace(',', '')
                line = " *".join([line[1], line[0], line[2], line[3]])
                return super().parseline(line)
            line = line.split()
            if len(line) == 3:
                #  For show and destroy
                line[2] = line[2].replace('"', '')
                line = " ".join([line[1], line[0], line[2]])
            elif len(line) >= 5:
                #  Update if attribute name and value are given
                line[2] = line[2].replace('"', '')
                line[2] = line[2].replace(',', '')
                line[3] = line[3].replace('"', '')
                line[3] = line[3].replace(',', '')
                line[4] = line[4].replace('"', '')
                line = " ".join([line[1], line[0], line[2], line[3], line[4]])
            else:
                line = " ".join([line[1], line[0]])
        return super().parseline(line)

    def do_quit(self, arg):
        """Type: `quit` to exit the console"""
        return True

    def do_EOF(self, arg):
        """Press: `Ctr + D` to exit the console"""
        print()
        return True

    def emptyline(self):
        """Overidding `emptyline` base class method """
        pass

    def do_create(self, arg):
        """Creates a new instance for the given class\
        \nUsage: create <class name>, or
        <class name>.create()\
        """
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
        """Prints the string representation of an instance\
        \nUsage: show <class name> <id>
        <class name>.show(<id>)\
        """
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
        """Deletes an instance based on name and id\
        \nUsage: destroy <class name> <id>
        <class name>.destroy(<id>)\
        """
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
        """Prints all string representation of all instances\
        \nUsage: all <class name>, or all
        <class name>.all()\
        """
        a = []
        if not arg:
            for value in storage.all().values():
                a.append(str(value))
            print(a)
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg in key:
                    a.append(str(value))
            print(a)

    def do_update(self, arg):
        """Update an instance based on the class name and id\
        \nUsage: update <class name> <id> <attribute name> <attribute value>
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation>)\
        """
        if '*' in arg:
            cmds = arg.split(' *')
            cmds[0] = cmds[0].replace('*', '', 1)
            cmds[2] = ast.literal_eval(cmds[2])
        else:
            cmds = arg.split(" ", 4)
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
                return
        if len(cmds) == 2:
            print("** attribute name missing **")
        elif len(cmds) == 3:
            if type(cmds[2]) is dict:
                for k, v in cmds[2].items():
                    setattr(storage.all()[key], k, v)
                    storage.save()
                return
            print("** value missing **")
        else:
            if len(cmds) == 4:
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

    def default(self, arg):
        """Parse lines which are not recognized as commands\
        \nUsage: <class name>.count()\
        """
        cmds = arg.split(' ')
        if cmds[0] == 'count':
            count = 0
            for key in storage.all():
                if cmds[1] in key:
                    count += 1
            print(count)
        else:
            return super().default(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
