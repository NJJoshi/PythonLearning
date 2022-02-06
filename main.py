# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import os.path


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # This is my path
    path = "C://NJ//Learning//Python//python-practice-examples"

    # to store files in a list
    list = []

    for (root, dirs, file) in os.walk(path):
        for f in file:
            if os.path.isfile('./*.ipynb') == True:
                print(f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
