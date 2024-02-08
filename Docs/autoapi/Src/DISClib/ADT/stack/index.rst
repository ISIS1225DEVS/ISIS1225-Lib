:py:mod:`Src.DISClib.ADT.stack`
===============================

.. py:module:: Src.DISClib.ADT.stack

.. autoapi-nested-parse::

   Este ADT representa una pila implementada sobre una lista doblemente encadenada. Esta pila (Stack) es un Tipo Abstracto de Datos (TAD/ADT) que permite almacenar una colección de elementos y operarlos en el mismo orden en que fueron agregados (LIFO - Last In First Out).

   La implementación de la cola se realiza sobre una lista doblemente
   encadenada (DoubleLinked) para garantizar que las operaciones de agregar y
   eliminar elementos se realicen en tiempo constante y no consumir memoria
   innecesaria.

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.stack.Stack




.. py:class:: Stack


   Bases: :py:obj:`Src.DISClib.DataStructures.doublelinkedlist.DoubleLinked`

   **Stack** representa una pila implementada sobre una lista doblemente encadenada (*DoubleLinked*) y @dataclass para que sea una estructura de datos genérica. Esta pila (*Stack*) es un Tipo Abstracto de Datos (TAD/ADT) que permite almacenar una colección de elementos y operarlos en el mismo orden en que fueron agregados (LIFO - Last In First Out).

   **IMPORTANTE:** *Stack* extiende de la clase *DoubleLinked*, por lo que hereda todos sus parametros internos y funciones.

   :param DoubleLinked: ADT *DISClib* que implementa las funciones básicas de una lista doblemente encadenada.
   :type DoubleLinked: dataclass

   :returns: ADT de tipo *Stack* o Pila, implementado sobre una lista doblemente encadenada.
   :rtype: Stack

   .. py:method:: push(element: Src.DISClib.Utils.default.T) -> None

      *push()* inserta o agrega un elemento en el tope del *Stack*.

      :param element: el elemento que se quiere agregar al *Stack*.
      :type element: T


   .. py:method:: pop() -> Src.DISClib.Utils.default.T

      *pop()* elimina o remueve el elemento en tope del ADT *Stack*.

      :returns: el elemento de la posición más alta (tope) del ADT *Stack*.
      :rtype: T


   .. py:method:: top() -> Optional[Src.DISClib.Utils.default.T]

      *top()* lee el elemento ubicado en el tope del ADT *Stack* sin eliminarlo.

      :returns: el elemento en la posición más alta (tope) del ADT *Stack*.
      :rtype: T



