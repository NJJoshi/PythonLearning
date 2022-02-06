from bisect import bisect_left


def binary_search(element_list, search_element):
    element_index = bisect_left(element_list, search_element)
    if element_index != len(element_list) and element_list[element_index] == search_element:
        return element_index
    else:
        return -1


def main():
    elements_list = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 0]
    search_element = 6
    index = binary_search(elements_list, search_element)
    if index == -1:
        print(search_element + " is absent")
    else:
        print('Very first occurrence of ', search_element , ' is present at index ', index)


main()
