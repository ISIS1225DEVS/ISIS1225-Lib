# importing testing framework
import unittest
import pytest
# importing the file(s) to test
from DISClib.DataStructures.node import Node
from DISClib.DataStructures.listnode import SingleNode
from DISClib.DataStructures.listnode import DoubleNode
# asserting module imports
assert Node
assert SingleNode
assert DoubleNode


@pytest.fixture(scope="module")
def global_params():
    """global_params the function returns a dictionary with the global
        parameters for testing.

    Returns:
        dict: dictionary with the global parameters for testing.
    """
    parameters = dict(
        # global variables for testing
        TEST_STR="Hello Node!",
        TEST_INT=42,
        TEST_FLOAT=42.0,
        TEST_BOOL=True,
        TEST_DICT={
            "key1": "Hello Node!",
            "key2": 42,
            "key3": 42.0,
            "key4": [
                "value1",
                "value2",
                "value3",
                ],
            "key5": {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                },
            "key6": None,
            "key7": True,
            },
        TEST_LT=[
            "value1",
            "value2",
            "value3",
            42,
            42.7,
            "Hello Node!",
            None,
            True,
            ],
        CHECK_ERR_LT=[
            int(1234),
            list(),
            dict(id=1, name="John Doe"),
            float(42.87),
            bool(False),
            str("Hello Node!"),
        ],
        CHECK_TYPE_LT=[
            str,
            int,
            float,
            bool,
            dict,
            list
        ]
    )
    return parameters


class TestNode(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        """inject_fixtures it injects the global parameters as a fixture.

        Args:
            global_params (dict): global parameters for testing.
        """
        self.global_params = global_params

    def test_new_default_node(self):
        """test_new_default_node test the creation of an empty list node.
        """
        # create an empty single linked list node
        node = Node()
        # assert for node information is None
        assert node.info is None

    def test_new_custom_node(self):
        """test_new_custom_node test the creation of a list node with
            custom data.
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
        """test_get_info test the retrieval of the list node information.
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
        """test_set_info test the update of the list node information.
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
        """test_node_typerr test the type error handling for invalid data types
            in node info.
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
        """test_node_handle_error test the error handling ad raise in the
            single linked list node.
        """
        # TODO complete test
        # getting the global variables
        # type error test data list
        # type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # # data type list
        # dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # param_keys = self.global_params.keys()
        # # iterate over the type error list and create a node for each type
        # for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
        #     if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
        #         test_data = self.global_params.get(key)
        #         # create a single linked list node with test_data
        #         with pytest.raises(TypeError) as excinfo:
        #             node = SingleNode(test_data)
        #             node.set_info(err)
        #         assert "Invalid data type" in str(excinfo.value)
        #         assert isinstance(test_data, dtype)
        #         assert dtype != err
        #         assert all([c1, c2, c3])
        pass


class TestSingleNode(unittest.TestCase):
    """TestSingleNode test class for testing the SingleNode class.

    Args:
        unittest (class): python class for unit testing.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        """inject_fixtures it injects the global parameters as a fixture.

        Args:
            global_params (dict): global parameters for testing.
        """
        self.global_params = global_params

    def test_new_default_single_node(self):
        """test_new_default_node test the creation of an empty single linked
            list node.
        """
        # create an empty single linked list node
        node = SingleNode()
        # assert for node information is None
        assert (node.info is None)
        # assert for node _next and next() are None
        assert (node.next() is None) and (node._next is None)

    def test_new_custom_single_node(self):
        """test_new_custom_node test the creation of a single linked list node
            with custom data.
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
        """test_node_next thes the node _next attribute and next() method in
            the single linked list node.
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
    """TestDoubleNode test class for testing the DoubleNode class.

    Args:
        unittest (class): python class for unit testing.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        """inject_fixtures it injects the global parameters as a fixture.

        Args:
            global_params (dict): global parameters for testing.
        """
        self.global_params = global_params

    def test_new_default_double_node(self):
        """test_new_default_node test the creation of an empty double linked.
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
        """test_new_custom_node test the creation of a double linked list node
            with custom data.
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
        """test_node_ref test the node references in the double linked list
            node. This includes the _next, next(), _prev and prev() attributes
            and methods.
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
