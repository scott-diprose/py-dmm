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
