"""
# TODO agregar descripcion del modulo y del ADT que implementa!!!

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# TODO complete imports
# native python modules
# import dataclass for defining the node class
from dataclasses import dataclass
# import modules for defining the Node type
from typing import Generic, Optional
# import inspect for getting the name of the current function
import inspect

# custom modules
# generic error handling and type checking
from Src.DISClib.Utils.error import error_handler
from Src.DISClib.Utils.default import T

# checking custom modules
assert error_handler
assert T


@dataclass
class Edge(Generic[T]):
    """Edge _summary_

    Args:
        Generic (_type_): _description_
    """
    # TODO implement the class
    pass


@dataclass
class Vertex(Generic[T]):
    """Vertex _summary_

    Args:
        Generic (_type_): _description_
    """
    # TODO implement the class
    pass


"""
 # TODO cambiar comentarios de lincencia segun estandard del equipo
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
 * Darío Correal
 """

# FIXME agregar el manejo de excepciones de la libreria
# TODO crear consistencia en para importar modulos
# import config
# assert config

"""
Este código está basado en las implementaciones propuestas en:
- Algorithms, 4th Edition.  R. Sedgewick
- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich
"""


# FIXME cambiar a SnakeCase el formato de funciones y variables
# TODO agregar anotaciones para documentacion automatica
def newEdge(va, vb, weight=0):
    """
    Crea un nuevo arco entrelos vertices va y vb
    """
    # FIXME cambiar por datatruct nativo de python
    edge = {'vertexA': va,
            'vertexB': vb,
            'weight': weight
            }
    return edge


def weight(edge):
    """
    Retorna el peso de un arco
    """
    # FIXME falta agregar el manejo de excepciones
    # FIXME ajustar comportamiento de edge segun funciones dict()
    # TODO agregar tipos de datos para input y output
    return edge['weight']


def either(edge):
    """
    Retorna el vertice A del arco
    """
    # FIXME falta agregar el manejo de excepciones
    # FIXME ajustar comportamiento de edge segun funciones dict()
    # TODO agregar tipos de datos para input y output
    return edge['vertexA']


def other(edge, veither):
    """
    Retorna el vertice B del arco
    """
    # FIXME falta agregar el manejo de excepciones
    # FIXME ajustar comportamiento de edge segun funciones dict()
    # TODO agregar tipos de datos para input y output
    # TODO mejorar documentacion para entender el funcionamiento
    if (veither == edge['vertexA']):
        return edge['vertexB']
    elif (veither == edge['vertexB']):
        return edge['vertexA']


def compareedges(edge1, edge2):
    """
    Compara dos arcos y retorna True si son iguales
    """
    # FIXME falta agregar el manejo de excepciones
    # FIXME ajustar comportamiento de edge segun funciones dict()
    # TODO agregar tipos de datos para input y output
    # TODO mejorar documentacion para entender el funcionamiento

    e1v = either(edge1)
    e2v = either(edge2)

    if e1v == e2v:
        if other(edge1, e1v) == other(edge2, e2v):
            return True
    return False
