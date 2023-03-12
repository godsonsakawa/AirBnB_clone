#!/usr/bin/python3
"""HBNBCommand console interpreter"""
import cmd
from shlex import split
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [x.strip(",") for x in split(arg)]
        else:
            lex = split(arg[:brackets.span()[0]])
            ret = [x.strip(",") for x in lex]
            ret.append(backets.group())
            return ret
    else:
        lex = split(arg[:curly_braces.span()[0]])
        ret = [x.strip(",") for x in lex]
        ret.append(curly_braces.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """Defines HBNBCommand console interpreter
    AttributeS:
           prompt (str): The command prompt
           __classes (dictionary): Contains all classes
    """
    prompt = "(hbnb)"
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def emptyline(self):
        """Does nothing if empty line is passed"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid
        Args:
            arg (str): The command argument passed
        """
        calls = {
                "create": self.do_create,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "all": self.do_all,
                "update": self.do_update
                }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in calls.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return calls[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the pogram"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """ Creates a new instance of BseModel, saves and prints its id
        Args:
            arg (str): The command line arguments
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """ Prints string representation of an instance based on class
        name and id
        Args:
            arg (str): The command line arguments
        """
        args = parse(arg)
        odict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in odict:
            print("** no instance found **")
        else:
            print(odict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instane based on the class name and id
        Args:
            arg (str): The command line arguments
        """

        args = parse(arg)
        odict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in odict:
            print("** no instance found **")
        else:
            del odict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on class instances
        Args:
            arg (str): The command arguments
        """
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Updates and instance based on class name and id by adding or
        updating attribute
        Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <dictionary>)
        Args:
            arg (str): The command line arguments
        """
        args = parse(arg)
        odict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in odict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = odict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                _type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = _type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = odict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    _type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = _type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
