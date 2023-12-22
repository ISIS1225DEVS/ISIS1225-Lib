"""
# -*- coding: utf-8 -*-
# TODO add docstring

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
EMPTY = "__EMPTY__"
"""
Constante que representa una entrada vacío en el LinearProbing, por defecto es "__EMPTY__".
"""


@dataclass
class LinearProbing(Generic[T]):
    """*LinearProbing* Es una clase que representa una tabla de hash con el método de encadenamiento por de separación (Separate Chaining). Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

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

    # reserved space for the hash table
    # :attr: nentries
    nentries: int = 1
    """
    Es el espacio reservado para la tabla de hash (n), por defecto es 1, pero debe configurarse según el número de entradas que se espera almacenar.
    """

    # starting load factor (alpha) for the hash table
    # :attr: alpha
    alpha: Optional[float] = DEFAULT_PROBING_ALPHA
    """
    Es el factor de carga (alpha) con el que se inicializa la tabla de hash, por defecto es 4.0.
    """

    # prime number (P) for the MAD compression function
    # :attr: prime
    prime: Optional[int] = DEFAULT_PRIME
    """
    Es el número primo (P) utilizado para calcular el código hash de la llave con la función de compresión MAD, por defecto es 109345121.
    """

    # actual place to store the entries in the hash table
    # :attr: hash_table
    hash_table: ArrayList[MapEntry[T]] = field(default_factory=ArrayList)

    """
    Es el indice de la tabla de hash donde se almacenan los *MapEntry*, implementado con un *ArrayList* de DISCLib. en el *__post_init__()* se inicializa con la capacidad inicial de la tabla de hash.
    """

    # boolean to indicate if the hash table can be rehashed
    # :attr: rehashable
    rehashable: bool = True
    """
    Es un booleano que indica si la tabla de hash se puede reconstruir utilizando el método de rehash, por defecto es True.
    """

    # starting capacity (M|m) for the hash table
    # :attr: mcapacity
    mcapacity: int = 1
    """
    Es la capacidad (M) con la que se inicializa la tabla de hash.
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

    # the type of the entry values in the hash table
    # :attr: _value_type
    _value_type: Optional[type] = None
    """
    Es el tipo de dato de los valores en la entrada que contiene la tabla de hash, por defecto es *None* y se configura al cargar el primera entrada en el mapa.
    """

    # the type of the entry keys in the hash table
    # :attr: _key_type
    _key_type: Optional[type] = None
    """
    Es el tipo de dato de las llaves en la entrada que contiene la tabla de hash, por defecto es *None* y se configura al cargar el primera entrada en el mapa.
    """

    # the cmp_function is used to compare emtries, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación opcional que se utiliza para comparar los elementos del LinearProbing, por defecto es *None* y el *__post_init__()* configura la función por defecto *ht_default_cmp_funcion()*.
    """

    # the key is used to compare entries, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del LinearProbing, Por defecto es *None* y el *__post_init__()* configura la llave por defecto la llave *id* en *DEFAULT_DICT_KEY*.
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
                self.cmp_function = ht_default_cmp_funcion
            # setting the default key
            if self.key is None:
                self.key = DEFAULT_DICT_KEY

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
                for entry in self.iodata:
                    key = entry.get(self.key)
                    self.put(key, entry)
            self.iodata = None
            self.nentries = self._size
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
            return ht_default_cmp_funcion(key1, entry2)
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

    def _check_type(self, entry: T) -> bool:
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
            if idx > -1:
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
            if self._check_type(new_entry):
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)
                # TODO do i need this?
                if hkey < 0 or hkey >= self.mcapacity:
                    err_msg = f"The hash for the key: {key} "
                    err_msg += f"is out of range fo capacity: {self.mcapacity}"
                    raise Exception(err_msg)
                # check the entry availability in the hash table
                idx = self._find_slot(hkey, key)
                self.hash_table.change_info(new_entry, idx)
                # there is no space available in the hash table
                if idx == -1:
                    raise Exception(f"Space not available for key: {key}")
                # otherwise, the entry is not in the hash table, add it
                else:
                    # get the entry of the hash table
                    entry = self.hash_table.get_element(idx)
                    # if the entry hasnt been added, add it
                    if entry is None:
                        self.hash_table.add_element(new_entry, idx)
                    # otherwise, update the entry
                    else:
                        self.hash_table.change_info(new_entry, idx)
                    # check if there was a collision
                    if hkey != idx:
                        self._collisions += 1
                    # update the size of the hash table
                    self._size += 1
                    self._cur_alpha = self._size / self.mcapacity
                # check if the structure needs to be rehashed
                if self._cur_alpha >= self.max_alpha:
                    self.rehash()
            
            
            
            
            # get the hash key for the entry
            hkey = hash_compress(key,
                                 self._scale,
                                 self._shift,
                                 self.prime,
                                 self.mcapacity)
            # TODO do i need this?
            if hkey < 0 or hkey >= self.mcapacity:
                err_msg = f"The hash for the key: {key}"
                err_msg += f"is out of range fo capacity: {self.mcapacity}"
                raise Exception(err_msg)
            # check the entry availability in the hash table
            idx = self._find_slot(hkey, key)
            self.hash_table.change_info(new_entry, idx)
            # there is no space available in the hash table
            if idx == -1:
                raise Exception(f"Space not available for key: {key}")
            # otherwise, the entry is not in the hash table, add it
            else:
                # get the entry of the hash table
                entry = self.hash_table.get_element(idx)
                # if the entry hasnt been added, add it
                if entry is None:
                    self.hash_table.add_element(new_entry, idx)
                # otherwise, update the entry
                else:
                    self.hash_table.change_info(new_entry, idx)
                # check if there was a collision
                if hkey != idx:
                    self._collisions += 1
                # update the size of the hash table
                self._size += 1
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
                raise Exception("The structure is empty")
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

    def check_bucket(self, key: T) -> Optional[T]:
        """*check_bucket()* devuelve el bucket asociado a la llave key dentro del LinearProbing, si no existe una entrada con la llave key, devuelve None.

        Args:
            key (T): llave asociada al bucket que se quiere buscar.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: bucket asociado a la llave key dentro del LinearProbing, None si no existe la entrada asociada a la llave key.
        """
        try:
            if self.is_empty():
                raise Exception("The structure is empty")
            else:
                # assume the entry is not in the structure
                bucket = None
                # get the hash key for the entry
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.mcapacity)
                # checking the entry index in the hash table
                idx = self._find_slot(hkey, key)
                # get the bucket according to the index
                bucket = self.hash_table.get_element(idx)
            return bucket
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
                raise Exception("The structure is empty")
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
                # checking the bucket
                bucket = self.hash_table.get_element(idx)
                if bucket is not None:
                    if idx >= 0:
                        # gettting the entry from the hash table
                        entry = bucket
                        # create a clean entry
                        clean_entry = MapEntry(None, None)
                        # update the entry in the hash table
                        self.hash_table.change_info(clean_entry, idx)
                        self._size -= 1
                        self._cur_alpha = self._size / self.mcapacity
                    # TODO maybe i don't need this
                    else:
                        raise Exception(f"Entry for Key: {key} not found")
            if self._cur_alpha < self.min_alpha:
                self.rehash()
            return entry
        except Exception as err:
            self._handle_error(err)

    def keys(self) -> ArrayList[T]:
        """*keys()* devuelve una lista (ArrayList) con todas las llaves de las entradas (parejas llave-valor) del LinearProbing.

        Returns:
            ArrayList[T]: lista (ArrayList) con todas las llaves del LinearProbing.
        """
        try:
            keys_lt = ArrayList(key=self.key)
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        print(entry)
                        keys_lt.add_last(entry.get_key())
            return keys_lt
        except Exception as err:
            self._handle_error(err)

    def values(self) -> ArrayList[T]:
        """*values()* devuelve una lista (ArrayList) con todos los valores de las entradas (parejas llave-valor) del LinearProbing.

        Returns:
            ArrayList[T]: lista (ArrayList) con todos los valores del LinearProbing.
        """
        try:
            values_lt = ArrayList(key=self.key)
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        values_lt.add_last(entry.get_value())
            return values_lt
        except Exception as err:
            self._handle_error(err)

    def entries(self) -> ArrayList[T]:
        """*entries()* devuelve una lista (ArrayList) con todas las entradas (parejas llave-valor) del LinearProbing.

        Returns:
            ArrayList[T]: lista (ArrayList) con todas las entradas del LinearProbing.
        """
        try:
            items_lt = ArrayList(key=self.key)
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        data = (entry.get_key(), entry.get_value())
                        items_lt.add_last(data)
            return items_lt
        except Exception as err:
            self._handle_error(err)

    def _find_slot(self, hkey: int, key: T) -> int:
        """_find_slot _summary_

        Args:
            hkey (int): _description_
            key (T): _description_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            # assume we don't find the entry
            print("inputs:", hkey, key)
            idx = -1
            # sets a limit for the number of probes
            max_probing = self.hash_table.size()
            # sets the initial search index
            i = 0
            # i = 
            # setting the found flag
            found = False
            # setting the number of probes
            cp = 0
            # look for the correct entry in the hash table
            print("max_probing:", max_probing)

            while not found and cp < max_probing:
                if cp == 0:
                    i = hkey
                if self._is_available(i):
                    entry = self.hash_table.get_element(i)
                    if idx == -1:
                        idx = i
                        found = True
                    if entry.get_key() is None:
                        found = True
                else:
                    entry = self.hash_table.get_element(i)
                    if self.cmp_function(key, entry) == 0:
                        idx = i
                        found = True
                i = int((i % self.mcapacity) + 1)
                cp += 1
            print(f"idx: {idx}, cp: {cp}")
            return idx
        except Exception as err:
            self._handle_error(err)

        def findSlot(map, key, hkey_t, cmpfunction):
            """
            Encuentra una posición libre en la tabla de hash.
            map: la tabla de hash
            key: la llave
            hkey_t: La posición inicial de la llave
            cmpfunction: funcion de comparación para la búsqueda de la llave
            """
            try:
                avail_idx = -1          # no se ha encontrado una posición aun
                si = 0
                table = map['table']
                while (si != hkey_t):  # Se busca una posición
                    if (si == 0):
                        si = hkey_t
                    if isAvailable(table, si):  # La posición esta disponible
                        entry_elm = lt.getElement(table, si)
                        if (avail_idx == -1):
                            avail_idx = si            # primera posición disponible
                        if entry_elm['key'] is None:       # nunca ha sido utilizada
                            break
                    else:                    # la posicion no estaba disponible
                        entry_elm = lt.getElement(table, si)
                        if cmpfunction(key, entry_elm) == 0:  # Es la llave
                            return si               # Se  retorna la posicion
                    si = (((si) % map['capacity'])+1)
                return -(avail_idx)    # numero negativo indica que el elemento no estaba
            except Exception as exp:
                # FIXME Ajustar mensaje de error para que sea más claro
                error.reraise(exp, 'Probe:findslot')


    def findSlot2(map, key, hashvalue, cmpfunction):
        """
        Encuentra una posición libre en la tabla de hash.
        map: la tabla de hash
        key: la llave
        hashvalue: La posición inicial de la llave
        cmpfunction: funcion de comparación para la búsqueda de la llave
        """
        try:
            avail = -1          # no se ha encontrado una posición aun
            searchpos = hashvalue
            table = map['table']
            found = False       # flag to indicate if a position has been found

            while not found:  # Se busca una posición
                if isAvailable(table, searchpos):  # La posición esta disponible
                    element = lt.getElement(table, searchpos)
                    if (avail == -1):
                        avail = searchpos            # primera posición disponible
                    if element['key'] is None:       # nunca ha sido utilizada
                        found = True
                else:                    # la posicion no estaba disponible
                    element = lt.getElement(table, searchpos)
                    if cmpfunction(key, element) == 0:  # Es la llave
                        found = True
                if not found:
                    searchpos = (((searchpos) % map['capacity'])+1)
                    if searchpos == hashvalue:
                        found = True

            # numero negativo indica que el elemento no estaba
            return searchpos if found else -(avail)
        except Exception as exp:
            # FIXME Ajustar mensaje de error para que sea más claro
            error.reraise(exp, 'Probe:findslot')

    def findSlot3(map, key, hashvalue, cmpfunction):
        """
        Encuentra una posición libre en la tabla de hash.
        map: la tabla de hash
        key: la llave
        hashvalue: La posición inicial de la llave
        cmpfunction: funcion de comparación para la búsqueda de la llave
        """
        try:
            avail = -1          # no se ha encontrado una posición aun
            searchpos = hashvalue
            table = map['table']
            probe_count = 0     # count the number of probes

            # Se busca una posición
            while (searchpos != hashvalue or probe_count < map['capacity']):
                if isAvailable(table, searchpos):  # La posición esta disponible
                    element = lt.getElement(table, searchpos)
                    if (avail == -1):
                        avail = searchpos            # primera posición disponible
                    if element['key'] is None:       # nunca ha sido utilizada
                        break
                else:                    # la posicion no estaba disponible
                    element = lt.getElement(table, searchpos)
                    if cmpfunction(key, element) == 0:  # Es la llave
                        avail = searchpos               # Se  guarda la posicion
                        break
                searchpos = (((searchpos) % map['capacity'])+1)
                probe_count += 1  # increment the probe count

            # numero negativo indica que el elemento no estaba
            return -(avail) if avail == -1 else avail
        except Exception as exp:
            # FIXME Ajustar mensaje de error para que sea más claro
            error.reraise(exp, 'Probe:findslot')

    def _is_available(self, idx: int) -> bool:
        """_is_available _summary_

        Args:
            idx (int): _description_

        Returns:
            bool: _description_
        """
        # TODO add docstring
        # assume the slot is unavailable
        available = False
        # get the entry from the map
        entry = self.hash_table.get_element(idx)
        # check the entry availability
        if entry.get_key() in (None, EMPTY):
            available = True
        # return the availability of the slot
        return available

    def rehash(self) -> None:
        """*rehash()* reconstruye la tabla de hash con una nueva capacidad (M) y un nuevo factor de carga (alpha) según los límites establecidos por el usuario en los atributos *max_alpha* y *min_alpha*.

        Si el factor de carga (alpha) es mayor que el límite superior (max_alpha), se duplica la capacidad (M) buscando el siguiente número primo y se reconstruye la tabla de hash.

        Si el factor de carga (alpha) es menor que el límite inferior (min_alpha), se reduce a la mitad la capacidad (M) de la tabla de hash buscando el siguiente número primo y se reconstruye la tabla de hash.
        """
        try:
            # check if the structure is rehashable
            if self.rehashable:
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

                # Create new table with empty buckets
                new_table = ArrayList([MapEntry()
                                       for _ in range(self.mcapacity)])

                # replace the old table with the new one
                self.hash_table = new_table

                # iterate over the old table
                for bucket in old_table:
                    if not bucket.is_empty():
                        for entry in bucket:
                            key = entry.get_key()
                            value = entry.get_value()
                            # print(key, value)
                            self.put(key, value)
        except Exception as err:
            self._handle_error(err)
