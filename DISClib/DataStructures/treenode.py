"""
Los ADTs en este módulo representan los nodos para diferentes tipos de árboles binarios o mapas ordenados. Estos incluyen los nodos para árboles de búsqueda (**BSTNode**), nodos para árboles rojo-negro (**RBTNode**), nodos para árboles AVL (**AVLNode**) y nodos árboles K-d (**KDTNode**).

Estos nodos se utilizan respectivamente en los ADT de árboles binarios de búsqueda o BST (Binary Search Tree), árboles rojo-negro o RBT (Red-Black Tree), árboles rojo-negro orientados a la izquierda p LLRBT (Left-Leaning Red-Black Tree), árboles AVL (Adelson-Velsky & Landis Tree) y árboles k-dimensionales (K-d Tree)

En **DISCLib** las estructuras están asociadas a las implementaciones en **BSTree**, **RBTree**, **LLRBTree**, **AVLTree** y **KDTree**.

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
from DISClib.DataStructures.mapentry import MapEntry

# checking custom modules
assert error_handler
assert T


# colors for the red-black tree
# :param RED
RED = 0
"""
Variable para representar el color negro en un nodo RBT.
"""

# :param BLACK
BLACK = 1
"""
Variable para representar el color negro en un nodo RBT.
"""


@dataclass
class BSTNode(MapEntry, Generic[T]):
    """**BSTNode** representa un nodo de un árbol binario de búsqueda o BST (Binary Search Tree). Basada en el ADT *MapEntry* que contiene la información del nodo (pareja llave-valor).

    Args:
        MapEntry (dataclass): ADT base para implementar una pareja llave-valor.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        BSTNode: ADT para un *BSTNode* o nodo para un árbol binario de búsqueda.
    """

    # optional reference to the left node of the same type
    # :attr: _left
    _left: Optional["BSTNode[T]"] = None
    """Referencia al nodo izquierdo del árbol.
    """

    # optional reference to the right node of the same type
    # :attr: _right
    _right: Optional["BSTNode[T]"] = None
    """Referencia al nodo derecho del árbol.
    """

    # subtree size (number of nodes in subtree) below this node
    # :attr: _size
    _size: int = 0
    """Tamaño del subárbol que cuelga de este nodo (número de nodos en el subárbol).
    """

    def left(self) -> Optional["BSTNode[T]"]:
        """*left()* recupera la referencia al nodo izquierdo del árbol. Si no existe retorna *None*.

        Returns:
            Optional[BSTNode[T]]: referencia al nodo izquierdo del árbol si existe.
        """
        return self._left

    def right(self) -> Optional["BSTNode[T]"]:
        """*right()* recupera la referencia al nodo derecho del árbol. Si no existe retorna *None*.

        Returns:
            Optional[BSTNode[T]]: referencia al nodo derecho del árbol si existe.
        """
        return self._right

    def size(self) -> int:
        """*size()* recupera el tamaño del subárbol que cuelga de este nodo.

        Returns:
            int: tamaño del subárbol que cuelga de este nodo.
        """
        return self._size


@dataclass
class RBTNode(BSTNode, Generic[T]):
    """**RBTNode** representa un nodo de un árbol rojo-negro (RBT: Red-Black Tree), o un árbol rojo-negro orientados a la izquierda (LLRBT: Left-Leaning Red-Black Tree) que contiene la información del nodo (pareja llave-valor).

    Args:
        BSTNode (dataclass): ADT base para implementar un nodo para un árbol binario de búsqueda.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
    """
    # optional reference to the parent node of the same type
    # :attr: _parent
    _parent: Optional["RBTNode[T]"] = None
    """
    Referencia al nodo padre del árbol.
    """

    # color of the node
    # :attr: _color
    _color: int = RED
    """
    Color del nodo, por defecto es rojo.
    """

    def parent(self) -> Optional["RBTNode[T]"]:
        """*parent()* recupera la referencia al nodo padre del árbol. Si no existe retorna *None*.

        Returns:
            Optional[RBTNode[T]]: referencia al nodo padre del árbol si existe.
        """
        return self._parent

    def color(self) -> int:
        """*color()* recupera el color del nodo.

        Returns:
            int: color del nodo.
        """
        return self._color

    def set_color(self, color: int) -> None:
        """*set_color()* establece el color del nodo.

        Args:
            color (int): color del nodo.
        """
        self._color = color

    def is_red(self) -> bool:
        """*is_red()* informa si el nodo es rojo.

        Returns:
            bool: True si el nodo es rojo, False de lo contrario.
        """
        return self._color == RED


@dataclass
class KDTNode(BSTNode, Generic[T]):
    """**KDTreeNode** representa un nodo de un árbol k-dimensionales o K-d Tree. Basada en el ADT *BSTNode* que contiene la información del nodo (pareja llave-valor).

    Args:
        BSTNode (dataclass): ADT base para implementar un nodo para un árbol binario de búsqueda.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
    """

    # optional dimension to split on (if None, split on largest dimension)
    # :attr: _split_dim
    split_dim: Optional[int] = None
    """
    Dimensión para dividir el nodo (si es *None*, dividir en la dimensión más grande).
    """

    def get_dimension(self) -> Optional[int]:
        """*get_dimension()* recupera la dimensión para dividir el nodo. Si no existe retorna *None*.

        Returns:
            Optional[int]: dimensión para dividir el nodo si existe.
        """
        return self.split_dim


@dataclass
class AVLNode(BSTNode, Generic[T]):
    """**AVLNode** representa un nodo de un árbol AVL (Adelson-Velsky & Landis Tree). Basada en el ADT *BSTNode* que contiene la información del nodo (pareja llave-valor).

    Args:
        BSTNode (dataclass): ADT base para implementar un nodo para un árbol binario de búsqueda.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.
    """

    # height-balance factor
    # :attr: _height
    _height: int = 0
    """
    Factor de balance de altura del nodo.
    """

    def height(self) -> int:
        """*height()* recupera el factor de balance del nodo.

        Returns:
            int: factor de balance del nodo.
        """
        return self._height

    def left_height(self) -> int:
        """*left_height()* recupera la altura del subárbol izquierdo del nodo.

        Returns:
            int: altura del subárbol izquierdo del nodo.
        """
        if self._left is None:
            return 0
        return self._left.height()

    def right_height(self) -> int:
        """*right_height()* recupera la altura del subárbol derecho del nodo.

        Returns:
            int: altura del subárbol derecho del nodo.
        """
        if self._right is None:
            return 0
        return self._right.height()
