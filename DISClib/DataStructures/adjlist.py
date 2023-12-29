"""
# TODO: agregar descripción del módulo

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass, field
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect

# custom modules
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import lt_default_cmp_funcion
from DISClib.Utils.default import T
from DISClib.Utils.default import DEFAULT_DICT_KEY
from DISClib.Utils.default import VALID_IO_TYPE

# checking custom modules
assert error_handler
assert lt_default_cmp_funcion
assert T
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE


@dataclass
class AdjacencyList(Generic[T]):
    """**AdjacencyList** representa la estructura de datos para arreglos dinamicos (Array List), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        AdjacencyList: ADT de tipo AdjacencyList o Arreglo Dinámico.

    """
    # input elements from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación personalizable por el usuario para reconocer los elementos dentro de la estructura. Es un argumento configurable al crear la estructura. Por defecto es la función *lt_default_cmp_funcion()* propia de *DISClib*.
    """

    # using default_factory to generate an empty list
    # :attr: elements
    elements: List[T] = field(default_factory=list)
    """
    Lista nativa de Python que contiene los elementos de la estructura.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del AdjacencyList, Por defecto es *None* y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.
    """

    # by default, the list is empty
    # FIXME inconsistent use between _size and size()
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del AdjacencyList.
        """
        try:
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DEFAULT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if elements are in a list, add them to the AdjacencyList
            # TODO sometime strange weird in tests
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """*default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el AdjacencyList. Es una función crucial para que la estructura de datos funcione correctamente.

        Args:
            elm1 (Any): primer elemento a comparar.
            elm2 (Any): segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            return lt_default_cmp_funcion(self.key, elm1, elm2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el AdjacencyList.

        Si se presenta un error en AdjacencyList, se formatea el error según el contexto (paquete/clase), la función que lo generó y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el AdjacencyList.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al AdjacencyList sea del mismo tipo contenido dentro de los elementos del AdjacencyList.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el AdjacencyList.

        Args:
            element (T): elemento que se quiere procesar en AdjacencyList.

        Returns:
            bool: operador que indica si el ADT AdjacencyList es del mismo tipo que el elemento que se quiere procesar.
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
 *
 * Dario Correal
 *
 """

# TODO crear consistencia en para importar modulos
# # import config
from DISClib.ADT import maps as map
from DISClib.ADT import lists as lt
from DISClib.DataStructures import adjcomponents as e
from DISClib.Utils import error as error
# assert config

"""
Este código está basado en las implementaciones propuestas en:
- Algorithms, 4th Edition.  R. Sedgewick
- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich
"""


# FIXME cambiar a SnakeCase el formato de funciones y variables
# TODO agregar anotaciones para documentacion automatica
def newGraph(size, cmpfunction, directed, type, datastructure):
    """
    Crea un grafo vacio

    Args:
        size: Tamaño inicial del grafo
        cmpfunction: Funcion de comparacion
        directed: Indica si el grafo es dirigido o no
    Returns:
        Un nuevo grafo vacío
    Raises:
        Exception
    """
    try:
        # FIXME cambiar por datatruct nativo de python
        graph = {'vertices': None,
                 'edges': 0,
                 'type': type,
                 'cmpfunction': cmpfunction,
                 'directed': directed,
                 'indegree': None,
                 'datastructure': datastructure
                 }

        # TODO dejar variables por defecto como constantes del modulo
        # FIXME ajustar comportamiento segun actualizaciones del ADT map

        graph['vertices'] = map.newMap(numelements=size,
                                       maptype='PROBING',
                                       cmpfunction=cmpfunction)
        if (directed):
            # FIXME ajustar comportamiento segun actualizaciones ADT map
            graph['indegree'] = map.newMap(numelements=size,
                                           maptype='PROBING',
                                           cmpfunction=cmpfunction)
        return graph
    except Exception as exp:
        # FIXME ajustar mensaje segun actualizaciones del modulo error
        error.reraise(exp, 'ajlist:newgraph')


def insertVertex(graph, vertex):
    """
    Inserta el vertice vertex en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea insertar
    Returns:
        El grafo graph con el nuevo vertice
    Raises:
        Exception
    """
    # TODO revisar si es necesario el return
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        edges = lt.newList()
        map.put(graph['vertices'], vertex, edges)
        if (graph['directed']):
            map.put(graph['indegree'], vertex, 0)
        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:insertvertex')


def removeVertex(graph, vertex):
    """
    Remueve el vertice vertex del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea remover
    Returns:
        El grafo sin el vertice vertex
    Raises:
        Exception
    """
    # TODO implementar funcion
    pass


def numVertices(graph):
    """
    Retorna el numero de vertices del  grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices del grafo
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        return map.size(graph['vertices'])
    except Exception as exp:
        error.reraise(exp, 'ajlist:numtvertex')


def numEdges(graph):
    """
    Retorna el numero de arcos en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices del grafo
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        return (graph['edges'])
    except Exception as exp:
        error.reraise(exp, 'ajlist:numedges')


def vertices(graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        La lista con los vertices del grafo
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        lstmap = map.keySet(graph['vertices'])
        return lstmap
    except Exception as exp:
        error.reraise(exp, 'ajlist:vertices')


def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        Una lista con los arcos del grafo
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        lstmap = map.valueSet(graph['vertices'])
        lstresp = lt.newList('SINGLE_LINKED', e.compareedges)
        for lstedge in lt.iterator(lstmap):
            for edge in lt.iterator(lstedge):
                if (graph['directed']):
                    lt.addLast(lstresp, edge)
                elif (not lt.isPresent(lstresp, edge)):
                    lt.addLast(lstresp, edge)
        return lstresp
    except Exception as exp:
        error.reraise(exp, 'ajlist:edges')


def degree(graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        element = map.get(graph['vertices'], vertex)
        lst = element['value']
        return (lt.size(lst))
    except Exception as exp:
        error.reraise(exp, 'ajlist:degree')


def indegree(graph, vertex):
    """
    Retorna el numero de arcos que llegan al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar comportamiento para acoplar a manejo de errores
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        if (graph['directed']):
            degree = map.get(graph['indegree'], vertex)
            return degree['value']
        return 0
    except Exception as exp:
        error.reraise(exp, 'ajlist:indegree')


def outdegree(graph, vertex):
    """
    Retorna el numero de arcos que salen del grafo vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar comportamiento para acoplar a manejo de errores
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        if (graph['directed']):
            element = map.get(graph['vertices'], vertex)
            lst = element['value']
            return (lt.size(lst))
        return 0
    except Exception as exp:
        error.reraise(exp, 'ajlist:outdegree')


def getEdge(graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice destino

    Returns:
        El arco que une los verices vertexa y vertexb
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        element = map.get(graph['vertices'], vertexa)
        lst = element['value']
        for edge in lt.iterator(lst):
            if (graph['directed']):
                if (e.either(edge) == vertexa and
                   (e.other(edge, e.either(edge)) == vertexb)):
                    return edge
            elif (e.either(edge) == vertexa or
                (e.other(edge, e.either(edge)) == vertexa)):
                if (e.either(edge) == vertexb or
                   (e.other(edge, e.either(edge)) == vertexb)):
                    return edge
        return None
    except Exception as exp:
        error.reraise(exp, 'ajlist:getedge')


def containsVertex(graph, vertex):
    """
    Retorna si el vertice vertex esta presente en el grafo

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: Vertice que se busca

    Returns:
       True si el vertice esta presente
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        return map.get(graph['vertices'], vertex) is not None
    except Exception as exp:
        error.reraise(exp, 'ajlist:containsvertex')


def addEdge(graph, vertexa, vertexb, weight=0):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
    Si el grafo es no dirigido se adiciona dos veces el mismo arco,
    en el mismo orden
    Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice de destino
        wight: peso del arco

    Returns:
       El grafo con el nuevo arco
    Raises:
        Exception
    """
    # TODO revisar si es necesario el return
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        # Se crea el arco
        edge = e.newEdge(vertexa, vertexb, weight)
        # Se obtienen las listas de adyacencias de cada vertice
        # Se anexa a cada lista el arco correspondiente
        entrya = map.get(graph['vertices'], vertexa)
        lt.addLast(entrya['value'], edge)
        if (not graph['directed']):
            entryb = map.get(graph['vertices'], vertexb)
            edgeb = e.newEdge(vertexb, vertexa, weight)
            lt.addLast(entryb['value'], edgeb)
        else:
            degree = map.get(graph['indegree'], vertexb)
            map.put(graph['indegree'], vertexb, degree['value']+1)
        graph['edges'] += 1
        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:addedge')


def adjacents(graph, vertex):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de adyacencias
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        element = map.get(graph['vertices'], vertex)
        lst = element['value']
        lstresp = lt.newList()
        for edge in lt.iterator(lst):
            v = e.either(edge)
            if (v == vertex):
                lt.addLast(lstresp, e.other(edge, v))
            else:
                lt.addLast(lstresp, v)
        return lstresp
    except Exception as exp:
        error.reraise(exp, 'ajlist:adjacents')


def adjacentEdges(graph, vertex):
    """
    Retorna una lista con todos los arcos asociados a los vértices
    adyacentes de vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de arcos adyacentes
    Raises:
        Exception
    """
    # TODO agregar tipos de datos para input y output
    # FIXME ajustar mensaje segun actualizaciones del modulo error
    try:
        element = map.get(graph['vertices'], vertex)
        lst = element['value']
        return lst
    except Exception as exp:
        error.reraise(exp, 'ajlist:adjacentEdges')
