"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 * Contribució n de:
 *
 * Dario Correal
 *
 """

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass, field
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic, TypeVar
# import inspect for getting the name of the current function
import inspect

# custom modules
import config
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.error import type_checker

# checking costum modules
assert config
assert error_handler
assert type_checker


# Type for the element stored in the list
T = TypeVar("T")    # T can be any type

"""
  Este módulo implementa una estructura de datos lineal,
  como un arreglo de apuntadores a los nodos de la lista.


  Este código está basado en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


@dataclass
class array_list(Generic[T]):
    """array_list _summary_

    Args:
        Generic (_type_): _description_
    """
    # TODO add docstring
    # using default_factory to generate an empty list
    elements: List[T] = field(default_factory=list)
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
        # if elements are in list, convert them to a array_list
        if isinstance(self.elements, list):
            elements = self.elements
            self.elements = list()
            for elm in elements:
                self.add_last(elm)
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

    def default_cmp_function_v2(self, elm1, elm2) -> int:
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
            py_type = (int, float, str, bool)
            elm1_type = isinstance(elm1, py_type)
            elm2_type = isinstance(elm2, py_type)
            none_type = (self.key is None)
            # using the key to compare elements
            if self.key is not None:
                # if the elements are dict, compare their main key
                if isinstance(elm1, dict) and isinstance(elm2, dict):
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
            # if elements are native types, compare them
            elif all([none_type, elm1_type, elm2_type]):
                # if one is greater than the other, return 1
                if elm1 > elm2:
                    return 1
                # if one is less than the other, return -1
                elif elm1 < elm2:
                    return -1
                # if they are equal, return 0
                elif elm1 == elm2:
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
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
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
            if self._size == 0 and len(self.elements) == 0:
                return True
            elif self._size > 0:
                # get the type of the first element
                cur_context = self.__class__.__name__
                cur_function = inspect.currentframe().f_code.co_name
                # check if the type of the element is valid
                type_checker(cur_context, cur_function, element)
                lt_type = type(self.elements[0])
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
            return self._size == 0 and len(self.elements) == 0
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
                self.elements.insert(0, element)
                self._size += 1
            else:
                raise Exception("Invalid element type")
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
                self.elements.append(element)
                self._size += 1
            else:
                raise Exception("Invalid element type")
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
                self.elements.insert(pos, element)
                self._size += 1
            else:
                raise Exception("Invalid element type")
        except Exception as exp:
            self._handle_error(exp)

    def get_first(self) -> T:
        """get_first _summary_

        Raises:
            Exception: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            else:
                return self.elements[0]
        except Exception as exp:
            self._handle_error(exp)

    def get_last(self) -> T:
        """get_last _summary_

        Raises:
            Exception: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            else:
                return self.elements[self._size-1]
        except Exception as exp:
            self._handle_error(exp)

    def get_element(self, pos: int) -> T:
        """get_element _summary_

        Args:
            pos (int): _description_

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            elif pos < 0 or pos > self._size-1:
                raise Exception("Index", pos, "is an invalid position")
            else:
                return self.elements[pos]
        except Exception as exp:
            self._handle_error(exp)

    def remove_first(self) -> T:
        """remove_first _summary_

        Raises:
            Exception: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            else:
                element = self.elements.pop(0)
                self._size -= 1
                return element
        except Exception as exp:
            self._handle_error(exp)

    def remove_last(self) -> T:
        """remove_last _summary_

        Raises:
            Exception: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            else:
                element = self.elements.pop(self._size-1)
                self._size -= 1
                return element
        except Exception as exp:
            self._handle_error(exp)

    def remove_element(self, pos: int) -> T:
        """remove_element _summary_

        Args:
            pos (int): _description_

        Raises:
            Exception: _description_

        Returns:
            T: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise Exception("Empty data structure")
            if pos < 0 or pos > self._size-1:
                raise Exception("Index", pos, "is an invalid position")
            else:
                element = self.elements.pop(pos-1)
                self._size -= 1
                return element
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
                # return self.cmp_function(current[self.key], temp[self.key])
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
                found = False
                i = 0
                # print("inside is present!!!")
                while not found and i < lt_size:
                    data = self.get_element(i)
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
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
        """
        # TODO add docstring
        try:
            if self._check_type(new_info):
                self.elements[pos] = new_info
            else:
                raise Exception("Invalid element type")
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

    def create_sublist(self, start: int, end: int) -> "array_list[T]":
        """create_sublist _summary_

        Args:
            start (int): _description_
            end (int): _description_

        Raises:
            Exception: _description_

        Returns:
            array_list[T]: _description_
        """
        # TODO add docstring
        try:
            if start < 0 or end > self._size or start > end:
                raise Exception("Invalid range")
            else:
                sub_lt = array_list(cmp_function=self.cmp_function,
                                    key=self.key)
                for i in range(start, end):
                    sub_lt.add_last(self.get_element(i))
                return sub_lt
        except Exception as exp:
            self._handle_error(exp)

    def concatenate(self, lst: "array_list[T]") -> "array_list[T]":
        """concatenate _summary_

        Args:
            lst (array_list[T]): _description_

        Raises:
            Exception: _description_

        Returns:
            array_list[T]: _description_
        """
        # TODO add docstring
        # FIXME check if the list is empty!!!
        try:
            if not isinstance(lst, array_list):
                raise Exception("Invalid list type")
            else:
                concat_lt = array_list(cmp_function=self.cmp_function,
                                       key=self.key)
                concat_lt.elements = self.elements + lst.elements
                concat_lt._size = self.size() + lst.size()
                return concat_lt
        except Exception as exp:
            self._handle_error(exp)

    def __iter__(self):
        """__iter__ _summary_

        Returns:
            _type_: _description_
        """
        # TODO add docstring
        try:
            return iter(self.elements)
        except Exception as exp:
            self._handle_error(exp)


# TODO Mejorar la documentación para especificar el uso del parámetro "key"
def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Un diccionario que representa la estructura de datos de una lista

    Raises:

    """
    pass


# FIXME Arreglar la documentación del código
def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, se incrementa
    el tamaño de la lista en uno.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el proceso
        fue exitoso

    Raises:
        Exception
    """
    pass


def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
    el apuntador a la útima posición. Se incrementa el tamaño de la lista en 1

    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    pass


def isEmpty(lst):
    """ Indica si la lista está vacía

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    pass


def size(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    pass


# TODO Verificar que la lista no sea vacía antes de obtener el primer elemento
def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    pass


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    pass


def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser mayor
    que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    pass


def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor  o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista.
    La lista no puede estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    pass


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
    pass


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
    pass


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.
    Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    pass


def isPresent(lst, e):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.
    Si esta presente, retorna la posición en la que se encuentra
    o cero (0) si no esta presente. Se utiliza la función de comparación
    utilizada durante la creación de la lista para comparar los elementos,
    la cual debe retornan cero si los elementos son iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    pass


def changeInfo(lst, pos, newinfo):
    """ Cambia la informacion contenida en el nodo de la lista
        que se encuentra en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el
        nodo de la posición pos

    Raises:
        Exception
    """
    pass


def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    pass


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la posicion
    pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    pass


def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    pass


# TODO Mejorar la documentacion para el return en caso de que no sean iguales
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
    # """
    pass
