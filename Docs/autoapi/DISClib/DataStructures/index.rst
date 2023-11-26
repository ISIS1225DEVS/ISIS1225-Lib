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
   node/index.rst
   probehashtable/index.rst
   probinghashmap/index.rst
   rbt/index.rst
   rbtnode/index.rst
   redblacktree/index.rst
   singlelinkedlist/index.rst
   treenode/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.ArrayList
   DISClib.DataStructures.SingleLinked




Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.file_path
   DISClib.DataStructures.file_dir


.. py:class:: ArrayList


   Bases: :py:obj:`Generic`\ [\ :py:obj:`DISClib.Utils.default.T`\ ]

   *ArrayList* representa la estructura de datos para arreglos dinamicos (Array List), Implementada con la anotación '@dataclass' de python y el decorador 'Generic[T]' para que sea una estructura de datos genérica.

   :param Generic: TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) que representa un ArrayList o Arreglo Dinámico generico.
   :type Generic: T

   :returns: ADT de tipo ArrayList o Arreglo Dinámico.
   :rtype: ArrayList

   .. py:attribute:: iodata
      :type: Optional[List[DISClib.Utils.default.T]]

      Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.

   .. py:attribute:: elements
      :type: List[DISClib.Utils.default.T]

      Lista nativa de Python que contiene los elementos de la estructura.

   .. py:attribute:: _size
      :type: int
      :value: 0

      Atributo privado que representa el tamaño de la estructura, por defecto es 0.

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[DISClib.Utils.default.T, DISClib.Utils.default.T], int]]

      Función de comparación opcional que se utiliza para comparar los elementos del ArrayList, por defecto es 'None' y el __post_init__ configura la función por defecto lt_default_cmp_funcion().

   .. py:attribute:: key
      :type: Optional[str]

      Nombre de la llave opcional que se utiliza para comparar los elementos del ArrayList, Por defecto es 'None' y el __post_init__ configura la llave por defecto la llave 'id' en DEFAULT_DICT_KEY.

   .. py:method:: __post_init__() -> None

      *__post_init__()* configura los valores por defecto para la llave (key) y la función de comparación (cmp_function). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del ArrayList.



   .. py:method:: default_cmp_function(elm1, elm2) -> int

      *default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el ArrayList. Es una función crucial para que la estructura de datos funcione correctamente.

      :param elm1: primer elemento a comparar.
      :type elm1: Any
      :param elm2: segundo elemento a comparar.
      :type elm2: Any

      :returns: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      *_handle_error()* función privada que maneja los errores que se pueden presentar en el ArrayList.

      Si se presenta un error en el ArrayList, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun sea considere conveniente.

      :param err: Excepción que se generó en el ArrayList.
      :type err: Exception


   .. py:method:: _check_type(element: DISClib.Utils.default.T) -> bool

      *_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al ArrayList sea del mismo tipo contenido dentro de los elementos del ArrayList.

      :raises TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el ArrayList.

      :param element: elemento que se quiere procesar en ArrayList.
      :type element: T

      :returns: operador que indica si el ADT ArrayList es del mismo tipo que el elemento que se quiere procesar.
      :rtype: bool


   .. py:method:: is_empty() -> bool

      *is_empty()* revisa si el ArrayList está vacía.

      :returns: operador que indica si la estructura ArrayList está vacía.
      :rtype: bool


   .. py:method:: size() -> int

      *size()* devuelve el numero de elementos que actualmente contiene el ArrayList.

      :returns: tamaño de la estructura ArrayList.
      :rtype: int


   .. py:method:: add_first(element: DISClib.Utils.default.T) -> None

      *add_first()* adiciona un elemento al inicio del ArrayList.

      :param element: elemento que se quiere agregar a la estructura.
      :type element: T

      :raises Exception: si la operación no se puede realizar, se invoca la función '_handle_error()' para manejar el error.


   .. py:method:: add_last(element: DISClib.Utils.default.T) -> None

      *add_last()* adiciona un elemento al final del ArrayList.

      :param element: elemento que se quiere agregar a la estructura.
      :type element: T

      :raises Exception: si la operación no se puede realizar, se invoca la función '_handle_error()' para manejar el error.


   .. py:method:: add_element(element: DISClib.Utils.default.T, pos: int) -> None

      *add_element()* adiciona un elemento en una posición dada del ArrayList.

      :param element: elemento que se quiere agregar a la estructura.
      :type element: T
      :param pos: índice en la que se quiere agregar el elemento.
      :type pos: int

      :raises IndexError: error si la posición es inválida.
      :raises IndexError: error si la estructura está vacía.


   .. py:method:: get_first() -> DISClib.Utils.default.T

      *get_first()* lee el primer elemento del ArrayList.

      :raises Exception: error si la estructura está vacía.

      :returns: el primer elemento del ArrayList.
      :rtype: T


   .. py:method:: get_last() -> DISClib.Utils.default.T

      *get_last()* lee el último elemento del ArrayList.

      :raises Exception: error si la estructura está vacía.

      :returns: el ultimo elemento del ArrayList.
      :rtype: T


   .. py:method:: get_element(pos: int) -> DISClib.Utils.default.T

      *get_element()* lee un elemento en una posición dada del ArrayList.

      Args:._size-1
          pos (int): índice en la que se quiere agregar el elemento.

      :raises Exception: error si la estructura está vacía.
      :raises Exception: error si la posición es inválida.

      :returns: el elemento en la posición dada del ArrayList.
      :rtype: T


   .. py:method:: remove_first() -> DISClib.Utils.default.T

      *remove_first()* elimina el primer elemento del ArrayList.

      :raises Exception: error si la estructura está vacía.

      :returns: el primer elemento eliminado del ArrayList.
      :rtype: T


   .. py:method:: remove_last() -> DISClib.Utils.default.T

      *remove_last()* elimina el último elemento del ArrayList.

      :raises Exception: error si la estructura está vacía.

      :returns: el ultimo elemento eliminado del ArrayList.
      :rtype: T


   .. py:method:: remove_element(pos: int) -> DISClib.Utils.default.T

      *remove_element()* elimina un elemento en una posición dada del ArrayList.

      :param pos: índice del que se quiere eliminar el elemento.
      :type pos: int

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si la posición es inválida.

      :returns: el elemento eliminado del ArrayList.
      :rtype: T


   .. py:method:: compare_elements(elem1: DISClib.Utils.default.T, elem2: DISClib.Utils.default.T) -> int

      *compare_elements()* compara dos elementos dentro del ArrayList según la función de comparación definida por el usuario o la función por defecto.

      :param elem1: Primer elemento a comparar.
      :type elem1: T
      :param elem2: Segundo elemento a comparar.
      :type elem2: T

      :raises TypeError: error si la función de comparación no está definida.

      :returns: -1 si elem1 es menor que elem2, 0 si son iguales, 1 si elem1 es mayor que elem2.
      :rtype: int


   .. py:method:: is_present(element: DISClib.Utils.default.T) -> int

      *is_present()* revisa si un elemento está en el ArrayList.

      :param element: elemento que se quiere revisar en el ArrayList.
      :type element: T

      :returns: la posición del elemento en el ArrayList, -1 si no está.
      :rtype: int


   .. py:method:: change_info(new_info: DISClib.Utils.default.T, pos: int) -> None

      *change_info()* cambia la información de un elemento en una posición dada.

      :param new_info: nueva información que se quiere agregar en el elemento.
      :type new_info: T
      :param pos: posición del elemento que se quiere cambiar.
      :type pos: int

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si la posición es inválida.


   .. py:method:: exchange(pos1: int, pos2: int) -> None

      *exchange()* intercambia la información de dos elementos en dos posiciones dadas.

      :param pos1: posición del primer elemento.
      :type pos1: int
      :param pos2: posición del segundo elemento.
      :type pos2: int

      :raises Exception: error si la estructura está vacía.
      :raises Exception: error si la posición del primer elemento es inválida.
      :raises Exception: error si la posición del segundo elemento es inválida.


   .. py:method:: sublist(start: int, end: int) -> ArrayList[T]

      *sublist()* crea una sublista de la estructura según unas posiciones dentro del ArrayList original.

      :param start: índice inicial de la sublista.
      :type start: int
      :param end: índice final de la sublista.
      :type end: int

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si la posición inicial o final son inválidas.

      :returns: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
      :rtype: ArrayList[T]


   .. py:method:: concat(other: ArrayList[T]) -> ArrayList[T]

      *concat()* concatena dos estructuras de datos ArrayList para crear una nueva estructura con los elementos de las dos estructuras.

      :param other: estructura de datos ArrayList que se quiere concatenar con la estructura original.
      :type other: ArrayList[T]

      :raises TypeError: error si la estructura que se quiere concatenar no es un ArrayList.
      :raises TypeError: error si la llave de la estructura que se quiere unir no es la misma que la llave de la estructura original.
      :raises TypeError: error si la función de comparación de la estructura que se quiere unir no es la misma que la función de comparación de la estructura original.

      :returns: Estructura de datos original ArrayList que contiene los elementos de las dos estructuras originales.
      :rtype: ArrayList[T]


   .. py:method:: __iter__()

      *__iter__* iterador intervinido la función nativa __iter__ para recorrer un ArrayList dentro de un ciclo 'for' de python.

      :returns: iterador Python sobre los elementos del ArrayList.
      :rtype: __iter__


   .. py:method:: __len__() -> int

      *__len__* función nativa intervenida que devuelve el tamaño del
      ArrayList.

      :returns: tamaño del ArrayList.
      :rtype: int



.. py:class:: SingleLinked


   Bases: :py:obj:`Generic`\ [\ :py:obj:`DISClib.Utils.default.T`\ ]

   *SingleLinked* Clase que representa una estructura de datos de tipo SingleLinked con la anotación '@dataclass' de python y el decorador 'Generic[T]' para indicar que es una estructura de datos genérica.

   :param Generic: TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) que representa un SingleLinked o Lista Sensillamente Encadenada.
   :type Generic: T

   :returns: ADT de tipo SingleLinked o Lista Sensillamente Encadenada.
   :rtype: SingleLinked

   .. py:attribute:: iodata
      :type: Optional[List[DISClib.Utils.default.T]]

      Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.

   .. py:attribute:: first
      :type: Optional[DISClib.DataStructures.listnode.SingleNode[DISClib.Utils.default.T]]

      Atributo publico que representa el primer nodo del SingleLinked.

   .. py:attribute:: last
      :type: Optional[DISClib.DataStructures.listnode.SingleNode[DISClib.Utils.default.T]]

      Atributo publico que representa el último nodo del SingleLinked.

   .. py:attribute:: _size
      :type: int
      :value: 0

      Atributo privado que representa el tamaño de la estructura, por defecto es 0.

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[DISClib.Utils.default.T, DISClib.Utils.default.T], int]]

      Función de comparación opcional que se utiliza para comparar los elementos del ArrayList, por defecto es 'None' y el __post_init__ configura la función por defecto lt_default_cmp_funcion().

   .. py:attribute:: key
      :type: Optional[str]

      Nombre de la llave opcional que se utiliza para comparar los elementos del ArrayList, Por defecto es 'None' y el __post_init__ configura la llave por defecto la llave 'id' en DEFAULT_DICT_KEY.

   .. py:method:: __post_init__() -> None

      *__post_init__()* configura los valores por defecto para la llave (key) y la función de comparación (cmp_function). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del SingleLinked.



   .. py:method:: default_cmp_function(elm1, elm2) -> int

      *default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el SingleLinked. Es una función crucial para que la estructura de datos funcione correctamente.

      :param elm1: primer elemento a comparar.
      :type elm1: Any
      :param elm2: segundo elemento a comparar.
      :type elm2: Any

      :returns: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      *_handle_error()* función privada que maneja los errores que se pueden presentar en el SingleLinked.

      Si se presenta un error en el SingleLinked, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

      :param err: Excepción que se generó en el SingleLinked.
      :type err: Exception


   .. py:method:: _check_type(element: DISClib.Utils.default.T) -> bool

      *_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al SingleLinked sea del mismo tipo contenido dentro de los elementos del SingleLinked.

      :raises TypeError: error si el tipo de dato del elemento que se quiere
      :raises agregar no es el mismo que el tipo de dato de los elementos que ya contiene el SingleLinked.:

      :param element: elemento que se quiere procesar en SingleLinked.
      :type element: T

      :returns: operador que indica si el ADT SingleLinked es del mismo tipo que el elemento que se quiere procesar.
      :rtype: bool


   .. py:method:: is_empty() -> bool

      *is_empty()* revisa si el SingleLinked está vacía.

      :returns: operador que indica si la estructura SingleLinked está vacía.
      :rtype: bool


   .. py:method:: size() -> int

      *size()* devuelve el numero de elementos que actualmente contiene el SingleLinked.

      :returns: tamaño de la estructura SingleLinked.
      :rtype: int


   .. py:method:: add_first(element: DISClib.Utils.default.T) -> None

      *add_first()* adiciona un elemento al inicio del SingleLinked.

      :param element: elemento que se quiere agregar a la estructura.
      :type element: T

      :raises Exception: si la operación no se puede realizar, se invoca la función '_handle_error()' para manejar el error.


   .. py:method:: add_last(element: DISClib.Utils.default.T) -> None

      *add_last()* adiciona un elemento al final del SingleLinked.

      :param element: elemento que se quiere agregar a la estructura.
      :type element: T

      :raises Exception: si la operación no se puede realizar, se invoca la función '_handle_error()' para manejar el error.


   .. py:method:: add_element(element: DISClib.Utils.default.T, pos: int) -> None

      *add_element()* adiciona un elemento en una posición dada del SingleLinked.

      :param element: elemento que se quiere agregar a la estructura.
      :type element: T
      :param pos: índice en la que se quiere agregar el elemento.
      :type pos: int

      :raises IndexError: error si la posición es inválida.
      :raises IndexError: error si la estructura está vacía.


   .. py:method:: get_first() -> Optional[DISClib.Utils.default.T]

      *get_first()* lee el primer elemento del SingleLinked.

      :raises Exception: error si la estructura está vacía.

      :returns: el primer elemento del SingleLinked.
      :rtype: Optional[T]


   .. py:method:: get_last() -> Optional[DISClib.Utils.default.T]

      *get_last()* lee el último elemento del SingleLinked.

      :raises Exception: error si la estructura está vacía.

      :returns: el ultimo elemento del SingleLinked.
      :rtype: Optional[T]


   .. py:method:: get_element(pos: int) -> Optional[DISClib.Utils.default.T]

      *get_element()* lee un elemento en una posición dada del SingleLinked.

      :param pos: índice en la que se quiere agregar el elemento.
      :type pos: int

      :raises Exception: error si la estructura está vacía.
      :raises Exception: error si la posición es inválida.

      :returns: el elemento en la posición dada del SingleLinked.
      :rtype: Optional[T]


   .. py:method:: remove_first() -> Optional[DISClib.Utils.default.T]

      *remove_first()* elimina el primer elemento del SingleLinked.

      :raises Exception: error si la estructura está vacía.

      :returns: el primer elemento eliminado del SingleLinked.
      :rtype: Optional[T]


   .. py:method:: remove_last() -> Optional[DISClib.Utils.default.T]

      *remove_last()* elimina el último elemento del SingleLinked.

      :raises Exception: error si la estructura está vacía.

      :returns: el ultimo elemento eliminado del SingleLinked.
      :rtype: Optional[T]


   .. py:method:: remove_element(pos: int) -> Optional[DISClib.Utils.default.T]

      *remove_element()* elimina un elemento en una posición dada del SingleLinked.

      :param pos: índice del que se quiere eliminar el elemento.
      :type pos: int

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si la posición es inválida.

      :returns: el elemento eliminado del SingleLinked.
      :rtype: Optional[T]


   .. py:method:: compare_elements(elem1: DISClib.Utils.default.T, elem2: DISClib.Utils.default.T) -> int

      *compare_elements()* compara dos elementos dentro del SingleLinked según la función de comparación definida por el usuario o la función por defecto.

      :param elem1: Primer elemento a comparar.
      :type elem1: T
      :param elem2: Segundo elemento a comparar.
      :type elem2: T

      :raises TypeError: error si la función de comparación no está definida.

      :returns: -1 si elem1 es menor que elem2, 0 si son iguales, 1 si elem1 es mayor que elem2.
      :rtype: int


   .. py:method:: is_present(element: DISClib.Utils.default.T) -> int

      *is_present()* revisa si un elemento está en el SingleLinked.

      :param element: elemento que se quiere revisar en el SingleLinked.
      :type element: T

      :returns: la posición del elemento en el SingleLinked, -1 si no está.
      :rtype: int


   .. py:method:: change_info(new_info: DISClib.Utils.default.T, pos: int) -> None

      *change_info()* cambia la información de un elemento en una posición dada.

      :param new_info: nueva información que se quiere agregar en el elemento.
      :type new_info: T
      :param pos: posición del elemento que se quiere cambiar.
      :type pos: int

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si la posición es inválida.


   .. py:method:: exchange(pos1: int, pos2: int) -> None

      *exchange()* intercambia la información de dos elementos en dos posiciones dadas.

      :param pos1: posición del primer elemento.
      :type pos1: int
      :param pos2: posición del segundo elemento.
      :type pos2: int

      :raises Exception: error si la estructura está vacía.
      :raises Exception: error si la posición del primer elemento es inválida.
      :raises Exception: error si la posición del segundo elemento es inválida.


   .. py:method:: sublist(start: int, end: int) -> SingleLinked[T]

      *sublist()* crea una sublista de la estructura según unas posiciones dentro del SingleLinked original.

      :param start: índice inicial de la sublista.
      :type start: int
      :param end: índice final de la sublista.
      :type end: int

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si la posición inicial o final son inválidas.

      :returns: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
      :rtype: SingleLinked[T]


   .. py:method:: concat(other: SingleLinked[T]) -> SingleLinked[T]

      *concat()* concatena dos estructuras de datos SingleLinked para crear una nueva estructura con los nodos de las dos estructuras.

      :param other: estructura de datos SingleLinked que se quiere concatenar con la estructura original.
      :type other: SingleLinked[T]

      :raises TypeError: error si la estructura que se quiere concatenar no es un SingleLinked.
      :raises TypeError: error si la llave de la estructura que se quiere unir no es la misma que la llave de la estructura original.
      :raises TypeError: error si la función de comparación de la estructura que se quiere unir no es la misma que la función de comparación de la estructura original.

      :returns: Estructura de datos SingleLinked original que contiene los elementos de las dos estructuras originales.
      :rtype: SingleLinked[T]


   .. py:method:: __iter__()

      *__iter__* iterador intervinido la función nativa __iter__ para recorrer un SingleLinked dentro de un ciclo 'for' de python.

      :returns: iterador sobre los elementos del SingleLinked.
      :rtype: iterator


   .. py:method:: __len__() -> int

      *__len__* función nativa intervenida que devuelve el tamaño del SingleLinked.

      :returns: tamaño del SingleLinked.
      :rtype: int



.. py:data:: file_path

   

.. py:data:: file_dir

   

