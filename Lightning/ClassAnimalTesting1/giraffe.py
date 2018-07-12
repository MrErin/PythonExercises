# each animal needs to say "I am a ___ and my habitat is ___"

from animal import Animal
from savannahHabitat import Savannah


class Giraffe(Animal, Savannah):

    def __init__(self, sex='female', markings=0, name='Noname'):
        """Creates the class of Giraffe

        Arguments:
        sex: must be strings 'male' or 'female'. If other value is passed, defaults to female.
        markings: integer representing the number of giraffe splotchy markings.
        """
        Animal.size = "Bigger than a breadbox"
        Animal.food = "Leaves I think"
        Animal.legs = 4
        if sex == 'female':
            Animal.male = False
            Animal.female = True
        elif sex == 'male':
            Animal.male = True
            Animal.female = False
        else:
            if __name__ == '__main__':
                print(
                    f'Attempted to create new Giraffe with sex of {sex}. This giraffe has defaulted to female per the Animal class.')
            Animal.male = False
            Animal.female = True
        self.habitat = Savannah().my_name()
        self.num_of_splotches = markings
        self.name = name

    def __str__(self):
        return f'This is a giraffe named {self.name}. \n Properties:\nsize: {self.size}\nfood: {self.food}\nnumber of legs: {self.legs}\nis male: {self.male}\nis female: {self.female}\nhabitat: {self.habitat}\nnumber of splotchy bits: {str(self.num_of_splotches)}'


if __name__ == '__main__':
    Bingo = Giraffe('male', 47, 'Bingo')
    Pearl = Giraffe('female', 36, 'Pearl')
    Kit = Giraffe('nonconforming', 83, 'Kit')

    print(Bingo)
    print(Pearl)
    print(Kit)
