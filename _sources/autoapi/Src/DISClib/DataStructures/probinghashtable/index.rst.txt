:py:mod:`Src.DISClib.DataStructures.probinghashtable`
=====================================================

.. py:module:: Src.DISClib.DataStructures.probinghashtable

.. autoapi-nested-parse::

   Este ADT representa una tabla de hash con el método de sondeo lineal (**LinearProbing**). Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

   En particular tiene funciones para encontrar espacio (*slots*) y registros (pareja llave-valor) disponibles en la tabla en caso de colisiones segun el metodo de sondeo lineal.

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.probinghashtable.LinearProbing




Attributes
~~~~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.probinghashtable.DEFAULT_PROBING_ALPHA
   Src.DISClib.DataStructures.probinghashtable.MAX_PROBING_ALPHA
   Src.DISClib.DataStructures.probinghashtable.MIN_PROBING_ALPHA
   Src.DISClib.DataStructures.probinghashtable.EMPTY


.. py:data:: DEFAULT_PROBING_ALPHA
   :type: float
   :value: 0.5

   Factor de carga (*alpha*) por defecto e ideal para el *LinearProbing*, por defecto es 0.50.

.. py:data:: MAX_PROBING_ALPHA
   :type: float
   :value: 0.8

   Factor de carga (*alpha*) máximo para el *LinearProbing*, por defecto es 0.80.

.. py:data:: MIN_PROBING_ALPHA
   :type: float
   :value: 0.2

   Factor de carga (*alpha*) mínimo para el *LinearProbing*, por defecto es 0.20

.. py:data:: EMPTY
   :value: '__EMPTY__'

   Constante que representa un registro vacío en el *LinearProbing*, por defecto es "__EMPTY__".

.. py:class:: LinearProbing


   Bases: :py:obj:`Generic`\ [\ :py:obj:`Src.DISClib.Utils.default.T`\ ]

   **LinearProbing** representa la estructura de datos de una tabla de hash con el método de encadenamiento por separación (*LinearProbing*). En la estructura la información se almacena en registros (parejas llave-valor) donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato. El indice es un *ArrayList* donde cada elemento es un espacio (*slot*) de la tabla de hash, y cada espacio (*slot*) contiene un registro *MapEntry* (pareja llave-valor) o está vacío (None | EMPTY

   :param Generic: TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
   :type Generic: T

   :returns: ADT de tipo *LinearProbing* o tabla de hash con separación por encadenamiento.
   :rtype: LinearProbing

   .. py:attribute:: iodata
      :type: Optional[List[Src.DISClib.Utils.default.T]]

      Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.

   .. py:attribute:: rehashable
      :type: bool
      :value: True

      Es el operador que indica si la tabla de hash se puede reconstruir utilizando el método de *rehash*, por defecto es 'True'.

   .. py:attribute:: nentries
      :type: int
      :value: 1

      espacio inicial reservado para la tabla de hash (n), por defecto es 1, pero debe configurarse según el número de entradas que se espera almacenar.

      *Nota*: el espacio reservado (n) no es la capacidad (M) de la tabla de hash.

   .. py:attribute:: mcapacity
      :type: int
      :value: 2

      Es la capacidad (M) con la que se inicializa la tabla de hash.

   .. py:attribute:: alpha
      :type: Optional[float]

      Es el factor de carga (*alpha*) con el que se inicializa la tabla de hash, por defecto es 0.50.

      *Nota*: alpha = n/M (n: número de entradas esperadas, M: capacidad de la tabla de hash).

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], int]]

      Función de comparación personalizable por el usuario para reconocer los registros (pareja llave-valor) dentro del *LinearProbing*. Por defecto es la función *lt_default_cmp_funcion()* propia de *DISClib*, puede ser un parametro al crear la estructura.

   .. py:attribute:: hash_table
      :type: Src.DISClib.DataStructures.arraylist.ArrayList[Src.DISClib.DataStructures.mapentry.MapEntry[Src.DISClib.Utils.default.T]]

      Es el indice de la tabla Hash donde se almacenan los *Buckets*. Por defecto es un *ArrayList* vacío que se inicializa con la capacidad (M) configurada.

   .. py:attribute:: key
      :type: Optional[str]

      Nombre de la llave personalizable por el usuario utilizada para reconocer los registros (pareja llave-valor) dentro del *LinearProbing*. Por defecto es la llave de diccionario (*dict*) *DEFAULT_DICT_KEY = 'id'* propia de *DISClib*, puede ser un parametro al crear la estructura.

   .. py:attribute:: prime
      :type: Optional[int]

      Es el número entero primo (P) utilizado para calcular el hash para la llave de la tabla utilizando la función de compresión MAD. Por defecto es 109345121 definido en el parametro *DEFAULT_PRIME* propio de *DISClib*.

      *Nota:* la función MAD es: *h(k) = ((a*k + b) mod P) mod M*, donde *a* y *b* son números enteros aleatorios, *P* es un número primo y *M* es la capacidad de la tabla de hash.

   .. py:attribute:: _scale
      :type: Optional[int]
      :value: 0

      Es el número entero propio de la estructura utilizado como pendiente (a) en la función MAD para calcular el código hash de la llave.

   .. py:attribute:: _shift
      :type: Optional[int]
      :value: 0

      Es el número entero propio de la estructura utilizado como desplazamiento (b) de la función MAD para calcular el código hash de la llave.

   .. py:attribute:: _cur_alpha
      :type: Optional[float]
      :value: 0

      Es el factor de carga (*alpha*) actual de la tabla de hash.

   .. py:attribute:: min_alpha
      :type: Optional[float]

      Es el factor de carga (*alpha*) mínimo de la tabla de hash, por defecto es 0.20 definido en el parametro *MIN_PROBING_ALPHA* propio de *DISClib*.

   .. py:attribute:: max_alpha
      :type: Optional[float]

      Es el factor de carga máximo de la tabla de hash, por defecto es 0.80 definido en el parametro *MAX_PROBING_ALPHA* propio de *DISClib*.

   .. py:attribute:: _size
      :type: int
      :value: 0

      Es el número de entradas (n) que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.

   .. py:attribute:: _collisions
      :type: Optional[int]
      :value: 0

      Es el número entero para contar las colisiones en la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.

   .. py:attribute:: _key_type
      :type: Optional[type]

      Es el tipo de dato para las llaves de los registros (pareja llave-valor) que contiene la tabla de hash, por defecto es *None* y se configura al cargar la primer registro.

   .. py:attribute:: _value_type
      :type: Optional[type]

      Es el tipo de dato para los valores de los registros (pareja llave-valor) que contiene la tabla de hash, por defecto es *None* y se configura al cargar la primer registro.

   .. py:method:: __post_init__() -> None

      *__post_init__()* configura los parametros personalizados por el usuario al crear el *LinearProbing*. En caso de no estar definidos, se asignan los valores por defecto, puede cargar listas nativas con el parametro *iodata* de python dentro de la estructura.



   .. py:method:: default_cmp_function(key1, entry2: Src.DISClib.DataStructures.mapentry.MapEntry) -> int

      *default_cmp_function()* es la función de comparación por defecto para comparar la llave de un elemento vs. el registro (pareja llave-valor) o *MapEntry* que se desea agregar al *LinearProbing*, es una función crucial para que la estructura funcione correctamente.

      :param key1: llave (*key*) de la primer registro a comparar.
      :type key1: Any
      :param entry2: segundo registro (pareja llave-valor) a comparar.
      :type entry2: MapEntry

      :returns: respuesta de la comparación entre los elementos, 0 si las llaves (*key*) son iguales, 1 si key1 es mayor que la llave (*key*) de entry2, -1 si key1 es menor.
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      *_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *LinearProbing*.

      Si se presenta un error en *LinearProbing*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DISCLib* para manejarlo segun se considere conveniente el usuario.

      :param err: Excepción que se generó en el *LinearProbing*.
      :type err: Exception


   .. py:method:: _check_type(entry: Src.DISClib.DataStructures.mapentry.MapEntry) -> bool

      *_check_type()* función propia de la estructura que revisa si el tipo de dato del registro (pareja llave-valor) que se desea agregar al *LinearProbing* es del mismo tipo contenido dentro de los *MapEntry* del *LinearProbing*.

      :param element: elemento que se desea procesar en *LinearProbing*.
      :type element: T

      :raises TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *LinearProbing*.

      :returns: operador que indica si el ADT *LinearProbing* es del mismo tipo que el elemento que se desea procesar.
      :rtype: bool


   .. py:method:: is_empty() -> bool

      *is_empty()* revisa si el *LinearProbing* está vacío.

      :returns: operador que indica si la estructura *LinearProbing* está vacía.
      :rtype: bool


   .. py:method:: size() -> int

      *size()* devuelve el numero de entradas *MapEntry* que actualmente contiene el *LinearProbing*.

      :returns: tamaño de la estructura *LinearProbing*.
      :rtype: int


   .. py:method:: contains(key: Src.DISClib.Utils.default.T) -> bool

      *contains()* responde si el *LinearProbing* contiene un registro *MapEntry* con la llave *key*.

      :param key: llave del registro (pareja llave-valor) que se desea buscar en el *LinearProbing*.
      :type key: T

      :raises IndexError: error si la estructura está vacía.

      :returns: operador que indica si el *LinearProbing* contiene o no un registro con la llave *key*.
      :rtype: bool


   .. py:method:: put(key: Src.DISClib.Utils.default.T, value: Src.DISClib.Utils.default.T) -> None

      *put()* agrega una nuevo registro *MapEntry* al *LinearProbing*, si la llave *key* ya existe en el *LinearProbing* se reemplaza su valor *value*.

      :param key: llave asociada la nuevo *MapEntry*.
      :type key: T
      :param value: el valor asociado al nuevo *MapEntry*.
      :type value: T

      :raises Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.


   .. py:method:: get(key: Src.DISClib.Utils.default.T) -> Optional[Src.DISClib.DataStructures.mapentry.MapEntry]

      *get()* recupera el registro *MapEntry* cuya llave *key* sea ogial a la que se encuentre dentro del *LinearProbing*, si no existe un registro con la llave, devuelve *None*.

      :param key: llave asociada al *MapEntry* que se desea buscar.
      :type key: T

      :raises IndexError: error si la estructura está vacía.

      :returns: *MapEntry* asociado a la llave *key* que se desea. *None* si no se encuentra.
      :rtype: Optional[MapEntry]


   .. py:method:: check_slots(key: Src.DISClib.Utils.default.T) -> Optional[Src.DISClib.DataStructures.singlelinkedlist.SingleLinked[Src.DISClib.DataStructures.mapentry.MapEntry]]

      *check_slots()* recupera la lista (*SingleLinked*) de registros (parejas llave-valor) asociadas a la llave *key* dentro del *LinearProbing*. Recupera los *MapEntry* con el mismo hash y si no existe, devuelve *None*.

      :param key: llave asociada a los *MapEntry* y *Slots* que se desean buscar.
      :type key: T

      :raises Exception: error si la estructura está vacía.

      :returns: lista sencillamente encadenada (*SingleLinked*) con todas los *MapEntry* asociados a la llave *key* dentro del *LinearProbing*.
      :rtype: Optional[SingleLinked[MapEntry]]


   .. py:method:: remove(key: Src.DISClib.Utils.default.T) -> Optional[Src.DISClib.Utils.default.T]

      *remove()* elimina el registro *MapEntry* cuya llave *key* sea igual a la que se encuentre dentro del *LinearProbing*, si no existe un registro con la llave, genera un error.

      :param key: llave asociada al *MapEntry* que se desea eliminar.
      :type key: T

      :raises IndexError: error si la estructura está vacía.
      :raises IndexError: error si el registro que se desea eliminar no existe dentro del *LinearProbing*.

      :returns: registro *MapEntry* que se eliminó del *LinearProbing*. *None* si no existe el registro asociada a la llave *key*.
      :rtype: Optional[MapEntry]


   .. py:method:: keys() -> Src.DISClib.DataStructures.singlelinkedlist.SingleLinked[Src.DISClib.Utils.default.T]

      *keys()* devuelve una lista (*SingleLinked*) con todas las llaves (*key*) de los registros (*MapEntry*) del *LinearProbing*.

      :returns: lista (*SingleLinked*) con todas las llaves (*key*) del *LinearProbing*.
      :rtype: SingleLinked[T]


   .. py:method:: values() -> Src.DISClib.DataStructures.singlelinkedlist.SingleLinked[Src.DISClib.Utils.default.T]

      *values()* devuelve una lista (*SingleLinked*) con todos los valores de los registros (*MapEntry*) del *LinearProbing*.

      :returns: lista (*SingleLinked*) con todos los valores (*value*) del *LinearProbing*.
      :rtype: SingleLinked[T]


   .. py:method:: entries() -> Src.DISClib.DataStructures.singlelinkedlist.SingleLinked[Src.DISClib.Utils.default.T]

      *entries()* devuelve una lista (*SingleLinked*) con tuplas de todas los registros (*MapEntry*) del *LinearProbing*. Cada tupla contiene en la primera posición la llave (*key*) y en la segunda posición el valor (*value*) del registro.

      :returns: lista (*SingleLinked*) de tuplas con todas los registros del *LinearProbing*.
      :rtype: SingleLinked[T]


   .. py:method:: _find_slot(hkey: int, key: Src.DISClib.Utils.default.T) -> int

      *_find_slot()* encuentra el indice del registro *MapEtry* en el *LinearProbing*, si el registro no existe, devuelve el indice del primer registro disponible.

      :param hkey: indice del registro (pareja llave-valor) en el *LinearProbing*.
      :type hkey: int
      :param key: llave del registro (pareja llave-valor) que se desea buscar.
      :type key: T

      :returns: devuelve el indice negativo si encuentra espacio disponible (None | EMPTY) o si el registro no existe, devuelve el indice positivo si el registro existe.
      :rtype: int


   .. py:method:: _is_available(entry: Src.DISClib.DataStructures.mapentry.MapEntry) -> bool

      *_is_available()* permite verificar si un registro *MapEntry* está disponible en el *LinearProbing*. Es decir si la llave es nula (None) o vacía (EMPTY).

      :param entry: registro (pareja llave-valor) que se desea verificar.
      :type entry: MapEntry

      :returns: operador que indica si el registro está disponible o no en el *LinearProbing*.
      :rtype: bool


   .. py:method:: rehash() -> None

      *rehash()* reconstruye la tabla de hash con una nueva capacidad (*M*) y un nuevo factor de carga (*alpha*) según los límites configurados por los parametros *max_alpha* y *min_alpha*.

      Si el factor de carga (*alpha*) es mayor que el límite superior (*max_alpha*), se duplica la capacidad (*M*) buscando el siguiente número primo (*P*) reconstruyendo la tabla.

      Si el factor de carga (*alpha) es menor que el límite inferior (*min_alpha*), se reduce a la mitad la capacidad (*M*) de la tabla buscando el siguiente número primo (*P*) reconstruyendo la tabla.


   .. py:method:: __len__() -> int

      *__len__()* función nativa de Python personalizada para el *LinearProbing*. Permite utilizar la función *len()* de Python para recuperar el tamaño del *LinearProbing*.

      :returns: tamaño del *LinearProbing*.
      :rtype: int



