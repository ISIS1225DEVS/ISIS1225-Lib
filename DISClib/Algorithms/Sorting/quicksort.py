"""
Este módulo contiene la implementación del algoritmo de ordenamiento rápido (quick sort) un algoritmo creado por Tony Hoare que utiliza el principio de dividir y conquistar para ordenar una secuencia de elementos. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

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


# TODO alternative function name: quick_sort
def quick_sort(lst: LT, sort_crit: Callable[[T, T], bool]) -> LT:
    """*merge_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento rápido (quick sort).

    Args:
        lst (LT): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        LT: La lista ordenada.
    """
    try:
        # recuperar el tamaño de la lista original
        lt_size = lst.size()
        # invocar la funcion recursiva
        lst = _quick_sort(lst, 0, lt_size - 1, sort_crit)
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)


def _quick_sort(lst: LT,
                low: int,
                high: int,
                sort_crit: Callable[[T, T], bool]):
    """*_quick_sort()* ordena recursivamente una lista de elementos. Primero se selecciona el pivote utilizando la funcion de particion. Luego se ejecuta la recursión con los elementos a la izquierda del pivote y a la derecha del pivote.

    Args:
        lst (LT): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        low (int): limite inferior de la sublista a ordenar segun el indice del pivote.
        high (int): limite superior de la sublista a ordenar segun el indice del pivote.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
    """
    # caso base de la recursión
    if low >= high:
        return
    # DIVIDIR
    # caso recursivo, seleccionar el pivote
    pivot = _partition(lst, low, high, sort_crit)
    # CONQUISTAR
    # invcocar recursivamente la funcion a la izquierda y derecha del pivote
    _quick_sort(lst, low, pivot - 1, sort_crit)
    _quick_sort(lst, pivot + 1, high - 1, sort_crit)


def _partition(lst: LT,
               low: int,
               high: int,
               sort_crit: Callable[[T, T], bool]) -> int:
    """*_partition()* selecciona el pivote de la lista y lo deja en su lugar, mientras mueve los elementos menores a la izquierda del pivote y los elementos mayores a la derecha del pivote.

    Args:
        lst (LT): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        low (int): limite inferior de la sublista a ordenar segun el indice del pivote.
        high (int): limite superior de la sublista a ordenar segun el indice del pivote.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        int: El nuevo indice del pivote.
    """
    # variables de control para encontrar el pivote
    # indice del pivote temporal
    i = low
    # iterador para recorrer la lista
    j = low + 1
    # mientras se este en el rango de la sublista
    while j < high:
        # recuperar el elemento temporal y el mas extremo en la lista
        t_elm = lst.get_element(j)
        e_high = lst.get_element(high)
        # CONQUISTAR
        # comparar el elemento temporal contra el mas extremo
        if sort_crit(t_elm, e_high):
            # si cumple la condicion, intercambiar los elementos
            lst.exchange(i, j)
            # actualizar el pivote temporal
            i += 1
        # actualizar el indice de la lista
        j += 1
    # RECOMBINAR
    # intercambiar ;ps elementos entre el pivote temporal y el mas extremo
    lst.exchange(i, high)
    return i
