:py:mod:`Src.DISClib.Algorithms.Sorting.selectionsort`
======================================================

.. py:module:: Src.DISClib.Algorithms.Sorting.selectionsort

.. autoapi-nested-parse::

   Este módulo contiene la implementación del algoritmo de ordenamiento por selección (selection sort). El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.Algorithms.Sorting.selectionsort.selection_sort



.. py:function:: selection_sort(lst: Src.DISClib.DataStructures.List, sort_crit: Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], bool]) -> Src.DISClib.DataStructures.List

   *selection_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por selección (selection sort).

   :param lst: La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
   :type lst: List
   :param sort_crit: Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
   :type sort_crit: Callable[[T, T], bool]

   :returns: La lista ordenada.
   :rtype: List


