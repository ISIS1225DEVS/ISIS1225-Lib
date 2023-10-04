""" _summary_
# TODO add summary

Attributes:
    T (type): _description_

Class:
    ArrayList(Generic[T]): _description_

    Functions:
        - __init__(): _description_
        - __post_init__(): _description_
        - default_cmp_function(): _description_
        - _handle_error(): _description_
        - _check_type(): _description_
        - is_empty(): _description_
        - size(): _description_
        - add_first(): _description_
        - add_last(): _description_
        - add_element(elem, pos): _description_
        - get_first(): _description_
        - get_last(): _description_
        - get_element(pos): _description_
        - remove_first(): _description_
        - remove_last(): _description_
        - remove_element(pos): _description_
        - compare_elements(elem1, elem2): _description_
        - is_present(elem): _description_
        - change_info(new_elem, pos): _description_
        - exchange(pos1, pos2): _description_
        - sublist(start, end): _description_
        - concat(other): _description_

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería, 2023
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
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
from DISClib.Utils.error import init_type_checker
from DISClib.Utils.error import VALID_DATA_TYPE_LT

# checking costum modules
assert config
assert error_handler
assert init_type_checker


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
class ArrayList(Generic[T]):
    """ArrayList _summary_

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
        try:
            # if the key is not defined, use the default
            if self.key is None:
                self.key = "id"
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if elements are in a list, add them to the ArrayList
            if isinstance(self.elements, list):
                elements = self.elements
                self.elements = list()
                for elm in elements:
                    self.add_last(elm)

        except Exception as err:
            self._handle_error(err)

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
            elm1_type = isinstance(elm1, VALID_DATA_TYPE_LT)
            elm2_type = isinstance(elm2, VALID_DATA_TYPE_LT)
            # none_type = (self.key is None)
            # if the elements are from different types, raise an exception
            if type(elm1) is not type(elm2):
                err_msg = f"Invalid comparison between {type(elm1)} and "
                err_msg += f"{type(elm2)} elements"
                raise TypeError(err_msg)
            # if there is a defined key
            elif self.key is not None:
                # if elements are dictionaries, compare their main key
                if isinstance(elm1, dict) and isinstance(elm2, dict):
                    key1 = elm1.get(self.key)
                    key2 = elm2.get(self.key)
                    if None in [key1, key2]:
                        err_msg = f"Invalid key: {self.key}, "
                        err_msg += "Key not found in one or both elements"
                        raise KeyError(err_msg)
                    # comparing elements
                    else:
                        # if one is less than the other, return -1
                        if key1 < key2:
                            return -1
                        # if they are equal, return 0
                        elif key1 == key2:
                            return 0
                        # if one is greater than the other, return 1
                        elif key1 > key2:
                            return 1
                        # otherwise, raise an exception
                        else:
                            err_msg = f"Invalid comparison between {key1} and "
                            err_msg += f"{key2} keys in elements."
                            raise TypeError(err_msg)
                # if elements are native types, compare them directly
                elif elm1_type and elm2_type:
                    # if one is less than the other, return -1
                    if elm1 < elm2:
                        return -1
                    # if one is greater than the other, return 1
                    elif elm1 > elm2:
                        return 1
                    # otherwise, they are equal, return 0
                    else:
                        return 0
        except Exception as err:
            self._handle_error(err)

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

    def is_empty(self) -> bool:
        """is_empty _summary_

        Returns:
            bool: _description_
        """
        # TODO add docstring
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    def size(self) -> int:
        """size _summary_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

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
        except Exception as err:
            self._handle_error(err)

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
        except Exception as err:
            self._handle_error(err)

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
            if not self.is_empty():
                if self._check_type(element):
                    if pos < 0 or pos > self._size:
                        raise IndexError("Position is out of range")
                    self.elements.insert(pos, element)
                    self._size += 1
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            return self.elements[0]
        except Exception as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            return self.elements[self._size-1]
        except Exception as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size-1:
                raise IndexError("Index", pos, "is out of range")
            return self.elements[pos]
        except Exception as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            element = self.elements.pop(0)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            element = self.elements.pop(self._size-1)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size-1:
                raise IndexError("Index", pos, "is out of range")
            element = self.elements.pop(pos)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """compare_elements _summary_

        Args:
            elem1 (T): _description_
            elem2 (T): _description_

        Returns:
            int: _description_
        """
        # TODO add docstring
        try:
            # if the key is defined but the cmp is not, use the default
            if self.key is not None and self.cmp_function is None:
                return self.default_cmp_function(elem1, elem2)
            # otherwise, use the custom cmp function
            if self.cmp_function is not None:
                return self.cmp_function(elem1, elem2)
            # raise an exception if the cmp function is not defined
            raise TypeError("Undefined compare function!!!")
        except Exception as err:
            self._handle_error(err)

    def is_present(self, element: T) -> int:
        """is_present _summary_

        Args:
            element (T): _description_

        Returns:
            int: _description_
        """
        # TODO add docstring
        # TODO change the method name to "find" or "present_in"?
        try:
            pos = -1
            if self._size > 0:
                found = False
                i = 0
                while not found and i < self._size-1:
                    data = self.get_element(i)
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
            return pos
        except Exception as err:
            self._handle_error(err)

    def change_info(self, new_info: T, pos: int) -> None:
        """change_info _summary_

        Args:
            new_info (T): _description_
            pos (int): _description_

        Raises:
            Exception: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size-1:
                raise IndexError("Index", pos, "is out of range")
            # if not self._check_type(new_info):
            elif self._check_type(new_info):
                # raise TypeError("Invalid element type")
                self.elements[pos] = new_info
        except (IndexError, TypeError) as err:
            self._handle_error(err)

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
                raise IndexError("Empty data structure")
            elif pos1 < 0 or pos1 > self._size-1:
                raise IndexError("Index", pos1, "is out of range")
            elif pos2 < 0 or pos2 > self._size-1:
                raise IndexError("Index", pos2, "is out of range")
            info_pos1 = self.get_element(pos1)
            info_pos2 = self.get_element(pos2)
            self.change_info(info_pos2, pos1)
            self.change_info(info_pos1, pos2)
            # FIXME check if i need the return in tests!!!
            # return self
        except Exception as err:
            self._handle_error(err)

    def sublist(self, start: int, end: int) -> "ArrayList[T]":
        """create_sublist _summary_

        Args:
            start (int): _description_
            end (int): _description_

        Raises:
            Exception: _description_

        Returns:
            ArrayList[T]: _description_
        """
        # TODO add docstring
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self._size-1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = ArrayList(cmp_function=self.cmp_function,
                               key=self.key)
            for i in range(start, end):
                element = self.get_element(i)
                if self._check_type(element):
                    sub_lt.add_last(element)
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "ArrayList[T]") -> "ArrayList[T]":
        """concat_list _summary_

        Args:
            other (ArrayList[T]): _description_

        Raises:
            Exception: _description_

        Returns:
            ArrayList[T]: _description_
        """
        # TODO add docstring
        try:
            if not isinstance(other, ArrayList):
                err_msg = f"Structure is not an ArrayList: {type(other)}"
                raise TypeError(err_msg)
            if self.key != other.key:
                raise TypeError(f"Invalid key: {self.key} != {other.key}")
            # checking function code
            code1 = self.cmp_function.__code__.co_code
            code2 = other.cmp_function.__code__.co_code
            if code1 != code2:
                err_msg = f"Invalid cmp_function: {self.cmp_function}"
                err_msg += f" != {other.cmp_function}"
                raise TypeError(err_msg)
            concat_lt = ArrayList(cmp_function=self.cmp_function,
                                  key=self.key)
            concat_lt.elements = self.elements + other.elements
            concat_lt._size = self._size + other._size
            return concat_lt
        except TypeError as err:
            self._handle_error(err)

    def __iter__(self):
        """__iter__ _summary_

        Returns:
            _type_: _description_
        """
        # TODO add docstring
        try:
            return iter(self.elements)
        except Exception as err:
            self._handle_error(err)


# TODO Mejorar la documentación para especificar el uso del parámetro "key"
# def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Un diccionario que representa la estructura de datos de una lista

    Raises:

    """
    # pass


# FIXME Arreglar la documentación del código
# def addFirst(lst, element):
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
    # pass


# def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
    el apuntador a la útima posición. Se incrementa el tamaño de la lista en 1

    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    # pass


# def isEmpty(lst):
    """ Indica si la lista está vacía

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    # pass


def size(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    # pass


# TODO Verificar que la lista no sea vacía antes de obtener el primer elemento
# def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    # pass


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    # pass


# def getElement(lst, pos):
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
    # pass


# def deleteElement(lst, pos):
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
    # pass


# def removeFirst(lst):
    """ Remueve el primer elemento de la lista.

    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.  Si la lista
    es vacía se retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    # pass


# def removeLast(lst):
    """ Remueve el último elemento de la lista.

    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    # pass


# def insertElement(lst, element, pos):
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
    # pass


# def isPresent(lst, e):
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
    # pass


# def changeInfo(lst, pos, newinfo):
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
    # pass


# def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    # pass


# def subList(lst, pos, numelem):
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
    # pass


# def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    # pass


# TODO Mejorar la documentacion para el return en caso de que no sean iguales
# def compareElements(lst, element, info):
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
    # pass
