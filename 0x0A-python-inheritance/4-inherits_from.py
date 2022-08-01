#!/usr/bin/python3
"""
Contians the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(tyhpe(obj), a_class) and type(obj) != a_class)
