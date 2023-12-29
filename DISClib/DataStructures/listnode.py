"""
Estos ADTs representan los nodos para una lista sencillamente encadenada (**SingleNode**) y una lista doblemente encadenada (**DoubleNode**).

Estos nodos se utilizan respectivamente en las estructuras dinámicas de lista sencillamente encadenada (**LinkedList**) y lista doblemente encadenada (**DoubleLinkedList**). Las cuales NO tienen un tamaño fijo y pueden crecer indefinidamente en la memoria disponible.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass for defining the node class
from dataclasses import dataclass
# import modules for defining the Node type
from typing import Optional, Generic

# custom modules
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import T
from DISClib.DataStructures.node import Node

# checking custom modules
assert error_handler
assert T


@dataclass
class SingleNode(Node, Generic[T]):
    """**SingleNode** representa un nodo de una lista sencillamente encadenada. Basada en el ADT *Node* que contiene la información del nodo.

    Args:
        Node (dataclass): ADT base para implementar un nodo con información genérica.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.


    Returns:
        SingleNode: ADT para un *SingleNode* o nodo para una lista sencillamente encadenada.
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["SingleNode[T]"] = None
    """
    Referencia al siguiente nodo de la lista.
    """

    def next(self) -> Optional["SingleNode[T]"]:
        """*next()* recupera la referencia el siguiente nodo de la lista. Si no existe retorna *None*.

        Returns:
            Optional[SingleNode[T]]: referencia al siguiente *Node* de la lista si existe.
        """
        return self._next


@dataclass
class DoubleNode(SingleNode, Generic[T]):
    """**DoubleNode** representa un nodo de una lista doblemente encadenada. Basada en el ADT *SingleNode* que contiene la información del nodo.

    Args:
        SingleNode (Dataclass): ADT base para implementar un nodo con información genérica.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        DoubleNode: ADT para un *DoubleNode* o nodo para una lista doblemente encadenada.
    """
    # optional reference to the previous node of the same type
    # :attr: _prev
    _prev: Optional["DoubleNode[T]"] = None
    """
    Referencia al anterior nodo anterior de la lista.
    """

    def prev(self) -> Optional["DoubleNode[T]"]:
        """*prev()* recupera la referencia al anterior *DoubleNode* de la lista. Si no existe retorna *None*.

        Returns:
            Optional[DoubleNode[T]]: referencia al anterior *DoubleNode* si existe.
        """
        return self._prev
