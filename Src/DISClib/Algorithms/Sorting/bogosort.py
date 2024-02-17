"""
Este módulo contiene la implementación del algoritmo de ordenamiento por azar (bogo sort). El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
import random
# import modules for defining the list types
from typing import Callable
# import inspect for getting the name of the current function
import inspect

# custom modules
from Src.DISClib.DataStructures import List
# generic error handling and type checking
from Src.DISClib.Utils.error import error_handler
from Src.DISClib.Utils.default import T

# checking custom modules
assert List
assert error_handler
assert T


def bogo_sort(lst: List, sort_crit: Callable[[T, T], bool]) -> List:
    """*bogo_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por azar (bogo sort).

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento cumple con el criterio, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    try:
        # recuperar el tamaño de la lista
        lt_size = lst.size()
        # mientras la lista no este ordenada
        while not _is_sorted(lst, sort_crit):
            for i in range(0, lt_size - 1):
                # genera un indice aleatorio que este dentro de la lista
                rand_i = random.randint(0, lt_size - 1)
                # se intercambia el elemento actual con el del indice generado
                lst.exchange(i, rand_i)
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)


def _is_sorted(lst: List, sort_crit: Callable[[T, T], bool]) -> bool:
    """*_is_sorted()* revisa si una lista está organizada de acuerdo al criterio de comparación.

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento cumple con el criterio, y *False* en caso contrario.

    Returns:
        bool: devuelve *True* si la lista está ordenada, *False* en caso contrario.
    """
    lt_size = lst.size()
    # recorre la lista de elementos
    for i in range(0, lt_size - 1):
        if not sort_crit(lst.get_element(i), lst.get_element(i + 1)):
            # si dos elementos consecutivos no estan ordenados
            return False
    return True
