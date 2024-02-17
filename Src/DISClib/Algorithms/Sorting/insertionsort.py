"""
Este módulo contiene la implementación del algoritmo de ordenamiento por inserción (insertion sort) creado por Konrad Zuse para ordenar una secuencia de elementos. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
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


# TODO alternative function name: insertion_sort
def insertion_sort(lst: List, sort_crit: Callable[[T, T], bool]) -> List:
    """*insertion_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por inserción (insertion sort).

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento cumple con el criterio, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    try:
        lt_size = lst.size()    # tamaño de la lista
        i = 0                   # indice del elemento actual
        # mientras este en el rango de la lista
        while i < lt_size:
            # asumo que la posicion actual es la del elemento mas pequeño
            j = i
            # mientras el elemento y su vecino sean mayores
            while j > 0 and sort_crit(lst.get_element(j),
                                      lst.get_element(j - 1)):
                # intercambiar los elementos
                lst.exchange(j, j - 1)
                j -= 1
            i += 1
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)
