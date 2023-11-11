# python native modules
# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the node
from typing import TypeVar

# valid data types for the node
VALID_DATA_TYPE_LT = (
    int,
    float,
    str,
    bool,
    dict,
    list,
    tuple,
    set,
    dataclass,
)

# Type for the element stored in the list
T = TypeVar("T")    # T can be any type


def lt_default_cmp_funcion(self, elm1, elm2) -> int:
    """lt_default_cmp_funcion _summary_

    Args:
        elm1 (_type_): _description_
        elm2 (_type_): _description_

    Raises:
        TypeError: _description_
        KeyError: _description_
        TypeError: _description_

    Returns:
        int: _description_
    """
    # TODO add documentation
    elm1_type = isinstance(elm1, VALID_DATA_TYPE_LT)
    elm2_type = isinstance(elm2, VALID_DATA_TYPE_LT)
    # none_type = (self.key is None)
    # if the elements are from different types, raise an exception
    if type(elm1) is not type(elm2):
        err_msg = f"Invalid comparison between {type(elm1)} and "
        err_msg += f"{type(elm2)} elements"
        raise TypeError(err_msg)
    # if there is a defined key
    elif self.key is not None:
        # if elements are dictionaries, compare their main key
        if isinstance(elm1, dict) and isinstance(elm2, dict):
            key1 = elm1.get(self.key)
            key2 = elm2.get(self.key)
            if None in [key1, key2]:
                err_msg = f"Invalid key: {self.key}, "
                err_msg += "Key not found in one or both elements"
                raise KeyError(err_msg)
            # comparing elements
            else:
                # if one is less than the other, return -1
                if key1 < key2:
                    return -1
                # if they are equal, return 0
                elif key1 == key2:
                    return 0
                # if one is greater than the other, return 1
                elif key1 > key2:
                    return 1
                # otherwise, raise an exception
                else:
                    err_msg = f"Invalid comparison between {key1} and "
                    err_msg += f"{key2} keys in elements."
                    raise TypeError(err_msg)
        # if elements are native types, compare them directly
        elif elm1_type and elm2_type:
            # if one is less than the other, return -1
            if elm1 < elm2:
                return -1
            # if one is greater than the other, return 1
            elif elm1 > elm2:
                return 1
            # otherwise, they are equal, return 0
            else:
                return 0
