import pyinputplus as pypi


class CustomGenerator:

    def __init__(self, iteration):
        self.iteration = iteration

    def my_generator(self):
        for i in range(self.iteration):
            if i % 2 == 0:
                yield i


def main():
    no_of_iteration = pypi.inputInt(prompt='Please enter number:', default=0)
    custom_generator = CustomGenerator(no_of_iteration)
    result_list = list(custom_generator.my_generator())
    print(result_list)


main()
