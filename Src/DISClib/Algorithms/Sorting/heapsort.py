"""
Este módulo contiene la implementación del algoritmo de ordenamiento por montículos (heap sort) un algoritmo creado por J.W.J. Williams que utiliza el principio de dividir y conquistar para ordenar una secuencia de elementos. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# FIXME: incluir de la contribución de: Jhostin Sánchez

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


# TODO alternative function name: heap_sort
def heap_sort(lst: List, sort_crit: Callable[[T, T], bool]) -> List:
    """*heap_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por montículos (heapsort).

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    try:
        # recuperar el tamaño de la lista
        lt_size = lst.size()
        # construir el montículo inicial
        lst = _heapify(lst, 0, lt_size - 1, sort_crit)
        i = lt_size - 1
        while i >= 0:
            # intercambiar el primer elemento con el ultimo
            lst.exchange(0, i)
            # reconstruir el montículo
            _sift(lst, 0, i - 1, sort_crit)
            i -= 1
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)


def _heapify(lst: List,
             low: int,
             high: int,
             sort_crit: Callable[[T, T], bool]) -> List:
    """*_heapify()* construye el montículo inicial del algoritmo de ordenamiento. Utiliza el criterio de ordenamiento para ajustar la lista al montículo y poder garantizar que los elementos tienen hijos izquierdos y derechos según el índice de árbol binario lleno reconstruido en el indice i*2+1 y i*2+2 respectivamente.

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        low (int): límite inferior de la sublista a ordenar según el índice de árbol binario lleno reconstruido.
        high (int): límite superior de la sublista a ordenar según el índice de árbol binario lleno reconstruido.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        List: lista ajustada al montículo según el criterio de ordenamiento.
    """
    # indice del elemento medio
    i = int(high / 2)
    # buscando el elemento mas grande
    while i >= low:
        # reconstruir el montículo
        _sift(lst, i, high, sort_crit)
        i -= 1
    return lst


# TODO: nombre alternativo: _sift_heap
def _sift(lst: List,
          low: int,
          high: int,
          sort_crit: Callable[[T, T], bool]):
    """*_sift()* ajusta la lista al montículo según el criterio de ordenamiento. Utiliza el criterio de ordenamiento para encontrar el elemento de mayor importancia en el montículo y ajusta la posición del elemento de acuerdo con él.

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        low (int): límite inferior de la sublista a ordenar según el índice del árbol binario lleno reconstruido.
        high (int): límite superior de la sublista a ordenar según el índice del árbol binario lleno reconstruido.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
    """
    # indice temporal del elemento padre
    parent = low
    # indice del hijo izquierdo en el montículo
    i_left = 2 * low + 1
    # indice del hijo derecho en el montículo
    i_right = 2 * low + 2

    # si el hijo izquierdo es mayor que el padre en el montículo
    if i_left < high and not sort_crit(lst.get_element(i_left),
                                       lst.get_element(parent)):
        parent = i_left

    # si el hijo derecho es mayor que el padre en el montículo
    if i_right < high and not sort_crit(lst.get_element(i_right),
                                        lst.get_element(parent)):
        parent = i_right

    # si el padre no es el elemento mas grande
    if parent != low:
        # intercambiar el padre con el elemento mas grande
        lst.exchange(low, parent)
        # invocar recursivamente la función
        _sift(lst, parent, high, sort_crit)
