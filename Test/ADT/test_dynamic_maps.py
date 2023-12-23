"""
*test_dynamic_maps.py* es el módulo que prueba el ADT dinámico y configurable *Map* de *DISClib* y sus funciones complementarias *clone()* y *translate()
"""
# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.maps import Map
from DISClib.ADT.maps import clone
from DISClib.ADT.maps import translate

# import the data to test
from Test.Data.test_data import get_dynamap_test_data

# asserting module imports
assert Map
assert clone
assert translate
assert get_dynamap_test_data


class TestDynamicMap(unittest.TestCase):
    pass
