"""
Este módulo contiene la implementación del algoritmo de ordenamiento por Shell (shell sort) creado por Donald Shell. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
    # Se utiliza la secuencia de incrementos 3x+1: 1, 4, 13, 40, 121, 364, 109, (D. Knuth); Sedgewick: 1,5,19,41,109,209,929,2161,...
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


# TODO alternative function name: shell_sort
def shell_sort(lst: List, sort_crit: Callable[[T, T], bool]) -> List:
    """*shell_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento Shell (shell sort).

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento cumple con el criterio, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    try:
        n = lst.size()  # tamaño de la lista
        h = 1   # gap inicial en 1
        while h < (n / 3):
            h = (3 * h) + 1    # secuencia de incrementos 3x+1

        # mientras el gap sea mayor o igual a 1
        while h >= 1:
            # itera sobre el rango entre la posicion del gap y el tamaño de la lista
            for i in range(h, n):
                j = i   # indice del elemento actual
                # mientras el indice sea mayor o igual al gap y el elemento actual sea menor que el elemento en la posicion j-gap
                while j >= h and sort_crit(lst.get_element(j),
                                           lst.get_element(j - h)):
                    # intercambiar los elementos
                    lst.exchange(j, j - h)
                    j -= h
            # reducir el gap en un tercio
            h //= 3
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)
