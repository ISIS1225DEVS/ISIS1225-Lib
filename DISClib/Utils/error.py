"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import TypeVar      # , Generic, Optional


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
