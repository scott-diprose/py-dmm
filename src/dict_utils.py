from collections import namedtuple

def nested_dict_to_namedtuple(src_dict: dict) -> namedtuple:
    """_summary_

    Args:
        src_dict (dict): _description_

    Returns:
        namedtuple: _description_
    """
    recursed_dict: dict = {}
    for key, value in src_dict.items():
        if isinstance(value, dict):
            recursed_dict[key] = nested_dict_to_namedtuple(value)
        else:
            recursed_dict[key] = value
    return namedtuple('tuple',
                        recursed_dict.keys())(*recursed_dict.values())
