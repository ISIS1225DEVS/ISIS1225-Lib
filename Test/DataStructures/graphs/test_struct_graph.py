"""
# TODO add module documentation
"""

# impoting testing framework
import unittest
import pytest
# import random
from typing import TypeVar


# importing the classes to test
from DISClib.DataStructures.adjlist import AdjancencyList
from DISClib.DataStructures.adjmatrix import AdjancecyMatrix
from DISClib.DataStructures.adjcomponents import Edge
from DISClib.DataStructures.adjcomponents import Vertex

# importing the data to test
from Test.Data.test_data import get_graph_test_data

# asserting module imports
assert AdjancecyMatrix
assert AdjancencyList
assert Edge
assert Vertex
assert get_graph_test_data

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


def cmp_g_test_function(key1: T, entry2: T) -> int:
    """cmp_g_test_function _summary_

    Args:
        key1 (T): _description_
        entry2 (T): _description_

    Raises:
        TypeError: _description_

    Returns:
        int: _description_
    """
    key2 = entry2.get_key()
    if type(key1) is not type(key2):
        err_msg = f"Invalid comparison between {type(key1)} and "
        err_msg += f"{type(key2)} keys"
        raise TypeError(err_msg)
    if (key1 == key2):
        return 0
    elif (key1 > key2):
        return 1
    return -1


class TestAdjacencyList(unittest.TestCase):
    """TestAdjacencyList _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Vertex* como un *fixture*.
        """
        self.global_params = get_graph_test_data()

    def test_default_adjlist(self):
        """test_default_vertex _summary_
        """
        graph = AdjancencyList()
        assert graph is not None


class TestAdjacencyMatrix(unittest.TestCase):
    """TestAdjacencyMatrix _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Vertex* como un *fixture*.
        """
        self.global_params = get_graph_test_data()

    def test_default_adjmatrix(self):
        """test_default_vertex _summary_
        """
        graph = AdjancecyMatrix()
        assert graph is not None
