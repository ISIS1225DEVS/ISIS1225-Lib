:py:mod:`Src.DISClib.Algorithms.Sorting.mergesort`
==================================================

.. py:module:: Src.DISClib.Algorithms.Sorting.mergesort

.. autoapi-nested-parse::

   Este módulo contiene la implementación del algoritmo de ordenamiento por selección por mezcla (merge sort) un algoritmo creado por John Von Neumann que utiliza el principio de dividir y conquistar para ordenar una secuencia de elementos. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.Algorithms.Sorting.mergesort.merge_sort
   Src.DISClib.Algorithms.Sorting.mergesort._merge



.. py:function:: merge_sort(lst: Src.DISClib.DataStructures.List, sort_crit: Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], bool]) -> Src.DISClib.DataStructures.List

   *merge_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por mezcla (merge sort).

   :param lst: La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
   :type lst: List
   :param sort_crit: Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
   :type sort_crit: Callable[[T, T], bool]

   :returns: La lista ordenada.
   :rtype: List


.. py:function:: _merge(left_lt: Src.DISClib.DataStructures.List, right_lt: Src.DISClib.DataStructures.List, lst: Src.DISClib.DataStructures.List, sort_crit: Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], bool]) -> Src.DISClib.DataStructures.List

   *_merge()* recombina las sublistas izquierda y derecha en una sola lista ordenada dentro del algoritmo de ordenamiento por mezcla (merge sort).

   :param left_lt: sublista izquierda creada recursivamente.
   :type left_lt: List
   :param right_lt: sublista derecha creada recursivamente.
   :type right_lt: List
   :param lst: La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*. Es la lista original que se va a ordenar.
   :type lst: List
   :param sort_crit: Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
   :type sort_crit: Callable[[T, T], bool]

   :returns: la lista ordenada
   :rtype: List


