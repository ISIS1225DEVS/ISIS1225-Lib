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

# importing the data to test
from Test.Data.test_data import get_nodetree_test_data

# asserting module imports
assert BSTNode
assert KDTNode
assert RBTNode
assert AVLNode


class TestBSTNode(unittest.TestCase):
    """**TestBSTNode** son las pruebas de tipo *unittest* que validan el funcionamiento de la estructura **Node**.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Node* como un *fixture*.
        """
        self.global_params = get_nodetree_test_data()

    def test_new_default_bstnode(self):
        """*test_new_default_node* prueba para crear un nodo vacío de una lista enlazada.
        """
        # create an empty single linked list node
        node = BSTNode()
        # assert for node information is None
        assert node.info is None


class TestKDTNode(unittest.TestCase):
    """**TestKDTNode** son las pruebas de tipo *unittest* que validan el funcionamiento de la estructura **Node**.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Node* como un *fixture*.
        """
        self.global_params = get_nodetree_test_data()

    def test_new_default_kdtnode(self):
        """*test_new_default_node* prueba para crear un nodo vacío de una lista enlazada.
        """
        # create an empty single linked list node
        node = BSTNode()
        # assert for node information is None
        assert node.info is None


class TestRBTNode(unittest.TestCase):
    """**TestRBTNode** son las pruebas de tipo *unittest* que validan el funcionamiento de la estructura **Node**.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Node* como un *fixture*.
        """
        self.global_params = get_nodetree_test_data()

    def test_new_default_rbtnode(self):
        """*test_new_default_node* prueba para crear un nodo vacío de una lista enlazada.
        """
        # create an empty single linked list node
        node = BSTNode()
        # assert for node information is None
        assert node.info is None


class TestAVLNode(unittest.TestCase):
    """**TestAVLNode** son las pruebas de tipo *unittest* que validan el funcionamiento de la estructura **Node**.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Node* como un *fixture*.
        """
        self.global_params = get_nodetree_test_data()

    def test_new_default_avlnode(self):
        """*test_new_default_node* prueba para crear un nodo vacío de una lista enlazada.
        """
        # create an empty single linked list node
        node = BSTNode()
        # assert for node information is None
        assert node.info is None
