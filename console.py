#!/usr/bin/python3
"""Defines the HBNBCommand console interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Defines HBNBCommand console interpreter.
    Attributes:
            prompt (str): The string to be displayed as the command prompt.
            __classes - Contains dictionary of all classes.
    """
    prompt = "(hbnb) "
    __classes = { "BaseModel": BaseModel, "User": User, "Place": Place,
                 "State": State, "City": City, "Amenity": Amenity,
                 "Review": Review
                 }
    
    __types = {
                "number_rooms": int, "number_bathrooms": int,
                "max_guest": int, "price_by_night": int,
                "latitude": float, "longitude": float
            }

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>
        Creates a new class instance with given key/values and prints its id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance_1 = HBNBCommand.__classes[arg]()
            instance_1.save()
            print(instance_1.id)

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id
        """
        args = arg.split()
        """
        check if the class name has been passed\
                and whether it exists.
        """
        try:
            cls_name = args[0]
            if cls_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print(" ** class name missing **")
            return

        try:
            id = args[1]
        except:
            print("** instance id missing **")
            return

        key = cls_name + "." + str(id)
        new_dict = storage.all()

        try:
            print(new_dict[key])
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        usage: destroy <class> <id> or <class>.sestroy(<id>)
        Delete a class instance of a given id
        """
        args = arg.split()

        '''
        Checks if a class has been passed or whetherit exists.
        '''
        try:
            cls_name = args[0]
            if cls_name not in HBNBCommand.__classes:
                print("** class doesn't exits **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except:
            print("** instance id missing **")
            return

        key = cls_name + "." + str(id)
        stored_obj = storage.all()

        try:
            del(stored_obj[key])
            storage.save()
        except Exception as e:
            print("**no instance found **")

    def do_all(self, arg):
        """
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given classs.
        If no class is specified, displays all instantiated objects.
        """
        obj_dict = storage.all()
        obj_list = []
        if not arg:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for key, obj in obj_dict.values():
                    if arg in key:
                        obj_list.append(str(obj))
                    print(obj_list)
    
    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute name> <attribute value>
        Update a class instance of a given id by adding or updating a given
        attribute key/value pair.
        """
        args = arg.split()
        try:
            cls_name = args[0]
            if cls_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
            key = cls_name + "." + str(id)
            if key not in storage.all():
                print("**no instance found **")
                return
        except:
            print("** instance id missing **")
            return

        try:
            attr = args[2]
        except:
            print("** attribute name missing **")
            return

        try:
            attr_value = args[3]
        except:
            print("** value missing **")
            return

        if "\"" in attr_value:
            attr_value = attr_value[1: -1]
        else:
            attr_value = HBNBCommand.__types[attr](value)

        object = storage.all()[key]
        setattr(object, attr, attr_value)
        object.save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
