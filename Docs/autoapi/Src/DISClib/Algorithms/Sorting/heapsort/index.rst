:py:mod:`Src.DISClib.Algorithms.Sorting.heapsort`
=================================================

.. py:module:: Src.DISClib.Algorithms.Sorting.heapsort

.. autoapi-nested-parse::

   Este módulo contiene la implementación del algoritmo de ordenamiento por montículos (heap sort) un algoritmo creado por J.W.J. Williams que utiliza el principio de dividir y conquistar para ordenar una secuencia de elementos. El algoritmo puede aplicarse a cualquier secuencia de elementos que puedan ser comparados entre sí como los ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.Algorithms.Sorting.heapsort.heap_sort
   Src.DISClib.Algorithms.Sorting.heapsort._heapify
   Src.DISClib.Algorithms.Sorting.heapsort._sift



.. py:function:: heap_sort(lst: Src.DISClib.DataStructures.List, sort_crit: Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], bool]) -> Src.DISClib.DataStructures.List

   *heap_sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por montículos (heap sort).

   :param lst: La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
   :type lst: List
   :param sort_crit: Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
   :type sort_crit: Callable[[T, T], bool]

   :returns: La lista ordenada.
   :rtype: List


.. py:function:: _heapify(lst: Src.DISClib.DataStructures.List, low: int, high: int, sort_crit: Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], bool]) -> Src.DISClib.DataStructures.List

   *_heapify()* construye un montículo inicial del algoritmo de ordenamiento. Utiliza el criterio de ordenamiento para ajustar la lista al montículo y poder garantizar que los elementos tienen hijos izquierdos y derechos según el índice de árbol binario lleno reconstruido en el indice i*2+1 y i*2+2 respectivamente.

   :param lst: La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
   :type lst: List
   :param low: límite inferior de la sublista a ordenar según el índice de árbol binario lleno reconstruido.
   :type low: int
   :param high: límite superior de la sublista a ordenar según el índice de árbol binario lleno reconstruido.
   :type high: int
   :param sort_crit: Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
   :type sort_crit: Callable[[T, T], bool]

   :returns: lista ajustada al montículo según el criterio de ordenamiento.
   :rtype: List


.. py:function:: _sift(lst: Src.DISClib.DataStructures.List, low: int, high: int, sort_crit: Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], bool])

   *_sift()* ajusta la lista al montículo según el criterio de ordenamiento. Utiliza el criterio de ordenamiento para encontrar el elemento de mayor importancia en el montículo y ajusta la posición del elemento de acuerdo con él.

   :param lst: La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
   :type lst: List
   :param low: límite inferior de la sublista a ordenar según el índice del árbol binario lleno reconstruido.
   :type low: int
   :param high: límite superior de la sublista a ordenar según el índice del árbol binario lleno reconstruido.
   :type high: int
   :param sort_crit: Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento es menor que el segundo elemento, y *False* en caso contrario.
   :type sort_crit: Callable[[T, T], bool]


