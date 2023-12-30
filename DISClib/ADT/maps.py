"""
Este módulo implementa el tipo abstracto de datos (TAD) Map sin orden. Se puede implementar sobre una estructura de datos Hash Table, con resolución de colisiones por sondeo lineal (Linear Probing) o encadenamiento por separado (Separate Chaining).

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
import copy

# custom modules
# node class for the linked list
from .dynamic import DynamicImporter

# generic error handling and type checking
from DISClib.Utils.default import T
from .dynamic import STRUCT_PGK_PATH


# checking costum modules and functions
assert DynamicImporter
assert T

# posible implementations for the ADT
# :param ADT_HT_MOD_DICT
ADT_HT_MOD_DICT: dict = {
    "SeparateChaining": "chaininghashtable",
    "LinearProbing": "probinghashtable",
}
"""
Referencia a los posibles módulos de implementación del ADT Map. Pueden ser "SeparateChaining" o "LinearProbing".
"""


def Map(dstruct: str = "SeparateChaining", **kwargs) -> T:
    """*Map()* Función dinámica que retorna una instancia del ADT Map según el tipo de estructura de datos seleccionada por el usuario.

    Args:
        dstruct (str, optional): Tipo de estructura de datos a instanciar. Por defecto es "SeparateChaining". Puende ser "SeparateChaining" o "LinearProbing".

    Raises:
        ValueError: error si el tipo de estructura de datos seleccionada no es válida.

    Returns:
        T: instancia del ADT Map que puede ser "SeparateChaining" o "LinearProbing".
    """
    try:
        package = f"{STRUCT_PGK_PATH}."
        package += f"{ADT_HT_MOD_DICT.get(dstruct)}"
        adt_list = DynamicImporter(dstruct, package, **kwargs)
        adt_instance = adt_list.get_instance()
        return adt_instance
    except Exception as exp:
        err_msg = f"Map type '{dstruct}' not found"
        err_msg += f" in {STRUCT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)


def translate_mp(src_ht: T, tgt_dstruct: str = "LinearProbing") -> T:
    """*translate_mp()* Transforma una instancia del ADT Map con una estructura de datos seleccionada en otra instancia del ADT Map con otra estructura de datos seleccionada.

    Args:
        src_ht (T): instancia del ADT Map a transformar.
        tgt_dstruct (str, optional): Tipo de estructura de datos objetivo a instanciar. Por defecto es "LinearProbing". Puenden ser "SeparateChaining" o "LinearProbing".

    Raises:
        ValueError: error si el tipo de estructura de datos no es válido.

    Returns:
        T: instancia del ADT Map que puede ser "SeparateChaining" o "LinearProbing".
    """
    # TODO update for separate chaining to linear probing
    try:
        tgt_ht = Map(dstruct=tgt_dstruct,
                     cmp_function=src_ht.cmp_function,
                     key=src_ht.key)
        # get keys and values from source map
        keys_lt = src_ht.keys()
        values_lt = src_ht.values()
        # put keys and values in target map
        for k, v in zip(keys_lt, values_lt):
            tgt_ht.put(k, v)
        return tgt_ht
    except Exception as exp:
        err_msg = f"Map type '{tgt_dstruct}' not found"
        err_msg += f" in {STRUCT_PGK_PATH}, "
        err_msg += str(exp)
        raise ValueError(err_msg)


def clone_mp(dstruct: T) -> T:
    """*clone_mp()* copia una instancia del ADT Map con una estructura de datos seleccionada.

    Args:
        dstruct (T): instancia del ADT Map a copiar.

    Returns:
        T: copia independiente de la instancia del ADT Map.
    """
    # TODO check if this works with deep copy
    return copy.deepcopy(dstruct)
