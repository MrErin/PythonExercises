# Note: if running this in VSCode, need to reopen VSCode in folder "ReadWriteCars"


class BuildCars():

    def create_dictionary(self):
        # rstrip removes the newline character from the text files
        car_makes = [line.rstrip() for line in open('car-makes.txt')]
        print(car_makes)
        car_models = [line.rstrip() for line in open('car-models.txt')]

        car_dictionary = dict()

        for make in car_makes:
            for model in car_models:
                if make[0] == model[0]:
                    if make in car_dictionary:
                        car_dictionary[make].append(model[2:])
                    else:
                        car_dictionary[make] = [model[2:]]
        print(car_dictionary)


if __name__ == '__main__':
    BuildCars().create_dictionary()
