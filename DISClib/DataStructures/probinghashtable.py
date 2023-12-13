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
from DISClib.Utils.numbers import next_prime
from DISClib.Utils.numbers import hash_compress
from DISClib.Utils.error import error_handler
# from DISClib.Utils.error import init_type_checker
from DISClib.Utils.default import ht_default_cmp_funcion
from DISClib.Utils.default import T
from DISClib.Utils.default import DEFAULT_DICT_KEY
from DISClib.Utils.default import VALID_IO_TYPE
from DISClib.Utils.default import DEFAULT_PRIME


# checking custom modules
assert MapEntry
assert ArrayList
assert next_prime
assert hash_compress
assert error_handler
# assert init_type_checker
assert ht_default_cmp_funcion
assert T
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE
assert DEFAULT_PRIME

# default load factor for separating chaining
# :data: DEFAULT_CHAINING_ALPHA
DEFAULT_CHAINING_ALPHA: float = 4.0


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

    # starting load factor for the hash table
    # :attr: _load_factor
    aLpha: Optional[float] = DEFAULT_CHAINING_ALPHA
    """
    Es el factor de carga con el que se inicializa la tabla de hash, por defecto es 4.0.
    """

    # prime number for the mad compression function
    # :attr: prime
    prime: Optional[int] = DEFAULT_PRIME
    """
    Es el número primo utilizado para calcular el código hash de la llave con la función de compresión MAD, por defecto es 109345121.
    """

    # actual place to store the elements in the hash table
    # :attr: table
    table: ArrayList[MapEntry[T]] = field(default_factory=ArrayList)

    """
    Es el indice de la tabla de hash donde se almacenan los 'Buckets', implementado con un 'ArrayList' de DISCLib. en el __post_init__ se inicializa con la capacidad inicial de la tabla de hash.
    """

    # boolean to indicate if the hash table can be rehashed
    # :attr: rehashable
    rehashable: bool = True
    """
    Es un booleano que indica si la tabla de hash se puede reconstruir utilizando el método de rehash, por defecto es True.
    """

    # starting capacity for the hash table
    # :attr: capacity
    capacity: int = 1
    """
    Es la capacidad (m) con la que se inicializa la tabla de hash.
    """

    # actual number of elements in the hash table
    # FIXME inconsistent use of _size and size()
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos dentro de la tabla de hash, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    # :attr: collisions
    _collisions: Optional[int] = 0
    """
    Es el número de colisiones en la tabla de hash.
    """

    # TODO create a MAD class to handle the compression function
    # private scale factor for the mad compression function
    # :attr: _scale
    _scale: Optional[int] = 0
    """
    Es el número utilizado para calcular el código hash de la llave.
    """
    # private shift factor for the mad compression function
    # :attr: _shift
    _shift: Optional[int] = 0
    """
    Es el número utilizado para calcular el código hash de la llave.
    """

    # optional limit factor
    # :attr: _limit_factor
    _limit_factor: Optional[float] = 0
    """
    Es el factor de carga limite antes de hacer rehash.
    """
    # optional current factor
    # :attr: _current_factor
    _current_factor: Optional[float] = 0
    """
    Es el factor de carga actual de la tabla de hash.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación opcional que se utiliza para comparar los elementos del LinearProbing, por defecto es 'None' y el __post_init__ configura la función por defecto lt_default_cmp_funcion().
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del LinearProbing, Por defecto es 'None' y el __post_init__ configura la llave por defecto la llave 'id' en DEFAULT_DICT_KEY.
    """

    def __post_init__(self) -> None:
        try:
            # setting capacity
            self.capacity = self._next_prime(self.elements // self.aLpha)
            # setting scale and shift for MAD compression function
            self._scale = random.randint(1, self.prime - 1)
            self._shift = random.randint(0, self.prime - 1)
            # setting the default compare function
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # setting the default key
            if self.key is None:
                self.key = DEFAULT_DICT_KEY
            # setting the default limit factor
            if self._limit_factor == 0:
                self._limit_factor = self.aLpha
            # setting the default current factor
            if self._current_factor == 0:
                self._current_factor = self._size / self.capacity

            self.table = ArrayList(cmp_function=self.cmp_function,
                                   key=self.key)
            i = 0
            while i < self.capacity:
                bucket = Bucket(cmp_function=self.cmp_function,
                                key=self.key)
                self.table.add_last(bucket)
                i += 1

            if isinstance(self.iodata, VALID_IO_TYPE):
                for entry in self.iodata:
                    self.put(entry[self.key], entry)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """*default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el LinearProbing. Es una función crucial para que la estructura de datos funcione correctamente.

        Args:
            elm1 (Any): primer elemento a comparar.
            elm2 (Any): segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            return ht_default_cmp_funcion(self.key, elm1, elm2)
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

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al LinearProbing sea del mismo tipo contenido dentro de los elementos del LinearProbing.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el LinearProbing.

        Args:
            element (T): elemento que se quiere procesar en LinearProbing.

        Returns:
            bool: operador que indica si el ADT LinearProbing es del mismo tipo que el elemento que se quiere procesar.
        """
        # TODO check usability of this function
        # if the structure is not empty, check the first element type
        if not self.is_empty():
            # get the type of the first element
            lt_type = type(self.elements[0])
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for element info: {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
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
        pass

    def put(self, key: T, value: T) -> None:
        pass

    def get(self, key: T) -> Optional[T]:
        pass

    def remove(self, key: T) -> None:
        pass

    def keys(self) -> ArrayList[T]:
        pass

    def values(self) -> ArrayList[T]:
        pass

    def rehash(self) -> None:
        pass






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
        loadfactor: Factor de carga maximo de la tabla
        cmpfunction: Funcion de comparación entre llaves
        datastructure: estructura de datos seleccionada
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
                     'currentfactor': 0,
                     'limitfactor': loadfactor,
                     'cmpfunction': None,
                     'size': 0,
                     'type': 'PROBING',
                     'datastructure': datastructure}
        if(cmpfunction is None):
            cmpfunc = defaultcompare
        else:
            cmpfunc = cmpfunction
        hashtable['cmpfunction'] = cmpfunc
        hashtable['table'] = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpfunc)
        for _ in range(capacity):
            entry = me.newMapEntry(None, None)
            lt.addLast(hashtable['table'], entry)
        return hashtable
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:newMap')


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
        hash = hashValue(map, key)      # Se obtiene el hashcode de la llave
        entry = me.newMapEntry(key, value)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        lt.changeInfo(map['table'], abs(pos), entry)
        if (pos < 0):           # Se reemplaza el valor con el nuevo valor
            map['size'] += 1
            map['currentfactor'] = map['size'] / map['capacity']

        if (map['currentfactor'] >= map['limitfactor']):
            rehash(map)
        return map
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:put')

#TODO Indicar en el retorno cuando es True y cuando es False, similar a la documentación de isEmpty
def contains(map, key):
    """ Retorna True si la llave key se encuentra en el map
        o False en caso contrario.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        True / False
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        if (pos > 0):
            return True
        else:
            return False
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:contains')

#TODO Indicar que la pareja llave valor es un mapentry
def get(map, key):
    """ Retorna la pareja llave, valor, cuya llave sea igual a key
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        Una pareja <llave,valor>
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        if pos > 0:
            element = lt.getElement(map['table'], pos)
            return element
        else:
            return None
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:get')

#TODO Modificar documentación para que sea similar a la de las demás funciones
def remove(map, key):
    """ Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        El map
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        if pos > 0:
            entry = me.newMapEntry('__EMPTY__', '__EMPTY__')
            lt.changeInfo(map['table'], pos, entry)
            map['size'] -= 1
        return map
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:remove')


def size(map):
    """  Retorna  el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    try:
        return map['size']
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:size')


def isEmpty(map):
    """ Informa si la tabla de hash se encuentra vacia
    Args:
        map: El map
    Returns:
        True: El map esta vacio
        False: El map no esta vacio
    Raises:
        Exception
    """
    try:
        empty = True
        for pos in range(lt.size(map['table'])):
            entry = lt.getElement(map['table'], pos+1)
            if (entry['key'] is not None and entry['key'] != '__EMPTY__'):
                empty = False
                break
        return empty
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:isEmpty')

#TODO indicar que la lista retornada es de la librería DISCLib
def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de llaves
    Raises:
        Exception
    """
    try:
        ltset = lt.newList()
        for pos in range(lt.size(map['table'])):
            entry = lt.getElement(map['table'], pos+1)
            if (entry['key'] is not None and entry['key'] != '__EMPTY__'):
                lt.addLast(ltset, entry['key'])
        return ltset
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:keyset')

#TODO indicar que la lista retornada es de la librería DISCLib
def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de valores
    Raises:
        Exception
    """
    try:
        ltset = lt.newList()
        for pos in range(lt.size(map['table'])):
            entry = lt.getElement(map['table'], pos+1)
            if (entry['value'] is not None and entry['value'] != '__EMPTY__'):
                lt.addLast(ltset, entry['value'])
        return ltset
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:valueset')


# __________________________________________________________________
#       Helper Functions
# __________________________________________________________________

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
    try:
        h = (hash(key))
        a = table['scale']
        b = table['shift']
        p = table['prime']
        m = table['capacity']
        value = int((abs(a*h + b) % p) % m) + 1
        return value
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:hashvalue')

#FIXME Añadir retorno y manejo de excepciones en la documentación
def findSlot(map, key, hashvalue, cmpfunction):
    """
    Encuentra una posición libre en la tabla de hash.
    map: la tabla de hash
    key: la llave
    hashvalue: La posición inicial de la llave
    cmpfunction: funcion de comparación para la búsqueda de la llave
    """
    try:
        avail = -1          # no se ha encontrado una posición aun
        searchpos = 0
        table = map['table']
        while (searchpos != hashvalue):  # Se busca una posición
            if (searchpos == 0):
                searchpos = hashvalue
            if isAvailable(table, searchpos):  # La posición esta disponible
                element = lt.getElement(table, searchpos)
                if (avail == -1):
                    avail = searchpos            # primera posición disponible
                if element['key'] is None:       # nunca ha sido utilizada
                    break
            else:                    # la posicion no estaba disponible
                element = lt.getElement(table, searchpos)
                if cmpfunction(key, element) == 0:  # Es la llave
                    return searchpos               # Se  retorna la posicion
            searchpos = (((searchpos) % map['capacity'])+1)
        return -(avail)    # numero negativo indica que el elemento no estaba
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:findslot')

#FIXME Agregar parametros, retorno y excepciones en la documentación.
def isAvailable(table, pos):
    """
    Informa si la posición pos esta disponible en la tabla de hash.
    Se entiende que una posición está disponible
    si su contenido es igual a None (no se ha usado esa posicion)
    o a __EMPTY__ (la posición fue liberada)
    """
    try:
        entry = lt.getElement(table, pos)
        if (entry['key'] is None or entry['key'] == '__EMPTY__'):
            return True
        return False
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:isAvailable')

#FIXME Agregar parametros, retorno y excepciones en la documentación.
def rehash(map):
    """
    Se aumenta la capacidad de la tabla al doble y se hace rehash de
    todos los elementos de la tabla.
    """
    try:
        newtable = lt.newList('ARRAY_LIST', map['cmpfunction'])
        capacity = nextPrime(map['capacity']*2)
        for _ in range(capacity):
            entry = me.newMapEntry(None, None)
            lt.addLast(newtable, entry)
        oldtable = map['table']
        map['size'] = 0
        map['currentfactor'] = 0
        map['table'] = newtable
        map['capacity'] = capacity
        for pos in range(lt.size(oldtable)):
            entry = lt.getElement(oldtable, pos+1)
            if (entry['key'] is not None and entry['key'] != '__EMPTY__'):
                hash = hashValue(map, entry['key'])
                loc = findSlot(map, entry['key'], hash, map['cmpfunction'])
                lt.changeInfo(map['table'], abs(loc), entry)
                if (loc < 0):
                    map['size'] += 1
                    map['currentfactor'] = map['size'] / map['capacity']
        return map
    except Exception as exp:
        # FIXME Ajustar mensaje de error para que sea más claro
        error.reraise(exp, 'Probe:rehash')


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

#FIXME Agregar documentación para que siga el formato que las demás funciones.
# Function to return the smallest
# prime number greater than N
# # This code is contributed by Sanjit_Prasad
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

#FIXME Agregar documentación.
def defaultcompare(key, element):
    if(key == element['key']):
        return 0
    elif(key > element['key']):
        return 1
    return -1
