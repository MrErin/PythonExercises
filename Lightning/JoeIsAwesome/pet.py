# 1) Give a pet its own prop of name
# 2) Give it a property of animal_type
# 3) animal_type needs to be an instance of a dog
# 4) assign an owner via a method
# 5) __str__ return a string with pet's name, # of legs, and what it says


class Pet():
    '''Describes a pet'''

    def __init__(self, name, critter_instance):
        self.name = name
        self.animal_type = critter_instance

    def assign_owner(self, owner_name):
        self.owner = owner_name

    def __str__(self):
        return f'The pet\'s name is {self.name}. It has {self.animal_type.leg_num} legs. It says, {self.animal_type.say_something()}. Its owner is {self.owner}. Its breed is {self.animal_type.breed}.'
