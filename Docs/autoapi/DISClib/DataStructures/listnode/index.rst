:py:mod:`DISClib.DataStructures.listnode`
=========================================

.. py:module:: DISClib.DataStructures.listnode


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.listnode.Node
   DISClib.DataStructures.listnode.SingleNode
   DISClib.DataStructures.listnode.DoubleNode




Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.listnode.T


.. py:data:: T

   

.. py:class:: Node


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   Node generic class for defining a node of a list.

   :param Generic: can be any python type.
   :type Generic: T

   :raises TypeError: only valid data types are allowed.

   :returns: generic node of a list.
   :rtype: Node

   .. py:attribute:: info
      :type: Optional[T]

      

   .. py:method:: __post_init__()

      __post_init__ the function checks the type of the information after
      the data structure initialization.


   .. py:method:: _handle_error(err: Exception) -> None

      _handle_error the generic function handles the error received as
          an argument.

      :param err: received error to handle.
      :type err: Exception


   .. py:method:: _check_type(element: T) -> None

      _check_type the function checks the type of the information received
          as an argument.

      :param element: information to check its type.
      :type element: T

      :raises TypeError: exception raised if the type of the new information is
          different from the type of the current information.

      :returns:

                returns True if the type of the new information is the same
                    as the type of the current information.
      :rtype: bool


   .. py:method:: set_info(element: T) -> None

      set_info the function sets the new information inside the node.

      :param element: new information for the node.
      :type element: T


   .. py:method:: get_info() -> T

      get_info the function returns the information inside the node.

      :returns: information of the node.
      :rtype: T



.. py:class:: SingleNode


   Bases: :py:obj:`Node`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   SingleNode generic class for defining a node of a single linked list.
   extends Node class.

   :param Node: generic node of a list.
   :type Node: dataclass
   :param Generic: can be any python type.
   :type Generic: T

   :returns: generic node of a single linked list.
   :rtype: SingleNode

   .. py:attribute:: _next
      :type: Optional[SingleNode[T]]

      

   .. py:method:: next() -> Optional[SingleNode[T]]

      next the function returns the next node of the list.

      :returns: next node of the list, if it exists.
      :rtype: SingleNode[T]



.. py:class:: DoubleNode


   Bases: :py:obj:`SingleNode`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   DoubleNode generic class for defining a node of a double linked list.
   extends SingleNode class.

   :param SingleNode: generic node of a single linked list.
   :type SingleNode: dataclass
   :param Generic: can be any python type.
   :type Generic: T

   :returns: generic node of a double linked list.
   :rtype: DoubleNode

   .. py:attribute:: _prev
      :type: Optional[DoubleNode[T]]

      

   .. py:method:: prev() -> Optional[DoubleNode[T]]

      prev the function returns the previous node of the list.

      :returns: the previous node of the list, if it exists.
      :rtype: DoubleNode[T]



