#!/usr/bin/python3
"""HBNBCommand console interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines HBNBCommand console interpreter
    AttributeS:
           prompt (str): The command prompt
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the pogram"""
        return True

    def do_EOF(self):
        """EOF signal to exit the program"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
