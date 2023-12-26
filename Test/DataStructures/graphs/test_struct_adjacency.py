"""
# TODO add module documentation
"""

# impoting testing framework
import unittest
import pytest
# import random
from typing import TypeVar


# importing the classes to test
from DISClib.DataStructures.adjcomponents import Edge
from DISClib.DataStructures.adjcomponents import Vertex

# importing the data to test
from Test.Data.test_data import get_gedgevertex_test_data

# asserting module imports
assert Edge
assert Vertex
assert get_gedgevertex_test_data

# Type for the element stored in the list
# :data: T: TypeVar
T = TypeVar("T")
"""
Variable nativa de Python para definir una estructura de datos genérica en los ADTs.
"""

# list of keys to ignore in the global parameters
# :data: IGNORE_KEYS_LT: list
IGNORE_KEYS_LT = (
    "TEST_NENTRIES",
    "TEST_SC_HT_CONFIG",
    "TEST_LP_HT_CONFIG",
    "CHECK_KEY_TYPE_LT",
    "CHECK_VALUE_TYPE_LT",
    "CHECK_KEY_ERR_LT",
    "CHECK_VALUE_ERR_LT"
)
"""
Lista de llaves a ignorar en los parámetros globales en las pruebas.
"""


class TestVertex(unittest.TestCase):
    """TestVertex _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Vertex* como un *fixture*.
        """
        self.global_params = get_gedgevertex_test_data()

    def test_default_vertex(self):
        """test_default_vertex _summary_
        """
        pass


class TestEdge(unittest.TestCase):
    """TestEdge _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Vertex* como un *fixture*.
        """
        self.global_params = get_gedgevertex_test_data()

    def test_default_edge(self):
        """test_default_vertex _summary_
        """
        pass
