#!/usr/bin/python3
"""The command interpreter for the AirBnB_clone project"""
import cmd
import models
from models.amenity import Amenity
from models.city import City

from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class for AirBnB_clone
    """
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = ('BaseModel', 'User', 'State', 'Review',
               'City', 'Amenity', 'Place')

    def preloop(self):
        """Displays a different prompt on non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """Modify display prompt on exiting in non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')
            return True
        return stop
    
    def parseline(self, line):
        """Adds support for the '.' syntax
        """
        if '.' in line:
            line = line.replace('.', ' ')
            line = line.replace('(', '').replace(')', '')
            line = line.split()
            line = line[1] + ' ' + line[0]
        return super().parseline(line)

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to a JSON file
        """
        if not arg:
            print('** class name missing **')
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
           class name and id
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Displays the string representation of all instances or
        all instances of a class
        """
        if not arg:
            for value in models.storage.all().values():
                print(value)
        
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if arg in key:
                    print(value)

    def do_update(self, arg):
        """Updates/adds to an instance's attributes
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')

        else:
            key = args[0] + '.' + args[1]
            if key not in models.storage.all():
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            
            else:
                if args[3][0] == args[3][-1] == '"':
                    args[3] = args[3][1:-1]
                if args[3].isdigit():
                    args[3] = int(args[3])
                if args[3].replace('.', '', 1).isdigit():
                    args[3] = float(args[3])

                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.all()[key].save()

    def do_quit(self, arg):
        """Exits the program with the command 'quit'
        """
        return True
    
    def do_EOF(self, arg):
        """Exits the program on receiving the EOF signal
        """
        print()
        return True
    
    def emptyline(self):
        """Does nothing when an empty line is entered
        """
        pass

    def do_help(self, arg):
        """Displays the help message for the given command
        """
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
