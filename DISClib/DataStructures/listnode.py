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

    Args:
        Generic (_type_): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    info: Optional[T] = None
    _next: Optional["single_node[T]"] = None

    def __post_init__(self):
        valid_types = VALID_DATA_TYPE_LT
        if self.info is not None:
            if not any(isinstance(self.info, t) for t in valid_types):
                raise TypeError("Single Linked List Node: " + TYPE_ERR_MSG)

    def next(self) -> Optional["single_node[T]"]:
        """get_next _summary_

        Returns:
            Optional["single_node[T]"]: _description_
        """
        return self._next


@dataclass
class double_node(Generic[T]):
    """double_node _summary_

    Args:
        Generic (_type_): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """

    info: Optional[T] = None
    _next: Optional["double_node[T]"] = None
    _prev: Optional["double_node[T]"] = None

    def get_element(self):
        """get_element _summary_

        :return: _description_
        :rtype: _type_
        """
        return self.info

    def __post_init__(self):
        valid_types = VALID_DATA_TYPE_LT
        if self.info is not None:
            if not any(isinstance(self.info, t) for t in valid_types):
                raise TypeError("Single Linked List Node: " + TYPE_ERR_MSG)

    def next(self) -> Optional["double_node[T]"]:
        """get_next _summary_

        Returns:
            _type_: _description_
        """
        return self._next

    def prev(self) -> Optional["double_node[T]"]:
        """get_prev _summary_

        Returns:
            _type_: _description_
        """
        return self._prev


def get_element(node: single_node[T] | double_node[T]) -> T:
    """get_element _summary_

    Args:
        node (single_node[T] | double_node[T]): _description_

    Returns:
        T: _description_
    """
    return node.info
