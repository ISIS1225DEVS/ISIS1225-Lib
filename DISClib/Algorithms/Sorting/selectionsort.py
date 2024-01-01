"""
Este módulo contiene la implementación del algoritmo de ordenamiento por selección (selection sort). El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import modules for defining the list types
from typing import Union, Callable
# import inspect for getting the name of the current function
import inspect

# custom modules
from DISClib.DataStructures.arraylist import ArrayList
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.doublelinkedlist import DoubleLinked
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import T

# checking custom modules
assert error_handler
assert T

# sort available list types
# :arg: LT: list type
LT = Union[ArrayList, SingleLinked, DoubleLinked]
"""
Lista de tipos de estructuras que se pueden ordenar por el algoritmo de ordenamiento (ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*)
"""


# TODO alternative function name: selection_sort
def sort(lst: LT, sort_crit: Callable[[T, T], bool]) -> LT:
    """
    Ordena una lista de elementos utilizando el algoritmo de ordenamiento por selección (selection sort).

    Args:
        lst (LT): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        LT: La lista ordenada.
    """
    try:
        lt_size = lst.size()    # tamaño de la lista
        i = 0                # indice del elemento actual
        while i < lt_size:
            # posicion del elemento mas pequeño
            min_idx = i
            j = i + 1
            while j < lt_size:
                # si encuentra un elemento mas pequeño
                if sort_crit(lst.get_element(j), lst.get_element(min_idx)):
                    # actualiza la posicion del elemento mas pequeño
                    min_idx = j
                j += 1
            # actualiza la posicion del elemento mas pequeño
            lst.exchange(i, min_idx)
            i += 1
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)
