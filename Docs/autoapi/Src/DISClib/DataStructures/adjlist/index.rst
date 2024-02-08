:py:mod:`Src.DISClib.DataStructures.adjlist`
============================================

.. py:module:: Src.DISClib.DataStructures.adjlist

.. autoapi-nested-parse::

   # TODO: agregar descripción del módulo

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.adjlist.AdjacencyList



Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.adjlist.newGraph
   Src.DISClib.DataStructures.adjlist.insertVertex
   Src.DISClib.DataStructures.adjlist.removeVertex
   Src.DISClib.DataStructures.adjlist.numVertices
   Src.DISClib.DataStructures.adjlist.numEdges
   Src.DISClib.DataStructures.adjlist.vertices
   Src.DISClib.DataStructures.adjlist.edges
   Src.DISClib.DataStructures.adjlist.degree
   Src.DISClib.DataStructures.adjlist.indegree
   Src.DISClib.DataStructures.adjlist.outdegree
   Src.DISClib.DataStructures.adjlist.getEdge
   Src.DISClib.DataStructures.adjlist.containsVertex
   Src.DISClib.DataStructures.adjlist.addEdge
   Src.DISClib.DataStructures.adjlist.adjacents
   Src.DISClib.DataStructures.adjlist.adjacentEdges



.. py:class:: AdjacencyList


   Bases: :py:obj:`Generic`\ [\ :py:obj:`Src.DISClib.Utils.default.T`\ ]

   **AdjacencyList** representa la estructura de datos para arreglos dinamicos (Array List), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

   :param Generic: TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
   :type Generic: T

   :returns: ADT de tipo AdjacencyList o Arreglo Dinámico.
   :rtype: AdjacencyList

   .. py:attribute:: iodata
      :type: Optional[List[Src.DISClib.Utils.default.T]]

      Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.

   .. py:attribute:: cmp_function
      :type: Optional[Callable[[Src.DISClib.Utils.default.T, Src.DISClib.Utils.default.T], int]]

      Función de comparación personalizable por el usuario para reconocer los elementos dentro de la estructura. Es un argumento configurable al crear la estructura. Por defecto es la función *lt_default_cmp_funcion()* propia de *DISClib*.

   .. py:attribute:: elements
      :type: List[Src.DISClib.Utils.default.T]

      Lista nativa de Python que contiene los elementos de la estructura.

   .. py:attribute:: key
      :type: Optional[str]

      Nombre de la llave opcional que se utiliza para comparar los elementos del AdjacencyList, Por defecto es *None* y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.

   .. py:attribute:: _size
      :type: int
      :value: 0

      Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.

   .. py:method:: __post_init__() -> None

      *__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del AdjacencyList.



   .. py:method:: default_cmp_function(elm1, elm2) -> int

      *default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el AdjacencyList. Es una función crucial para que la estructura de datos funcione correctamente.

      :param elm1: primer elemento a comparar.
      :type elm1: Any
      :param elm2: segundo elemento a comparar.
      :type elm2: Any

      :returns: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
      :rtype: int


   .. py:method:: _handle_error(err: Exception) -> None

      *_handle_error()* función privada que maneja los errores que se pueden presentar en el AdjacencyList.

      Si se presenta un error en AdjacencyList, se formatea el error según el contexto (paquete/clase), la función que lo generó y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

      :param err: Excepción que se generó en el AdjacencyList.
      :type err: Exception


   .. py:method:: _check_type(element: Src.DISClib.Utils.default.T) -> bool

      *_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al AdjacencyList sea del mismo tipo contenido dentro de los elementos del AdjacencyList.

      :raises TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el AdjacencyList.

      :param element: elemento que se quiere procesar en AdjacencyList.
      :type element: T

      :returns: operador que indica si el ADT AdjacencyList es del mismo tipo que el elemento que se quiere procesar.
      :rtype: bool



.. py:function:: newGraph(size, cmpfunction, directed, type, datastructure)

   Crea un grafo vacio

   :param size: Tamaño inicial del grafo
   :param cmpfunction: Funcion de comparacion
   :param directed: Indica si el grafo es dirigido o no

   :returns: Un nuevo grafo vacío

   :raises Exception:


.. py:function:: insertVertex(graph, vertex)

   Inserta el vertice vertex en el grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice que se desea insertar

   :returns: El grafo graph con el nuevo vertice

   :raises Exception:


.. py:function:: removeVertex(graph, vertex)

   Remueve el vertice vertex del grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice que se desea remover

   :returns: El grafo sin el vertice vertex

   :raises Exception:


.. py:function:: numVertices(graph)

   Retorna el numero de vertices del  grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: El numero de vertices del grafo

   :raises Exception:


.. py:function:: numEdges(graph)

   Retorna el numero de arcos en el grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: El numero de vertices del grafo

   :raises Exception:


.. py:function:: vertices(graph)

   Retorna una lista con todos los vertices del grafo graph
   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: La lista con los vertices del grafo

   :raises Exception:


.. py:function:: edges(graph)

   Retorna una lista con todos los arcos del grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: Una lista con los arcos del grafo

   :raises Exception:


.. py:function:: degree(graph, vertex)

   Retorna el numero de arcos asociados al vertice vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se desea conocer el grado

   :returns: El grado del vertice

   :raises Exception:


.. py:function:: indegree(graph, vertex)

   Retorna el numero de arcos que llegan al vertice vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se desea conocer el grado

   :returns: El grado del vertice

   :raises Exception:


.. py:function:: outdegree(graph, vertex)

   Retorna el numero de arcos que salen del grafo vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se desea conocer el grado

   :returns: El grado del vertice

   :raises Exception:


.. py:function:: getEdge(graph, vertexa, vertexb)

   Retorna el arco asociado a los vertices vertexa ---- vertexb

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertexa: Vertice de inicio
   :param vertexb: Vertice destino

   :returns: El arco que une los verices vertexa y vertexb

   :raises Exception:


.. py:function:: containsVertex(graph, vertex)

   Retorna si el vertice vertex esta presente en el grafo

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: Vertice que se busca

   :returns: True si el vertice esta presente

   :raises Exception:


.. py:function:: addEdge(graph, vertexa, vertexb, weight=0)

   Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
   Si el grafo es no dirigido se adiciona dos veces el mismo arco,
   en el mismo orden
   Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertexa: Vertice de inicio
   :param vertexb: Vertice de destino
   :param wight: peso del arco

   :returns: El grafo con el nuevo arco

   :raises Exception:


.. py:function:: adjacents(graph, vertex)

   Retorna una lista con todos los vertices adyacentes al vertice vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se quiere la lista

   :returns: La lista de adyacencias

   :raises Exception:


.. py:function:: adjacentEdges(graph, vertex)

   Retorna una lista con todos los arcos asociados a los vértices
   adyacentes de vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se quiere la lista

   :returns: La lista de arcos adyacentes

   :raises Exception:


