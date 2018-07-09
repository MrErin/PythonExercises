# Using the `random` module and the `range` method, generate a list of 20 random numbers between 0 and 49.
# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is `[2, 5]`, the final list will be `[4, 25]`.

import random

random_numbers = [random.randint(0, 49) for x in range(20)]
print(random_numbers)

random_squared = [x * x for x in random_numbers]
print(random_squared)
