# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import Generic, TypeVar, Optional, Union
import inspect

# importing DISClib type + error handling
import config
from DISClib.Utils.error import error_handler
from DISClib.Utils.error import type_checker
assert config


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
# TYPE_ERR_MSG = "Invalid data type for node info"


@dataclass
class single_node(Generic[T]):
    """single_node _summary_

    Args:
        Generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    # TODO add docstring
    info: Optional[T] = None
    _next: Optional["single_node[T]"] = None

    def __post_init__(self):
        """__post_init__ _summary_
        """
        # TODO add docstring
        if self.info is not None:
            cur_function = inspect.currentframe().f_code.co_name
            cur_context = self.__class__.__name__
            type_checker(cur_context, cur_function, self.info)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error _summary_

        Args:
            err (Exception): _description_
        """
        # TODO add docstring
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def next(self) -> Optional["single_node[T]"]:
        """next _summary_

        Returns:
            _type_: _description_
        """
        # TODO add docstring
        return self._next

    def get_element(self) -> T:
        """get_element _summary_

        Returns:
            T: _description_
        """
        # TODO add docstring
        return _get_element(self)

    def set_element(self, element: T) -> None:
        """set_element _summary_

        Args:
            element (T): _description_
        """
        # TODO add docstring
        try:
            _set_element(self, element)
        except Exception as exp:
            self._handle_error(exp)


@dataclass
class double_node(Generic[T]):
    """double_node _summary_

    Args:
        Generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    # TODO add docstring
    info: Optional[T] = None
    _next: Optional["double_node[T]"] = None
    _prev: Optional["double_node[T]"] = None

    def __post_init__(self):
        """__post_init__ _summary_
        """
        # TODO add docstring
        if self.info is not None:
            cur_function = inspect.currentframe().f_code.co_name
            cur_context = self.__class__.__name__
            type_checker(cur_context, cur_function, self.info)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error _summary_

        Args:
            err (Exception): _description_
        """
        # TODO add docstring
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def next(self) -> Optional["double_node[T]"]:
        """next _summary_

        Returns:
            _type_: _description_
        """
        # TODO add docstring
        return self._next

    def prev(self) -> Optional["double_node[T]"]:
        """prev _summary_

        Returns:
            _type_: _description_
        """
        # TODO add docstring
        return self._prev

    def get_element(self) -> T:
        """get_element _summary_

        Returns:
            T: _description_
        """
        # TODO add docstring
        return _get_element(self)

    def set_element(self, element: T) -> None:
        """set_element _summary_

        Args:
            element (T): _description_
        """
        # TODO add docstring
        try:
            _set_element(self, element)
        except Exception as exp:
            self._handle_error(exp)


# TODO add docstring
NODE_TP_LT = Union[single_node[T], double_node[T]]


def _get_element(node: NODE_TP_LT) -> T:
    """_get_element _summary_

    Args:
        node (NODE_TP_LT): _description_

    Returns:
        T: _description_
    """
    # TODO add docstring
    return node.info


def _set_element(node: NODE_TP_LT, element: T) -> None:
    """_set_element _summary_

    Args:
        node (NODE_TP_LT): _description_
        element (T): _description_
    """
    # TODO add docstring
    node.info = element
