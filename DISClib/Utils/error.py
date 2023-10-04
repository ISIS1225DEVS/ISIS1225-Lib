""" _summary_
# TODO add summary

Attributes:
    T (type): _description_
    TYPE_ERR_MSG (str): _description_
    VALID_DATA_TYPE_LT (tuple): _description_

Functions:
    error_handler(context: str, func_name: str, err: Exception) -> None:
        error_handler receives the context, function name and error to raise.
    init_type_checker(context: str, func_name: str, info: T) -> None:
        init_type_checker receives the context, function name and info to check
            its type after class initialization.

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería, 2023
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
"""

# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import TypeVar


# Type for the element stored at the node
T = TypeVar("T")    # T can be any type


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

# generic error message for invalid data type
TYPE_ERR_MSG = "Invalid data type"


def error_handler(context: str,
                  func_name: str,
                  err: Exception) -> None:
    """error_handler receives the context, function name and error to raise.

    Args:
        context (str): name of the class where the error occurred.
        func_name (str): name of the function where the error occurred.
        err (Exception): exception raised.

    Raises:
        type: exception with the error message and traceback.
    """
    err_msg = f"Error in {context}.{func_name}: {err}"
    raise type(err)(err_msg).with_traceback(err.__traceback__)


def init_type_checker(context: str,
                      func_name: str,
                      info: T) -> None:
    """init_type_checker receives the context, function name and info to check
        its type after class initialization.

    Args:
        context (str): name of the class where the check is performed.
        func_name (str): name of the function where the check is performed.
        info (T): info to check its type.

    Raises:
        TypeError: exception with the type error message.
    """
    if not isinstance(info, VALID_DATA_TYPE_LT):
        err_msg = f"Error in {context}.{func_name}: {TYPE_ERR_MSG}"
        raise TypeError(err_msg)
