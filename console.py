#!/usr/bin/python3

"""
Console
Entry point for command interpreter
Should be able to make, edit, and delete things
"""
import shlex
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class created for command processor
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """
        quits out of the program
        """
        quit()

    def do_EOF(self, line):
        """
        End of file for the program
        """
        print()
        raise SystemExit

    def empty_line(self):
        """
        does nothing passes epty line
        """
        pass

    def do_create(self, line):
        """
        New instance of BaseModel
        """
        cmd_ln = self.parseline(line)[0]
        if len(line) == 0:
            print("** class name missing **")
        elif cmd_ln not in self.classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(cmd_ln)()
            new_object.save()
            print(new_object.id)

    def do_show(self, line):
        """
        Prints str of an instance based on class name and id
        """
        cmd_ln = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if cmd_ln is None:
            print("** class name missing **")
        elif cmd_ln not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            instance_class_name = models.storage.all().get(cmd_ln + '.' + arg)
            if instance_class_name is None:
                print("** no instance found **")
            else:
                print(instance_class_name)

    def do_destroy(self, line):
        """
        delete instance based on class name and id
        """
        cmd_ln = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if cmd_ln is None:
            print("** class name missing **")
        elif cmd_ln not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            temp = cmd_ln + '.' + arg
            instance_class_name = models.storage.all().get(temp)
            if instance_class_name is None:
                print("** no instance found **")
            else:
                del models.storage.all()[temp]
                models.storage.save()

    def do_all(self, line):
        """
        prints str of ALL instances if its class name or not
        """
        cmd_ln = self.parseline(line)[0]
        objt = models.storage.all()
        if cmd_ln is None:
            print([str(objt[obj]) for obj in objt])
        elif cmd_ln in self.classes:
            temp = objt.keys()
            print([str(objt[temp]) for key in temp if key.startswith(cmd_ln)])
        else:
            print("** class doesn't exist **")

    """def do_update(self, args):
        if args == "":
            print("** class name missing **")
        else:
            if args not in class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id is missing **")
                else:
                    key = args[0] + "." + args[1]
                    if key not in models.storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** instance id missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                setattr(models.storage.all()[key]),
                                args[2], args[4]
                                models.storage.save()
"""
    def do_update(self, line):
        """
        updates instance based on class name & id
        with adding or updating and attribute
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
