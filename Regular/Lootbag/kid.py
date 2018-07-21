class Kid:

    def __init__(self, name=None, is_nice=True):
        """Creates a new kid for the loot bag

        Keyword Arguments:
            name {str}: child's name (default: None)
            is_nice bool -- can be False ("naughty") or True ("nice") (default: {True})
        Attributes:
            name
            is_nice
            toys: set of toys assigned to child
            delivered: can be True or False (default: False)
        """
        self.name = name.capitalize()
        self.is_nice = is_nice
        self.toys = set()
        self.delivered = False

    def add_toy(self, toy_name):
        """Adds the toy_name to the child's list"""
        self.toys.add(toy_name)
        print(f"{toy_name} added to {self.name}'s toy list.")

    def remove_toy(self, toy_name):
        """Removes the toy_name from the child's list"""
        self.toys.remove(toy_name)
        print(f"{toy_name} removed from {self.name}'s toy list.")

    def toy_list(self):
        """Returns a formatted list of toys for this child"""
        print(f"*** {self.name}'s Toy List ***")
        return("\n".join(t.capitalize() for t in self.toys))

    def deliver_all_toys(self):
        """Marks all toys delivered for this child"""
        if self.delivered == False and self.is_nice == True:
            self.delivered = True
            print(f"All of {self.name}'s toys have been delivered!")
        elif self.delivered == False and self.is_nice == False:
            self.delivered = True
            print(f"Delivered coal to that brat, {self.name}.")
        else:
            print(f"You already delivered {self.name}'s toys, you senile Santa!")
