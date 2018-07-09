# Create a Dog class that:
# 1) Inherits from Animal
# 2) Has its own prop of "breed"
# 3) initializes the Animal class with'species', 'leg_num' and 'domesticated' attributes

from animal import Animal


class Dog(Animal):
    '''Describes a domesticated dog'''

    def __init__(self, breed="mutt"):
        self.breed = breed
        Animal.leg_num = 4
        Animal.domesticated = True
        Animal.species = "canid"
        Animal.say_something

    def __str__(self):
        return f'This is a {Animal.species} of the breed {self.breed} with {Animal.leg_num} legs.'


if __name__ == '__main__':
    new_dog = Dog()
    print(new_dog)
    print('This animal says ', new_dog.say_something())
