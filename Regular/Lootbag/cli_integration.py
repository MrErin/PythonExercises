import sys
from lootbag import Lootbag
from kid import Kid


Yellow_Bag = Lootbag('yellow')
Candace = Kid('candace', 1)
Derek = Kid('derek', 0)
Yellow_Bag.kids.add(Candace)
Yellow_Bag.kids.add(Derek)
Candace.add_toy('crayons')


# Requirements
# 1. Add a toy: (3 args): the word "add", the name of the gift, the name of the child (lootbag.py add kite suzy)
# remove suzy kite
# list children currently receiving presents (using the ls command)
# list all toys for a specific child (ls suzy)
# mark all of a child's toys delivered (delivered suzy)


if len(sys.argv) > 1 and sys.argv[1] == "add":
    # add kite suzy
    # !This looks like it works, but it doesn't. Can't figure out why. It says the toy is added to the list, but printing the list shows that it isn't added. Unit testing shows that the toy DOES get added so IDFK.
    for k in Yellow_Bag.kids:
        if (sys.argv[3]).capitalize() == k.name:
            k.add_toy(sys.argv[2])
            k.toy_list()
elif len(sys.argv) > 1 and sys.argv[1] == "remove":
    # remove suzy kite
    # !Because the add command doesn't work, this one doesn't work. You can't remove a toy if it isn't in there in the first place.
    for k in Yellow_Bag.kids:
        if (sys.argv[2]) == k.name:
            k.remove_toy(sys.argv[3])
elif len(sys.argv) == 2 and sys.argv[1] == "ls":
    # list children currently receiving presents (using the ls command)
    Yellow_Bag.kid_list()
elif len(sys.argv) > 1 and sys.argv[1] == "ls":
    # list all toys for a specific child (ls suzy)
    for k in Yellow_Bag.kids:
        if (sys.argv[2]) == k.name:
            k.toy_list()
elif len(sys.argv) > 1 and sys.argv[1] == "delivered":
    # mark all of a child's toys delivered (delivered suzy)
    for k in Yellow_Bag.kids:
        if (sys.argv[2]) == k.name:
            k.deliver_all_toys()
