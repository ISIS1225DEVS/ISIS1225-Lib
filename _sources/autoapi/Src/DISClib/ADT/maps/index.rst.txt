:py:mod:`Src.DISClib.ADT.maps`
==============================

.. py:module:: Src.DISClib.ADT.maps

.. autoapi-nested-parse::

   Este módulo implementa el tipo abstracto de datos (TAD) Map sin orden. Se puede implementar sobre una estructura de datos Hash Table, con resolución de colisiones por sondeo lineal (Linear Probing) o encadenamiento por separado (Separate Chaining).

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.maps.Map
   Src.DISClib.ADT.maps.clone_mp
   Src.DISClib.ADT.maps.translate_mp



Attributes
~~~~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.maps.ADT_HT_MOD_DICT


.. py:data:: ADT_HT_MOD_DICT
   :type: dict

   Referencia a los posibles módulos de implementación del ADT Map. Pueden ser "SeparateChaining" o "LinearProbing".

.. py:function:: Map(dstruct: str = 'SeparateChaining', **kwargs) -> Src.DISClib.Utils.default.T

   *Map()* Función dinámica que retorna una instancia del ADT Map según el tipo de estructura de datos seleccionada por el usuario.

   :param dstruct: Tipo de estructura de datos a instanciar. Por defecto es "SeparateChaining". Puende ser "SeparateChaining" o "LinearProbing".
   :type dstruct: str, optional

   :raises ValueError: error si el tipo de estructura de datos seleccionada no es válida.

   :returns: instancia del ADT Map que puede ser "SeparateChaining" o "LinearProbing".
   :rtype: T


.. py:function:: clone_mp(og_mp: Src.DISClib.Utils.default.T) -> Src.DISClib.Utils.default.T

   *clone_mp()* copia una instancia del ADT Map con una estructura de datos seleccionada.

   :param og_mp: instancia del ADT *Map* a copiar.
   :type og_mp: T

   :returns: copia independiente de la instancia del ADT *Map*.
   :rtype: T


.. py:function:: translate_mp(src_mp: Src.DISClib.Utils.default.T, tgt_dstruct: str = 'LinearProbing') -> Src.DISClib.Utils.default.T

   *translate_mp()* Transforma una instancia del ADT Map con una estructura de datos seleccionada en otra instancia del ADT Map con otra estructura de datos seleccionada.

   :param src_mp: instancia del ADT Map a transformar.
   :type src_mp: T
   :param tgt_dstruct: Tipo de estructura de datos objetivo a instanciar. Por defecto es "LinearProbing". Puenden ser "SeparateChaining" o "LinearProbing".
   :type tgt_dstruct: str, optional

   :raises ValueError: error si el tipo de estructura de datos no es válido.

   :returns: instancia del ADT Map que puede ser "SeparateChaining" o "LinearProbing".
   :rtype: T


