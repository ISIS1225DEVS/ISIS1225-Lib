﻿"""
*test_struct_nodes* es el módulo que prueba las estructuras de datos *Node*, *SingleNode* y *DoubleNode* para el ADT dinámico y configurable *List*.
"""

# import testing package
import unittest
import pytest

# importing the modules to test
from DISClib.DataStructures.node import Node
from DISClib.DataStructures.listnode import SingleNode
from DISClib.DataStructures.listnode import DoubleNode

# importing the data to test
from Test.Data.test_data import get_node_test_data

# asserting module imports
assert Node
assert SingleNode
assert DoubleNode
assert get_node_test_data


class TestNode(unittest.TestCase):
    """*TestNode* es la clase *unittest* que prueba la clase *Node*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Node* como un *fixture*.
        """
        self.global_params = get_node_test_data()

    def test_new_default_node(self):
        """*test_new_default_node* prueba la creación de un nodo vacío de una lista enlazada.
        """
        # create an empty single linked list node
        node = Node()
        # assert for node information is None
        assert node.info is None

    def test_new_custom_node(self):
        """*test_new_custom_node()* prueba la creación de un nodo *Node* de una lista enlazada con datos personalizados.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a single linked list node with test_data
                node = Node(test_data)
                # assert for node info is not None
                assert node.info == test_data
                # assert for node info is the same type as test_data
                assert isinstance(node.info, dtype)

    def test_get_info(self):
        """*test_get_info()* prueba como obtener la información del nodo *Node* de la lista enlazada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params list and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a single linked list node with test_data
                node = Node(test_data)
                # assert the node info is the test_data
                assert node.info == test_data
                # assert the data can be retrieved with the get_info()
                assert node.get_info() == test_data
                # assert get_info() returns the same type as test_data
                assert isinstance(node.get_info(), dtype)

    def test_set_info(self):
        """*test_set_info()* prueba como actualizar la información del nodo *Node* de la lista enlazada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params list and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create an empty single linked list node
                node = Node()
                # update the node info with test data using set_info()
                node.set_info(test_data)
                # assert the node info is test_data
                assert node.info == test_data
                # assert the info type is the same as test_data
                assert isinstance(node.info, dtype)
                assert isinstance(test_data, dtype)

    def test_node_typerr(self):
        """*test_node_typerr()* prueba el manejo de errores y excepciones en el nodo *Node* de la lista enlazada.
        """
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a single linked list node with test_data
                with pytest.raises(TypeError) as excinfo:
                    node = Node(test_data)
                    # induce the error by changing the node info type
                    node.set_info(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data, dtype)
                # assert the node info is not the same type as err
                assert dtype != err

    def test_node_handle_error(self):
        """*test_node_handle_error()* prueba el manejo de errores y excepciones en el nodo *Node* de la lista enlazada.
        """
        # TODO complete test
        pass


class TestSingleNode(unittest.TestCase):
    """*TestSingleNode* es la clase *unittest* que prueba la clase *SingleNode*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *SingleNode* como un *fixture*.
        """
        self.global_params = get_node_test_data()

    def test_new_default_single_node(self):
        """*test_new_default_node()* prueba la creación de un nodo vacío de una lista sencillamente encadenada *SingleNode*.
        """
        # create an empty single linked list node
        node = SingleNode()
        # assert for node information is None
        assert (node.info is None)
        # assert for node _next and next() are None
        assert (node.next() is None) and (node._next is None)

    def test_new_custom_single_node(self):
        """*test_new_custom_node()* prueba la creación de un nodo *SingleNode* de una lista sencillamente encadenada con datos personalizados.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a single linked list node with test_data
                node = SingleNode(test_data)
                # assert for node info is not None
                assert node.info == test_data
                # assert for node info is the same type as test_data
                assert isinstance(node.info, dtype)
                # assert the node _next and next() are None
                assert (node.next() is None) and (node._next is None)

    def test_single_node_next(self):
        """*test_node_next()* prueba el manejo de referencias del siguiente nodo *SingleNode* de la lista sencillamente encadenada.
        """
        # iterate over the global params list and create a node for each type
        for key in self.global_params.keys():
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create 2 single linked list node
                node1 = SingleNode(test_data)
                node2 = SingleNode(test_data)
                # assert the node _next and next() are None in both nodes
                assert (node1.next() is None) and (node1._next is None)
                assert (node2.next() is None) and (node2._next is None)
                # concatenate the nodes
                node1._next = node2
                # assert the node _next and next() are not None in node1
                assert (node1.next() is not None) and (node1._next is not None)
                # assert the node _next and next() are node2 in node1
                assert (node1.next() is node2) and (node1._next is node2)
                # assert the node _next and next() are None in node2
                assert (node2.next() is None) and (node2._next is None)


class TestDoubleNode(unittest.TestCase):
    """*TestDoubleNode* es la clase *unittest* que prueba la clase *DoubleNode*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *DoubleNode* como un *fixture*.
        """
        self.global_params = get_node_test_data()

    def test_new_default_double_node(self):
        """*test_new_default_node()* prueba la creación de un nodo vacío de una lista doblemente encadenada *DoubleNode*.
        """
        # create an empty single linked list node
        node = DoubleNode()
        # assert for node information is None
        assert node.info is None
        # assert for node _next and next() are None
        assert (node.next() is None) and (node._next is None)
        # assert for node _prev and prev() are None
        assert (node.prev() is None) and (node._prev is None)

    def test_new_custom_double_node(self):
        """*test_new_custom_node()* prueba la creación de un nodo *DoubleNode* de una lista doblemente encadenada con datos personalizados.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a double linked list node with test_data
                node = DoubleNode(test_data)
                # assert for node info is the test_data
                assert node.info == test_data
                # assert for node info is the same type as test_data
                assert isinstance(node.info, dtype)
                # assert for node _next and next() are None
                assert (node.next() is None) and (node._next is None)
                # assert for node _prev and prev() are None
                assert (node.prev() is None) and (node._prev is None)

    def test_double_node_refs(self):
        """*test_double_node_refs()* prueba el manejo de referencias al siguiente y anterior nodo *DoubleNode* de la lista doblemente encadenada.
        """
        # getting the global variables
        # iterate over the global params and create a node for each type
        for key in self.global_params.keys():
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create 2 double linked list nodes
                node1 = DoubleNode(test_data)
                node2 = DoubleNode(test_data)
                # DEFAULT REFERENCES
                # assert the node _next and next() are None in both nodes
                assert (node1.next() is None) and (node1._next is None)
                assert (node2.next() is None) and (node2._next is None)
                # assert the node _prev and prev() are None in both nodes
                assert (node1.prev() is None) and (node1._prev is None)
                assert (node2.prev() is None) and (node2._prev is None)

                # CUSTOM REFERENCES
                # concatenate the nodes
                node1._next = node2
                node2._prev = node1
                # assert the node _next and next() are not None in node1
                assert (node1.next() is not None) and (node1._next is not None)
                # assert the node _prev and prev() are not None in node2
                assert (node2.prev() is not None) and (node2._prev is not None)
                # assert node1 next() and _next are node2
                assert (node1.next() is node2) and (node1._next is node2)
                # assert node2 prev() and _prev are node1
                assert (node2.prev() is node1) and (node2._prev is node1)
