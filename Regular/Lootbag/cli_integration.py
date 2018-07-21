import sys
from lootbag import Lootbag
from kid import Kid


Blue_Bag = Lootbag('blue')
Candace = Kid('candace', 1)
Derek = Kid('derek', 0)
Blue_Bag.kids.add(Candace)
Blue_Bag.kids.add(Derek)

# Requirements
# 1. Add a toy: (3 args): the word "add", the name of the gift, the name of the child (lootbag.py add kite suzy)
# remove suzy kite
# list children currently receiving presents (using the ls command)
# list all toys for a specific child (ls suzy)
# mark all of a child's toys delivered (delivered suzy)


if len(sys.argv) > 1 and sys.argv[1] == "add":
    # add kite suzy
    for k in Blue_Bag.kids:
        if (sys.argv[3]).capitalize() == k.name:
            k.add_toy(sys.argv[2])
            k.toy_list()
elif sys.argv[1] == "remove":
    # remove suzy kite
    for k in Blue_Bag.kids:
        if (sys.argv[2]) == k.name:
            k.remove_toy(sys.argv[3])


# remove suzy kite

# list children currently receiving presents (using the ls command)

# list all toys for a specific child (ls suzy)

# mark all of a child's toys delivered (delivered suzy)
