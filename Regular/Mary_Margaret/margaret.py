import sys
import pickle
import os


class Margaret:

    def write_message_to_file(self, message):
        here = os.path.dirname(os.path.realpath(__file__))
        filename = "mary_margaret_file.txt"
        filepath = os.path.join(here, filename)

        try:
            with open(filepath, 'a') as something:
                something.write(f'Margaret: {message}\n')
        except IOError:
            print("Wrong path provided")


if __name__ == '__main__':
    my_Margaret = Margaret()
    my_Margaret.write_message_to_file('Hellow')
    my_Margaret.write_message_to_file('Hellow you')
    my_Margaret.write_message_to_file('Hellow how is you')
