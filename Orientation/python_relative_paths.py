import os

# This file will create a new directory in this script's directory. The new directory will be called "subdir" and the file created inside it will be "myfile.txt"

# get the current script path.
here = os.path.dirname(os.path.realpath(__file__))
subdir = "subdir"
filename = "myfile.txt"
filepath = os.path.join(here, subdir, filename)

# create your subdirectory
os.mkdir(os.path.join(here, subdir))

# create an empty file.
try:
    f = open(filepath, 'w')
    f.close()
except IOError:
    print("Wrong path provided")
