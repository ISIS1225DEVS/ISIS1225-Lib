"""
Este módulo implementa el tipo abstracto de datos (TAD) lista. Dinámicamente se puede implementar sobre una estructura de datos sea encadenada de forma sencilla (SingleLinked), doble (DoubleLinked) o como un arreglo dinámico (ArrayList).

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# custom modules
# node class for the linked list
from .dynamic import DynamicImporter
from .dynamic import STRUCT_PGK_PATH

# generic error handling and type checking
from Src.DISClib.Utils.default import T

# checking costum modules and functions
assert DynamicImporter
assert T


# posible implementations for the ADT
# :param ADT_LT_MOD_DICT
ADT_LT_MOD_DICT: dict = {
    "ArrayList": "arraylist",
    "SingleLinked": "singlelinkedlist",
    "DoubleLinked": "doublelinkedlist",
}
"""
Referencia a los posibles módulos de implementación del ADT List. Pueden ser "ArrayList", "SingleLinked" o "DoubleLinked".
"""


def List(dstruct: str = "ArrayList", **kwargs) -> T:
    """*List()* Función dinámica que que retorna una instancia del ADT List según el tipo de estructura de datos seleccionada por el usuario.

    Args:
        dstruct (str, optional): Tipo de estructura de datos a instanciar. Por defecto es "ArrayList". Puende ser "ArrayList", "SingleLinked" o "DoubleLinked".

    Raises:
        ValueError: error si el tipo de estructura de datos seleccionada no es válida.

    Returns:
        T: instancia del ADT List que puede ser "ArrayList", "SingleLinked" o "DoubleLinked".
    """
    try:
        package = f"{STRUCT_PGK_PATH}."
        package += f"{ADT_LT_MOD_DICT.get(dstruct)}"
        adt_list = DynamicImporter(dstruct, package, **kwargs)
        adt_instance = adt_list.get_instance()
        return adt_instance
    except Exception as exp:
        err_msg = f"'{dstruct}' List type not found"
        err_msg += f" in {STRUCT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)


def clone_lt(og_lt: T) -> T:
    """*clone()* copia una instancia del ADT List con una estructura de datos seleccionada.

    Args:
        og_lt (T): instancia del ADT *List* a copiar.

    Returns:
        T: copia independiente de la instancia del ADT *List*.
    """
    try:
        og_dstruct = type(og_lt).__name__
        cl_lt = List(dstruct=og_dstruct,
                     cmp_function=og_lt.cmp_function,
                     key=og_lt.key)
        for data in og_lt:
            cl_lt.add_last(data)
        return cl_lt
    except Exception as exp:
        og_dstruct = type(og_lt).__name__
        err_msg = f"Unable to clone List, '{og_dstruct}' type not found"
        err_msg += f" in {STRUCT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)


def translate_lt(src_lt: T, tgt_dstruct: str = "SingleLinked") -> T:
    """*translate()* Transforma una instancia del ADT List con una estructura de datos seleccionada en otra instancia del ADT List con otra estructura de datos seleccionada.

    Args:
        src_lt (T): instancia del ADT List a transformar.
        tgt_dstruct (str, optional): Tipo de estructura de datos objetivo a instanciar. Por defecto es "SingleLinked". Puenden ser "ArrayList", "SingleLinked" o "DoubleLinked".

    Raises:
        ValueError: error si el tipo de estructura de datos no es válido.

    Returns:
        T: instancia del ADT List que puede ser "ArrayList", "SingleLinked" o "DoubleLinked".
    """
    # TODO add Queue and Stack to the ADT explicit allowed types
    try:
        src_dstruct = type(src_lt).__name__
        tgt_lt = List(dstruct=tgt_dstruct,
                      cmp_function=src_lt.cmp_function,
                      key=src_lt.key)
        for elm in src_lt:
            tgt_lt.add_last(elm)
        return tgt_lt
    except Exception as exp:
        err_msg = f"Unable to translate List '{src_dstruct}', "
        err_msg += f"'{tgt_dstruct}' List type not found"
        err_msg += f" in {STRUCT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)
