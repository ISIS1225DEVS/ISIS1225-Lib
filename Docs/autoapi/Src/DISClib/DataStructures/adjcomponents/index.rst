:py:mod:`Src.DISClib.DataStructures.adjcomponents`
==================================================

.. py:module:: Src.DISClib.DataStructures.adjcomponents

.. autoapi-nested-parse::

   # TODO agregar descripcion del modulo y del ADT que implementa!!!

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.adjcomponents.Edge
   Src.DISClib.DataStructures.adjcomponents.Vertex



Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.adjcomponents.newEdge
   Src.DISClib.DataStructures.adjcomponents.weight
   Src.DISClib.DataStructures.adjcomponents.either
   Src.DISClib.DataStructures.adjcomponents.other
   Src.DISClib.DataStructures.adjcomponents.compareedges



.. py:class:: Edge


   Bases: :py:obj:`Generic`\ [\ :py:obj:`Src.DISClib.Utils.default.T`\ ]

   Edge _summary_

   :param Generic: _description_
   :type Generic: _type_


.. py:class:: Vertex


   Bases: :py:obj:`Generic`\ [\ :py:obj:`Src.DISClib.Utils.default.T`\ ]

   Vertex _summary_

   :param Generic: _description_
   :type Generic: _type_


.. py:function:: newEdge(va, vb, weight=0)

   Crea un nuevo arco entrelos vertices va y vb


.. py:function:: weight(edge)

   Retorna el peso de un arco


.. py:function:: either(edge)

   Retorna el vertice A del arco


.. py:function:: other(edge, veither)

   Retorna el vertice B del arco


.. py:function:: compareedges(edge1, edge2)

   Compara dos arcos y retorna True si son iguales


