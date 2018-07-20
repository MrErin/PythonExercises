import sys

from kid import Kid

# Requirements
# 1. Add a toy: (3 args): the word "add", the name of the gift, the name of the child (lootbag.py add kite suzy)
# remove suzy kite
# list children currently receiving presents (using the ls command)
# list all toys for a specific child (ls suzy)
# mark all of a child's toys delivered (delivered suzy)


class Lootbag:

    def __init__(self, color='green'):
        """Creates a loot bag of the specified color.

        Keyword Arguments:
            color {str} -- Bag color (default: {'green'})
        """
        self.color = color
        self.kids = set()

    def kid_list(self):
        """Returns the list of kids"""
        print("----- Kid List -----")
        for k in self.kids:
            print("{} ({behavior})".format(
                (k.name), behavior="nice" if k.is_nice == True else "naughty"))

    def delivery_list(self):
        """Returns the list of kids who WILL receive toys"""
        print("----- Delivery List -----")
        for k in self.kids:
            if k.is_nice == True and k.toys and k.delivered == False:
                print(f"{k.name}:\n")
                print(k.toy_list())

    def __str__(self):
        return f"This bag is colored {self.color}."


if __name__ == '__main__':
    Blue_Bag = Lootbag('blue')
    Amy = Kid('Amy', 1)
    Bruce = Kid('Bruce', 0)
    Blue_Bag.kids.add(Amy)
    Blue_Bag.kids.add(Bruce)
    # Amy.add_toy('bike')
    # Amy.add_toy('sailboat')
    # Amy.add_toy('ball')
    # Bruce.add_toy('coal')

    # print(Blue_Bag)
    # Blue_Bag.kid_list()
    # Blue_Bag.delivery_list()

    if len(sys.argv) > 1 and sys.argv[1] == "add":
        # add kite suzy
        for b in Blue_Bag.kids:
            if (sys.argv[3]) == b.name:
                b.add_toy(sys.argv[2])
                b.toy_list()
            else:
                print('That child is not on the list')

# remove suzy kite

# list children currently receiving presents (using the ls command)

# list all toys for a specific child (ls suzy)

# mark all of a child's toys delivered (delivered suzy)
