:py:mod:`DISClib.DataStructures`
================================

.. py:module:: DISClib.DataStructures


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   adjlist/index.rst
   adjmatrix/index.rst
   arraylist/index.rst
   binarysearchtree/index.rst
   bst/index.rst
   bstnode/index.rst
   chaininghashmap/index.rst
   doublelinkedlist/index.rst
   edge/index.rst
   heap/index.rst
   iminpqnode/index.rst
   indexheap/index.rst
   listnode/index.rst
   mapentry/index.rst
   nodetree/index.rst
   probehashtable/index.rst
   probinghashmap/index.rst
   rbt/index.rst
   rbtnode/index.rst
   redblacktree/index.rst
   singlelinkedlist/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.ArrayList
   DISClib.DataStructures.SingleLinked
   DISClib.DataStructures.DoubleLinked




Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.file_path
   DISClib.DataStructures.file_dir


.. py:class:: ArrayList


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   ArrayList _summary_

   :param Generic: _description_
   :type Generic: _type_

   .. py:attribute:: elements
      :type: List[T]

      

   .. py:attribute:: _size
      :type: int
      :value: 0

      

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[T, T], int]]

      

   .. py:attribute:: key
      :type: Optional[str]

      

   .. py:method:: __post_init__() -> None

      __post_init__ _summary_



   .. py:method:: default_cmp_function(elm1, elm2) -> int

      default_cmp_function _summary_

      :param elm1: _description_
      :type elm1: _type_
      :param elm2: _description_
      :type elm2: _type_

      :raises Exception: _description_
      :raises Exception: _description_

      :returns: _description_
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      _handle_error _summary_

      :param err: _description_
      :type err: Exception


   .. py:method:: _check_type(element: T) -> bool

      _check_type _summary_

      :param element: _description_
      :type element: T

      :returns: _description_
      :rtype: bool


   .. py:method:: is_empty() -> bool

      is_empty _summary_

      :returns: _description_
      :rtype: bool


   .. py:method:: size() -> int

      size _summary_

      :returns: _description_
      :rtype: int


   .. py:method:: add_first(element: T) -> None

      add_first _summary_

      :param element: _description_
      :type element: T

      :raises Exception: _description_


   .. py:method:: add_last(element: T) -> None

      add_last _summary_

      :param element: _description_
      :type element: T

      :raises Exception: _description_


   .. py:method:: add_element(element: T, pos: int) -> None

      add_element _summary_

      :param element: _description_
      :type element: T
      :param pos: _description_
      :type pos: int

      :raises Exception: _description_


   .. py:method:: get_first() -> T

      get_first _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: T


   .. py:method:: get_last() -> T

      get_last _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: T


   .. py:method:: get_element(pos: int) -> T

      get_element _summary_

      :param pos: _description_
      :type pos: int

      :raises Exception: _description_
      :raises Exception: _description_

      :returns: _description_
      :rtype: T


   .. py:method:: remove_first() -> T

      remove_first _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: T


   .. py:method:: remove_last() -> T

      remove_last _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: T


   .. py:method:: remove_element(pos: int) -> T

      remove_element _summary_

      :param pos: _description_
      :type pos: int

      :raises Exception: _description_

      :returns: _description_
      :rtype: T


   .. py:method:: compare_elements(elem1: T, elem2: T) -> int

      compare_elements _summary_

      :param elem1: _description_
      :type elem1: T
      :param elem2: _description_
      :type elem2: T

      :returns: _description_
      :rtype: int


   .. py:method:: is_present(element: T) -> int

      is_present _summary_

      :param element: _description_
      :type element: T

      :returns: _description_
      :rtype: int


   .. py:method:: change_info(new_info: T, pos: int) -> None

      change_info _summary_

      :param new_info: _description_
      :type new_info: T
      :param pos: _description_
      :type pos: int

      :raises Exception: _description_


   .. py:method:: exchange(pos1: int, pos2: int) -> None

      exchange _summary_

      :param pos1: _description_
      :type pos1: int
      :param pos2: _description_
      :type pos2: int

      :raises Exception: _description_
      :raises Exception: _description_
      :raises Exception: _description_


   .. py:method:: sublist(start: int, end: int) -> ArrayList[T]

      create_sublist _summary_

      :param start: _description_
      :type start: int
      :param end: _description_
      :type end: int

      :raises Exception: _description_

      :returns: _description_
      :rtype: ArrayList[T]


   .. py:method:: concat(other: ArrayList[T]) -> ArrayList[T]

      concat_list _summary_

      :param other: _description_
      :type other: ArrayList[T]

      :raises Exception: _description_

      :returns: _description_
      :rtype: ArrayList[T]


   .. py:method:: __iter__()

      __iter__ _summary_

      :returns: _description_
      :rtype: _type_



.. py:class:: SingleLinked


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   SingleLinked _summary_

   :param Generic: _description_
   :type Generic: _type_

   .. py:attribute:: first
      :type: Optional[DISClib.DataStructures.listnode.SingleNode[T]]

      

   .. py:attribute:: last
      :type: Optional[DISClib.DataStructures.listnode.SingleNode[T]]

      

   .. py:attribute:: _size
      :type: int
      :value: 0

      

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[T, T], int]]

      

   .. py:attribute:: key
      :type: Optional[str]

      

   .. py:method:: __post_init__() -> None

      __post_init__ _summary_



   .. py:method:: default_cmp_function(elm1, elm2) -> int

      default_cmp_function _summary_

      :param elm1: _description_
      :type elm1: _type_
      :param elm2: _description_
      :type elm2: _type_

      :raises Exception: _description_
      :raises Exception: _description_

      :returns: _description_
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      _handle_error _summary_

      :param err: _description_
      :type err: Exception


   .. py:method:: _check_type(element: T) -> bool

      _check_type _summary_

      :param element: _description_
      :type element: T

      :returns: _description_
      :rtype: bool


   .. py:method:: is_empty() -> bool

      is_empty _summary_

      :returns: _description_
      :rtype: bool


   .. py:method:: size() -> int

      size _summary_

      :returns: _description_
      :rtype: int


   .. py:method:: add_first(element: T) -> None

      add_first _summary_

      :param element: _description_
      :type element: T

      :raises Exception: _description_


   .. py:method:: add_last(element: T) -> None

      add_last _summary_

      :param element: _description_
      :type element: T

      :raises Exception: _description_


   .. py:method:: add_element(element: T, pos: int) -> None

      add_element _summary_

      :param element: _description_
      :type element: T
      :param pos: _description_
      :type pos: int

      :raises Exception: _description_


   .. py:method:: get_first() -> Optional[T]

      get_first _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: Optional[T]


   .. py:method:: get_last() -> Optional[T]

      get_last _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: Optional[T]


   .. py:method:: get_element(pos: int) -> Optional[T]

      get_element _summary_

      :param pos: _description_
      :type pos: int

      :raises Exception: _description_

      :returns: _description_
      :rtype: Optional[T]


   .. py:method:: remove_first() -> Optional[T]

      remove_first _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: Optional[T]


   .. py:method:: remove_last() -> Optional[T]

      remove_last _summary_

      :raises Exception: _description_

      :returns: _description_
      :rtype: Optional[T]


   .. py:method:: remove_element(pos: int) -> Optional[T]

      remove_element _summary_

      :param pos: _description_
      :type pos: int

      :raises Exception: _description_

      :returns: _description_
      :rtype: Optional[T]


   .. py:method:: compare_elements(current: T, temp: T) -> int

      compare_elements _summary_

      :param current: _description_
      :type current: T
      :param temp: _description_
      :type temp: T

      :returns: _description_
      :rtype: int


   .. py:method:: is_present(element: T) -> int

      is_present _summary_

      :param element: _description_
      :type element: T

      :returns: _description_
      :rtype: int


   .. py:method:: change_info(pos: int, new_info: T) -> None

      change_info _summary_

      :param pos: _description_
      :type pos: int
      :param new_info: _description_
      :type new_info: T

      :raises Exception: _description_
      :raises Exception: _description_


   .. py:method:: exchange(pos1: int, pos2: int) -> None

      exchange _summary_

      :param pos1: _description_
      :type pos1: int
      :param pos2: _description_
      :type pos2: int

      :raises Exception: _description_
      :raises Exception: _description_
      :raises Exception: _description_


   .. py:method:: create_sublist(start: int, end: int) -> SingleLinked[T]


   .. py:method:: concatenate(lst: SingleLinked[T]) -> SingleLinked[T]


   .. py:method:: __iter__() -> DISClib.DataStructures.listnode.SingleNode[T]



.. py:class:: DoubleLinked


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   DoubleLinked _summary_

   :param Generic: _description_
   :type Generic: _type_

   .. py:attribute:: first
      :type: Optional[DISClib.DataStructures.listnode.DoubleNode[T]]

      

   .. py:attribute:: last
      :type: Optional[DISClib.DataStructures.listnode.DoubleNode[T]]

      

   .. py:attribute:: _size
      :type: int
      :value: 0

      

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[T, T], int]]

      

   .. py:attribute:: key
      :type: Optional[str]

      


.. py:data:: file_path

   

.. py:data:: file_dir

   

