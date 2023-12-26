"""
*test_struct_nodes* es el módulo que prueba las estructuras de datos **Node** (en TestNode), **SingleNode** (en TestSingleNode) y **DoubleNode** (en TestDoubleNode) para el ADT dinámico y configurable **List**.
"""

# import testing package
import unittest
import pytest

# importing the modules to test
from DISClib.DataStructures.treenode import BSTNode
from DISClib.DataStructures.treenode import KDTNode
from DISClib.DataStructures.treenode import RBTNode
from DISClib.DataStructures.treenode import AVLNode
from DISClib.DataStructures.listnode import SingleNode
from DISClib.DataStructures.listnode import DoubleNode

# importing the data to test
from Test.Data.test_data import get_nodelist_test_data

# asserting module imports
assert Node
assert SingleNode
assert DoubleNode
assert get_nodelist_test_data


class TestNode(unittest.TestCase):
    """**TestNode** son las pruebas de tipo *unittest* que validan el funcionamiento de la estructura **Node**.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Node* como un *fixture*.
        """
        self.global_params = get_nodelist_test_data()

    def test_new_default_node(self):
        """*test_new_default_node* prueba para crear un nodo vacío de una lista enlazada.
        """
        # create an empty single linked list node
        node = Node()
        # assert for node information is None
        assert node.info is None
