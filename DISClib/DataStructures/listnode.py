# import dataclass for defining the node type
from dataclasses import dataclass
# import typing for defining the type of the element stored at the node
from typing import Generic, TypeVar, Optional
# import inspect for getting the name of the current function
import inspect
# importing DISClib type + error handling
import config
from DISClib.Utils.error import error_handler
from DISClib.Utils.error import init_type_checker
assert error_handler
assert init_type_checker
assert config

# Type for the element stored at the node
T = TypeVar("T")    # T can be any type


@dataclass
class SingleNode(Generic[T]):
    """SingleNode data class to represents a node of a single linked list.

    Args:
        Generic (T): type of the information stored at the node.

    Returns:
        SingleNode: node of a single linked list.
    """
    # optional information of any type
    info: Optional[T] = None
    # optional reference to the next node of the same type
    _next: Optional["SingleNode[T]"] = None

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
        except Exception as exp:
            self._handle_error(exp)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error the generic function handles the error received as
            an argument.

        Args:
            err (Exception): received error to handle.
        """
        # TODO add docstring
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def get_info(self) -> T:
        """get_info the function returns the information inside the node.

        Returns:
            T: information of the node.
        """
        # TODO add docstring
        return self.info

    def set_info(self, element: T) -> None:
        """set_info the function sets the new information inside the node.

        Args:
            element (T): new information for the node.

        Raises:
            TypeError: exception raised if the type of the new information is
                different from the type of the current information.
        """

        # TODO add docstring
        if not isinstance(element, type(self.info)):
            err_msg = f"Invalid data type: {type(self.info)} "
            err_msg += f"for element info: {type(element)}"
            raise TypeError(err_msg)
        self.info = element

    def next(self) -> Optional["SingleNode[T]"]:
        """next the function returns the next node of the list.

        Returns:
            SingleNode[T]: next node of the list, if it exists.
        """
        # TODO add docstring
        return self._next


@dataclass
class DoubleNode(Generic[T]):
    """DoubleNode data class to represents a node of a double linked list.

    Args:
        Generic (T): type of the information stored at the node.

    Returns:
        DoubleNode: node of a double linked list.
    """
    # optional information of any type
    info: Optional[T] = None
    # optional reference to the next node of the same type
    _next: Optional["DoubleNode[T]"] = None
    # optional reference to the previous node of the same type
    _prev: Optional["DoubleNode[T]"] = None

    def __post_init__(self):
        """__post_init__ the function checks the type of the information after
            the data structure initialization.
        """
        # TODO add docstring
        try:
            if self.info is not None:
                cur_function = inspect.currentframe().f_code.co_name
                cur_context = self.__class__.__name__
                init_type_checker(cur_context, cur_function, self.info)
        except Exception as exp:
            self._handle_error(exp)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error the generic function handles the error received as
            an argument.

        Args:
            err (Exception): received error to handle.
        """
        # TODO add docstring
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def next(self) -> Optional["DoubleNode[T]"]:
        """next the function returns the next node of the list.

        Returns:
            DoubleNode[T]: the next node of the list, if it exists.
        """
        # TODO add docstring
        return self._next

    def prev(self) -> Optional["DoubleNode[T]"]:
        """prev the function returns the previous node of the list.

        Returns:
            DoubleNode[T]: the previous node of the list, if it exists.
        """
        # TODO add docstring
        return self._prev

    def get_info(self) -> T:
        """get_info the function returns the information inside the node.

        Returns:
            T: information of the node.
        """
        # TODO add docstring
        return self.info

    def set_info(self, element: T) -> None:
        """set_info the function sets the new information inside the node.

        Args:
            element (T): new information for the node.

        Raises:
            TypeError: exception raised if the type of the new information is
                different from the type of the current information.
        """
        # TODO add docstring
        if not isinstance(element, type(self.info)):
            err_msg = f"Invalid data type: {type(self.info)} "
            err_msg += f"for element info: {type(element)}"
            raise TypeError(err_msg)
        self.info = element
