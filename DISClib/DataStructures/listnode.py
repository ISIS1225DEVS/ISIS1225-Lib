"""
Estas clases representan los nodos para una lista sencillamente encadenada (SingleNode) y una lista doblemente encadenada (DoubleNode).

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
from DISClib.Utils.error import init_type_checker
from DISClib.Utils.default import T
from DISClib.DataStructures.node import Node

# checking costum modules
assert error_handler
assert init_type_checker
assert T


@dataclass
class SingleNode(Node, Generic[T]):
    """SingleNode Clase que representa un nodo de una lista sencillamente encadenada. Extiende la clase Node y contiene la información del nodo.

    Args:
        Node (dataclass): Clase base para implementar un nodo de una lista.
        Generic (T): TAD/ADT que representa el tipo de dato de la información dentro del nodo.

    Returns:
        SingleNode: ADT para un nodo de una lista sencillamente encadenada.
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["SingleNode[T]"] = None
    """Referencia al siguiente nodo de la lista."""

    def next(self) -> Optional["SingleNode[T]"]:
        """next recupera el siguiente nodo de la lista si existe.

        Returns:
            SingleNode: referencia al siguiente nodo de la lista.
        """
        return self._next


@dataclass
class DoubleNode(SingleNode, Generic[T]):
    """DoubleNode Clase que representa un nodo de una lista doblemente encadenada. Extiende las clases SingleNode y Node.

    Args:
        SingleNode (Dataclass): Calse base para implementar un nodo de una lista sencillamente encadenada.
        Generic (T): TAD/ADT que representa el tipo de dato de la información dentro del nodo.

    Returns:
        DoubleNode: ADT para un nodo de una lista doblemente encadenada.
    """
    # optional reference to the previous node of the same type
    # :attr: _prev
    _prev: Optional["DoubleNode[T]"] = None
    """Referencia al nodo anterior de la lista."""

    def prev(self) -> Optional["DoubleNode[T]"]:
        """prev recupera el nodo anterior de la lista si existe.

        Returns:
            _type_: referencia al nodo anterior de la lista.
        """
        return self._prev
