# Create a tuple named `zoo` that contains your favorite animals.
zoo = ('jackalope', 'griffin', 'manticore')

# Find one of your animals using the `.index(value)` method on the tuple.
print(zoo.index('manticore'))

# Determine if an animal is in your tuple


def is_fave(fave):
    if fave in zoo:
        print(f'The {fave} is my favorite animal and it\'s in the zoo!')
    else:
        print(f'The {fave} is my favorite animal but it\'s not in the zoo.')


is_fave('jackalope')
is_fave('unicorn')

# Create a variable for each of the animals in your tuple with this cool feature of Python.
# ! Google: tuple unpacking
(lizard, fox, mammoth) = zoo

# Will print the first element of the tuple
print(lizard)

# Convert your tuple into a list.
print(f'As tuple: {zoo}')
print(f'As list: {list(zoo)}')

# Use `extend()` to add three more animals to your zoo.
zoo_list = list(zoo)
zoo_list.extend(['troll', 'phoenix', 'chupacabra'])
print(zoo_list)

# Convert the list back into a tuple.
zoo = tuple(zoo_list)
print(zoo)
