"""
Este ADT representa una tabla de hash con el método de sondeo lineal (Linear Probing). Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

En particular tiene funciones para encontrar espacio y entradas (pareja llave-valor) disponibles en la tabla en caso de colisiones segun el metodo de sondeo lineal.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# native python modules
# import dataclass to define the hash table
from dataclasses import dataclass, field
# import modules for defining the entry type in the hash table
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
# :data: DEFAULT_PROBING_ALPHA
DEFAULT_PROBING_ALPHA: float = 0.5
"""
Factor de carga (alpha) por defecto e ideal para el LinearProbing, por defecto es 0.5.
"""

# :data: MAX_PROBING_ALPHA
MAX_PROBING_ALPHA: float = 0.8
"""
Factor de carga (alpha) máximo para el LinearProbing, por defecto es 8.0.
"""

# :data: MIN_PROBING_ALPHA
MIN_PROBING_ALPHA: float = 0.2
"""
Factor de carga (alpha) mínimo para el LinearProbing, por defecto es 2.0.
"""

# :data: EMPTY
# TODO check if this is the best way to handle empty entries
EMPTY = "__EMPTY__"
"""
Constante que representa una entrada vacío en el LinearProbing, por defecto es "__EMPTY__".
"""


@dataclass
class LinearProbing(Generic[T]):
    """**LinearProbing** Es una clase que representa una tabla de hash con el método de encadenamiento por de separación (Separate Chaining). Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

    Args:
        Generic (T): Tipo de dato genérico dentro del registro del mapa.

    Raises:
        TypeError: error si la información del registro del mapa (llave o valor) no son del tipo adecuado.

    Returns:
        LinearProbing: ADT de tipo LinearProbing o tabla de hash con separación por encadenamiento.
    """
    # input tuples from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.
    """

    # boolean to indicate if the hash table can be rehashed
    # :attr: rehashable
    rehashable: bool = True
    """
    Es un booleano que indica si la tabla de hash se puede reconstruir utilizando el método de rehash, por defecto es True.
    """

    # reserved space for the hash table
    # :attr: nentries
    nentries: int = 1
    """
    Es el espacio reservado para la tabla de hash (n), por defecto es 1, pero debe configurarse según el número de entradas que se espera almacenar.
    """

    # starting capacity (M|m) for the hash table
    # :attr: mcapacity
    mcapacity: int = 2
    """
    Es la capacidad (M) con la que se inicializa la tabla de hash.
    """

    # starting load factor (alpha) for the hash table
    # :attr: alpha
    alpha: Optional[float] = DEFAULT_PROBING_ALPHA
    """
    Es el factor de carga (alpha) con el que se inicializa la tabla de hash, por defecto es 4.0.
    """

    # the cmp_function is used to compare emtries, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación opcional que se utiliza para comparar los elementos del LinearProbing, por defecto es *None* y el *__post_init__()* configura la función por defecto *ht_default_cmp_funcion()*.
    """

    # actual place to store the entries in the hash table
    # :attr: hash_table
    hash_table: ArrayList[MapEntry[T]] = field(default_factory=ArrayList)

    """
    Es el indice de la tabla de hash donde se almacenan los *MapEntry*, implementado con un *ArrayList* de DISCLib. en el *__post_init__()* se inicializa con la capacidad inicial de la tabla de hash.
    """

    # the key is used to compare entries, not defined by default
    # :attr: key
    key: Optional[str] = DEFAULT_DICT_KEY
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del SeparateChaining, Por defecto la llave es la cadena de caracteres *"id"* definida en *DEFAULT_DICT_KEY*.
    """

    # prime number (P) for the MAD compression function
    # :attr: prime
    prime: Optional[int] = DEFAULT_PRIME
    """
    Es el número primo (P) utilizado para calcular el código hash de la llave con la función de compresión MAD, por defecto es 109345121 definido en *DEFAULT_PRIME*.
    """

    # TODO create a MAD class to handle the compression function?
    # private scale (a) factor for the mad compression function
    # :attr: _scale
    _scale: Optional[int] = 0
    """
    Es el número utilizado para calcular el código hash de la llave.
    """
    # private shift (b) factor for the mad compression function
    # :attr: _shift
    _shift: Optional[int] = 0
    """
    Es el número utilizado para calcular el código hash de la llave.
    """

    # current factor (alpha) for the working hash table
    # :attr: _cur_alpha
    _cur_alpha: Optional[float] = 0
    """
    Es el factor de carga actual de la tabla de hash.
    """

    # maximum load factor (alpha) for the hash table
    # :attr: max_alpha
    max_alpha: Optional[float] = MAX_PROBING_ALPHA
    """
    Es el factor de carga máximo de la tabla de hash, por defecto es 8.0.
    """

    # minimum load factor (alpha) for the hash table
    # :attr: min_alpha
    min_alpha: Optional[float] = MIN_PROBING_ALPHA
    """
    Es el factor de carga mínimo de la tabla de hash, por defecto es 2.0.
    """

    # actual number of used entries (n) in the hash table
    # FIXME inconsistent use of _size and size()
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos (n) dentro de la tabla de hash, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    # :attr: collisions
    _collisions: Optional[int] = 0
    """
    Es el número de colisiones en la tabla de hash.
    """

    # the type of the entry keys in the hash table
    # :attr: _key_type
    _key_type: Optional[type] = None
    """
    Es el tipo de dato de las llaves en la entrada que contiene la tabla de hash, por defecto es *None* y se configura al cargar el primera entrada en el mapa.
    """

    # the type of the entry values in the hash table
    # :attr: _value_type
    _value_type: Optional[type] = None
    """
    Es el tipo de dato de los valores en la entrada que contiene la tabla de hash, por defecto es *None* y se configura al cargar el primera entrada en el mapa.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los valores por defecto de la estructura LinearProbing después de la inicialización de la misma. Configura los factores de carga (alpha), el número primo (P) para la función de compresión MAD, la capacidad (M) de la tabla de hash, la función de comparación y la llave para comparar los elementos del LinearProbing, y finalmente inicializa la tabla de hash con la capacidad (M) configurada.
        """
        # TODO check if this is the best way make the initialization
        try:
            # setting capacity
            self.mcapacity = next_prime(self.nentries // self.alpha)
            # setting scale and shift for MAD compression function
            self._scale = random.randint(1, self.prime - 1)
            self._shift = random.randint(0, self.prime - 1)
            # setting the default compare function
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function

            # initializing the hash table
            self.hash_table = ArrayList(cmp_function=self.cmp_function,
                                        key=self.key)
            i = 0
            # bulding buckets in the hash table
            while i < self.mcapacity:
                # adding an empty entry to the hash table
                entry = MapEntry()
                self.hash_table.add_last(entry)
                i += 1

            # setting the current load factor
            if self._cur_alpha == 0:
                self._cur_alpha = self._size / self.mcapacity

            # TODO check if this is the best way to initialize the structure
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
            # # fix discrepancies between the size and the number of entries (n)
            # if self._size != self.nentries:
            #     self.nentries = self._size
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, key1, entry2: MapEntry) -> int:
        """*default_cmp_function()* procesa la llave existente en la entrada del LinearProbing y la compara con la llave del a entrada que se quiere agregar al LinearProbing.
        Args:
            key1 (Any): llave de la primera entrada a comparar.
            entry2 (MapEntry): segunda entrada (pareja llave-valor) a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si las llaves son iguales, 1 si key1 es mayor que la llave de entry2, -1 si key1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            # return ht_default_cmp_funcion(key1, entry2)
            return ht_default_cmp_funcion(self.key, key1, entry2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el LinearProbing.

        Si se presenta un error en el LinearProbing, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun sea considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el LinearProbing.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, entry: MapEntry) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato de la entrada que se quiere agregar al LinearProbing sea del mismo tipo contenido dentro de los elementos del LinearProbing.

        Raises:
            TypeError: error si el tipo de dato de la entrada que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el LinearProbing.

        Args:
            entry (T): entrada que se quiere procesar en LinearProbing.

        Returns:
            bool: operador que indica si el ADT LinearProbing es del mismo tipo que la entrada que se quiere procesar.
        """
        # TODO check usability of this function
        # if datastruct is empty, set the entry type
        key = entry.get_key()
        value = entry.get_value()
        if self.is_empty():
            self._key_type = type(key)
            self._value_type = type(value)
            # self._data_type = type(entry)
        # check if the new entry is the same type as the other entries
        if key != EMPTY and value != EMPTY:
            if not isinstance(key, self._key_type):
                err_msg = f"Invalid key type: {type(key)} "
                err_msg += f"for structure configured with: {self._key_type}"
                raise TypeError(err_msg)
            elif not isinstance(value, self._value_type):
                err_msg = f"Invalid value type: {type(value)} "
                err_msg += f"for structure configured with: {self._value_type}"
                raise TypeError(err_msg)
        # otherwise, the type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el LinearProbing está vacío.

        Returns:
            bool: operador que indica si la estructura LinearProbing está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el numero de elementos que actualmente contiene el LinearProbing.

        Returns:
            int: tamaño de la estructura LinearProbing.
        """
        # TODO change the method to @property "size"?
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def contains(self, key: T) -> bool:
        """*contains()* responde si el LinearProbing contiene una entrada con la llave key.

        Args:
            key (T): llave de la entrada (pareja llave-valor) que se quiere buscar en el LinearProbing.

        Returns:
            bool: operador que indica si el LinearProbing contiene o no una entrada con la llave key.
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
                # look for the entry in the hash table
                idx = self._find_slot(hkey, key)
                # if the index of the entry is inside the hash table
                entry = self.hash_table.get_element(idx)
                if idx >= 0 and entry.get_key() == key:
                    found = True
                return found
        except Exception as err:
            self._handle_error(err)

    def put(self, key: T, value: T) -> None:
        """*put()* agrega una entrada (pareja llave-valor) al LinearProbing, si la llave ya existe en el LinearProbing, se reemplaza el valor.

        Args:
            key (T): llave asociada a la nueva entrada.
            value (T): el valor asociado a la nueva entrada.

        Raises:
            Exception: si el indice de la entrada en el mapa está fuera de los limites establecidos, se genera un error.
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

                # check the entry slot availability in the hash table
                idx = self._find_slot(hkey, key)
                # if the idx is inside the hash table, update hash table stats
                if idx >= 0 and idx < self.mcapacity:
                    # check slot availability for hash table stats
                    entry = self.hash_table.get_element(idx)
                    # if the slot is available, update the size
                    if self._is_available(entry):
                        self._size += 1
                    # if index and hash key are different, update collisions
                    if hkey != idx:
                        self._collisions += 1
                    # update the entry index of the hash table regardless
                    self.hash_table.change_info(new_entry, idx)
                # if capacity is full, add the entry to the end of the table
                # useful when rehash is disabled
                elif idx >= self.mcapacity - 1:
                    self._size += 1
                    self.mcapacity += 1
                    self._collisions += 1
                    self.hash_table.add_last(new_entry)

                # updtate the current load factor
                self._cur_alpha = self._size / self.mcapacity

                # check if the structure needs to be rehashed
                if self._cur_alpha >= self.max_alpha:
                    self.rehash()
        except Exception as err:
            self._handle_error(err)

    def get(self, key: T) -> Optional[T]:
        """*get()* devuelve la entrada (pareja llave-valor) cuya llave sea igual a key dentro del LinearProbing, si no existe una entrada con la llave key, devuelve None.

        Args:
            key (T): llave asociada a la entrada que se quiere buscar.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: entrada (pareja llave-valor) con la llave igual a key dentro del LinearProbing, None si no existe la entrada asociada a la llave key.
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
                # checking the entry index in the hash table
                idx = self._find_slot(hkey, key)
                # if the entry is in the hashmap, return it
                if idx >= 0:
                    entry = self.hash_table.get_element(idx)
                return entry
        except Exception as err:
            self._handle_error(err)

    def check_slots(self, key: T) -> SingleLinked[T]:
        """*check_slots()* devuelve una lista (SingleLinked) con todas las entradas (parejas llave-valor) asociadas a la llave dentro del *LinearProbing*. Si no existe una entrada asociada, devuelve None.

        Args:
            key (T): llave asociada al Slot que se quiere buscar.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[SingleLinked[T]]: lista sencillamente encadenada (SingleLinked) con todas las entradas (parejas llave-valor) asociadas a la llave key dentro del *LinearProbing*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            else:
                # assume the entry is not in the structure
                slots = SingleLinked(key=self.key,
                                     cmp_function=self.cmp_function)
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)
                entry = self.hash_table.get_element(hkey)
                # adding the entry to the list if it's not empty
                if entry.get_key() is not None or entry.set_key() != EMPTY:
                    slots.add_last(entry)
                # checking the entry index in the hash table
                idx = self._find_slot(hkey, key)
                # if the entry is in the hashmap, return it
                if idx >= 0:
                    # get the bucket according to the index
                    entry = self.hash_table.get_element(idx)
                    # adding the entry to the list if it's not empty
                    if entry.get_key() is not None or entry.set_key() != EMPTY:
                        slots.add_last(entry)
            return slots
        except Exception as err:
            self._handle_error(err)

    def remove(self, key: T) -> Optional[T]:
        """*remove()* elimina la entrada (pareja llave-valor) cuya llave sea igual a key dentro del LinearProbing, si no existe una entrada con la llave key, devuelve None.

        Args:
            key (T): llave asociada a la entrada que se quiere eliminar.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la entrada que se quiere eliminar no existe dentro del bucket

        Returns:
            Optional[T]: entrada (pareja llave-valor) que se eliminó del LinearProbing, None si no existe la entrada asociada a la llave key.
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

                # finding the entry index in the hash table
                idx = self._find_slot(hkey, key)
                # if the entry is in the hashmap, remove it
                if idx >= 0 and idx < self.mcapacity:
                    # gettting the entry from the hash table
                    entry = self.hash_table.get_element(idx)
                    # create a clean entry
                    clean_entry = MapEntry(EMPTY, EMPTY)
                    # replace the entry with the clean entry
                    self.hash_table.change_info(clean_entry, idx)
                    # update the hash table stats
                    self._size -= 1
                    self._cur_alpha = self._size / self.mcapacity
                # TODO maybe i don't need this
                else:
                    raise Exception(f"Entry for Key: {key} not found")
            # if the structure needs to be rehashed, rehash it
            if self._cur_alpha < self.min_alpha:
                self.rehash()
            return entry
        except Exception as err:
            self._handle_error(err)

    def keys(self) -> SingleLinked[T]:
        """*keys()* devuelve una lista (SingleLinked) con todas las llaves de las entradas (parejas llave-valor) del LinearProbing.

        Returns:
            SingleLinked[T]: lista (SingleLinked) con todas las llaves del LinearProbing.
        """
        try:
            keys_lt = SingleLinked(key=self.key)
            for entry in self.hash_table:
                if not self._is_available(entry):
                    keys_lt.add_last(entry.get_key())
            return keys_lt
        except Exception as err:
            self._handle_error(err)

    def values(self) -> SingleLinked[T]:
        """*values()* devuelve una lista (SingleLinked) con todos los valores de las entradas (parejas llave-valor) del LinearProbing.

        Returns:
            SingleLinked[T]: lista (SingleLinked) con todos los valores del LinearProbing.
        """
        try:
            values_lt = SingleLinked(key=self.key)
            for entry in self.hash_table:
                if not self._is_available(entry):
                    values_lt.add_last(entry.get_value())
            return values_lt
        except Exception as err:
            self._handle_error(err)

    def entries(self) -> SingleLinked[T]:
        """*entries()* devuelve una lista (SingleLinked) con todas las entradas (parejas llave-valor) del LinearProbing.

        Returns:
            SingleLinked[T]: lista (SingleLinked) con todas las entradas del LinearProbing.
        """
        try:
            entries_lt = SingleLinked(key=self.key)
            for entry in self.hash_table:
                if not self._is_available(entry):
                    key = entry.get_key()
                    value = entry.get_value()
                    data = (key, value)
                    entries_lt.add_last(data)
            return entries_lt
        except Exception as err:
            self._handle_error(err)

    def _find_slot(self, hkey: int, key: T) -> int:
        """*_find_slot()* encuentra el indice de la entrada (pareja llave-valor) en el LinearProbing, si la entrada no existe, devuelve el indice de la primera entrada disponible.

        Args:
            hkey (int): indice de la entrada (pareja llave-valor) en el LinearProbing.
            key (T): llave de la entrada (pareja llave-valor) que se quiere buscar.

        Returns:
            int: devuelve el indice negativo si encuentra espacio disponible (None | EMPTY) o si la entrada no existe, devuelve el indice positivo si la entrada existe.
        """
        try:
            # define the max number of probes to avoid infinite loops
            max_probes = self.mcapacity

            # assume we don't find the entry or an available slot
            # found flag to existing entry
            found = False
            # available flag to empty entry
            available = False

            # start the probe counter
            pc = 0
            # existing entry index
            j = -1
            # available entry index
            idx = -1

            # start in the hash key position
            i = hkey

            # loop entries while it's not found or available
            while not (found or available) and pc < max_probes:
                # get the entry from the hash table
                entry = self.hash_table.get_element(i)
                # check if the entry is available
                if self._is_available(entry):
                    # update the available entry index
                    if idx == -1:
                        idx = i
                    # update the available flag
                    if entry.get_key() is None:
                        available = True
                # otherwise, check if the entry is the same
                else:
                    # compare the new kew with existing entry
                    if self.cmp_function(key, entry) == 0:
                        # update the existing entry index and found flag
                        j = i
                        found = True
                # update the probe counter and the entry index
                i = int(i % self.mcapacity) + 1
                # if the entry index is out of range, reset it
                if i >= self.mcapacity:
                    i = 0
                pc += 1
            # if the entry is found, return the existing entry index
            if found:
                return j
            # if available space found, return the index*-1 for the new entry
            elif available:
                return idx
            # otherwise, return the max number of probes plus one
            else:
                return max_probes + 1
        except Exception as err:
            self._handle_error(err)

    def _is_available(self, entry: MapEntry) -> bool:
        """*_is_available()* permite verificar si una entrada (pareja llave-valor) está disponible en el LinearProbing. Es decir si la llave es nula (None) o vacía (EMPTY).

        Args:
            entry (MapEntry): entrada (pareja llave-valor) que se quiere verificar.

        Returns:
            bool: operador que indica si la entrada está disponible o no en el LinearProbing.
        """
        # assume the slot is unavailable
        available = False
        # check the entry availability
        if entry.get_key() is None or entry.get_key() == EMPTY:
            available = True
        # return the slot availability
        return available

    def rehash(self) -> None:
        """*rehash()* reconstruye la tabla de hash con una nueva capacidad (M) y un nuevo factor de carga (alpha) según los límites establecidos por el usuario en los atributos *max_alpha* y *min_alpha*.

        Si el factor de carga (alpha) es mayor que el límite superior (max_alpha), se duplica la capacidad (M) buscando el siguiente número primo y se reconstruye la tabla de hash.

        Si el factor de carga (alpha) es menor que el límite inferior (min_alpha), se reduce a la mitad la capacidad (M) de la tabla de hash buscando el siguiente número primo y se reconstruye la tabla de hash.
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
                # TODO check if the reduced capacity is a good fit
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

                # initializing the new hash table with empty entries
                i = 0
                while i < self.mcapacity:
                    # adding an empty entry to the hash table
                    entry = MapEntry()
                    new_table.add_last(entry)
                    i += 1

                # replace the old table with the new one
                self.hash_table = new_table

                # iterate over the old table
                for entry in old_table:
                    if entry.get_key() is not None and entry.get_key() != EMPTY:
                        key = entry.get_key()
                        value = entry.get_value()
                        self.put(key, value)
        except Exception as err:
            self._handle_error(err)
