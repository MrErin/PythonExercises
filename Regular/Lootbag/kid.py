class Kid():

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
        self.name = name
        self.is_nice = is_nice
        self.toys = set()
        self.delivered = False

    def add_toy(self, toy_name):
        self.toys.add(toy_name)

    def remove_toy(self, toy_name):
        self.toys.remove(toy_name)

    def toy_list(self):
        """Returns a formatted list of toys for this child"""
        return ",\n".join(self.toys)

    def deliver_all_toys(self):
        if self.delivered = False:
            self.delivered = True
            return f"All of {self.name}'s toys have been delivered!"
        else:
            return f"You already delivered {self.name}'s toys, you senile Santa!"
