:py:mod:`DISClib.DataStructures.listnode`
=========================================

.. py:module:: DISClib.DataStructures.listnode

.. autoapi-nested-parse::

   Estas clases representan los nodos para una lista sencillamente encadenada (SingleNode) y una lista doblemente encadenada (DoubleNode).

   Estos nodos se utilizan respectivamente en las estructuras dinámicas de lista sencillamente encadenada (LinkedList) y lista doblemente encadenadA(DoubleLinkedList). Las cuales NO tienen un tamaño fijo y pueden crecer indefinidamente en la memoria disponible.

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.listnode.SingleNode
   DISClib.DataStructures.listnode.DoubleNode




.. py:class:: SingleNode


   Bases: :py:obj:`DISClib.DataStructures.node.Node`, :py:obj:`Generic`\ [\ :py:obj:`DISClib.Utils.default.T`\ ]

   SingleNode Clase que representa un nodo de una lista sencillamente encadenada. Extiende la clase Node y contiene la información del nodo.

   :param Node: Clase base para implementar un nodo de una lista.
   :type Node: dataclass
   :param Generic: TAD/ADT que representa el tipo de dato de la información dentro del nodo.
   :type Generic: T

   :returns: ADT para un nodo de una lista sencillamente encadenada.
   :rtype: SingleNode

   .. py:attribute:: _next
      :type: Optional[SingleNode[T]]

      Referencia al siguiente nodo de la lista.

   .. py:method:: next() -> Optional[SingleNode[T]]

      next recupera el siguiente nodo de la lista si existe.

      :returns: referencia al siguiente nodo de la lista.
      :rtype: SingleNode



.. py:class:: DoubleNode


   Bases: :py:obj:`SingleNode`, :py:obj:`Generic`\ [\ :py:obj:`DISClib.Utils.default.T`\ ]

   DoubleNode Clase que representa un nodo de una lista doblemente encadenada. Extiende las clases SingleNode y Node.

   :param SingleNode: Calse base para implementar un nodo de una lista sencillamente encadenada.
   :type SingleNode: Dataclass
   :param Generic: TAD/ADT que representa el tipo de dato de la información dentro del nodo.
   :type Generic: T

   :returns: ADT para un nodo de una lista doblemente encadenada.
   :rtype: DoubleNode

   .. py:attribute:: _prev
      :type: Optional[DoubleNode[T]]

      Referencia al nodo anterior de la lista.

   .. py:method:: prev() -> Optional[DoubleNode[T]]

      prev recupera el nodo anterior de la lista si existe.

      :returns: referencia al nodo anterior de la lista.
      :rtype: _type_



