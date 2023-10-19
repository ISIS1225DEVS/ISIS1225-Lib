:py:mod:`DISClib.DataStructures.arraylist`
==========================================

.. py:module:: DISClib.DataStructures.arraylist

.. autoapi-nested-parse::

   _summary_
   # TODO add summary

   .. attribute:: T

      _description_

      :type: type

   Class:
       ArrayList(Generic[T]): _description_

       Functions:
           - __init__(): _description_
           - __post_init__(): _description_
           - default_cmp_function(): _description_
           - _handle_error(): _description_
           - _check_type(): _description_
           - is_empty(): _description_
           - size(): _description_
           - add_first(): _description_
           - add_last(): _description_
           - add_element(elem, pos): _description_
           - get_first(): _description_
           - get_last(): _description_
           - get_element(pos): _description_
           - remove_first(): _description_
           - remove_last(): _description_
           - remove_element(pos): _description_
           - compare_elements(elem1, elem2): _description_
           - is_present(elem): _description_
           - change_info(new_elem, pos): _description_
           - exchange(pos1, pos2): _description_
           - sublist(start, end): _description_
           - concat(other): _description_

   Copyrigth:
       Universidad de los Andes, Bogotá - Colombia, South America
       Facultad de Ingeniería, 2023
       Departamento de Ingeniería de Sistemas y Computación DISC
       Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.arraylist.ArrayList



Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.arraylist.size
   DISClib.DataStructures.arraylist.lastElement



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.arraylist.T


.. py:data:: T

   Este módulo implementa una estructura de datos lineal,
   como un arreglo de apuntadores a los nodos de la lista.


   Este código está basado en la implementación
   propuesta por R.Sedgewick y Kevin Wayne en su libro
   Algorithms, 4th Edition

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



.. py:function:: size(lst)

   Informa el número de elementos de la lista.

   Args
       lst: La lista a examinar

   :raises Exception:


.. py:function:: lastElement(lst)

   Retorna el último elemento de una  lista no vacia.
       No se elimina el elemento.

   :param lst: La lista a examinar

   :raises Exception:


