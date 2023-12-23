"""
*test_adt_stack.py* es el módulo que prueba el ADT *Stack* (pila) de *DISClib* basado en una lista sencillamente encadenada (SinglyLinked).
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.stack import Stack

# import the data to test
from Test.Data.test_data import get_list_test_data

# asserting module imports
assert Stack
assert get_list_test_data


class TestStack(unittest.TestCase):
    """TestStack _summary_

    Args:
        unittest (_type_): _description_
    """
    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """inject_fixtures _summary_
        """
        self.global_params = get_list_test_data()

    def test_new_default_stack(self):
        """test_default_stack _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None

    def test_new_custom_stack(self):
        """test_custom_stack _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None

    def test_push(self):
        """test_push _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None

    def test_pop(self):
        """test_pop _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None

    def test_top(self):
        """test_top _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None

    def test_is_empty(self):
        """test_is_empty _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None

    def test_size(self):
        """test_size _summary_
        """
        # get the global parameters
        # params = self.global_params

        # create the stack
        stack = Stack()
        assert stack is not None
