""" Este módulo implementa el tipo abstracto de datos (TAD) lista.
    Dinámicamente se puede implementar sobre una estructura de datos
    sea encadenada de forma sencilla (SingleLinked), doble (DoubleLinked)
    o como un arreglo dinámico (ArrayList).

    Este código y sus modificaciones para Python está basado en la
    implementación propuesta por los siguientes autores/libros:
        1) Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
        2) Data Structures and Algorithms in Python, Michael T. Goodrich,
            Roberto Tamassia y Michael H. Goldwasser.

Attributes:
    T (type): variable que representa el tipo de dato de los elementos
        contenidos en el ADT List.
    ADT_LT_PGK_PATH (str): ruta del paquete principal del ADT List.
    ADT_LT_MOD_DICT (dict): diccionario que contiene los posibles
        módulos de implementación del ADT List.

Functions:
    - List(): función con patrón de diseño factory que retorna una
        instancia del ADT List según el tipo de estructura de datos
        seleccionada.
    - transform(): función que transforma una instancia del ADT List
        en otra instancia del ADT List con una estructura de datos
        seleccionada.

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería,
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
"""
# native python modules
# import importlib

# custom modules
# node class for the linked list
from .dynamic import DynamicImporter

# generic error handling and type checking
from DISClib.Utils.default import T

# checking costum modules and functions
assert DynamicImporter
assert T

# main package data structure path
ADT_LT_PGK_PATH = "DISClib.DataStructures"

# posible implementations for the ADT
ADT_LT_MOD_DICT = {
    "ArrayList": "arraylist",
    "SingleLinked": "singlelinkedlist",
    "DoubleLinked": "doublelinkedlist",
}


# TODO is this really factory pattern?
def List(dstruct: str = "ArrayList", **kwargs) -> T:
    """List Función con patrón de diseño factory que retorna una
        instancia del ADT List según el tipo de estructura de datos
        seleccionada.

    Args:
        dstruct (str, optional): Tipo de estructura de datos a instanciar.
        Por defecto es "ArrayList". Puenden ser "ArrayList", "SingleLinked"
        o "DoubleLinked".

    Raises:
        ValueError: error si el tipo de estructura de datos no es válido.

    Returns:
        T: instancia del ADT List que puede ser "ArrayList", "SingleLinked"
        o "DoubleLinked".
    """
    try:
        package = f"{ADT_LT_PGK_PATH}."
        package += f"{ADT_LT_MOD_DICT.get(dstruct)}"
        adt_list = DynamicImporter(dstruct, package, **kwargs)
        adt_instance = adt_list.start()
        return adt_instance
    except Exception as exp:
        # raise ValueError("Invalid list type: " + str(exp))
        err_msg = f"List type '{dstruct}' not found"
        err_msg += f" in {ADT_LT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)


def transform(src_lt: T, tgt_dstruct: str = "SingleLinked") -> T:
    """transform Transforma una instancia del ADT List en otra instancia
        del ADT List con una estructura de datos seleccionada.

    Args:
        src_lt (T): instancia del ADT List a transformar.
        tgt_dstruct (str, optional): Tipo de estructura de datos objetivo
        a instanciar. Por defecto es "SingleLinked". Puenden ser
        "ArrayList", "SingleLinked" o "DoubleLinked".

    Raises:
        ValueError: error si el tipo de estructura de datos no es válido.

    Returns:
        T: instancia del ADT List que puede ser "ArrayList", "SingleLinked"
        o "DoubleLinked".
    """
    try:
        tgt_lt = List(dstruct=tgt_dstruct)
        for elm in src_lt:
            tgt_lt.add_last(elm)
        tgt_lt.cmp_function = src_lt.cmp_function
        tgt_lt.key = src_lt.key
        return tgt_lt
    except Exception as exp:
        err_msg = f"List type '{tgt_dstruct}' not found"
        err_msg += f" in {ADT_LT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)


