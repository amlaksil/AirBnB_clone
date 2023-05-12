#!/usr/bin/python3
"""The command interpreter for the AirBnB_clone project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class for AirBnB_clone"""
    prompt = '(hbnb) '

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
