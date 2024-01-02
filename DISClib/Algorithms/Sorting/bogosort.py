"""
Este módulo contiene la implementación del algoritmo de ordenamiento por azar (bogo sort). El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
import random
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
# :arg: List: list type
List = Union[ArrayList, SingleLinked, DoubleLinked]
"""
Lista de tipos de estructuras que se pueden ordenar por el algoritmo de ordenamiento (ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*)
"""
def bogo_sort(lst: List, sort_crit: Callable[[T, T], bool]) -> List:
    """*bogo_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por azar (bogo sort).

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    
    try:
        lt_size = lst.size() # tamaño de la lista
        
        while not is_sorted(lst, sort_crit, lt_size):  # revisa si la lista esta ordenada
            
           for pos in range(0, lt_size-1):                          
               random_pos = random.randint(0, lt_size-1) #se genera un indice aleatorio que este dentro de la lista
               lst.exchange(pos, random_pos)             #se intercambia el elemento actual con el del indice generado                  
        
        return lst
    
    except Exception as err:
        # get current module and function name
        cur_context = __name__.split(".")[-1]
        cur_function = inspect.currentframe().f_code.co_name
        # handle the error
        error_handler(cur_context, cur_function, err)



def is_sorted(lst: List, sort_crit: Callable[[T, T],bool] , size: int) -> bool:
    """*is_sorted()* revisa si una lista está organizada de acuerdo al criterio de comparación.

    Args:
        lst (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
        size (int): El tamaño de la lista.
    Returns:
        True: Si la lista está ordenada.
        False: Si la lista no está ordenada.
    """
    
    for pos in range(0,size-1):
        if not sort_crit(lst.get_element(pos) , lst.get_element(pos+1)):      
            #si dos elementos consecutivos no estan ordenados
            return False
        
        
    return True




