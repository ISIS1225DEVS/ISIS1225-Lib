# importing testing framework
import unittest
import pytest
# importing the file(s) to test
import config
from DISClib.DataStructures.listnode import single_node
from DISClib.DataStructures.listnode import double_node
# asserting module imports
assert config
assert single_node
assert double_node


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
            str,
            int,
            float,
            bool,
            dict,
            list,
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
        node = single_node()
        # assert that the node data is None
        assert node.info is None
        # assert that the node _next() is None or a single_node
        assert (node.next() is None) and (node._next is None)

    def test_new_custom_node(self):
        """test_new_node _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create an empty single linked list node
        node = single_node()
        # assert that the node data is None
        assert node.info is None
        # create a single linked list node
        node = single_node(test_str)
        # assert that the node data is not None
        assert node.info == test_str
        # assert that the node _next() is None or a single_node
        assert (node.next() is None) and (node._next is None)



    def test_get_element(self):
        """test_get_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create a single linked list node
        node = single_node(test_str)
        # get the node data with module function
        data = node.get_info()
        # assert that the node data is not None
        assert data == test_str
        # assert that the data can be retrieved with the class function
        assert node.get_info() == test_str

    def test_set_element(self):
        """test_set_element _summary_
        """
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create a single linked list node
        node = single_node()
        # set the node data with module function
        node.set_info(test_str)
        # assert that the node data is not None
        assert node.info == test_str
        # reset test string
        node.info = ""
        #  set node wit the class function
        node.set_info(test_str)
        # assert that the data can be retrieved with the get_info function
        assert node.get_info() == test_str

    def test_next(self):
        """test_next _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create a single linked list node
        node = single_node(test_str)
        # assert that the node _next() is None or a single_node
        assert (node.next() is None) and (node._next is None)

    def test_node_type(self):
        """test_node_type _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        test_int = self.global_params.get("TEST_INT")
        test_float = self.global_params.get("TEST_FLOAT")
        test_bool = self.global_params.get("TEST_BOOL")
        test_dict = self.global_params.get("TEST_DICT")
        test_lt = self.global_params.get("TEST_LT")

        # create an empty single_node
        node = single_node()
        # assert that the node is a single_node
        assert isinstance(node, single_node)
        # assert the node _next() reference is None
        assert (node.next() is None) and (node._next is None)

        # TESTING WITH STRING
        # create a single_node with string info
        node = single_node(test_str)
        # assert that the node info is a string
        assert isinstance(node.info, str)

        # TESTING WITH INT
        # create a single linked list node
        node = single_node(test_int)
        # assert that the node info is an int
        assert isinstance(node.info, int)

        # TESTING WITH FLOAT
        # create a single_node with float info
        node = single_node(test_float)
        # assert that the node info is a float
        assert isinstance(node.info, float)

        # TESTING WOTH BOOL
        # create a single_node with bool info
        node = single_node(test_bool)
        # assert that the node info is a bool
        assert isinstance(node.info, bool)

        # TESTING WITH LIST
        # create a single_node with list info
        node = single_node(test_lt)
        # assert that the node info is a dict
        assert isinstance(node.info, list)

        # TESTING WITH DICT
        # create a single_node with dict info
        node = single_node(test_dict)
        # assert that the node info is a dict
        assert isinstance(node.info, dict)

        # assert that the node info keys are the same as the dict keys
        for key in test_dict.keys():
            assert key in node.info.keys()
            assert isinstance(node.info[key], type(test_dict[key]))
        # assert the node _next() reference is None
        assert (node.next() is None) and (node._next is None)

    def test_node_ref(self):
        """test_node_ref _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create two different single linked list nodes
        node_a = single_node(test_str)
        node_b = single_node("Hello Next Node!")
        # assigning node_a _next() reference to node_b
        node_a._next = node_b
        # assert that node_a _next() reference is node_b
        assert node_a.next() == node_b
        # assert that node_b reference to next is none
        sll_instance = isinstance(node_b.next(), single_node)
        assert node_b.next() is None and not sll_instance

    def test_node_typerr(self):
        """test_node_typerr _summary_
        """
        # TODO add docstring
        # getting the global variables
        # type error test data list
        with pytest.raises(TypeError) as excinfo:
        
        
        
        
        type_err_lt = [
            self.global_params.get("TEST_STR"),
            self.global_params.get("TEST_INT"),
            self.global_params.get("TEST_FLOAT"),
            self.global_params.get("TEST_BOOL"),
            self.global_params.get("TEST_DICT"),
            self.global_params.get("TEST_LT"),
            ]
        # list to check the type error
        check_err_lt = self.global_params.get("CHECK_ERR_LT")

        # iterate over the type error list
        for dtype, check in zip(type_err_lt, check_err_lt):
            # create a single linked list node with type error data
            node = single_node(dtype)
            try:
                # try to change the node info to a different type
                node.info = check
            except Exception as exc:
                # assert if the type error is raised
                assert isinstance(exc, TypeError)
                assert exc.args[0] == "Invalid data type for node info"


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

    def test_new_node(self):
        """test_new_node _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create a double linked list node
        node = double_node()
        # assert that the node data is not None
        assert node.info is None
        # create a double linked list node
        node = double_node(test_str)
        # assert that the node data is not None
        assert node.info == test_str
        # assert that the node _next() is None or a double_node
        assert (node.next() is None) and (node._next is None)
        # assert that the node _prev() is None or a double_node
        assert (node.prev() is None) and (node._prev is None)

    def test_get_element(self):
        """test_get_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create a double linked list node
        node = double_node(test_str)
        # get the node data with class function
        data = node.get_info()
        # assert that the node data is not None
        assert data == test_str
        # assert that the data can be retrieved with the get_info function
        assert node.get_info() == test_str

    def test_set_element(self):
        """test_set_element _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create a double linked list node
        node = double_node()
        # set the node data with module function
        node.set_info(test_str)
        # assert that the node data is not None
        assert node.info == test_str
        # reset test string
        node.info = ""
        #  set node wit the class function
        node.set_info(test_str)
        # assert that the data can be retrieved with the get_info function
        assert node.get_info() == test_str

    def test_node_type(self):
        """test_node_type _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        test_int = self.global_params.get("TEST_INT")
        test_float = self.global_params.get("TEST_FLOAT")
        test_bool = self.global_params.get("TEST_BOOL")
        test_lt = self.global_params.get("TEST_LT")
        test_dict = self.global_params.get("TEST_DICT")

        # TESTING WITH STRING
        # create a double_node with string info
        node = double_node(test_str)
        # assert that the node info is a string
        assert isinstance(node.info, str)
        # assert the node _next() reference is None
        assert (node.next() is None) or (node.next() is None)
        assert (node.prev() is None) or (node.prev() is None)

        # TESTING WITH INT
        # create a single linked list node
        node = double_node(test_int)
        # assert that the node is a double_node
        assert isinstance(node, double_node)
        # assert that the node info is an int
        assert isinstance(node.info, int)

        # TESTING WITH FLOAT
        # create a double_node with float info
        node = double_node(test_float)
        # assert that the node info is a float
        assert isinstance(node.info, float)

        # TESTING WOTH BOOL
        # create a double_node with bool info
        node = double_node(test_bool)
        # assert that the node info is a bool
        assert isinstance(node.info, bool)

        # TESTING WITH LIST
        # create a double_node with list info
        node = double_node(test_lt)
        # assert that the node info is a list
        assert isinstance(node.info, list)
        # assert that the node info keys are the same as the list keys
        for i in range(len(test_lt)):
            assert node.info[i] == test_lt[i]

        # TESTING WITH DICT
        # create a double_node with dict info
        node = double_node(test_dict)
        # assert that the node is a double_node
        assert isinstance(node, double_node)
        # assert that the node info is a dict
        assert isinstance(node.info, dict)
        # assert that the node info keys are the same as the dict keys
        for key in test_dict.keys():
            assert key in node.info.keys()
            assert isinstance(node.info[key], type(test_dict[key]))
        # assert the node _next() reference is None
        assert (node.next() is None) or (node.next() is None)
        assert (node.prev() is None) or (node.prev() is None)

    def test_node_ref(self):
        """test_node_ref _summary_
        """
        # TODO add docstring
        # getting the global variables
        test_str = self.global_params.get("TEST_STR")
        # create three different double linked list nodes
        node_a = double_node(test_str)
        node_b = double_node("Hello Next Node!")
        node_c = double_node("Hello Prev Node!")

        # assigning node_a _next reference to node_b
        node_a._next = node_b
        # assigning node_b _prev reference to node_c
        node_a._prev = node_c
        # assert that node_a _next() reference is node_b
        assert node_a.next() == node_b
        # assert that node_b _prev() reference is node_c
        assert node_a.prev() == node_c
        # assert that node_b _next() reference is None or a double_node
        assert node_a.next() is not None or node_a.next() == node_b
        # assert that node_c _prev() reference is None or a double_node
        assert node_a.prev() is not None or node_a.prev() == node_c

    def test_node_typerr(self):
        """test_node_typerr _summary_
        """
        # TODO add docstring
        # getting the global variables
        # type error test data list
        type_err_lt = [
            self.global_params.get("TEST_STR"),
            self.global_params.get("TEST_INT"),
            self.global_params.get("TEST_FLOAT"),
            self.global_params.get("TEST_BOOL"),
            self.global_params.get("TEST_DICT"),
            self.global_params.get("TEST_LT"),
            ]
        # list to check the type error
        check_err_lt = self.global_params.get("CHECK_ERR_LT")

        # iterate over the type error list
        for dtype, check in zip(type_err_lt, check_err_lt):
            # create a single linked list node with type error data
            node = double_node(dtype)
            try:
                # try to change the node info to a different type
                node.info = check
            except Exception as exc:
                # assert if the type error is raised
                assert isinstance(exc, TypeError)
                assert exc.args[0] == "Invalid data type for node info"


# if __name__ == "__main__":
#     pytest.main(["-v", "-s", "test_struct_listnode.py"])
