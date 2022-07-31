"""
Utilites for transforming Python dictionaries returned when loading json or yaml.
"""
from collections import namedtuple


def nested_dict_to_namedtuple(src_dict: dict) -> namedtuple:
    """Turns the provided dictionary, potentially with nested dictionaries
    into a named tuple. Providing for the use of dot notation when accessing
    the new object.

    Args:
        src_dict (dict): Python dictionary to be converted.

    Returns:
        namedtuple: New object containing the data from the
        provided dictionary.
    """
    recursed_dict: dict = {}
    for key, value in src_dict.items():
        if isinstance(value, dict):
            recursed_dict[key] = nested_dict_to_namedtuple(value)
        else:
            recursed_dict[key] = value
    return namedtuple('tuple',
                        recursed_dict.keys())(*recursed_dict.values())


# https://realpython.com/python-metaclasses/#defining-a-class-dynamically
# https://www.freecodecamp.org/news/dynamic-class-definition-in-python-3e6f7d20a381/
# https://www.geeksforgeeks.org/create-classes-dynamically-in-python/


# def nested_dict_to_dynamic_class_instance(src_dict: dict) -> object:
#     """Returns a class structured according to the supplied hierarchical data.
#       With some base functionality included.
#     """

# Syntax:
#     type(name, bases, attributes)
# Parameters:
#     name: The user defined name of the class
#     bases: A list of base classes, and its type is tuple
#     attributes: the data members and methods contained in the class


# E.G. program to create class dynamically

# # constructor
# def constructor(self, arg):
# 	self.constructor_arg = arg

# # method
# def displayMethod(self, arg):
# 	print(arg)

# # class method
# @classmethod
# def classMethod(cls, arg):
# 	print(arg)

# # creating class dynamically
# Geeks = type("Geeks", (object, ), {
# 	# constructor
# 	"__init__": constructor,

# 	# data members
# 	"string_attribute": "Geeks 4 geeks !",
# 	"int_attribute": 1706256,

# 	# member functions
# 	"func_arg": displayMethod,
# 	"class_func": classMethod
# })



# # creating objects for example
# obj = Geeks("constructor argument")
# print(obj.constructor_arg)
# print(obj.string_attribute)
# print(obj.int_attribute)
# obj.func_arg("Geeks for Geeks")
# Geeks.class_func("Class Dynamically Created !")
