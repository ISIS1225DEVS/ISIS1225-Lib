"""
Este módulo contiene la implementación del algoritmo de ordenamiento por selección por mezcla (merge sort) un algoritmo creado por John Von Neumann que utiliza el principio de dividir y conquistar para ordenar una secuencia de elementos. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

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
from DISClib.DataStructures import List
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import T

# checking custom modules
assert List
assert error_handler
assert T


# TODO alternative function name: merge_sort
def merge_sort(lst: List, sort_crit: Callable[[T, T], bool]) -> List:
    """*merge_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por mezcla (merge sort).

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    try:
        # recuperar el tamaño de la lista
        lt_size = lst.size()
        # si la lista es mayor a 1, es decir no es trivial
        if lt_size > 1:
            # DIVIDIR
            # encontrar el punto medio de la lista, redondeando hacia abajo
            mid = int(lt_size / 2)
            # dividir la lista en dos sublistas izquierda y derecha
            left_lt = lst.sublist(0, mid - 1)
            right_lt = lst.sublist(mid, lt_size - 1)
            # ordenar recursivamente las sublistas izquierda y derecha
            # CONQUISTAR
            merge_sort(left_lt, sort_crit)
            merge_sort(right_lt, sort_crit)
            # RECOMBINAR
            # recomponer las sublistas izquierda y derecha en la original
            lst = _merge(left_lt, right_lt, lst, sort_crit)
        return lst
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)


def _merge(left_lt: List,
           right_lt: List,
           lst: List,
           sort_crit: Callable[[T, T], bool]) -> List:
    """*_merge()* recombina las sublistas izquierda y derecha en una sola lista ordenada dentro del algoritmo de ordenamiento por mezcla (merge sort).

    Args:
        left_lt (List): sublista izquierda creada recursivamente.
        right_lt (List): sublista derecha creada recursivamente.
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*. Es la lista original que se va a ordenar.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        List: la lista ordenada
    """
    # iteradores para la lista izquierda, derecha y original
    i = 0
    j = 0
    k = 0
    # __len__ y size() son funciones de python y DISClib equivalentes
    # mientras se este en el rango de la lista original
    while k < lst.size():
        # si se esta dentro del rango de la lista izquierda y derecha
        if i < left_lt.size() and j < right_lt.size():
            # recuperar los elementos de ambas listas
            e_left = left_lt.get_element(i)
            e_right = right_lt.get_element(j)
            # comparar los elementos de ambas listas
            if sort_crit(e_left, e_right):
                # actualizar la lista original con el elemento de la lista izquierda
                lst.change_info(e_left, k)
                i += 1
            # si no se cumple la condicion anterior
            else:
                # actualizar la lista original con el elemento de la lista derecha
                lst.change_info(e_right, k)
                j += 1
        # COMPARAR LOS ELEMENTOS QUE NO ESTAN EN AMBAS LISTAS
        # si se esta dentro del rango de la lista izquierda
        elif i < len(left_lt):
            # actualizar la lista original con el elemento de la lista izquierda
            e_left = left_lt.get_element(i)
            lst.change_info(e_left, k)
            i += 1
        # si se esta dentro del rango de la lista derecha
        elif j < len(right_lt):
            # actualizar la lista original con el elemento de la lista derecha
            e_right = right_lt.get_element(j)
            lst.change_info(e_right, k)
            j += 1
        k += 1
    return lst
