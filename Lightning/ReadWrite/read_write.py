# permissions:
# r: read only
# w: write only
# If you use this on a non-empty file, it will be overwritten
# a: append
# If you use this on a non-empty file, it will be added to the bottom
# r+: read and write

# Note: if running this in VS Code it will drop the new file in the relative root directory. You may need to specify the file path in python, which is a huge pain in the ass.

with open("read_write.txt", "w") as my_file:
    my_file.write("Hello C25!!.")
