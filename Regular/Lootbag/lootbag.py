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
        """Returns the list of deliveries by child"""
        print("----- Delivery List -----")
        for k in self.kids:
            if k.is_nice == True and k.toys and k.delivered == False:
                print(k.toy_list())
            if k.is_nice == False and k.delivered == False:
                print(f"*** {k.name}'s Toy List ***")
                print('Coal')

    def __str__(self):
        return f"This bag is colored {self.color}."


if __name__ == '__main__':
    Blue_Bag = Lootbag('blue')
    Amy = Kid('amy', 1)
    Bruce = Kid('bruce', 0)
    Blue_Bag.kids.add(Amy)
    Blue_Bag.kids.add(Bruce)
    Amy.add_toy('bike')
    Amy.add_toy('sailboat')
    Amy.add_toy('ball')

    print(Blue_Bag)
    Blue_Bag.kid_list()
    Blue_Bag.delivery_list()
    Amy.deliver_all_toys()
    Bruce.deliver_all_toys()
    Amy.deliver_all_toys()
    Bruce.deliver_all_toys()
