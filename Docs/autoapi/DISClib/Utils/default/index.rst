:py:mod:`DISClib.Utils.default`
===============================

.. py:module:: DISClib.Utils.default

.. autoapi-nested-parse::

   Módulo con variables globales y funciones de comparación por defecto para uso por todo *DISClib* y sus ADTs.

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.Utils.default.lt_default_cmp_funcion



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.Utils.default.VALID_DATA_TYPE_LT
   DISClib.Utils.default.DEFAULT_DICT_KEY
   DISClib.Utils.default.VALID_IO_TYPE
   DISClib.Utils.default.T


.. py:data:: VALID_DATA_TYPE_LT
   :type: tuple
   :value: ()

   Tupla con los tipos de datos nativos en Python que son comparables en los ADTs.

.. py:data:: DEFAULT_DICT_KEY
   :type: str
   :value: 'id'

   Llave por defecto para comparar diccionarios en los ADTs.

.. py:data:: VALID_IO_TYPE
   :type: tuple
   :value: ()

   Tupla con los tipos de datos nativos en Python que son válidos para entrada y salida de datos al inicializar un ADT.

.. py:data:: T

   Variable nativa de Python para definir un tipo de @dataclass genérico.

.. py:function:: lt_default_cmp_funcion(key, elm1, elm2) -> int

   lt_default_cmp_funcion función de comparación por defecto para los elementos del ADT List (ArrayList, SingleLinked, DoublyLinked). pueden ser de tipo nativo o definido por el usuario.

   :param key: llave para comparar los elementos de tipo diccionario.
   :type key: str
   :param elm1: primer elemento a comparar.
   :type elm1: any
   :param elm2: segundo elemento a comparar.
   :type elm2: any

   :raises TypeError: error de tipo de dato si los elementos de tipo nativo en Python no son comparables.
   :raises KeyError: error de clave si la llave para comparar los diccionarios no existe.
   :raises TypeError: error de tipo de dato si los elementos no son comparables.

   :returns: retorna -1 si elm1 es menor que elm2, 0 si son iguales y 1 si elm1 es mayor que elm2.
   :rtype: int


