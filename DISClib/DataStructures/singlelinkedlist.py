"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Dario Correal
 *
 """

# native python modules
# import dataclass to define the single linked list
from dataclasses import dataclass
# import modules for defining the element's type in the list
from typing import Optional, Callable, Generic, TypeVar
# import inspect for getting the name of the current function
import inspect

# importing DISClib type + error handling
# custom modules
import config
# generic error message and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.error import type_checker
# single linked list node
from DISClib.DataStructures.listnode import single_node as node

# checking costum modules
assert config
assert error_handler
assert type_checker

"""
  Este módulo implementa una estructura de datos lineal mediante una lista
  encadenada sencillamente para almacenar una colección de elementos.
  Los elementos se cuentan desde la posición 1.

  Este código está basado en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


# Type for the element stored in the list
T = TypeVar("T")    # T can be any type


class sll_iterator:
    """ _summary_

    Raises:
        StopIteration: _description_

    Returns:
        _type_: _description_
    """
    # TODO add docstring
    def __init__(self, current: Optional[node[T]]) -> None:
        """__init__ _summary_

        Args:
            current (Optional[node[T]]): _description_
        """
        # TODO add docstring
        self._current = current

    def __iter__(self) -> "sll_iterator[T]":
        """__iter__ _summary_

        Returns:
            sll_iterator[T]: _description_
        """
        # TODO add docstring
        return self

    def __next__(self) -> T:
        """__next__ _summary_

        Raises:
            StopIteration: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        if self._current is None:
            raise StopIteration
        else:
            ans = self._current.get_info()
            self._current = self._current.next()
            return ans


@dataclass
class single_linked(Generic[T]):
    """single_linked _summary_

    Args:
        Generic (_type_): _description_
    """    
    # TODO add docstring
    first: Optional[node[T]] = None
    last: Optional[node[T]] = None
    # by default, the list is empty
    _size: int = 0
    # the cmp_function is used to compare elements, not defined by default
    cmp_function: Optional[Callable[[T, T], int]] = None
    # the key is used to compare elements, not defined by default
    key: Optional[str] = None

    def __post_init__(self) -> None:
        """__post_init__ _summary_
        """
        # TODO add docstring
        # if the key is not defined, use the default
        if self.key is None:
            self.key = "id"
        # if the comparison function is not defined, use the default
        if self.cmp_function is None and self.key is not None:
            self.cmp_function = self.default_cmp_function

    def default_cmp_function(self, elm1, elm2) -> int:
        """default_cmp_function _summary_

        Args:
            elm1 (_type_): _description_
            elm2 (_type_): _description_

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            # using the key to compare elements
            if self.key is not None:
                key1 = elm1.get(self.key)
                key2 = elm2.get(self.key)
                # check if the key is present in both elements
                if None in [key1, key2]:
                    raise Exception("Invalid key")
                # comparing elements
                else:
                    # if one is greater than the other, return 1
                    if key1 > key2:
                        return 1
                    # if one is less than the other, return -1
                    elif key1 < key2:
                        return -1
                    # if they are equal, return 0
                    elif key1 == key2:
                        return 0
                    # otherwise, raise an exception
                    else:
                        raise Exception("Invalid comparison")
        except Exception as exp:
            self._handle_error(exp)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error _summary_

        Args:
            err (Exception): _description_
        """
        # TODO add docstring
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """_check_type _summary_

        Args:
            element (T): _description_

        Returns:
            bool: _description_
        """
        # TODO add docstring
        try:

            if self._size == 0 and None in (self.first, self.last):
                return True
            elif self._size > 0:
                # get the type of the first element
                cur_context = self.__class__.__name__
                cur_function = inspect.currentframe().f_code.co_name
                # check if the type of the element is valid
                type_checker(cur_context, cur_function, element)
                lt_type = type(self.first.get_info())
                # check if element type and list type are the same
                if isinstance(element, lt_type):
                    return True
            else:
                return False
        except Exception as exp:
            self._handle_error(exp)

    def is_empty(self) -> bool:
        """is_empty _summary_

        Returns:
            bool: _description_
        """
        # TODO add docstring
        try:
            null_node = all([self.first is None,
                             self.last is None])
            return self._size == 0 and null_node
        except Exception as exp:
            self._handle_error(exp)

    def size(self) -> int:
        """size _summary_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            return self._size
        except Exception as exp:
            self._handle_error(exp)

    def add_first(self, element: T) -> None:
        """add_first _summary_

        Args:
            element (T): _description_

        Raises:
            Exception: _description_
        """
        # TODO add docstring
        try:
            if self._check_type(element):
                # create a new node
                new_node = node(element)
                new_node._next = self.first
                self.first = new_node
                if self._size == 0:
                    self.last = self.first
                self._size += 1
            else:
                raise Exception("Invalid node type")
        except Exception as exp:
            self._handle_error(exp)

    def add_last(self, element: T) -> None:
        """add_last _summary_

        Args:
            element (T): _description_

        Raises:
            Exception: _description_
        """
        # TODO add docstring
        try:
            if self._check_type(element):
                # create a new node
                new_node = node(element)
                if self._size == 0:
                    self.first = new_node
                else:
                    self.last._next = new_node
                self.last = new_node
                self._size += 1
            else:
                raise Exception("Invalid node type")
        except Exception as exp:
            self._handle_error(exp)

    def add_element(self, element: T, pos: int) -> None:
        """add_element _summary_

        Args:
            element (T): _description_
            pos (int): _description_

        Raises:
            Exception: _description_
        """
        # TODO add docstring
        try:
            if self._check_type(element):
                new_node = node(element)

                if self._size == 0:
                    self.first = new_node
                    self.last = new_node

                elif pos == 0 and self._size > 0:
                    new_node._next = self.first
                    self.first = new_node

                else:
                    idx = 1
                    prev = self.first
                    current = self.first

                    while idx < pos:
                        prev = current
                        current = current.next()
                        idx += 1
                    new_node._next = current
                    prev._next = new_node
                self._size += 1
            else:
                raise Exception("Invalid node type")
        except Exception as exp:
            self._handle_error(exp)

    def get_first(self) -> Optional[T]:
        """get_first _summary_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        # TODO add docstring
        # TODO check algorithm
        try:
            ans = None
            if self.is_empty():
                raise Exception("Empty data structure")
            if self.first is not None:
                ans = self.first.get_info()
            return ans
        except Exception as exp:
            self._handle_error(exp)

    def get_last(self) -> Optional[T]:
        """get_last _summary_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        # TODO add docstring
        # TODO check algorithm
        try:
            ans = None
            if self.is_empty():
                raise Exception("Empty data structure")
            if self.last is not None:
                ans = self.last.get_info()
            return ans
        except Exception as exp:
            self._handle_error(exp)

    def get_element(self, pos: int) -> Optional[T]:
        """get_element _summary_

        Args:
            pos (int): _description_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        # TODO add docstring
        # TODO check algorithm
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if pos > self._size or pos < 1:
                raise Exception("Index", pos, "is an invalid position")
            else:
                current = self.first
                idx = 1
                while idx < pos:
                    current = current.next()
                    idx += 1
                return current.get_info()
        except Exception as exp:
            self._handle_error(exp)

    def remove_first(self) -> Optional[T]:
        """remove_first _summary_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        # TODO add docstring
        # TODO check algorithm
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if self._size > 0 and self.first is not None:
                temp = self.first.next()
                node = self.first
                self.first = temp
                self._size -= 1
                if self._size == 0:
                    # self.last = self.first
                    self.last = None
                    self.first = None
                return node.get_info()
            else:
                return None
        except Exception as exp:
            self._handle_error(exp)

    def remove_last(self) -> Optional[T]:
        """remove_last _summary_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        # TODO add docstring
        # TODO check algorithm
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if self._size > 0 and self.last is not None:
                if self.first == self.last:
                    node = self.first
                    self.last = None
                    self.first = None
                else:
                    temp = self.first
                    while temp.next() != self.last:
                        temp = temp.next()
                    node = self.last
                    self.last = temp
                    self.last._next = None
                self._size -= 1
                return node.get_info()
            else:
                return None
        except Exception as exp:
            self._handle_error(exp)

    def remove_element(self, pos: int) -> Optional[T]:
        """remove_element _summary_

        Args:
            pos (int): _description_

        Raises:
            Exception: _description_

        Returns:
            Optional[T]: _description_
        """
        # TODO add docstring
        # TODO check algorithm
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if pos < 0 or pos > self._size-1:
                raise Exception("Index", pos, "is an invalid position")
            current = self.first
            prev = self.first
            idx = 0
            if pos == 1:
                self.first = self.first.next()
                self._size -= 1
            elif pos > 1:
                while idx < pos:
                    idx += 1
                    prev = current
                    current = current.next()
                prev._next = current.next()
                self._size -= 1
            return current.get_info()
        except Exception as exp:
            self._handle_error(exp)

    def compare_elements(self, current: T, temp: T) -> int:
        """compare_elements _summary_

        Args:
            current (T): _description_
            temp (T): _description_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            if self.key is not None and self.cmp_function is None:
                return self.default_cmp_function(current, temp)
            else:
                return self.cmp_function(current, temp)
        except Exception as exp:
            self._handle_error(exp)

    def is_present(self, element: T) -> int:
        
        
        """is_present _summary_

        Args:
            element (T): _description_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            lt_size = self._size
            pos = -1
            if lt_size > 0:
                node = self.first
                found = False
                idx = 0
                while not found and idx < lt_size:
                    data = node.get_info()
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = idx
                    idx += 1
                    if node.next() is not None:
                        node = node.next()
            return pos
        except Exception as exp:
            self._handle_error(exp)

    def change_info(self, pos: int, new_info: T) -> None:
        """change_info _summary_

        Args:
            pos (int): _description_
            new_info (T): _description_

        Raises:
            Exception: _description_
            Exception: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if pos > self._size or pos < 1:
                raise Exception("Index", pos, "is an invalid position")
            current = self.first
            idx = 1
            while idx < pos:
                current = current.next()
                idx += 1
            current.set_info(new_info)
        except Exception as exp:
            self._handle_error(exp)

    def exchange(self, pos1: int, pos2: int) -> None:
        """exchange _summary_

        Args:
            pos1 (int): _description_
            pos2 (int): _description_

        Raises:
            Exception: _description_
            Exception: _description_
            Exception: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if pos1 > self._size or pos1 < 1:
                raise Exception("Index", pos1, "is an invalid position")
            if pos2 > self._size or pos2 < 1:
                raise Exception("Index", pos2, "is an invalid position")
            else:
                info_pos1 = self.get_element(pos1)
                info_pos2 = self.get_element(pos2)
                self.change_info(pos1, info_pos2)
                self.change_info(pos2, info_pos1)
                # FIXME check if i need the return in tests!!!
                # return self
        except Exception as exp:
            self._handle_error(exp)

    def create_sublist(self, start: int, end: int) -> "single_linked[T]":
        # TODO add docstring
        try:
            if start < 0 or end > self._size or start > end:
                raise Exception("Invalid sublist")
            else:
                sub_lt = single_linked(cmp_function=self.cmp_function,
                                       key=self.key)
                for i in range(start, end):
                    sub_lt.add_last(self.get_element(i))
                return sub_lt
        except Exception as exp:
            self._handle_error(exp)

    def concatenate(self, lst: "single_linked[T]") -> "single_linked[T]":
        # TODO add docstring
        # FIXXME check the algorithm complexity
        try:
            if not isinstance(lst, single_linked):
                raise Exception("Invalid list type")
            else:
                concat_lt = single_linked(cmp_function=self.cmp_function,
                                          key=self.key)
                concat_lt.first = self.first
                concat_lt.last = self.last
                concat_lt.last._next = lst.first
                concat_lt.last = lst.last
                concat_lt._size = self.size() + lst.size()
                return concat_lt
        except Exception as exp:
            self._handle_error(exp)

    def __iter__(self) -> sll_iterator[T]:
        # TODO add docstring
        return sll_iterator(self.first)




# TODO documentar el uso especifico del parámetro "key" en listas
# TODO Eliminar la carga de datos de la función newList
# FIXME Cambiar el nombre de la funcion para usar snake_case
def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacia.

    Se inicializan los apuntadores a la primera y ultima posicion en None.
    El tipo de la listase inicializa como SINGLE_LINKED
    Args:
        cmpfunction: Función de comparación para los elementos de la lista.
        Si no se provee una función de comparación, se utilizará la función
        de comparación por defecto pero se debe suministrar un valor para key

        key: Identificador que se debe utilizar para la comparación de
        elementos de la lista

        filename: Si se provee este valor, se creará una lista a partir de
        la informacion que se encuentra en el archivo CSV

        delimiter: Si se provee un archivo para crear la lista, indica el
        delimitador a usar para separar los campos del archivo CSV

    Returns:
        Un diccionario que representa la estructura de datos de una lista
        encadanada vacia.

    Raises:

    """
    newlist = {'first': None,
               'last': None,
               'size': 0,
               'key': key,
               'type': 'SINGLE_LINKED',
               'datastructure': module
               }

    if (cmpfunction is None):
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if (filename is not None):
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=delim)
        for line in input_file:
            addLast(newlist, line)
    return newlist


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
# TODO Verificar que el elemento que se esta agregando no sea None
def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, ajusta el apuntador
    al primer elemento e incrementa el tamaño de la lista.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el proceso
        fue exitoso

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        new_node['next'] = lst['first']
        lst['first'] = new_node
        if (lst['size'] == 0):
            lst['last'] = lst['first']
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->addFirst: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
# TODO Verificar que el elemento que se esta agregando no sea None
def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
     el apuntador a la útima posición.
    Se incrementa el tamaño de la lista en 1
    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)

        if lst['size'] == 0:
            lst['first'] = new_node
        else:
            lst['last']['next'] = new_node
        lst['last'] = new_node
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->addLast: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def isEmpty(lst):
    """ Indica si la lista está vacía
    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['size'] == 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->isEmpty: ')


# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def size(lst):
    """ Informa el número de elementos de la lista.
    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['size']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->size: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
     No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['first'] is not None:
            return lst['first']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->fisrtElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['last'] is not None:
            return lst['last']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->lastElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser
    mayor que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        searchpos = 1
        node = lst['first']
        while searchpos < pos:
            searchpos += 1
            node = node['next']
        return node['info']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->getElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista.
    La lista no puede estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        node = lst['first']
        prev = lst['first']
        searchpos = 1
        if (pos == 1):
            lst['first'] = lst['first']['next']
            lst['size'] -= 1
        elif(pos > 1):
            while searchpos < pos:
                searchpos += 1
                prev = node
                node = node['next']
            prev['next'] = node['next']
            lst['size'] -= 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->deleteElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def removeFirst(lst):
    """ Remueve el primer elemento de la lista.
    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.  Si la lista
    es vacía se retorna None.
    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['first'] is not None:
            temp = lst['first']['next']
            node = lst['first']
            lst['first'] = temp
            lst['size'] -= 1
            if (lst['size'] == 0):
                lst['last'] = lst['first']
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->removeFirst: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def removeLast(lst):
    """ Remueve el último elemento de la lista.

    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['size'] > 0:
            if lst['first'] == lst['last']:
                node = lst['first']
                lst['last'] = None
                lst['first'] = None
            else:
                temp = lst['first']
                while temp['next'] != lst['last']:
                    temp = temp['next']
                node = lst['last']
                lst['last'] = temp
                lst['last']['next'] = None
            lst['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
# TODO Verificar que el elemento que se esta agregando no sea None
def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        if (lst['size'] == 0):
            lst['first'] = new_node
            lst['last'] = new_node

        elif ((lst['size'] > 0) and (pos == 1)):
            new_node['next'] = lst['first']
            lst['first'] = new_node

        else:
            cont = 1
            prev = lst['first']
            current = lst['first']
            while cont < pos:
                prev = current
                current = current['next']
                cont += 1
            new_node['next'] = current
            prev['next'] = new_node

        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->insertElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.  Si esta presente,
    retorna la posición en la que se encuentra  o cero (0) si no esta presente.
    Se utiliza la función de comparación utilizada durante la creación
    de la lista para comparar los elementos.
    La cual debe retornar cero en caso de que los elementos sean iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        size = lst['size']
        if size > 0:
            node = lst['first']
            keyexist = False
            for keypos in range(1, size+1):
                if (node is not None):
                    if (compareElements(lst, element, node['info']) == 0):
                        keyexist = True
                        break
                    node = node['next']
            if keyexist:
                return keypos
        return 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->isPresent: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def changeInfo(lst, pos, newinfo):
    """ Cambia la informacion contenida en el nodo de la lista que se encuentra
         en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de
        la posición pos

    Raises:
        Exception
    """
    try:
        current = lst['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->changeInfo: ')


# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    try:
        infopos1 = getElement(lst, pos1)
        infopos2 = getElement(lst, pos2)
        changeInfo(lst, pos1, infopos2)
        changeInfo(lst, pos2, infopos1)
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->exchange: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos,con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        sublst = {'first': None,
                  'last': None,
                  'size': 0,
                  'type': 'SINGLE_LINKED',
                  'key': lst['key'],
                  'datastructure': lst['datastructure'],
                  'cmpfunction': lst['cmpfunction']}
        cont = 1
        loc = pos
        while cont <= numelem:
            elem = getElement(lst, loc)
            addLast(sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->subList: ')


# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    try:
        if(lst is not None):
            current = lst['first']
            while current is not None:
                yield current['info']
                current = current['next']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->Iterator')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo detallado de excepciones con mensajes más especificos
def compareElements(lst, element, info):
    """ Compara dos elementos

    Se utiliza la función de comparación por defecto si key es None
    o la función provista por el usuario en caso contrario
    Args:
        lst: La lista con los elementos
        element:  El elemento que se esta buscando en la lista
        info: El elemento de la lista que se está analizando

    Returns:  0 si los elementos son iguales

    Raises:
        Exception
    """
    try:
        if(lst['key'] is not None):
            return lst['cmpfunction'](element[lst['key']], info[lst['key']])
        else:
            return lst['cmpfunction'](element, info)
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->compareElements')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# FIXME Cambiar el nombre de la funcion para que referencie mejor la cmp func
def defaultfunction(id1, id2):
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0
