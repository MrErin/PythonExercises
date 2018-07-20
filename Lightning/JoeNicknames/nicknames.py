# Allows us to use CLI with this file
import sys

# Allows us to work with external files
import os

# Random generators

from random import randint

# data for our files
nickset = {"The Mooch", "Knuckles", "Burninator", "Kneecap", "Ole Red", "Bubba",
           "OG", "KitKat", "Spanky", "Monkeybutt", "L`il Devil", "Bird Person", "Fancy Slacks"}

nameset = {"Bob Smith", "Charise Anderson", "Jissie David", "Henry Goldberg", "Greg Korte", "Steve Brownlee",
           "Kimmy Bird", "Joe Shepherd", "Emily Lemmon", "Brenda Long", "Harold Brown", "Megan Ducharme", "Darth Vader"}

# set up the relative paths for this project:
here = os.path.dirname(os.path.realpath(__file__))
nickset_file = "nickset.txt"
nameset_file = "nameset.txt"
nickset_filepath = os.path.join(here, nickset_file)
nameset_filepath = os.path.join(here, nameset_file)

try:
    i = open(nickset_filepath, "w")
    i.close()
except IOError:
    print("wrong path provided")

try:
    a = open(nameset_filepath, "w")
    a.close()
except IOError:
    print("wrong path provided")

with open(nickset_filepath, "a") as nicknames:

    # This part will only run the first time. It creates/populates the files on the initial load.
    if os.path.getsize(nickset_filepath) == 0:
        print("File is empty", os.path.getsize(nickset_filepath))
        for nick in nickset:
            nicknames.write(nick + '\n')

with open(nameset_filepath, 'w') as names:
    for name in nameset:
        names.write(name + '\n')


class NameFactory():
    """Smooshes together the names and nicknames, mob style: FirstName "Nickname" LastName"""

    # You need to use @staticmethod if you want to call a function inside a class without instantiating it. At the end of this file, we run the methods from the class directly.
    # We do it this way for two reasons: 1.) telling Python that we aren't passing self into the method will save some amount of processing work and 2.) it is a signal to the developer that this is a helper function, not something that will typically be called on its own.

    @staticmethod
    # The leading underscore in the method name indicates it's a private method, which means it generally won't be called from outside its class.
    def _get_nicknames():
        """returns a set of nicknames read from a text file"""

        with open(nickset_filepath, "r") as nicknames:

            # readlines creates a list of each line
            return nicknames.readlines()

    @staticmethod
    def _get_names():
        """returns a set of names read from a text file"""

        with open(nameset_filepath, "r") as names:
            return names.readlines()

    def assign_nicknames(self):
        """randomly pairs a nickname with a name. outputs as list"""

        names = self._get_names()
        nicknames = self._get_nicknames()

        return[f"{name.strip().split(' ')[0]} \"{nicknames[randint(0, len(nicknames)-1)].strip()}\" {name.strip().split(' ')[1]}" for name in names]

    def add_nick(self, new_nick):
        """allows user to save a new nickname to the existing collection.
        Parameters: 

        new_nick(str): a nickname passed from the command line
        """

        print("new_nick", new_nick)

        with open(nickset_filepath, "a") as nickfile:
            nickfile.write(new_nick + '\n')


if __name__ == '__main__':
    name_maker = NameFactory()

    # You have to check for the argument this way to make sure it doesn't error out (that's the first if) and the sys.argv[1] argument is not a static list, it's just the next thing you pass after writing the filename.
    # python nicknames.py add_nick "heloise"
    # In the above example, "nicknames.py" is sysargv[0]
    # "add_nick" is sysargv[1]
    # "heloise" is sysargv[2]

    # If there is a sysargv[1] and that arg is "add_nick"...
    if len(sys.argv) > 1 and sys.argv[1] == "add_nick":
        # run this method, passing in sysargv[2]
        name_maker.add_nick(sys.argv[2])
        print("New nickname added. Thanks.")
    else:
        print(name_maker.assign_nicknames())
    # * To use CLI:
    # * cd into the directory
    # * To print the list of mob names: "python nicknames.py name_maker"
    # * To add a new name to the list: "python nicknames.py add_nick '[new nickname]'"
