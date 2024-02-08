:py:mod:`Src.DISClib.DataStructures.leftleaningrbtree`
======================================================

.. py:module:: Src.DISClib.DataStructures.leftleaningrbtree

.. autoapi-nested-parse::

   # TODO: agregar descripción del módulo

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.leftleaningrbtree.LeftLeanRedBlackTree




.. py:class:: LeftLeanRedBlackTree


   Bases: :py:obj:`Generic`\ [\ :py:obj:`Src.DISClib.Utils.default.T`\ ]

   **LeftLeanRedBlackTree** representa la estructura de datos para arreglos dinamicos (Array List), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

   :param Generic: TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
   :type Generic: T

   :returns: ADT de tipo LeftLeanRedBlackTree o Arreglo Dinámico.
   :rtype: LeftLeanRedBlackTree

   .. py:attribute:: iodata
      :type: Optional[List[Src.DISClib.Utils.default.T]]

      Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.uctura.uctura.uctura.

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], int]]

      Función de comparación personalizable por el usuario para reconocer los elementos dentro de la estructura. Es un argumento configurable al crear la estructura. Por defecto es la función *lt_default_cmp_funcion()* propia de *DISClib*.

   .. py:attribute:: elements
      :type: List[Src.DISClib.Utils.default.T]

      Lista nativa de Python que contiene los elementos de la estructura.

   .. py:attribute:: key
      :type: Optional[str]

      Nombre de la llave opcional que se utiliza para comparar los elementos del LeftLeanRedBlackTree, Por defecto es *None* y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.

   .. py:attribute:: _size
      :type: int
      :value: 0

      Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.

   .. py:method:: __post_init__() -> None

      *__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del LeftLeanRedBlackTree.



   .. py:method:: default_cmp_function(elm1, elm2) -> int

      *default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el LeftLeanRedBlackTree. Es una función crucial para que la estructura de datos funcione correctamente.

      :param elm1: primer elemento a comparar.
      :type elm1: Any
      :param elm2: segundo elemento a comparar.
      :type elm2: Any

      :returns: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      *_handle_error()* función privada que maneja los errores que se pueden presentar en el LeftLeanRedBlackTree.

      Si se presenta un error en LeftLeanRedBlackTree, se formatea el error según el contexto (paquete/clase), la función que lo generó y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

      :param err: Excepción que se generó en el LeftLeanRedBlackTree.
      :type err: Exception


   .. py:method:: _check_type(element: Src.DISClib.Utils.default.T) -> bool

      *_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al LeftLeanRedBlackTree sea del mismo tipo contenido dentro de los elementos del LeftLeanRedBlackTree.

      :raises TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el LeftLeanRedBlackTree.

      :param element: elemento que se quiere procesar en LeftLeanRedBlackTree.
      :type element: T

      :returns: operador que indica si el ADT LeftLeanRedBlackTree es del mismo tipo que el elemento que se quiere procesar.
      :rtype: bool



