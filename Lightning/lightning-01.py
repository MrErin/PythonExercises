# Write a function that takes a list, a number, and a string as args.
# The string parameter should have a default value.
# In the function body, loop over the list and output the items.
# Use slice to loop through only the first n items in the array, where n = the value of the second argument.
# Each item should be prefaced by value of the string argument
#   One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
# Try it out! Execute the function both with and without passing in a value for the string parameter


def lightning(list, num, str="This is the default "):
    sliceList = list[0:num]
    for item in sliceList:
        print(f'{str} {item}')


a_list = ["one", "two", "three", "four", "five"]
a_num = 3
lightning(a_list, a_num, 'wokka ')


# Joe's solution:
def print_cities(cities, num, str="I have visited the city of "):
    for city in cities[:num]:
        print(f'{str} {city}')


city_list = ["Corbin", "San Francisco", "Boston", "Austin", "Los Angeles"]

print_cities(city_list, 5, "I have spent time in this place: ")
print_cities(city_list, 1, "My mother grew up in ")


# Patrick's solution

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


def adder(string, list, num=4):
    for index, x in zip(range(num), list):
        print(string, x)


adder("I like the letter", letters, 5)
