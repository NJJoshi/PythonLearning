from log.AppLogging import ApplicationLogging
import pyinputplus as pypi

log_obj = ApplicationLogging()


class WordFrequencyCounter:

    def __init__(self, statement):
        self.statement = statement

    def count_frequency_of_words(self, split_by=" "):
        my_str = self.statement
        split_str = my_str.split(split_by)
        result = {}
        for i in split_str:
            if result.get(i) is None:
                result[i] = my_str.count(i)
        return result


def main():
    my_input_str = pypi.inputStr(prompt='Please enter string', default="")
    log_file = open('word_count.log', 'w')
    if len(my_input_str) > 0:
        word_count = WordFrequencyCounter(my_input_str)
        result = word_count.count_frequency_of_words()
        log_obj.log_info(log_file, 'Final result:'+ str(result))
    else:
        log_obj.log_info(log_file, 'Please provide some string input for word frequency count')

    return None


main()
