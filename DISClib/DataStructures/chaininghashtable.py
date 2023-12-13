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
# import modules for defining the element's type in the hash table
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
from DISClib.Utils.numbers import next_prime
from DISClib.Utils.numbers import hash_compress
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import ht_default_cmp_funcion
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


@dataclass
class Bucket(SingleLinked, Generic[T]):
    """*Bucket* Clase que representa un bucket de una tabla de hash. Esta clase hereda de la clase SingleLinked de DISCLib para representar un bucket de una tabla de hash con el método de encadenamiento por separación (Separate Chaining).

    Args:
        SingleLinked (T): Lista sencillamente encadenada que representa un bucket de una tabla de hash con el método de encadenamiento por separación (Separate Chaining).
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para representar una estructura de datos genérica en python.
    """
    pass


@dataclass
class SeparateChaining(Generic[T]):
    """*SeparateChaining* Es una clase que representa una tabla de hash con el método de encadenamiento por de separación (Separate Chaining). Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

    Args:
        Generic (T): Tipo de dato genérico dentro del registro del mapa.

    Raises:
        TypeError: error si la información del registro del mapa (llave o valor) no son del tipo adecuado.

    Returns:
        SeparateChaining: ADT de tipo SeparateChaining o tabla de hash con separación por encadenamiento.
    """
    # input elements from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.
    """

    # reserved space for the hash table
    # :attr: N
    elements: int = 1
    """
    Es el espacio reservado para la tabla de hash (n), por defecto es 1, pero debe configurarse según el número de elementos que se espera almacenar.
    """

    # starting load factor (alpha) for the hash table
    # :attr: alpha
    alpha: Optional[float] = DEFAULT_CHAINING_ALPHA
    """
    Es el factor de carga (alpha) con el que se inicializa la tabla de hash, por defecto es 4.0.
    """

    # prime number (P) for the MAD compression function
    # :attr: prime
    prime: Optional[int] = DEFAULT_PRIME
    """
    Es el número primo (P) utilizado para calcular el código hash de la llave con la función de compresión MAD, por defecto es 109345121.
    """

    # actual place to store the elements in the hash table
    # :attr: hash_table
    hash_table: ArrayList[Bucket[T]] = field(default_factory=ArrayList)

    """
    Es el indice de la tabla de hash donde se almacenan los 'Buckets', implementado con un 'ArrayList' de DISCLib. en el __post_init__ se inicializa con la capacidad inicial de la tabla de hash.
    """

    # boolean to indicate if the hash table can be rehashed
    # :attr: rehashable
    rehashable: bool = True
    """
    Es un booleano que indica si la tabla de hash se puede reconstruir utilizando el método de rehash, por defecto es True.
    """

    # starting capacity (M) for the hash table
    # :attr: capacity
    capacity: int = 1
    """
    Es la capacidad (M) con la que se inicializa la tabla de hash.
    """

    # actual number of elements (n) in the hash table
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

    # optional limit load factor (alpha) for rehashing
    # :attr: _limit_alpha
    _limit_alpha: Optional[float] = 0
    """
    Es el factor de carga limite antes de hacer rehash.
    """
    # optional current factor (alpha) for the working hash table
    # :attr: _cur_alpha
    _cur_alpha: Optional[float] = 0
    """
    Es el factor de carga actual de la tabla de hash.
    """

    # the type of the elements in the hash table
    # :attr: _data_type
    _data_type: Optional[type] = None
    """
    Es el tipo de dato de los elementos que contiene la tabla de hash, por defecto es 'None' y se configura al cargar el primer elemento en el mapa.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación opcional que se utiliza para comparar los elementos del SeparateChaining, por defecto es 'None' y el __post_init__ configura la función por defecto lt_default_cmp_funcion().
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del SeparateChaining, Por defecto es 'None' y el __post_init__ configura la llave por defecto la llave 'id' en DEFAULT_DICT_KEY.
    """

    def __post_init__(self) -> None:
        """__post_init__ _summary_
        """
        # TODO check if this is the best way make the initialization
        try:
            # setting capacity
            self.capacity = next_prime(self.elements // self.alpha)
            # setting scale and shift for MAD compression function
            self._scale = random.randint(1, self.prime - 1)
            self._shift = random.randint(0, self.prime - 1)
            # setting the default compare function
            if self.cmp_function is None:
                self.cmp_function = ht_default_cmp_funcion
            # setting the default key
            if self.key is None:
                self.key = DEFAULT_DICT_KEY
            # setting the default limit factor
            if self._limit_alpha == 0:
                self._limit_alpha = self.alpha

            # initializing the hash table
            self.hash_table = ArrayList()
            i = 0
            # bulding buckets in the hash table
            while i < self.capacity:
                bucket = Bucket(cmp_function=self.cmp_function,
                                key=self.key)
                self.hash_table.add_last(bucket)
                i += 1

            # setting the current load factor
            if self._cur_alpha == 0:
                self._cur_alpha = self._size / self.capacity

            # TODO check if this is the best way to initialize the structure
            if isinstance(self.iodata, VALID_IO_TYPE):
                for entry in self.iodata:
                    key = entry.get(self.key)
                    self.put(key, entry)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, key1, entry2: MapEntry) -> int:
        """*default_cmp_function()* procesa la llave existente en el elemento del 'SeparateChaining' y la compara con el elemento que se quiere agregar al 'SeparateChaining'.

        Args:
            key1 (Any): llave del primer elemento a comparar.
            entry2 (MapEntry): entrada del mapa del segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si las llaves son iguales, 1 si key1 es mayor que la llave de entry2, -1 si key1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            return ht_default_cmp_funcion(key1, entry2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el SeparateChaining.

        Si se presenta un error en el SeparateChaining, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun sea considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el SeparateChaining.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al SeparateChaining sea del mismo tipo contenido dentro de los elementos del SeparateChaining.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el SeparateChaining.

        Args:
            element (T): elemento que se quiere procesar en SeparateChaining.

        Returns:
            bool: operador que indica si el ADT SeparateChaining es del mismo tipo que el elemento que se quiere procesar.
        """
        # TODO check usability of this function
        # if datastruct is empty, set the entry type
        if self.is_empty():
            self._data_type = type(element)
        # else if the structure is not empty, check the element data type
        elif self._data_type is not type(element):
            err_msg = f"Invalid data type: {type(element)} "
            err_msg += f"for structure configured with type: {self._data_type}"
            raise TypeError(err_msg)
        # finally, check if the new element is a valid datatype
        elif self._data_type not in VALID_DATA_TYPE_LT:
            err_msg = f"Invalid data type: {type(self._data_type)}"
            err_msg += f"for element info: {type(element)}"
            raise TypeError(err_msg)
        # otherwise, the type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el SeparateChaining está vacío.

        Returns:
            bool: operador que indica si la estructura SeparateChaining está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el numero de elementos que actualmente contiene el SeparateChaining.

        Returns:
            int: tamaño de la estructura SeparateChaining.
        """
        # TODO change the method to @property "size"?
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def contains(self, key: T) -> bool:
        """contains _summary_

        Args:
            key (T): _description_

        Returns:
            bool: _description_
        """
        try:
            # assume the element is not in the structure
            found = False
            # use the MAD compression function to get the hash key
            hkey = hash_compress(key,
                                 self._scale,
                                 self._shift,
                                 self.prime,
                                 self.capacity)
            # look into the bucket
            bucket = self.hash_table.get_element(hkey)
            idx = bucket.find(key)
            # if the element is in the bucket, return True
            if idx > -1:
                found = True
            return found
        except Exception as err:
            self._handle_error(err)

    def put(self, key: T, value: T) -> None:
        """put _summary_

        Args:
            key (T): _description_
            value (T): _description_

        Raises:
            Exception: _description_
        """
        try:
            # create a new entry for the element
            new_entry = MapEntry(key, value)
            # get the hash key for the element
            hkey = hash_compress(key,
                                 self._scale,
                                 self._shift,
                                 self.prime,
                                 self.capacity)
            # TODO do i need this?
            if hkey < 0 or hkey >= self.capacity:
                err_msg = f"The hash for the key: {key}"
                err_msg += f"is out of range fo capacity: {self.capacity}"
                raise Exception(err_msg)
            # checking the bucket
            bucket = self.hash_table.get_element(hkey)
            idx = bucket.find(key)
            # the entry is not in the bucket, add it and a collision
            if idx > 0:
                bucket.change_info(new_entry, idx)
            # otherwise, update the existing entry
            else:
                if not bucket.is_empty():
                    self._collisions += 1
                bucket.add_last(new_entry)
                self._size += 1
                self._cur_alpha = self._size / self.capacity
            # check if the structure needs to be rehashed
            if self._cur_alpha >= self._limit_alpha:
                self.rehash()
        except Exception as err:
            self._handle_error(err)

    def get(self, key: T) -> Optional[T]:
        """get _summary_

        Args:
            key (T): _description_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        try:
            if self.is_empty():
                raise Exception("The structure is empty")
            else:
                # assume the element is not in the structure
                entry = None
                # get the hash key for the element
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.capacity)
                # checking the bucket
                bucket = self.hash_table.get_element(hkey)
                idx = bucket.find(key)
                # if the element is in the bucket, return it
                if idx > -1:
                    entry = bucket.get_element(idx)
                return entry
        except Exception as err:
            self._handle_error(err)

    def remove(self, key: T) -> None:
        """remove _summary_

        Args:
            key (T): _description_

        Raises:
            Exception: _description_
        """
        try:
            if self.is_empty():
                raise Exception("The structure is empty")
            else:
                # get the hash key for the element
                hkey = hash_compress(key,
                                     self._scale,
                                     self._shift,
                                     self.prime,
                                     self.capacity)
                # checking the bucket
                bucket = self.hash_table.get_element(hkey)
                if bucket is not None:

                    idx = bucket.find(key)
                    if idx > -1:
                        bucket.delete_element(idx)
                        self._size -= 1
                        self._cur_alpha = self._size / self.capacity
        except Exception as err:
            self._handle_error(err)

    def keys(self) -> ArrayList[T]:
        """keys _summary_

        Returns:
            ArrayList[T]: _description_
        """
        try:
            keys_lt = ArrayList(cmp_function=self.cmp_function,
                                   key=self.key)
            for bucket in self.hash_table:
                print(bucket)
                if not bucket.is_empty():
                    for entry in bucket:
                        print(entry)
                        keys_lt.add_last(entry.get_key())
            return keys_lt
        except Exception as err:
            self._handle_error(err)

    def values(self) -> ArrayList[T]:
        """values _summary_

        Returns:
            ArrayList[T]: _description_
        """
        try:
            values_lt = ArrayList(cmp_function=self.cmp_function,
                                     key=self.key)
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        values_lt.add_last(entry.get_value())
            return values_lt
        except Exception as err:
            self._handle_error(err)

    def entries(self) -> ArrayList[T]:
        """entries _summary_

        Returns:
            ArrayList[T]: _description_
        """
        try:
            items_lt = ArrayList(cmp_function=self.cmp_function,
                                    key=self.key)
            for bucket in self.hash_table:
                if not bucket.is_empty():
                    for entry in bucket:
                        items_lt.add_last(entry)
            return items_lt
        except Exception as err:
            self._handle_error(err)

    def rehash(self) -> None:
        """rehash _summary_
        """
        try:
            # check if the structure is rehashable
            if self.rehashable:
                # create a new hash table
                new_table = ArrayList(cmp_function=self.cmp_function,
                                      key=self.key)
                # keep the old table
                old_table = self.hash_table
                # find the new capacity
                new_capacity = next_prime(self.capacity * 2)
                self.capacity = new_capacity

                # reseting the size, collisions and current load factor
                self._size = 0
                self._collisions = 0
                self._cur_alpha = 0

                # populate the new table with empty buckets
                i = 0
                while i < new_capacity:
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
                            print(key, value)
                            self.put(key, value)
        except Exception as err:
            self._handle_error(err)

# GENERAL
#FIXME Cambiar todas las funciones y variables al formato snake_case
#TODO Explicar más a profundidad que tipo de excepciones y errores puede generar cada función

#FIXME Modificar documentación relacionada a numelements
def newMap(numelements, prime, loadfactor, cmpfunction, datastructure):
    """Crea una tabla de simbolos (map) sin orden

    Crea una tabla de hash con capacidad igual a nuelements
    (primo mas cercano al doble de numelements).
    prime es un número primo utilizado para  el cálculo de los codigos
    de hash, si no es provisto se  utiliza el primo 109345121.

    Args:
        numelements: Tamaño inicial de la tabla
        prime: Número primo utilizado en la función MAD
        loadfactor: Factor de carga inicial de la tabla
        cmpfunc: Funcion de comparación entre llaves
    Returns:
        Un nuevo map
    Raises:
        Exception
    """
    try:
        capacity = nextPrime(numelements//loadfactor)
        scale = rd.randint(1, prime-1)
        shift = rd.randint(0, prime-1)
        #FIXME Cambiar por dataclass para facilitar su modelado y manejo errores
        hashtable = {'prime': prime,
                     'capacity': capacity,
                     'scale': scale,
                     'shift': shift,
                     'table': None,
                     'size': 0,
                     'limitfactor': loadfactor,
                     'currentfactor': 0,
                     'type': 'CHAINING',
                     'datastructure': datastructure}
        if(cmpfunction is None):
            cmpfunc = defaultcompare
        else:
            cmpfunc = cmpfunction
        hashtable['cmpfunction'] = cmpfunc
        hashtable['table'] = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpfunc)
        for _ in range(capacity):
            bucket = lt.newList(datastructure='SINGLE_LINKED',
                                cmpfunction=hashtable['cmpfunction'])
            lt.addLast(hashtable['table'], bucket)
        return hashtable
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Chain:newMap')

# #TODO Indicar en el retorno cuando es True y cuando es False, similar a la documentación de isEmpty
# def contains(map, key):
#     """ Retorna True si la llave key se encuentra en el map
#         o False en caso contrario.
#     Args:
#         map: El map a donde se guarda la pareja
#         key: la llave asociada a la pareja

#     Returns:
#         True / False
#     Raises:
#         Exception
#     """
#     try:
#         hash = hashValue(map, key)
#         bucket = lt.getElement(map['table'], hash)
#         pos = lt.isPresent(bucket, key)
#         if pos > 0:
#             return True
#         else:
#             return False
#     except Exception as exp:
#         # FIXME Ajustar mensaje de error para que sea más claro
#         error.reraise(exp, 'Chain:contains')


def put(map, key, value):
    """ Ingresa una pareja llave,valor a la tabla de hash.
    Si la llave ya existe en la tabla, se reemplaza el valor

    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja
        value: el valor asociado a la pareja
    Returns:
        El map
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        bucket = lt.getElement(map['table'], hash)
        entry = me.newMapEntry(key, value)
        pos = lt.isPresent(bucket, key)
        if pos > 0:    # La pareja ya exista, se reemplaza el valor
            lt.changeInfo(bucket, pos, entry)
        else:
            lt.addLast(bucket, entry)   # La llave no existia
            map['size'] += 1
            map['currentfactor'] = map['size'] / map['capacity']

        if (map['currentfactor'] >= map['limitfactor']):
            rehash(map)

        return map
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Chain:put')

# #TODO Indicar que la pareja llave valor es un mapentry
# def get(map, key):
#     """ Retorna la pareja llave, valor, cuya llave sea igual a key
#     Args:
#         map: El map a donde se guarda la pareja
#         key: la llave asociada a la pareja

#     Returns:
#         Una pareja <llave,valor>
#     Raises:
#         Exception
#     """
#     try:
#         hash = hashValue(map, key)
#         bucket = lt.getElement(map['table'], hash)
#         pos = lt.isPresent(bucket, key)
#         if pos > 0:
#             return lt.getElement(bucket, pos)
#         else:
#             return None
#     except Exception as exp:
#         # FIXME Ajustar mensaje de error para que sea más claro
#         error.reraise(exp, 'Chain:get')

# #TODO Modificar documentación para que sea similar a las demás funciones
# def remove(map, key):
#     """ Elimina la pareja llave,valor, donde llave == key.
#     Args:
#         map: El map a donde se guarda la pareja
#         key: la llave asociada a la pareja

#     Returns:
#         El map
#     Raises:
#         Exception
#     """
#     try:
#         hash = hashValue(map, key)
#         bucket = lt.getElement(map['table'], hash)
#         if (bucket is not None):
#             pos = lt.isPresent(bucket, key)
#             if pos > 0:
#                 lt.deleteElement(bucket, pos)
#                 map['size'] -= 1
#         return map
#     except Exception as exp:
#         # FIXME Ajustar mensaje de error para que sea más claro
#         error.reraise(exp, 'Chain:remove')


# def size(map):
#     """  Retorna  el número de entradas en la tabla de hash.
#     Args:
#         map: El map
#     Returns:
#         Tamaño del map
#     Raises:
#         Exception
#     """
#     return map['size']


# def isEmpty(map):
#     """ Informa si la tabla de hash se encuentra vacia
#     Args:
#         map: El map
#     Returns:
#         True: El map esta vacio
#         False: El map no esta vacio
#     Raises:
#         Exception
#     """
#     try:
#         bucket = lt.newList()
#         empty = True
#         for pos in range(lt.size(map['table'])):
#             bucket = lt.getElement(map['table'], pos+1)
#             if lt.isEmpty(bucket) is False:
#                 empty = False
#                 break
#         return empty
#     except Exception as exp:
#         # FIXME Ajustar mensaje de error para que sea más claro
#         error.reraise(exp, 'Chain:isempty')

# #TODO Indicar que la lista es de DISCLib
# def keySet(map):
#     """
#     Retorna una lista con todas las llaves de la tabla de hash

#     Args:
#         map: El map
#     Returns:
#         lista de llaves
#     Raises:
#         Exception
#     """
#     try:
#         ltset = lt.newList('SINGLE_LINKED', map['cmpfunction'])
#         for pos in range(lt.size(map['table'])):
#             bucket = lt.getElement(map['table'], pos+1)
#             if(not lt.isEmpty(bucket)):
#                 for element in range(lt.size(bucket)):
#                     entry = lt.getElement(bucket, element+1)
#                     lt.addLast(ltset, entry['key'])
#         return ltset
#     except Exception as exp:
#         # FIXME Ajustar mensaje de error para que sea más claro
#         error.reraise(exp, 'Chain:keyset')

# #TODO Indicar que la lista es de DISCLib
# def valueSet(map):
#     """
#     Retorna una lista con todos los valores de la tabla de hash

#     Args:
#         map: El map
#     Returns:
#         lista de valores
#     Raises:
#         Exception
#     """
#     try:
#         ltset = lt.newList('SINGLE_LINKED', map['cmpfunction'])
#         for pos in range(lt.size(map['table'])):
#             bucket = lt.getElement(map['table'], pos+1)
#             if (not lt.isEmpty(bucket)):
#                 for element in range(lt.size(bucket)):
#                     entry = lt.getElement(bucket, element+1)
#                     lt.addLast(ltset, entry['value'])
#         return ltset
#     except Exception as exp:
#         # FIXME Ajustar mensaje de error para que sea más claro
#         error.reraise(exp, 'Chain, valueset')


# __________________________________________________________________
#       Helper Functions
# __________________________________________________________________

#FIXME Agregar parametros, retorno y excepciones en la documentación.
def rehash(map):
    """
    Se aumenta la capacida de la tabla al doble y se hace
    rehash de todos los elementos de la tabla
    """
    try:
        newtable = lt.newList('ARRAY_LIST', map['cmpfunction'])
        capacity = nextPrime(map['capacity']*2)
        oldtable = map['table']
        for _ in range(capacity):
            bucket = lt.newList(datastructure='SINGLE_LINKED',
                                cmpfunction=map['cmpfunction'])
            lt.addLast(newtable, bucket)
        map['size'] = 0
        map['currentfactor'] = 0
        map['table'] = newtable
        map['capacity'] = capacity
        for pos in range(1, lt.size(oldtable)+1):
            bucket = lt.getElement(oldtable, pos)
            if (lt.size(bucket) > 0):
                for posbucket in range(1, lt.size(bucket)+1):
                    entry = lt.getElement(bucket, posbucket)
                    put(map, entry['key'], entry['value'])
        return map
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, "Chain:rehash")

#FIXME Agregar parametros, retorno y excepciones en la documentación.
def hashValue(table, key):
    """
    Calcula un hash para una llave, utilizando el método
    MAD : hashValue(y) = ((ay + b) % p) % M.
    Donde:
    M es el tamaño de la tabla, primo
    p es un primo mayor a M,
    a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0
    """
    h = (hash(key))
    a = table['scale']
    b = table['shift']
    p = table['prime']
    m = table['capacity']
    value = int((abs(a*h + b) % p) % m) + 1
    return value


# Function that returns True if n
# is prime else returns False
# This code is contributed by Sanjit_Prasad

#FIXME Agregar documentación para que siga el formato que las demás funciones.
def isPrime(n):
    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    if(n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False

    return True


# Function to return the smallest
# prime number greater than N
# # This code is contributed by Sanjit_Prasad
#FIXME Agregar documentación para que siga el formato que las demás funciones.
def nextPrime(N):
    # Base case
    if (N <= 1):
        return 2
    prime = int(N)
    found = False
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
        if(isPrime(prime) is True):
            found = True
    return int(prime)

#FIXME Agregar documentación para que siga el formato que las demás funciones.
def defaultcompare(key, element):
    if(key == element['key']):
        return 0
    elif(key > element['key']):
        return 1
    return -1
