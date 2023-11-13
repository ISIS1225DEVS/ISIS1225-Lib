""" Módulo con variables globales y funciones de comparación por defecto
    para uso por todo DISClib y sus ADTs.

    Este código y sus modificaciones para Python está basado en la
    implementación propuesta por los siguientes autores/libros:
        1) Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
        2) Data Structures and Algorithms in Python, Michael T. Goodrich,
            Roberto Tamassia y Michael H. Goldwasser.

Attributes:
    VALID_DATA_TYPE_LT (tuple): tupla con los tipos de datos nativos en Python
        que son comparables en los ADTs.
    DEFAULT_DICT_KEY (str): llave por defecto para comparar diccionarios en los
        ADTs.
    T (type): marca nativa de Python para definir un tipo de @dataclass
        genérico.
    VALID_IO_TYPE (tuple): tupla con los tipos de datos nativos en Python
        que son válidos para entrada y salida al inicializar un ADT.

Functions:
    - lt_default_cmp_funcion(): comparación por defecto para dos elementos
        en el ADT List (ArrayList, LinkedList, DoublyLinkedList).
    # TODO add documentation

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería, 2023
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
"""

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

# default key for comparing dictionaries
DEFAULT_DICT_KEY = "id"

# allowed input/output types for the ADTs
VALID_IO_TYPE = (
    list,
    tuple,
    set,
)

# Type for the element stored in the list
T = TypeVar("T")    # T can be any type


def lt_default_cmp_funcion(key, elm1, elm2) -> int:
    """lt_default_cmp_funcion función de comparación por defecto para
        los elementos del ADT List (ArrayList, LinkedList, DoublyLinkedList).
        pueden ser de tipo nativo o definido por el usuario.

    Args:
        key (str): llave para comparar los elementos de tipo diccionario.
        elm1 (any): primer elemento a comparar.
        elm2 (any): segundo elemento a comparar.

    Raises:
        TypeError: error de tipo de dato si los elementos de tipo nativo en
            Python no son comparables.
        KeyError: error de clave si la llave para comparar los diccionarios
            no existe.
        TypeError: error de tipo de dato si los elementos no son comparables.

    Returns:
        int: retorna -1 si elm1 es menor que elm2, 0 si son iguales y 1 si
    """
    # TODO add documentation
    elm1_type = isinstance(elm1, VALID_DATA_TYPE_LT)
    elm2_type = isinstance(elm2, VALID_DATA_TYPE_LT)
    # if the elements are from different types, raise an exception
    if type(elm1) is not type(elm2):
        err_msg = f"Invalid comparison between {type(elm1)} and "
        err_msg += f"{type(elm2)} elements"
        raise TypeError(err_msg)
    # if there is a defined key
    elif key is not None:
        # if elements are dictionaries, compare their main key
        if isinstance(elm1, dict) and isinstance(elm2, dict):
            key1 = elm1.get(DEFAULT_DICT_KEY)
            key2 = elm2.get(DEFAULT_DICT_KEY)
            if None in [key1, key2]:
                err_msg = f"Invalid key: {DEFAULT_DICT_KEY}, "
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
