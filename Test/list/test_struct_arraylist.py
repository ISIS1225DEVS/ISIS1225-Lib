# impoting testing framework
import unittest
import pytest
import random
# importing the class to be tested
import config
from DISClib.DataStructures.arraylist import ArrayList
# as al
# asserting module existence
assert config
# assert al
assert ArrayList


@pytest.fixture(scope="module")
def global_params():
    """global_params the function returns a dictionary with the global
        parameters for testing.

    Returns:
        dict: dictionary with the global parameters for testing.
    """
    parameters = dict(
        TEST_STR_LT=[
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
        ],
        TEST_INT_LT=[
            1,
            2,
            3,
            4,
            5,
            6,
            7,
        ],
        TEST_FLOAT_LT=[
            1.1,
            2.2,
            3.3,
            4.4,
            5.5,
            6.6,
            7.7,
        ],
        TEST_BOOL_LT=[
            True,
            False,
            True,
            False,
            True,
            False,
            True,
        ],
        TEST_DICT_LT=[
            {"a": 1, "id": 1},
            {"a": 2, "id": 2},
            {"a": 3, "id": 3},
            {"a": 4, "id": 4},
            {"a": 5, "id": 5},
            {"a": 6, "id": 6},
            {"a": 7, "id": 7},
        ],
        TEST_CUSTOM_DICT_LT=[
            {"a": 1, "uuid": "a1", "b": 1.1},
            {"a": 2, "uuid": "a2", "b": 2.2},
            {"a": 3, "uuid": "a3", "b": 3.3},
            {"a": 4, "uuid": "a4", "b": 4.4},
            {"a": 5, "uuid": "a5", "b": 5.5},
            {"a": 6, "uuid": "a6", "b": 6.6},
            {"a": 7, "uuid": "a7", "b": 7.7},
        ],
        TEST_LIST_LT=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
            [16, 17, 18],
            [19, 20, 21],
        ],
        TEST_TUPLE_LT=[
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15),
            (16, 17, 18),
            (19, 20, 21),
        ],
        TEST_SET_LT=[
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12},
            {13, 14, 15},
            {16, 17, 18},
            {19, 20, 21},
        ],
        CHECK_TYPE_LT=[
            str,
            int,
            float,
            bool,
            dict,
            dict,
            list,
            tuple,
            set,
        ],
        CHECK_ERR_LT=[
            set,
            tuple,
            list,
            dict,
            bool,
            float,
            int,
            str,
            dict,
        ],
    )
    # FIXME do we need this? it is okey?
    TEST_ARRAY_LIST_LT = list()
    for i in parameters.get("TEST_INT_LT"):
        temp_lt = parameters.get("TEST_DICT_LT")
        tal = ArrayList(temp_lt)
        TEST_ARRAY_LIST_LT.append(tal)
    parameters["TEST_AL_LT"] = TEST_ARRAY_LIST_LT
    return parameters


# @pytest.fixture(scope="module")
def cmp_test_function(elm1: dict, elm2: dict) -> int:
    """cmp_test_function test function for comparing elements.
    only works for dictionaries with a key "uuid".

    Args:
        elm1 (dict): first element to compare.
        elm2 (dict): second element to compare.

    Raises:
        Exception: error if the key is not present in both elements.
        Exception: error if the comparison is invalid.

    Returns:
        int: 1 if the first element is greater than the second, -1 if the
            first element is less than the second, 0 if they are equal.
    """
    key = "uuid"
    key1 = elm1.get(key)
    key2 = elm2.get(key)
    # check if the key is present in both elements
    if None in [key1, key2]:
        raise Exception("Invalid key")
    # comparing elements
    else:
        # if one is greater than the other, return 1
        if key1 > key2:
            return 1
        # if one is less than the other, return -1
        elif key1 < key2:
            return -1
        # if they are equal, return 0
        elif key1 == key2:
            return 0
        # otherwise, raise an exception
        else:
            raise Exception("Invalid comparison")


class TestArrayList(unittest.TestCase):
    """TestArrayList test class testing for the ArrayList class.

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

    def test_new_default_arraylist(self):
        """test_init test the initialization of an empty array list.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # assert for the arraylist is not None
        c1 = ar_lt is not None
        # assert for the arraylist is empty
        c2 = ar_lt._size == 0
        # assert if the arraylist elements is empty
        c3 = ar_lt.elements == []
        # assert if the arraylist key is "id"
        c4 = ar_lt.key == "id"
        # assert if the arraylist cmp_function is default_cmp_function
        c5 = ar_lt.cmp_function == ar_lt.default_cmp_function
        # assert if the arraylist is an instance of ArrayList
        c6 = isinstance(ar_lt, ArrayList)
        # assert all 6 conditions are true
        assert all([c1, c2, c3, c4, c5, c6])

    def test_new_custom_arraylist(self):
        """test_new_custom_arraylist test the initialization of a custom
            array list with elements of different types.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                ar_lt = ArrayList(test_data)
                # assert for the arraylist is not None
                c1 = ar_lt is not None
                # assert for the arraylist size is equal to test_data
                c2 = ar_lt._size == len(test_data)
                # assert for the arraylist elements is equal to test_data
                c3 = ar_lt.elements == test_data
                # assert for the arraylist key is "id"
                c4 = ar_lt.key == "id"
                # assert for the arraylist cmp_function is default_cmp_function
                c5 = ar_lt.cmp_function == ar_lt.default_cmp_function
                # assert for the arraylist is an instance of ArrayList
                c6 = isinstance(ar_lt, ArrayList)
                # assert for the arraylist elements are of the same type
                c7 = isinstance(ar_lt.elements[0], dtype)
                # assert all 7 conditions are true
                assert all([c1, c2, c3, c4, c5, c6, c7])

    def test_custom_key(self):
        """test_custom_key test the initialization of a custom arraylist
            with elements and a custom key.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                ar_lt = ArrayList(elements=test_data,
                                  key="uuid")
                # assert for the arraylist is not None
                c1 = ar_lt is not None
                # assert for the arraylist size is equal to test_data
                c2 = ar_lt._size == len(test_data)
                # assert for the arraylist elements is equal to test_data
                c3 = ar_lt.elements == test_data
                # assert for the arraylist key is "uuid"
                c4 = ar_lt.key == "uuid"
                # assert for the arraylist cmp_function is default_cmp_function
                c5 = ar_lt.cmp_function == ar_lt.default_cmp_function
                # assert for the arraylist is an instance of ArrayList
                c6 = isinstance(ar_lt, ArrayList)
                # assert for the arraylist elements are of the same type
                c7 = isinstance(ar_lt.elements[0], dtype)
                # assert all 7 conditions are true
                assert all([c1, c2, c3, c4, c5, c6, c7])

    def test_custom_cmp_function(self):
        """test_custom_cmp_function test the initialization of a custom
            arraylist with elements and a custom cmp_function.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                ar_lt = ArrayList(elements=test_data,
                                  cmp_function=cmp_test_function)
                # assert for the arraylist is not None
                c1 = ar_lt is not None
                # assert for the arraylist size is equal to test_data
                c2 = ar_lt._size == len(test_data)
                # assert for the arraylist elements is equal to test_data
                c3 = ar_lt.elements == test_data
                # assert for the arraylist key is the default "id"
                c4 = ar_lt.key == "id"
                # assert for the arraylist cmp_function is the custom function
                c5 = ar_lt.cmp_function == cmp_test_function
                # assert for the arraylist is an instance of ArrayList
                c6 = isinstance(ar_lt, ArrayList)
                # assert for the arraylist elements are of the same type
                c7 = isinstance(ar_lt.elements[0], dtype)
                # assert all 7 conditions are true
                assert all([c1, c2, c3, c4, c5, c6, c7])

    def test_size(self):
        """test_get_size test the size method of the arraylist. with empty
            and non-empty arraylists.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # assert for the arraylist size is 0 with size method
        c1 = ar_lt.size() == 0
        # assert for the arraylist size is 0 with _size attribute
        c2 = ar_lt._size == 0
        # check if the arraylist elements is empty
        c3 = ar_lt.elements == []
        # assert all 3 conditions are true
        assert all([c1, c2, c3])
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # getting the test data
            test_data = self.global_params.get(key)
            # create a new arraylist with the test data
            ar_lt = ArrayList(elements=test_data)
            # assert for the arraylist size() is equal to test_data
            c1 = ar_lt.size() == len(test_data)
            # assert for the arraylist _size is equal to test_data
            c2 = ar_lt._size == len(test_data)
            # assert for the arraylist elements is equal to test_data
            c3 = ar_lt.elements == test_data
            # assert all 3 conditions are true
            assert all([c1, c2, c3])

    def test_is_empty(self):
        """test_is_empty test the is_empty method of the arraylist with empty
            and non-empty arraylists.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # assert for the arraylist is empty
        c1 = ar_lt.is_empty() is True
        # assert for the arraylist elements is empty
        c2 = ar_lt.elements == []
        # assert all 2 conditions are true
        assert all([c1, c2])
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # get the test data
            test_data = self.global_params.get(key)
            # create a new arraylist with the test data
            ar_lt = ArrayList(elements=test_data)
            # assert for the arraylist is not empty
            c1 = ar_lt.is_empty() is False
            # assert for the arraylist elements is equal to test_data
            c2 = ar_lt.elements == test_data
            # assert all 2 conditions are true
            assert all([c1, c2])

    def test_get_first(self):
        """test_get_first test the get_first method of the arraylist with empty
            and non-empty arraylists.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_first()
        # assert for the exception type
        c1 = excinfo.type == Exception
        # assert for the exception message
        c2 = "Empty data structure" in str(excinfo.value)
        # assert all 2 conditions are true
        assert all([c1, c2])
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # assert for the arraylist get_first() is equal to test_data
                c1 = ar_lt.get_first() == test_data[0]
                # assert if arraylist size() is equal to test_len
                c2 = (ar_lt.size() == test_len)
                # assert all 2 conditions are true
                assert all([c1, c2])

    def test_get_last(self):
        """test_get_last test the get_last method of the arraylist with empty
            and non-empty arraylists.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_last method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_last()
        # assert for the exception type
        c1 = excinfo.type == Exception
        # assert for the exception message
        c2 = "Empty data structure" in str(excinfo.value)
        # assert all 2 conditions are true
        assert all([c1, c2])
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # assert for the arraylist get_last() is equal to test_data
                c1 = ar_lt.get_last() == test_data[-1]
                # assert if arraylist size() is equal to test_len
                c2 = (ar_lt.size() == test_len)
                # assert all 2 conditions are true
                assert all([c1, c2])

    def test_get_element(self):
        """test_get_element _summary_
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.get_element(i)
        # assert for the exception type
        c1 = excinfo.type == Exception
        # assert for the exception message
        c2 = "Empty data structure" in str(excinfo.value)
        # assert all 2 conditions are true
        assert all([c1, c2])
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # iterate over the test data
                for i in range(len(test_data)):
                    # assert for get_element(i) is equal to test_data[i]
                    c1 = ar_lt.get_element(i) == test_data[i]
                    # assert if arraylist size() is equal to test_len
                    c2 = (ar_lt.size() == test_len)
                    # assert all 2 conditions are true
                    assert all([c1, c2])

    def test_remove_first(self):
        """test_remove_first _summary_
        """
        # TODO add docstring
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_len = len(test_data)
            test_al = ArrayList(elements=test_data)
            for i in range(len(test_data)):
                t_data = test_data[i]
                t_elm = test_al.remove_first()
                assert t_elm == t_data
                a = (test_al._size == (test_len - i - 1))
                b = (test_al.size() == (test_len - i - 1))
                assert all([a, b])
                # assert test_al._size == (test_len - i - 1)
                # assert test_al.size() == (test_len - i - 1)

    def test_remove_last(self):
        """test_remove_last _summary_
        """
        # TODO add docstring

    def test_remove_element(self):
        """test_remove_element _summary_
        """
        # TODO add docstring

    def test_add_first(self):
        """test_add_first _summary_
        """
        # TODO add docstring

    def test_add_last(self):
        """test_add_last _summary_
        """
        # TODO add docstring

    def test_add_element(self):
        """test_add_element _summary_
        """
        # TODO add docstring

    def test_compare_elements(self):
        """test_compare_elements _summary_
        """
        # TODO add docstring

    def test_is_present(self):
        """test_is_present _summary_
        """
        # TODO add docstring

    def test_change_info(self):
        """test_change_element _summary_
        """
        # TODO add docstring

    def test_exchange(self):
        """test_exchange _summary_
        """
        # TODO add docstring

    def test_create_sublist(self):
        """test_create_sublist _summary_
        """
        # TODO add docstring

    def test_concatenate(self):
        """test_concatenate _summary_
        """
        # TODO add docstring

    def test_iterator(self):
        """test_iterator _summary_
        """
        # TODO add docstring
