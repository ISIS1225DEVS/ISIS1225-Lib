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
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config
from DISClib.Utils.error import handle_error
import csv
# import dataclass for defining the node type
from dataclasses import dataclass, field
# import typing for defining the type of the element stored at the node
from typing import List, Optional, Callable, Generic, TypeVar
import inspect
assert config


# Type for the element stored at the node
T = TypeVar("T")    # T can be any type

# valid data types for the node
VALID_DATA_TYPE_LT = [
    int,
    float,
    str,
    bool,
    dict,
    list,
    tuple,
    set,
    dataclass,
]

"""
  Este módulo implementa una estructura de datos lineal,
  como un arreglo de apuntadores a los nodos de la lista.


  Este código está basado en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


def default_cmp_function(id1, id2):
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    elif id1 == id2:
        return 0
    else:
        raise Exception("Invalid comparison")


@dataclass
class array_list(Generic[T]):
    """array_list _summary_

    Args:
        Generic (_type_): _description_
    """
    # using default_factory to generate an empty list
    elements: List[T] = field(default_factory=list)
    _size: int = 0
    # type: str = "ARRAY_LIST"
    # using a default_cmp_function to compare elements
    cmp_function: Optional[Callable[[T, T], int]] = default_cmp_function
    key: Optional[str] = None
    data_struct: Optional[str] = None

    def __post_init__(self):
        # TODO maybe i need it in the future
        pass

    def _handle_error(self, err: Exception) -> None:
        """_handle_error _summary_

        Args:
            err (Exception): _description_
        """
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        handle_error(cur_context, cur_function, err)

    def is_empty(self) -> bool:
        try:
            return self._size == 0
        except Exception as exp:
            self._handle_error(exp)

    def size(self) -> int:
        try:
            return self._size
        except Exception as exp:
            self._handle_error(exp)

    def add_first(self, element: T) -> None:
        try:
            self.elements.insert(0, element)
            self._size += 1
        except Exception as exp:
            self._handle_error(exp)

    def add_last(self, element: T) -> None:
        try:
            self.elements.append(element)
            self._size += 1
        except Exception as exp:
            self._handle_error(exp)

    def add_element(self, element: T, pos: int) -> None:
        try:
            self.elements.insert(pos-1, element)
            self._size += 1
        except Exception as exp:
            self._handle_error(exp)

    def get_first(self) -> T:
        try:
            return self.elements[0]
        except Exception as exp:
            self._handle_error(exp)

    def get_last(self) -> T:
        try:
            return self.elements[self._size-1]
        except Exception as exp:
            self._handle_error(exp)

    def get_element(self, pos: int) -> T:
        try:
            return self.elements[pos-1]
        except Exception as exp:
            self._handle_error(exp)

    def remove_element(self, pos: int) -> T:
        try:
            element = self.elements.pop(pos-1)
            self._size -= 1
            return element
        except Exception as exp:
            self._handle_error(exp)

    def remove_first(self) -> T:
        try:
            element = self.elements.pop(0)
            self._size -= 1
            return element
        except Exception as exp:
            self._handle_error(exp)

    def remove_last(self) -> T:
        try:
            element = self.elements.pop(self._size-1)
            self._size -= 1
            return element
        except Exception as exp:
            self._handle_error(exp)

    def compare_elements(self, element: T, info: T) -> int:
        try:
            if self.key is not None:
                return self.cmp_function(element[self.key], info[self.key])
            else:
                return self.cmp_function(element, info)
        except Exception as exp:
            self._handle_error(exp)

    def is_present(self, element: T) -> int:
        try:
            lt_size = self.size()
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
        try:
            self.elements[pos] = new_info
        except Exception as exp:
            self._handle_error(exp)

    def exchange(self, pos1: int, pos2: int) -> None:
        try:
            info_pos1 = self.get_element(pos1)
            info_pos2 = self.get_element(pos2)
            self.change_info(pos1, info_pos2)
            self.change_info(pos2, info_pos1)
            # return self
        except Exception as exp:
            self._handle_error(exp)

    def create_sublist(self, start: int, end: int) -> "array_list[T]":
        try:
            if start < 0 or end > self.size() or start > end:
                raise Exception("Invalid range")
            else:
                sub_lt = array_list(cmp_function=self.cmp_function)
                for i in range(start, end):
                    sub_lt.add_last(self.get_element(i))
                return sub_lt
                # sub_lt = copy.deepcopy(self)
                # sub_lt.elements = sub_lt.elements[start:end]
                # sub_lt._size = end - start
                # return sub_lt
        except Exception as exp:
            self._handle_error(exp)

    def concatenate(self, lst: "array_list[T]") -> "array_list[T]":
        try:
            if not isinstance(lst, array_list):
                raise Exception("Invalid list type")
            # else:
            concat_lt = array_list(cmp_function=self.cmp_function)
            concat_lt.elements = self.elements + lst.elements
            concat_lt._size = self.size() + lst.size()
            return concat_lt
        except Exception as exp:
            self._handle_error(exp)

    def __iter__(self):
        try:
            return iter(self.elements)
        except Exception as exp:
            self._handle_error(exp)


def cmp_test(e1, e2):
    try:
        if e1["id"] > e2["id"]:
            return 1
        elif e1["id"] < e2["id"]:
            return -1
        elif e1["id"] == e2["id"]:
            return 0
    except Exception:
        raise Exception("Invalid comparison in cmp_test")


if __name__ == "__main__":

    a = array_list()
    print(type(a))
    print(type(a.elements))
    # print(inspect.getmembers(__name__))
    a.add_first({"data": "a", "id": 1})
    a.add_first({"data": "b", "id": 2})
    a.add_first({"data": "c", "id": 3})
    a.add_last({"data": "d", "id": 4})
    a.add_last({"data": "e", "id": 5})
    # a.add_first("bla")

    for i in a:
        print(i, type(i))

    print(a.get_first())
    print(a.get_last())
    print(a.size())
    print(a.is_present({"id": 2}))

    b = array_list(cmp_function=cmp_test)
    b.add_first({"data": "d", "id": 4})
    b.add_last({"data": "e", "id": 5})

    b = a.concatenate(b)
    print(b.size())

    c = a.create_sublist(1, 3)
    print(c.size())
    

#TODO Eliminar la carga de datos de la función newList
#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Mejorar la documentación para especificar el uso del parámetro "key" en listas

def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Un diccionario que representa la estructura de datos de una lista

    Raises:

    """
    newlist = {'elements': [],
               'size': 0,
               'type': 'ARRAY_LIST',
               'cmpfunction': cmpfunction,
               'key': key,
               'datastructure': module

               }

    if(cmpfunction is None):
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if (filename is not None):
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=delim)
        for line in input_file:
            addLast(newlist, line)
    return (newlist)

#FIXME Cambiar el nombre de la funcion para usar snake_case
#FIXME Arreglar la documentación del código
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
#TODO Verificar que el elemento que se esta agregando no sea None
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
    try:
        lst['elements'].insert(0, element)
        lst['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->addFirst: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
#TODO Verificar que el elemento que se esta agregando no sea None
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
    try:
        lst['elements'].append(element)
        lst['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->addLast: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
        error.reraise(exp, 'arraylist->isEmpty: ')

#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
        error.reraise(exp, 'arraylist->size: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
#TODO Verificar que la lista no sea vacía antes de obtener el primer elemento
def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['elements'][0]
    except Exception as exp:
        error.reraise(exp, 'arraylist->firstElement: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['elements'][lst['size']-1]
    except Exception as exp:
        error.reraise(exp, 'arraylist->lastElement: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
    try:
        return lst['elements'][pos-1]
    except Exception as exp:
        error.reraise(exp, 'arraylist->getElement: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
    try:
        lst['elements'].pop(pos-1)
        lst['size'] -= 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->deleteElement: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
        element = lst['elements'].pop(0)
        lst['size'] -= 1
        return element
    except Exception as exp:
        error.reraise(exp, 'arraylist->removeFirst: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
        element = lst['elements'].pop(lst['size']-1)
        lst['size'] -= 1
        return element
    except Exception as exp:
        error.reraise(exp, 'arraylist->remoLast: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
#TODO Verificar que el elemento que se esta agregando no sea None
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
    try:
        lst['elements'].insert(pos-1, element)
        lst['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->insertElement: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
    try:
        size = lst['size']
        if size > 0:
            keyexist = False
            for keypos in range(1, size+1):
                info = lst['elements'][keypos-1]
                if (compareElements(lst, e, info) == 0):
                    keyexist = True
                    break
            if keyexist:
                return keypos
        return 0
    except Exception as exp:
        error.reraise(exp, 'arraylist->isPresent: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
#TODO Verificar que el elemento que se esta agregando no sea None
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
    try:
        lst['elements'][pos-1] = newinfo
    except Exception as exp:
        error.reraise(exp, 'arraylist->changeInfo: ')

#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
#TODO Verificar que las posiciones que se pasan por parametro estén dentro del rango de la lista
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
        error.reraise(exp, 'arraylist->exchange: ')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
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
    try:
        sublst = {'elements': [],
                  'size': 0,
                  'type': 'ARRAY_LIST',
                  'key': lst['key'],
                  'datastructure': lst['datastructure'],
                  'cmpfunction': lst['cmpfunction']}
        elem = pos-1
        cont = 1
        while cont <= numelem:
            sublst['elements'].append(lst['elements'][elem])
            sublst['size'] += 1
            elem += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'arraylist->subList: ')

#TODO Implementar manejo más detallado de excepciones con mensajes más especificos
def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    try:
        if(lst is not None):
            for pos in range(0, lst['size']):
                yield lst['elements'][pos]
    except Exception as exp:
        error.reraise(exp, 'arraylist->Iterator')

#FIXME Cambiar el nombre de la funcion para usar snake_case
#TODO Mejorar la documentacion para el return en caso de que no sean iguales
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
    if(lst['key'] is not None):
        return lst['cmpfunction'](element[lst['key']], info[lst['key']])
    else:
        return lst['cmpfunction'](element, info)

#FIXME Cambiar el nombre de la funcion para que referencie mejor a una compare function
#FIXME Cambiar el nombre de la funcion para usar snake_case

def defaultfunction(id1, id2):
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0