"""
 * Copyright 2020, Departamento de sistemas y Computación,
 Universidad de Los Andes
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

import importlib
import config
# from DISClib.DataStructures.arraylist import ArrayList
assert config
# assert ArrayList


ADT_LT_PGk_PATH = "DISClib.DataStructures"


# ADT_LIST_MOD_DICT = {
#     "ArrayList": "arraylist",
#     "SingleLinked": "singlelinkedlist",
#     "DoubleLinked": "doublelinkedlist",
# }


class List(object):

    instance = None
    implementation = None
    module_name = None
    module = None
    implementation_class = None

    def __init__(self, implementation: str = "ArrayList", **kwargs):
        try:
            self.implementation = implementation
            self.module_name = f"{ADT_LT_PGk_PATH}.{implementation.lower()}"
            self.module = importlib.import_module(self.module_name)
        except ModuleNotFoundError:
            raise ValueError(f"Invalid implementation: {implementation}")
        self.implementation_class = getattr(self.module,
                                            self.implementation)
        self.instance = self.implementation_class(**kwargs)

    def __post_init__(self):
        self.__class__.__name__ = self.implementation

    def __repr__(self) -> str:
        return self.instance.__repr__()

    def __getattr__(self, name):
        # delegate attribute access to the implementation instance
        return getattr(self.instance, name)

    def start(self):
        # FIXME this is a hack!!!
        return self.instance

    @classmethod
    def __class__(self) -> type:
        # FIXME this is not working
        # delegate type() to the implementation instance
        return self.instance.__class__

    @classmethod
    def __instancecheck__(self, instance) -> bool:
        # check if the instance is an instance of the implementation class
        # FIXME this is not working
        return isinstance(instance, self.instance.__class__)

"""
  Este módulo implementa el tipo abstracto de datos (TAD) lista.
  Se puede implementar sobre una estructura de datos encadenada de forma
  sencilla, doble o como un arreglo
"""


def cmp_test(a, b):
    key = "testkey"
    ka = a.get(key)
    kb = b.get(key)
    if ka < kb:
        return -1
    elif ka > kb:
        return 1
    else:
        return 0


test_list = List(implementation="ArrayList").start()
print(test_list)
print(type(test_list))

test_data = [1, 2, 3, 4, 5]

for i in test_data:
    test_list.add_last(i)

print(test_list)

test_data = [
    {"testkey": 1, "testvalue": "one"},
    {"testkey": 2, "testvalue": "two"},
    {"testkey": 3, "testvalue": "three"},
    {"testkey": 4, "testvalue": "four"},
    {"testkey": 5, "testvalue": "five"},
]

test_list = List(implementation="ArrayList",
                 elements=test_data,
                 cmp_function=cmp_test).start()
print(test_list)

for d in test_list:
    print(d)


                #  cmpfunction=None, key=None, filename=None, delimiter=",")


# FIXME Cambiar formato de funciones a snake_case
# TODO Implementar manejo más detallado de excepciones
# TODO Mejorar la documentacion del retorno del compare functions
# TODO Mejorar la documentación para el uso del parámetro "key" en listas
def newList(datastructure='SINGLE_LINKED',
            cmpfunction=None,
            key=None,
            filename=None,
            delimiter=","):
    """Crea una lista vacia

    Args:
        datastructure:  Tipo de estructura de datos a utilizar para implementar
        la lista. Los tipos posibles pueden ser: ARRAY_LIST,
        SINGLE_LINKED y DOUBLE_LINKED.

        cmpfunction: Función de comparación para los elementos de la lista.
        Si no se provee función de comparación se utiliza la función
        por defecto pero se debe proveer un valor para key.
        Si se provee una función de comparación el valor de Key debe ser None.

        Key:  Identificador utilizado para comparar dos elementos de la lista
        con la función de comaparación por defecto.

        filename: Si se provee este valor, se crea una lista a partir
        de los elementos encontrados en el archivo.
        Se espera que sea un archivo CSV UTF8.

        delimiter: Si se pasa un archivo en el parámetro filename, se utiliza
        este valor para separar los campos. El valor por defecto es una coma.

    Returns:
        Una nueva lista
    Raises:
        Exception
    """
    try:
        module = listSelector(datastructure)
        lst = module.newList(
            cmpfunction,
            module,
            key,
            filename,
            delimiter
        )
        return lst
    except Exception as exp:
        raise Exception('TADList->newList: ' + str(exp))
        # error.reraise(exp, 'TADList->newList: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, se incrementa
    el tamaño de la lista en uno.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el
        proceso fue exitoso

    Raises:
        Exception
    """
    try:
        lst['datastructure'].addFirst(lst, element)
    except Exception as exp:
        raise Exception('TADList->addFirst: ' + str(exp))
        # error.reraise(exp, 'TADList->addFirst: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
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
        lst['datastructure'].addLast(lst, element)
    except Exception as exp:
        raise Exception('TADList->addLast: ' + str(exp))
        # error.reraise(exp, 'TADList->addLast: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
# TODO Mejorar la documentación para definir el return en cada caso
def isEmpty(lst):
    """ Indica si la lista está vacía

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].isEmpty(lst)
    except Exception as exp:
        raise Exception('TADList->isEmpty: ' + str(exp))
        # error.reraise(exp, 'TADList->isEmpty: ')


# TODO Implementar manejo más detallado de excepciones
# TODO Mejorar la documentación para definir el return en cada caso
def size(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].size(lst)
    except Exception as exp:
        raise Exception('TADList->size: ' + str(exp))
        # error.reraise(exp, 'TADList->size: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].firstElement(lst)
    except Exception as exp:
        raise Exception('TADList->firstElement: ' + str(exp))
        # error.reraise(exp, 'TADList->firstElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].lastElement(lst)
    except Exception as exp:
        raise Exception('TADList->lastElement: ' + str(exp))
        # error.reraise(exp, 'TADList->LastElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
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
        return lst['datastructure'].getElement(lst, pos)
    except Exception as exp:
        raise Exception('TADList->getElement: ' + str(exp))
        # error.reraise(exp, 'List->getElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor  o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista. La lista no puede
    estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        lst['datastructure'].deleteElement(lst, pos)
    except Exception as exp:
        raise Exception('TADList->deleteElement: ' + str(exp))
        # error.reraise(exp, 'TADList->deleteElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def removeFirst(lst):
    """ Remueve el primer elemento de la lista.

    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.
    Si la lista es vacía se retorna None.

    Args:
        lst: La lista a examinar

    Returns:
        El primer elemento de la lista
    Raises:
        Exception
    """
    try:
        return lst['datastructure'].removeFirst(lst)
    except Exception as exp:
        raise Exception('TADList->removeFirst: ' + str(exp))
        # error.reraise(exp, 'TADList->removeFirst: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def removeLast(lst):
    """ Remueve el último elemento de la lista.

    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Returns:
        El ultimo elemento de la lista
    Raises:
        Exception
    """
    try:
        return lst['datastructure'].removeLast(lst)
    except Exception as exp:
        raise Exception('TADList->removeLast: ' + str(exp))
        # error.reraise(exp, 'TADList->removeLast: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
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
        lst['datastructure'].insertElement(lst, element, pos)
    except Exception as exp:
        raise Exception('TADList->insertElement: ' + str(exp))
        # error.reraise(exp, 'TADList->insertElement: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.
    Si esta presente, retorna la posición en la que se encuentra
    o cero (0) si no esta presente. Se utiliza la función de comparación
    utilizada durante la creación de la lista para comparar los elementos.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar
    Returns:

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].isPresent(lst, element)
    except Exception as exp:
        raise Exception('TADList->isPresent: ' + str(exp))
        # error.reraise(exp, 'TADList->isPresent: ')


# TODO Implementar manejo más detallado de excepciones
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
        lst['datastructure'].exchange(lst, pos1, pos2)
    except Exception as exp:
        raise Exception('List->exchange: ' + str(exp))
        # error.reraise(exp, 'List->exchange: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def changeInfo(lst, pos, element):
    """ Cambia la informacion contenida en el nodo de la lista
        que se encuentra en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de
        la posición pos

    Raises:
        Exception
    """
    try:
        lst['datastructure'].changeInfo(lst, pos, element)
    except Exception as exp:
        raise Exception('List->changeInfo: ' + str(exp))
        # error.reraise(exp, 'List->changeInfo: ')


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo más detallado de excepciones
def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].subList(lst, pos, numelem)
    except Exception as exp:
        raise Exception('List->subList: ' + str(exp))
        # error.reraise(exp, 'List->subList: ')


# TODO Implementar manejo más detallado de excepciones
# TODO Mejorar la documentacion de lo que hace esta funcion
def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    try:
        return lst['datastructure'].iterator(lst)
    except Exception as exp:
        raise Exception('List->Iterator: ' + str(exp))
        # error.reraise(exp, 'List->Iterator: ')


"""
Selector dinamico de la estructua de datos solicitada
"""
# TODO convertir en data class
switch_module = {
    "ARRAY_LIST": ".arraylist",
    "SINGLE_LINKED": ".singlelinkedlist",
    "DOUBLE_LINKED": ".doublelinkedlist"
}


# FIXME Cambiar el nombre de la funcion para usar snake_case
# TODO Implementar manejo de excepciones para switch_module (Raise ValueError)
# TODO Especificar los tipos de datos de entrada y salida de cada función
def listSelector(datastructure):
    """
    Carga dinamicamente el import de la estructura de datos
    seleccionada
    """
    ds = switch_module.get(datastructure)
    module = importlib.import_module(ds, package="DISClib.DataStructures")
    return module
