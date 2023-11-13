""" Módulo con funciones para manejo de errores genericas para
    todo DISClib.

    Este código y sus modificaciones para Python está basado en la
    implementación propuesta por los siguientes autores/libros:
        1) Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
        2) Data Structures and Algorithms in Python, Michael T. Goodrich,
            Roberto Tamassia y Michael H. Goldwasser.

Attributes:
    T (type): marca nativa de Python para definir un tipo de @dataclass
        genérico.
    TYPE_ERR_MSG (str): mensaje de error para tipo de dato inválido.
    VALID_DATA_TYPE_LT (tuple): tupla con los tipos de datos nativos en Python
        que son comparables en los ADTs.

Functions:
    - error_handler(): manejo de errores genérico.
    - init_type_checker(): chequeo de tipo de dato genérico al inicializar
        un ADT.
    # TODO add documentation

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería, 2023
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
"""
# native python modules
# import typing for defining the type of the elements
# from typing import TypeVar

# custom modules
# import global variables
from DISClib.Utils.default import VALID_DATA_TYPE_LT
from DISClib.Utils.default import T


# generic error message for invalid data type
TYPE_ERR_MSG = "Invalid data type"


def error_handler(context: str,
                  func_name: str,
                  err: Exception) -> None:
    """error_handler receives the context, function name and error to raise
    inside an specific module or class.

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
