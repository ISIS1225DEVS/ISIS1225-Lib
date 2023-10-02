# importing testing framework
import unittest
import pytest
# importing the file(s) to test
import config
from DISClib.DataStructures.listnode import SingleNode
from DISClib.DataStructures.listnode import DoubleNode
# asserting module imports
assert config
assert SingleNode
assert DoubleNode


@pytest.fixture(scope="module")
def global_params():
    """global_params _summary_

    Returns:
        _type_: _description_
    """
    # TODO add docstring
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


class test_single_node(unittest.TestCase):
    """test_single_node _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        """inject_fixtures _summary_

        Args:
            global_params (_type_): _description_
        """
        # TODO add docstring
        self.global_params = global_params

    def test_new_default_node(self):
        """test_new_default_node _summary_
        """
        # TODO add docstring
        # create an empty single linked list node
        node = SingleNode()
        # assert for node information is None
        c1 = (node.info is None)
        # assert for node _next and next() are None
        c2 = (node.next() is None) and (node._next is None)
        # assert both conditions are true
        assert all([c1, c2])

    def test_new_custom_node(self):
        """test_new_custom_node _summary_
        """
        # TODO add docstring
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
                c1 = node.info == test_data
                # assert for node info is the same type as test_data
                c2 = isinstance(node.info, dtype)
                # assert the node _next and next() are None
                c3 = (node.next() is None) and (node._next is None)
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_get_element(self):
        """test_get_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over the global params list and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a single linked list node with test_data
                node = SingleNode(test_data)
                # assert the node info is the test_data
                c1 = node.info == test_data
                # assert the data can be retrieved with the get_info()
                c2 = node.get_info() == test_data
                # assert get_info() returns the same type as test_data
                c3 = isinstance(node.get_info(), dtype)
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_set_element(self):
        """test_set_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over the global params list and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create an empty single linked list node
                node = SingleNode()
                # update the node info with test data using set_info()
                node.set_info(test_data)
                # assert the node info is test_data
                c1 = node.info == test_data
                # assert the info type is the same as test_data
                c2 = isinstance(node.info, dtype)
                c3 = isinstance(test_data, dtype)
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_node_next(self):
        """test_node_next _summary_
        """
        # getting the global variables
        # iterate over the global params list and create a node for each type
        for key in self.global_params.keys():
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create 2 single linked list node
                node1 = SingleNode(test_data)
                node2 = SingleNode(test_data)
                # assert the node _next and next() are None in both nodes
                c1 = (node1.next() is None) and (node1._next is None)
                c2 = (node2.next() is None) and (node2._next is None)
                assert all([c1, c2])
                # concatenate the nodes
                node1._next = node2
                # assert the node _next and next() are not None in node1
                c1 = (node1.next() is not None) and (node1._next is not None)
                # assert the node _next and next() are node2 in node1
                c2 = (node1.next() is node2) and (node1._next is node2)
                # assert the node _next and next() are None in node2
                c3 = (node2.next() is None) and (node2._next is None)
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_node_typerr(self):
        """test_node_typerr _summary_
        """
        # TODO add docstring
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
                    node = SingleNode(test_data)
                    # induce the error by changing the node info type
                    node.set_info(err)
                # assert the type error is raised
                c1 = "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                c2 = isinstance(test_data, dtype)
                # assert the node info is not the same type as err
                c3 = dtype != err
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_node_handle_error(self):
        """test_node_handle_error _summary_
        """
        # TODO add docstring
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
        #         c1 = "Invalid data type" in str(excinfo.value)
        #         c2 = isinstance(test_data, dtype)
        #         c3 = dtype != err
        #         assert all([c1, c2, c3])
        pass


class test_double_node(unittest.TestCase):
    """test_double_node _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        """inject_fixtures _summary_

        Args:
            global_params (_type_): _description_
        """
        # TODO add docstring
        self.global_params = global_params

    def test_new_default_node(self):
        """test_new_default_node _summary_
        """
        # TODO add docstring
        # create an empty single linked list node
        node = DoubleNode()
        # assert for node information is None
        c1 = node.info is None
        # assert for node _next and next() are None
        c2 = (node.next() is None) and (node._next is None)
        # assert for node _prev and prev() are None
        c3 = (node.prev() is None) and (node._prev is None)
        # assert all 3 conditions are true
        assert all([c1, c2, c3])

    def test_new_custom_node(self):
        """test_new_custom_node _summary_
        """
        # TODO add docstring
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
                c1 = node.info == test_data
                # assert for node info is the same type as test_data
                c2 = isinstance(node.info, dtype)
                # assert for node _next and next() are None
                c3 = (node.next() is None) and (node._next is None)
                # assert for node _prev and prev() are None
                c4 = (node.prev() is None) and (node._prev is None)
                # assert all 4 conditions are true
                assert all([c1, c2, c3, c4])

    def test_get_element(self):
        """test_get_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over the global params and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a double linked list node with test_data
                node = DoubleNode(test_data)
                # assert the node info is the test_data
                c1 = node.info == test_data
                # assert the data can be retrieved with the get_info()
                c2 = node.get_info() == test_data
                # assert get_info() returns the same type as test_data
                c3 = isinstance(node.get_info(), dtype)
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_set_element(self):
        """test_set_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over the global params and create a node for each type
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create an empty double linked list node
                node = DoubleNode()
                # update the node info with test data using set_info()
                node.set_info(test_data)
                # assert the node info is test_data
                c1 = node.info == test_data
                # assert the info type is the same as test_data
                c2 = isinstance(node.info, dtype)
                # assert the original test_data type as the same
                c3 = isinstance(test_data, dtype)
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_node_refs(self):
        """test_node_ref _summary_
        """
        # TODO add docstring
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
                c1 = (node1.next() is None) and (node1._next is None)
                c2 = (node2.next() is None) and (node2._next is None)
                # assert the node _prev and prev() are None in both nodes
                c3 = (node1.prev() is None) and (node1._prev is None)
                c4 = (node2.prev() is None) and (node2._prev is None)
                # assert all 4 conditions are true
                assert all([c1, c2, c3, c4])
                # CUSTOM REFERENCES
                # concatenate the nodes
                node1._next = node2
                node2._prev = node1
                # assert the node _next and next() are not None in node1
                c1 = (node1.next() is not None) and (node1._next is not None)
                # assert the node _prev and prev() are not None in node2
                c2 = (node2.prev() is not None) and (node2._prev is not None)
                # assert node1 next() and _next are node2
                c3 = (node1.next() is node2) and (node1._next is node2)
                # assert node2 prev() and _prev are node1
                c4 = (node2.prev() is node1) and (node2._prev is node1)
                # assert all 4 conditions are true
                assert all([c1, c2, c3, c4])

    def test_node_typerr(self):
        """test_node_typerr _summary_
        """
        # TODO add docstring
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
                # create a double linked list node with test_data
                with pytest.raises(TypeError) as excinfo:
                    node = DoubleNode(test_data)
                    # induce the error by changing the node info type
                    node.set_info(err)
                # assert the type error is raised
                c1 = "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                c2 = isinstance(test_data, dtype)
                # assert the node info is not the same type as err
                c3 = dtype != err
                # assert all 3 conditions are true
                assert all([c1, c2, c3])

    def test_node_handle_error(self):
        """test_node_handle_error _summary_
        """
        # TODO add docstring
        # TODO complete test
        pass
    