:py:mod:`Src.DISClib.DataStructures.node`
=========================================

.. py:module:: Src.DISClib.DataStructures.node

.. autoapi-nested-parse::

   Este ADT representa un nodo **Node** de información de una estructura de datos dinámica, las cuales pueden ser: listas sencillas, listas doblemente encadenadas, pilas, colas, BST, RBT, entre otras.

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.node.Node




.. py:class:: Node


   Bases: :py:obj:`Generic`\ [\ :py:obj:`Src.DISClib.Utils.default.T`\ ]

   **Node** Es el ADT que representar la información de un nodo de una estructura de datos dinámica y las funciones basicas para acceder a ella. Puede utilizarse para representar un nodo de una lista sencilla o doblemente encadenada.

   :param Generic: TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
   :type Generic: T

   :returns: ADT de tipo *Node* o nodo de información.
   :rtype: Node

   .. py:attribute:: info
      :type: Optional[Src.DISClib.Utils.default.T]

      Es la información contenida en el nodo.

   .. py:method:: _handle_error(err: Exception) -> None

      *_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *Node*.

      Si se presenta un error en *SingleLinked*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DISCLib* para manejarlo segun se considere conveniente el usuario.

      :param err: Excepción que se generó en el *Node*.
      :type err: Exception


   .. py:method:: _check_type(element: Src.DISClib.Utils.default.T) -> bool

      *_check_type()* función propia de la estructura que verifica que la información de *Node* sea del tipo adecuado.

      :param element: elemento que se desea procesar en *Node*.
      :type element: T

      :raises TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *Node*.

      :returns: operador que indica si el ADT *Node* es del mismo tipo que el elemento que se desea procesar.
      :rtype: bool


   .. py:method:: set_info(info: Src.DISClib.Utils.default.T) -> None

      *set_info()* establece la información de *Node*.

      :param info: información que se desea actualizar en *Node*.
      :type info: T


   .. py:method:: get_info() -> Src.DISClib.Utils.default.T

      *get_info()* recupera la información de *Node*.

      :returns: información de *Node*.
      :rtype: T



