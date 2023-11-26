"""
Módulo para manejar errores genéricos en los ADTs y todo *DISCLib*.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# native python modules
# import typing for defining the type of the elements
# from typing import TypeVar

# custom modules
# import global variables
from DISClib.Utils.default import VALID_DATA_TYPE_LT
from DISClib.Utils.default import T

# error msg for invalid data type
# :data: TYPE_ERR_MSG
TYPE_ERR_MSG: str = "Invalid data type"
"""
Contiene el mensaje de error para tipo de dato inválido.
"""


def error_handler(context: str,
                  func_name: str,
                  err: Exception) -> None:
    """*error_handler()* recibe el contexto, nombre de la función y la excepción para lanzar una excepción con el mensaje de error y el traceback.

    Args:
        context (str): nombre del contexto donde ocurrió el error.
        func_name (str): nombre de la función donde ocurrió el error.
        err (Exception): excepción lanzada.

    Raises:
        type: excepción con el mensaje de error y el traceback.
    """
    err_msg = f"Error in {context}.{func_name}: {err}"
    raise type(err)(err_msg).with_traceback(err.__traceback__)


def init_type_checker(context: str,
                      func_name: str,
                      info: T) -> None:
    """*init_type_checker()* recibe el contexto, nombre de la función y la info
    para verificar su tipo después de la inicialización de la clase.

    Args:
        context (str): nombre del contexto donde ocurrió el error.
        func_name (str): nombre de la función donde ocurrió el error.
        info (T): tipo de dato de la información a verificar.

    Raises:
        TypeError: excepción con el mensaje de error de tipo de dato.
    """
    if not isinstance(info, VALID_DATA_TYPE_LT):
        err_msg = f"Error in {context}.{func_name}: {TYPE_ERR_MSG}"
        raise TypeError(err_msg)
