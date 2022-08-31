#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a _dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

            return (a_dictionary)
