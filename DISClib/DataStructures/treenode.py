"""
Estos ADTs representan los nodos para una lista sencillamente encadenada (SingleNode) y una lista doblemente encadenada (DoubleNode).

Estos nodos se utilizan respectivamente en las estructuras dinámicas de lista sencillamente encadenada (LinkedList) y lista doblemente encadenadA(DoubleLinkedList). Las cuales NO tienen un tamaño fijo y pueden crecer indefinidamente en la memoria disponible.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass for defining the node class
from dataclasses import dataclass
# import modules for defining the Node type
from typing import Generic, Optional

# custom modules
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import T
from DISClib.DataStructures.node import Node

# checking custom modules
assert error_handler
assert T


@dataclass
class BSTNode(Node, Generic[T]):
    """BSTNode _summary_

    Args:
        Node (_type_): _description_
        Generic (_type_): _description_
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["BSTNode[T]"] = None
    """Referencia al siguiente nodo de la lista."""

    def next(self) -> Optional["BSTNode[T]"]:
        pass


@dataclass
class AVLNode(BSTNode, Generic[T]):
    """AVLNode _summary_

    Args:
        BSTNode (_type_): _description_
        Generic (_type_): _description_
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["AVLNode[T]"] = None
    """Referencia al siguiente nodo de la lista."""

    def next(self) -> Optional["AVLNode[T]"]:
        pass
    
    
@dataclass
class RBTNode(BSTNode, Generic[T]):
    """RBTNode _summary_

    Args:
        BSTNode (_type_): _description_
        Generic (_type_): _description_
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["RBTNode[T]"] = None
    """Referencia al siguiente nodo de la lista."""

    def next(self) -> Optional["RBTNode[T]"]:
        pass


@dataclass
class KDNode(BSTNode, Generic[T]):
    """KDNode _summary_

    Args:
        BSTNode (_type_): _description_
        Generic (_type_): _description_
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["KDNode[T]"] = None
    """Referencia al siguiente nodo de la lista."""

    def next(self) -> Optional["KDNode[T]"]:
        pass


"""
BST NODE!!!!!!!!
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
* Contribución de:
*
* Dario Correal
*
"""
# GENERAL
#FIXME Cambiar todas las funciones y variables al formato snake_case
#TODO Explicar más a profundidad que tipo de excepciones y errores puede generar cada función

def newNode(key, value, size):
    """ Crea un nuevo nodo para un árbol binario y lo retorna
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    #FIXME Modelar como dataclass
    node = {'key': key,
            'value': value,
            'size': size,
            'left': None,
            'right': None,
            'type': 'BST'}
    return node


def getValue(node):
    """ Retorna el valor asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        El valor almacenado en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return(node['value'])
    return node


def getKey(node):
    """ Retorna la llave asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        La llave almacenada en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return(node['key'])
    return node



"""
RBT NODE!!!!!!!!
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

# GENERAL
# FIXME Cambiar todas las funciones y variables al formato snake_case
# TODO Explicar tipo de excepciones y errores puede generar cada función


RED = 0
BLACK = 1


def newNode(key, value, size, color):
    """
    Crea un nuevo nodo para un árbol rojo-negro  y lo retorna.
    color:0 - rojo  color:1 - negro
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo
        color: El color inicial del nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    # FIXME Modelar como dataclass
    node = {'key': key,
            'value': value,
            'size': size,
            'parent': None,
            'left': None,
            'right': None,
            'color': color,
            'type': 'RBT'}

    return node


def isRed(node):
    """
    Informa si un nodo es rojo
    Args:
        node: El nodo a revisar

    Returns:
        True si el nodo es rojo, False de lo contrario
    Raises:
        Exception
    """
    return (node['color'] == RED)


def getValue(node):
    """ Retorna el valor asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        El valor almacenado en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return (node['value'])
    return node


def getKey(node):
    """ Retorna la llave asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        La llave almacenada en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return (node['key'])
    return node
