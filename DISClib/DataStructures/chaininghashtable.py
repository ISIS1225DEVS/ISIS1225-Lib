"""
Este ADT representa una tabla de hash con el método de encadenamiento por de separación (**SeparateChaining**). Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

Ademas, contiene la estructura **Bucket** basada en una lista sencillamente enlazada (*SingleLinked*) donde se almacenan los registros (parejas llave-valor) que sufren colisiones en la tabla de hash.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# native python modules
# import dataclass to define the hash table
from dataclasses import dataclass, field
# import modules for defining the entries type in the hash table
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect
# random module for the MAD compression function
import random

# custom modules
# generic error handling and type checking
from DISClib.DataStructures.mapentry import MapEntry
from DISClib.DataStructures.arraylist import ArrayList
from DISClib.DataStructures.singlelinkedlist import SingleLinked
# util functions for the hash table
from DISClib.Utils.numbers import next_prime
from DISClib.Utils.numbers import hash_compress
from DISClib.Utils.error import error_handler
# default cmp function for the hash table
from DISClib.Utils.default import ht_default_cmp_funcion
# default data type for the hash table
from DISClib.Utils.default import T
from DISClib.Utils.default import VALID_DATA_TYPE_LT
from DISClib.Utils.default import DEFAULT_DICT_KEY
from DISClib.Utils.default import VALID_IO_TYPE
from DISClib.Utils.default import DEFAULT_PRIME


# checking custom modules
assert MapEntry
assert ArrayList
assert SingleLinked
assert next_prime
assert hash_compress
assert error_handler
assert ht_default_cmp_funcion
assert T
assert VALID_DATA_TYPE_LT
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE
assert DEFAULT_PRIME

# default load factor for separating chaining
# :data: DEFAULT_CHAINING_ALPHA
DEFAULT_CHAINING_ALPHA: float = 4.0
"""
Factor de carga (*alpha*) por defecto e ideal para el *SeparateChaining*, por defecto es 4.0.
"""

# :data: MAX_CHAINING_ALPHA
MAX_CHAINING_ALPHA: float = 8.0
"""
Factor de carga (*alpha*) máximo para el *SeparateChaining*, por defecto es 8.0.
"""

# :data: MIN_CHAINING_ALPHA
MIN_CHAINING_ALPHA: float = 2.0
"""
Factor de carga (*alpha*) mínimo para el *SeparateChaining*, por defecto es 2.0.
"""


@dataclass
class Bucket(SingleLinked, Generic[T]):
    """**Bucket** representa un bucket de una tabla de hash con el método de encadenamiento por separación (Separate Chaining). La estructura esta basada (hereda) en una lista sencillamente enlazada (*SingleLinked*) de *DISCLib*.

    Clase que representa un bucket de una tabla de hash. Esta clase hereda de la clase SingleLinked de DISCLib para representar un bucket de una tabla de hash con el método de encadenamiento por separación (Separate Chaining).

    Args:
        SingleLinked (T): Lista sencillamente encadenada para representar un *Bucket* en *SeparateChaining*. Hereda de *SingleLinked*.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
    """
    # the same as ..
    pass


@dataclass
class SeparateChaining(Generic[T]):
    """**SeparateChaining** representa la estructura de datos de una tabla de hash con el método de encadenamiento por separación (*SeparateChaining*). En la estructura la información se almacena en registros (parejas llave-valor) donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato. El indice es un *ArrayList* donde cada elemento es un *Bucket* que contiene los registros *MapEntry* que sufren colisiones en la tabla de hash.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        SeparateChaining: ADT de tipo *SeparateChaining* o tabla de hash con separación por encadenamiento.
    """
    # input tuples from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.
    """

    # boolean to indicate if the hash table can be rehashed
    # :attr: rehashable
    rehashable: bool = True
    """
    Es el operador que indica si la tabla de hash se puede reconstruir utilizando el método de *rehash*, por defecto es 'True'.
    """

    # reserved space for the hash table
    # :attr: nentries
    nentries: int = 1
    """
    espacio inicial reservado para la tabla de hash (n), por defecto es 1, pero debe configurarse según el número de entradas que se espera almacenar.

    *Nota*: el espacio reservado (n) no es la capacidad (M) de la tabla de hash.
    """

    # starting capacity (M|m) for the hash table
    # :attr: mcapacity
    mcapacity: int = 1
    """
    Es la capacidad (M) con la que se inicializa la tabla de hash.
    """

    # starting load factor (alpha) for the hash table
    # :attr: alpha
    alpha: Optional[float] = DEFAULT_CHAINING_ALPHA
    """
    Es el factor de carga (*alpha*) con el que se inicializa la tabla de hash, por defecto es 4.0.

    *Nota*: alpha = n/M (n: número de entradas esperadas, M: capacidad de la tabla de hash).
    """

    # the cmp_function is used to compare emtries, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación personalizable por el usuario para reconocer los registros (pareja llave-valor) dentro del *SeparateChaining*. Por defecto es la función *lt_default_cmp_funcion()* propia de *DISClib*, puede ser un parametro al crear la estructura.
    """

    # actual place to store the entries in the hash table
    # :attr: hash_table
    hash_table: ArrayList[Bucket[T]] = field(default_factory=ArrayList)

    """
    Es el indice de la tabla Hash donde se almacenan los *Buckets*. Por defecto es un *ArrayList* vacío que se inicializa con la capacidad (M) configurada.
    """
    # the key is used to compare entries, not defined by default
    # :attr: key
    key: Optional[str] = DEFAULT_DICT_KEY
    """
    Nombre de la llave personalizable por el usuario utilizada para reconocer los registros (pareja llave-valor) dentro del *SeparateChaining*. Por defecto es la llave de diccionario (*dict*) *DEFAULT_DICT_KEY = 'id'* propia de *DISClib*, puede ser un parametro al crear la estructura.
    """

    # prime number (P) for the MAD compression function
    # :attr: prime
    prime: Optional[int] = DEFAULT_PRIME
    """
    Es el número entero primo (P) utilizado para calcular el hash para la llave de la tabla utilizando la función de compresión MAD. Por defecto es 109345121 definido en el parametro *DEFAULT_PRIME* propio de *DISClib*.

    *Nota:* la función MAD es: *h(k) = ((a*k + b) mod P) mod M*, donde *a* y *b* son números enteros aleatorios, *P* es un número primo y *M* es la capacidad de la tabla de hash.
    """

    # private scale (a) factor for the mad compression function
    # :attr: _scale
    _scale: Optional[int] = 0
    """
    Es el número entero propio de la estructura utilizado como pendiente (a) en la función MAD para calcular el código hash de la llave.
    """
    # private shift (b) factor for the mad compression function
    # :attr: _shift
    _shift: Optional[int] = 0
    """
    Es el número entero propio de la estructura utilizado como desplazamiento (b) de la función MAD para calcular el código hash de la llave.
    """

    # current factor (alpha) for the working hash table
    # :attr: _cur_alpha
    _cur_alpha: Optional[float] = 0.0
    """
    Es el factor de carga (*alpha*) actual de la tabla de hash.
    """

    # minimum load factor (alpha) for the hash table
    # :attr: min_alpha
    min_alpha: Optional[float] = MIN_CHAINING_ALPHA
    """
    Es el factor de carga (*alpha*) mínimo de la tabla de hash, por defecto es 2.0 definido en el parametro *MIN_CHAINING_ALPHA* propio de *DISClib*.
    """

    # maximum load factor (alpha) for the hash table
    # :attr: max_alpha
    max_alpha: Optional[float] = MAX_CHAINING_ALPHA
    """
    Es el factor de carga máximo de la tabla de hash, por defecto es 8.0 definido en el parametro *MAX_CHAINING_ALPHA* propio de *DISClib*.
    """

    # actual number of used entries (n) in the hash table
    # FIXME inconsistent use of _size and size()
    # :attr: _size
    _size: int = 0
    """
    Es el número de entradas (n) que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    # :attr: collisions
    _collisions: Optional[int] = 0
    """
    Es el número entero para contar las colisiones en la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    # the type of the entry keys in the hash table
    # :attr: _key_type
    _key_type: Optional[type] = None
    """
    Es el tipo de dato para las llaves de los registros (pareja llave-valor) que contiene la tabla de hash, por defecto es *None* y se configura al cargar la primer registro.
    """

    # the type of the entry values in the hash table
    # :attr: _value_type
    _value_type: Optional[type] = None
    """
    Es el tipo de dato para los valores de los registros (pareja llave-valor) que contiene la tabla de hash, por defecto es *None* y se configura al cargar la primer registro.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los parametros personalizados por el usuario al crear el *SeparateChaining*. En caso de no estar definidos, se asignan los valores por defecto, puede cargar listas nativas con el parametro *iodata* de python dentro de la estructura.
        """
        try:
            # setting capacity
            self.mcapacity = next_prime(self.nentries // self.alpha)
            # setting scale and shift for MAD compression function
            self._scale = random.randint(1, self.prime - 1)
            self._shift = random.randint(0, self.prime - 1)
            # setting the default compare function
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function

            # initializing new hash table
            self.hash_table = ArrayList(cmp_function=self.cmp_function,
                                        key=self.key)
            i = 0
            # bulding buckets in the hash table
            while i < self.mcapacity:
                # bucket is a SingleLinked list
                bucket = Bucket(cmp_function=self.cmp_function,
                                key=self.key)
                # add the bucket to the hash table
                self.hash_table.add_last(bucket)
                i += 1

            # setting the current load factor
            if self._cur_alpha == 0:
                self._cur_alpha = self._size / self.mcapacity

            # TODO is the best way to create the structure???
            if isinstance(self.iodata, VALID_IO_TYPE):
                # get the type of the data in the list
                # if is a dict, use the key type
                if isinstance(self.iodata[0], dict):
                    for entry in self.iodata:
                        key = entry.get(self.key)
                        self.put(key, entry)
                # otherwise, manage as data list
                else:
                    for data in self.iodata:
                        self.put(data, data)
            # clean input data
            self.iodata = None
            # TODO rethink this part
            # # fix discrepancies between size and number of entries (n).
            # if self._size != self.nentries:
            #     self.nentries = self._size
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, key1, entry2: MapEntry) -> int:
        """*default_cmp_function()* es la función de comparación por defecto para comparar la llave de un elemento vs. el registro (pareja llave-valor) o *MapEntry* que se desea agregar al *SeparateChaining*, es una función crucial para que la estructura funcione correctamente.

        Args:
            key1 (Any): llave (*key*) del primer registro a comparar.
            entry2 (MapEntry): segundo registro (pareja llave-valor) a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si las llaves (*key*) son iguales, 1 si key1 es mayor que la llave (*key*) de entry2, -1 si key1 es menor.
        """
        try:
            # using the default compare function for the key
            return ht_default_cmp_funcion(self.key, key1, entry2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *SeparateChaining*.

        Si se presenta un error en *SeparateChaining*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DISCLib* para manejarlo segun se considere conveniente el usuario.

        Args:
            err (Exception): Excepción que se generó en el *SeparateChaining*.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, entry: MapEntry) -> bool:
        """*_check_type()* función propia de la estructura que revisa si el tipo de dato del registro (pareja llave-valor) que se desea agregar al *SeparateChaining* es del mismo tipo contenido dentro de los *MapEntry* del *SeparateChaining*.

        Args:
            element (T): elemento que se desea procesar en *SeparateChaining*.

        Raises:
            TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *SeparateChaining*.

        Returns:
            bool: operador que indica si el ADT *SeparateChaining* es del mismo tipo que el elemento que se desea procesar.
        """
        # TODO check usability of this function
        # if datastruct is empty, set the entry type
        if self.is_empty():
            self._key_type = type(entry.get_key())
            self._value_type = type(entry.get_value())
            # self._data_type = type(entry)
        # check if the new entry is the same type as the other entries
        elif self._key_type is not type(entry.get_key()):
            err_msg = f"Invalid key type: {type(entry.get_key())} "
            err_msg += f"for structure configured with type: {self._key_type}"
            raise TypeError(err_msg)
        elif self._value_type is not type(entry.get_value()):
            err_msg = f"Invalid value type: {type(entry.get_value())} "
            err_msg += f"for structure configured with type: {self._value_type}"
            raise TypeError(err_msg)
        # otherwise, the type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el *SeparateChaining* está vacío.

        Returns:
            bool: operador que indica si la estructura *SeparateChaining* está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el numero de entradas *MapEntry* que actualmente contiene el *SeparateChaining*.

        Returns:
            int: tamaño de la estructura *SeparateChaining*.
        """
        # TODO change the method to @property "size"?
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def contains(self, key: T) -> bool:
        """*contains()* responde si el *SeparateChaining* contiene un registro *MapEntry* con la llave *key*.

        Args:
            key (T): llave del registro (pareja llave-valor) que se desea buscar en el *SeparateChaining*.

        Raises:
            IndexError: error si la estructura está vacía.

        Returns:
            bool: operador que indica si el *SeparateChaining* contiene o no un registro con la llave *key*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            else:
                # assume the entry is not in the structure
                found = False
                # use the MAD compression function to get the hash key
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)
                # look into the bucket
                bucket = self.hash_table.get_element(hkey)
                idx = bucket.find(key)
                # if the entry is in the bucket, return True
                if idx > -1:
                    found = True
                return found
        except Exception as err:
            self._handle_error(err)

    def put(self, key: T, value: T) -> None:
        """*put()* agrega un nuevo registro *MapEntry* al *SeparateChaining*, si la llave *key* ya existe en el *SeparateChaining* se reemplaza su valor *value*.

        Args:
            key (T): llave asociada la nuevo *MapEntry*.
            value (T): el valor asociado al nuevo *MapEntry*.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # create a new entry for the entry
            new_entry = MapEntry(key, value)
            # cheking the type of the entry
            if self._check_type(new_entry):
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)

                # checking the bucket
                bucket = self.hash_table.get_element(hkey)
                idx = bucket.find(key)
                # the entry is not in the bucket, add it and a collision
                # the entry is already in the bucket, update it
                if idx > -1:
                    bucket.change_info(new_entry, idx)
                # otherwise, is a new entry
                else:
                    if not bucket.is_empty():
                        self._collisions += 1
                    bucket.add_last(new_entry)
                    self._size += 1
                    self._cur_alpha = self._size / self.mcapacity
                # check if the structure needs to be rehashed
                if self._cur_alpha >= self.max_alpha:
                    self.rehash()
        except Exception as err:
            self._handle_error(err)

    def get(self, key: T) -> Optional[MapEntry]:
        """*get()* recupera el registro *MapEntry* cuya llave *key* sea ogial a la que se encuentre dentro del *SeparateChaining*, si no existe un registro con la llave, devuelve *None*.

        Args:
            key (T): llave asociada al *MapEntry* que se desea buscar.

        Raises:
            IndexError: error si la estructura está vacía.

        Returns:
            Optional[MapEntry]: *MapEntry* asociado a la llave *key* que se desea. *None* si no se encuentra.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            else:
                # assume the entry is not in the structure
                entry = None
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)

                # checking the bucket
                bucket = self.hash_table.get_element(hkey)
                idx = bucket.find(key)
                # if the entry is in the bucket, return it
                if idx > -1:
                    entry = bucket.get_element(idx)
                return entry
        except Exception as err:
            self._handle_error(err)

    def check_bucket(self, key: T) -> Optional[Bucket]:
        """*check_bucket()* revisa el *Bucket* asociado a la llave *key* dentro del *SeparateChaining*. Recupera todo el *Bucket* asociado a la llave y si no existe, devuelve *None*.

        Args:
            key (T): llave asociada al *Bucket* que se desea revisar

        Raises:
            IndexError: error si la estructura está vacía.

        Returns:
            Optional[Bucket]: *Bucket* asociado a la llave *key* que se desea. *None* si no se encuentra.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            else:
                # assume the entry is not in the structure
                bucket = None
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)

                # checking the bucket
                bucket = self.hash_table.get_element(hkey)
                return bucket
        except Exception as err:
            self._handle_error(err)

    def remove(self, key: T) -> Optional[MapEntry]:
        """*remove()* elimina el registro *MapEntry* cuya llave *key* sea igual a la que se encuentre dentro del *SeparateChaining*, si no existe un registro con la llave, genera un error.

        Args:
            key (T): llave asociada al *MapEntry* que se desea eliminar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si el registro que se desea eliminar no existe dentro del *SeparateChaining*.

        Returns:
            Optional[MapEntry]: registro *MapEntry* que se eliminó del *SeparateChaining*. *None* si no existe el registro asociada a la llave *key*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            else:
                entry = None
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)

                # checking the bucket
                bucket = self.hash_table.get_element(hkey)
                if not bucket.is_empty():
                    idx = bucket.find(key)
                    if idx >= 0:
                        entry = bucket.remove_element(idx)
                        self._size -= 1
                        self._cur_alpha = self._size / self.mcapacity
                    # TODO maybe i don't need this
                    else:
                        raise IndexError(f"Entry for Key: {key} not found")
            if self._cur_alpha < self.min_alpha:
                self.rehash()
            return entry
        except Exception as err:
            self._handle_error(err)

    def keys(self) -> SingleLinked[T]:
        """*keys()* devuelve una lista (*SingleLinked*) con todas las llaves (*key*) de los registros (*MapEntry*) del *SeparateChaining*.

        Returns:
            SingleLinked[T]: lista (*SingleLinked*) con todas las llaves (*key*) del *SeparateChaining*.
        """
        try:
            keys_lt = SingleLinked(key=self.key)
            # TODO improve with SingleLinked concat() method?
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        keys_lt.add_last(entry.get_key())
            return keys_lt
        except Exception as err:
            self._handle_error(err)

    def values(self) -> SingleLinked[T]:
        """*values()* devuelve una lista (*SingleLinked*) con todos los valores de los registros (*MapEntry*) del *SeparateChaining*.

        Returns:
            SingleLinked[T]: lista (*SingleLinked*) con todos los valores (*value*) del *SeparateChaining*.
        """
        try:
            values_lt = SingleLinked(key=self.key)
            # TODO improve with SingleLinked concat() method?
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        values_lt.add_last(entry.get_value())
            return values_lt
        except Exception as err:
            self._handle_error(err)

    def entries(self) -> SingleLinked[T]:
        """*entries()* devuelve una lista (*SingleLinked*) con tuplas de todas los registros (*MapEntry*) del *SeparateChaining*. Cada tupla contiene en la primera posición la llave (*key*) y en la segunda posición el valor (*value*) del registro.

        Returns:
            SingleLinked[T]: lista (*SingleLinked*) de tuplas con todas los registros del *SeparateChaining*.
        """
        try:
            entries_lt = SingleLinked(key=self.key)
            # TODO improve with SingleLinked concat() method?
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        data = (entry.get_key(), entry.get_value())
                        entries_lt.add_last(data)
            return entries_lt
        except Exception as err:
            self._handle_error(err)

    def rehash(self) -> None:
        """*rehash()* reconstruye la tabla de hash con una nueva capacidad (*M*) y un nuevo factor de carga (*alpha*) según los límites configurados por los parametros *max_alpha* y *min_alpha*.

        Si el factor de carga (*alpha*) es mayor que el límite superior (*max_alpha*), se duplica la capacidad (*M*) buscando el siguiente número primo (*P*) reconstruyendo la tabla.

        Si el factor de carga (*alpha) es menor que el límite inferior (*min_alpha*), se reduce a la mitad la capacidad (*M*) de la tabla buscando el siguiente número primo (*P*) reconstruyendo la tabla.
        """
        try:
            # check if the structure is rehashable
            if self.rehashable:
                # gettting the current capacity to avoid null errors
                new_capacity = self.mcapacity
                # find the new capacity according to limits
                # augmenting the capacity
                if self._cur_alpha >= self.max_alpha:
                    new_capacity = next_prime(self.mcapacity * 2)
                # reducing the capacity
                elif self._cur_alpha < self.min_alpha:
                    new_capacity = next_prime(self.mcapacity // 2)

                # asigning the new capacity
                self.mcapacity = new_capacity

                # reseting the size, collisions and current load factor
                self._size = 0
                self._collisions = 0
                self._cur_alpha = 0

                # creating the new hash table
                new_table = ArrayList(cmp_function=self.cmp_function,
                                      key=self.key)
                # keep in memory the old hash table
                old_table = self.hash_table

                # Create the empty buckets in thenew hash table
                i = 0
                while i < self.mcapacity:
                    # bucket is a SingleLinked list
                    bucket = Bucket(cmp_function=self.cmp_function,
                                    key=self.key)
                    new_table.add_last(bucket)
                    i += 1

                # replace the old table with the new one
                self.hash_table = new_table

                # iterate over the old table
                for bucket in old_table:
                    if not bucket.is_empty():
                        for entry in bucket:
                            key = entry.get_key()
                            value = entry.get_value()
                            self.put(key, value)
        except Exception as err:
            self._handle_error(err)
