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
    pass
