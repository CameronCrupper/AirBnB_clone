#!/usr/bin/python3

"""
Console
Entry point for command interpreter
Should be able to make, edit, and delete things
"""

import cmd


class HBNBCommand(cmd.Cmd):


    propmpt = '(hbnb) '

    def lets_quit(self):
        """
        quits out of the program
        """
        return True

    def lets_EOF(self):
        """
        End of file for the program
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
