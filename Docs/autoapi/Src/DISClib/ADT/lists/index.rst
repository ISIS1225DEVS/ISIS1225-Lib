:py:mod:`Src.DISClib.ADT.lists`
===============================

.. py:module:: Src.DISClib.ADT.lists

.. autoapi-nested-parse::

   Este módulo implementa el tipo abstracto de datos (TAD) lista. Dinámicamente se puede implementar sobre una estructura de datos sea encadenada de forma sencilla (SingleLinked), doble (DoubleLinked) o como un arreglo dinámico (ArrayList).

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.lists.List
   Src.DISClib.ADT.lists.clone_lt
   Src.DISClib.ADT.lists.translate_lt



Attributes
~~~~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.lists.ADT_LT_MOD_DICT


.. py:data:: ADT_LT_MOD_DICT
   :type: dict

   Referencia a los posibles módulos de implementación del ADT List. Pueden ser "ArrayList", "SingleLinked" o "DoubleLinked".

.. py:function:: List(dstruct: str = 'ArrayList', **kwargs) -> Src.DISClib.Utils.default.T

   *List()* Función dinámica que que retorna una instancia del ADT List según el tipo de estructura de datos seleccionada por el usuario.

   :param dstruct: Tipo de estructura de datos a instanciar. Por defecto es "ArrayList". Puende ser "ArrayList", "SingleLinked" o "DoubleLinked".
   :type dstruct: str, optional

   :raises ValueError: error si el tipo de estructura de datos seleccionada no es válida.

   :returns: instancia del ADT List que puede ser "ArrayList", "SingleLinked" o "DoubleLinked".
   :rtype: T


.. py:function:: clone_lt(og_lt: Src.DISClib.Utils.default.T) -> Src.DISClib.Utils.default.T

   *clone()* copia una instancia del ADT List con una estructura de datos seleccionada.

   :param og_lt: instancia del ADT *List* a copiar.
   :type og_lt: T

   :returns: copia independiente de la instancia del ADT *List*.
   :rtype: T


.. py:function:: translate_lt(src_lt: Src.DISClib.Utils.default.T, tgt_dstruct: str = 'SingleLinked') -> Src.DISClib.Utils.default.T

   *translate()* Transforma una instancia del ADT List con una estructura de datos seleccionada en otra instancia del ADT List con otra estructura de datos seleccionada.

   :param src_lt: instancia del ADT List a transformar.
   :type src_lt: T
   :param tgt_dstruct: Tipo de estructura de datos objetivo a instanciar. Por defecto es "SingleLinked". Puenden ser "ArrayList", "SingleLinked" o "DoubleLinked".
   :type tgt_dstruct: str, optional

   :raises ValueError: error si el tipo de estructura de datos no es válido.

   :returns: instancia del ADT List que puede ser "ArrayList", "SingleLinked" o "DoubleLinked".
   :rtype: T


