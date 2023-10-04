# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import Generic, TypeVar, Optional
# import inspect for getting the name of the current function
import inspect
# importing DISClib type + error handling
# import config
from DISClib.Utils.error import error_handler
from DISClib.Utils.error import init_type_checker
assert error_handler
assert init_type_checker
# assert config

# Type for the element stored at the node
T = TypeVar("T")    # T can be any type


@dataclass
class Node(Generic[T]):
    """Node generic class for defining a node of a list.

    Args:
        Generic (T): can be any python type.

    Raises:
        TypeError: only valid data types are allowed.

    Returns:
        Node: generic node of a list.
    """
    # optional information of any type
    info: Optional[T] = None

    def __post_init__(self):
        """__post_init__ the function checks the type of the information after
            the data structure initialization.
        """
        try:
            # if the info attribute is not None, check its type
            if self.info is not None:
                cur_function = inspect.currentframe().f_code.co_name
                cur_context = self.__class__.__name__
                init_type_checker(cur_context, cur_function, self.info)
        # if an error occurs, handle it
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error the generic function handles the error received as
            an argument.

        Args:
            err (Exception): received error to handle.
        """
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> None:
        """_check_type the function checks the type of the information received
            as an argument.

        Args:
            element (T): information to check its type.

        Raises:
            TypeError: exception raised if the type of the new information is
                different from the type of the current information.

        Returns:
            bool: returns True if the type of the new information is the same
                as the type of the current information.
        """
        if element is not None and not isinstance(element, type(self.info)):
            err_msg = f"Invalid data type: {type(self.info)} "
            err_msg += f"for element info: {type(element)}"
            raise TypeError(err_msg)
        return True

    def set_info(self, element: T) -> None:
        """set_info the function sets the new information inside the node.

        Args:
            element (T): new information for the node.
        """
        if self.info is not None:
            self._check_type(element)
        self.info = element

    def get_info(self) -> T:
        """get_info the function returns the information inside the node.

        Returns:
            T: information of the node.
        """
        return self.info


@dataclass
class SingleNode(Node, Generic[T]):
    """SingleNode generic class for defining a node of a single linked list.
    extends Node class.

    Args:
        Node (dataclass): generic node of a list.
        Generic (T): can be any python type.

    Returns:
        SingleNode: generic node of a single linked list.
    """
    # optional reference to the next node of the same type
    _next: Optional["SingleNode[T]"] = None

    def next(self) -> Optional["SingleNode[T]"]:
        """next the function returns the next node of the list.

        Returns:
            SingleNode[T]: next node of the list, if it exists.
        """
        return self._next


@dataclass
class DoubleNode(SingleNode, Generic[T]):
    """DoubleNode generic class for defining a node of a double linked list.
    extends SingleNode class.

    Args:
        SingleNode (dataclass): generic node of a single linked list.
        Generic (T): can be any python type.

    Returns:
        DoubleNode: generic node of a double linked list.
    """
    # optional reference to the previous node of the same type
    _prev: Optional["DoubleNode[T]"] = None

    def prev(self) -> Optional["DoubleNode[T]"]:
        """prev the function returns the previous node of the list.

        Returns:
            DoubleNode[T]: the previous node of the list, if it exists.
        """
        return self._prev
