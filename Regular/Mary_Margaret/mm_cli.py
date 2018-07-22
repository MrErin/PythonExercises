import sys
import os

here = os.path.dirname(os.path.realpath(__file__))
filename = "mary_margaret_file.txt"
filepath = os.path.join(here, filename)

try:
    with open(filepath, 'a') as something:
        something.write(f'Margaret: {message}\n')
except IOError:
    print("Wrong path provided")
