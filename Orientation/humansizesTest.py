# This imports the code in humansizes for use in this file.

import humansizes
print(humansizes.approximate_size(80808080, True))

# humansizes's __name__ dunderscore function was "main" in its own file. When it's imported, its name becomes its filename
print(humansizes.__name__)

# This prints the developer's documentation (the part in triple quotes) for the given function
print(humansizes.approximate_size.__doc__)
