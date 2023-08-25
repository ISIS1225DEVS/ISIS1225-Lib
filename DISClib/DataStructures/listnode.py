# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import Generic, TypeVar, Optional


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

# generic error message for invalid data type
TYPE_ERR_MSG = "Invalid data type for node info"


@dataclass
class single_node(Generic[T]):
    """single_node _summary_

    :param Generic: _description_
    :type Generic: _type_
    :return: _description_
    :rtype: _type_
    """
    info: T
    next_node: Optional["single_node[T]"] = None

    def __post_init__(self):
        valid_types = VALID_DATA_TYPE_LT
        if not any(isinstance(self.info, t) for t in valid_types):
            raise TypeError("Single Linked List Node: " + TYPE_ERR_MSG)

    def get_element(self) -> T:
        """get_element _summary_

        :return: _description_
        :rtype: T
        """
        return self.info


@dataclass
class double_node(Generic[T]):
    """double_node _summary_

    :param Generic: _description_
    :type Generic: _type_
    :return: _description_
    :rtype: _type_
    """
    info: T
    next_node: Optional["double_node[T]"] = None
    prev_node: Optional["double_node[T]"] = None

    def get_element(self):
        """get_element _summary_

        :return: _description_
        :rtype: _type_
        """
        return self.info

    def __post_init__(self):
        valid_types = VALID_DATA_TYPE_LT
        if not any(isinstance(self.info, t) for t in valid_types):
            raise TypeError("Double Linked List Node: " + TYPE_ERR_MSG)


def get_element(node: single_node[T] | double_node[T]) -> T:
    """get_element _summary_

    :param node: _description_
    :type node: single_node[T] | double_node[T]
    :return: _description_
    :rtype: T
    """
    return node.info


# def newSingleNode(element):
#         """
#         Estructura que contiene la información a guardar en una lista encadenada
#         """
#         node = {"info": element, "next": None}
#         return(node)


# def getElement(node):
#         """
#         Retorna la información de un nodo
#         Args:
#             node: El nodo a examinar
#         Returns:
#             La información almacenada en el nodo
#         """
#         return node["info"]


# def newDoubleNode(element):
#         """
#         Estructura que contiene la información a guardar en una lista encadenada
#         doblemente
#         """
#         node = {"info": element,
#                         "next": None,
#                         "prev": None
#                         }
#         return node
