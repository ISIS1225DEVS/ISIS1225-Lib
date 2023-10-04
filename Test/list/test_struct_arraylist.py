# impoting testing framework
import unittest
import pytest
import random
# importing the class to be tested
# import config
from DISClib.DataStructures.arraylist import ArrayList
# asserting module existence
# assert config
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
            {"a": 1, "uuid": "a1", "b": 1.1, "id": 1},
            {"a": 2, "uuid": "a2", "b": 2.2, "id": 2},
            {"a": 3, "uuid": "a3", "b": 3.3, "id": 3},
            {"a": 4, "uuid": "a4", "b": 4.4, "id": 4},
            {"a": 5, "uuid": "a5", "b": 5.5, "id": 5},
            {"a": 6, "uuid": "a6", "b": 6.6, "id": 6},
            {"a": 7, "uuid": "a7", "b": 7.7, "id": 7},
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
        """Tests the initialization of an empty ArrayList.
        """
        # Test an empty ArrayList
        empty_list = ArrayList()
        # Test if ArrayList is not None
        assert empty_list is not None
        # Test if ArrayList is empty
        assert empty_list._size == 0
        # Test if ArrayList elements is empty
        assert empty_list.elements == []
        # Test if ArrayList key is "id"
        assert empty_list.key == "id"
        # Test if ArrayList cmp_function is default_cmp_function
        assert empty_list.cmp_function == empty_list.default_cmp_function
        # Test if ArrayList is an instance of ArrayList
        assert isinstance(empty_list, ArrayList)

    def test_default_cmp_function(self):
        """test_default_cmp_function test the default_cmp_function of the
            arraylist with different types of elements.
        """
        # create a new empty arraylist with the default cmp function
        ar_lt = ArrayList()
        # iterate over tglobal params and use the default cmp function
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # iterate over the test data
                for i in range(len(test_data)):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i-1]
                        ne = test_data[i+1]
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = ar_lt.default_cmp_function(ce, pe) in exp_res
                        res2 = ar_lt.default_cmp_function(ce, ce) in exp_res
                        res3 = ar_lt.default_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_new_custom_arraylist(self):
        """test_new_custom_arraylist test the initialization of a custom
            array list with elements of different types.
        """
        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                ar_lt = ArrayList(test_data)
                # test for the arraylist is not None
                assert ar_lt is not None
                # test for the arraylist size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the arraylist elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the arraylist key is "id"
                assert ar_lt.key == "id"
                # test for the arraylist cmp_function is default_cmp_function
                assert ar_lt.cmp_function == ar_lt.default_cmp_function
                # test for the arraylist is an instance of ArrayList
                assert isinstance(ar_lt, ArrayList)
                # test for the arraylist elements are of the same type
                assert isinstance(ar_lt.elements[0], data_type)

    def test_custom_key(self):
        """test_custom_key test the initialization of a custom arraylist
            with elements and a custom key.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                test_data = self.global_params.get(key)
                ar_lt = ArrayList(elements=test_data,
                                  key="uuid")
                # test for the arraylist is not None
                assert ar_lt is not None
                # test for the arraylist size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the arraylist elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the arraylist key is "uuid"
                assert ar_lt.key == "uuid"
                # test for the arraylist cmp_function is default_cmp_function
                assert ar_lt.cmp_function == ar_lt.default_cmp_function
                # test for the arraylist is an instance of ArrayList
                assert isinstance(ar_lt, ArrayList)
                # test for the arraylist elements are of the same type
                assert isinstance(ar_lt.elements[0], dtype)

    def test_custom_cmp_function(self):
        """test_custom_cmp_function test the initialization of a custom
            arraylist with elements and a custom cmp_function.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                test_data = self.global_params.get(key)
                ar_lt = ArrayList(elements=test_data,
                                  cmp_function=cmp_test_function)
                # test for the arraylist is not None
                assert ar_lt is not None
                # test for the arraylist size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the arraylist elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the arraylist key is the default "id"
                assert ar_lt.key == "id"
                # test for the arraylist cmp_function is the custom function
                assert ar_lt.cmp_function == cmp_test_function
                # test for the arraylist is an instance of ArrayList
                assert isinstance(ar_lt, ArrayList)
                # test for the arraylist elements are of the same type
                assert isinstance(ar_lt.elements[0], dtype)

    def test_size(self):
        """test_get_size test the size method of the arraylist. with empty
            and non-empty arraylists.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # test for the arraylist size is 0 with size method
        assert ar_lt.size() == 0
        # test for the arraylist size is 0 with _size attribute
        assert ar_lt._size == 0
        # check if the arraylist elements is empty
        assert ar_lt.elements == []

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # getting the test data
            test_data = self.global_params.get(key)
            # create a new arraylist with the test data
            ar_lt = ArrayList(elements=test_data)
            # test for the arraylist size() is equal to test_data
            assert ar_lt.size() == len(test_data)
            # test for the arraylist _size is equal to test_data
            assert ar_lt._size == len(test_data)
            # test for the arraylist elements is equal to test_data
            assert ar_lt.elements == test_data

    def test_is_empty(self):
        """test_is_empty test the is_empty method of the arraylist with empty
            and non-empty arraylists.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # test for the arraylist is empty
        assert ar_lt.is_empty() is True
        # test for the arraylist elements is empty
        assert ar_lt.elements == []

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # get the test data
            test_data = self.global_params.get(key)
            # create a new arraylist with the test data
            ar_lt = ArrayList(elements=test_data)
            # test for the arraylist is not empty
            assert ar_lt.is_empty() is False
            # test for the arraylist elements is equal to test_data
            assert ar_lt.elements == test_data

    def test_add_first(self):
        """test_add_first test the add_first method of the arraylist with empty
            arraylists with different types of elements.
        """
        # testing type handling
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                with pytest.raises(TypeError) as excinfo:
                    ar_lt = ArrayList(test_data)
                    # induce the error by adding an element of a different type
                    ar_lt.add_first(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_first method normal behavior
                ar_lt = ArrayList()
                # iterate over the test data
                for i in range(len(test_data)):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the arraylist
                    ar_lt.add_first(t_data)
                    # get the first element of the arraylist
                    t_elem = ar_lt.get_first()
                    # test for the arraylist get_first() is equal to test_data
                    assert t_elem == t_data
                    # test if the arraylist size is equal to test_len
                    assert (ar_lt.size() == i+1)

    def test_add_last(self):
        """test_add_last test the add_last method of the arraylist with empty
            arraylists with different types of elements. Checks for TypeError
            exceptions.
        """
        # testing type handling
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                with pytest.raises(TypeError) as excinfo:
                    ar_lt = ArrayList(test_data)
                    # induce the error by adding an element of a different type
                    ar_lt.add_last(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_lat method normal behavior
                ar_lt = ArrayList()
                # iterate over the test data
                for i in range(len(test_data)):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the arraylist
                    ar_lt.add_last(t_data)
                    # get the first element of the arraylist
                    t_elem = ar_lt.get_last()
                    # test for the arraylist get_last() is equal to test_data
                    assert t_elem == t_data
                    # test if the arraylist size is equal to test_len
                    assert (ar_lt.size() == i+1)

    def test_add_element(self):
        """test_add_element test the add_element method of the arraylist with
            empty and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.add_element(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # select a random valid index in the test data
                i = random.randint(0, test_len-1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the add_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len*2, test_len*3)
                    ar_lt.add_element(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len-1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the arraylist
                ar_lt.add_element(t_data, i)
                # get the added element in the index of the arraylist
                t_elem = ar_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the arraylist size is equal to test_len
                assert (ar_lt.size() == (test_len + 1))

    def test_get_first(self):
        """test_get_first test the get_first method of the arraylist with empty
            and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            # if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
            # get the test data
            test_data = self.global_params.get(key)
            # get the length of the test data
            test_len = len(test_data)
            # create a new arraylist with the test data
            ar_lt = ArrayList(elements=test_data)
            # test for the arraylist get_first() is equal to test_data
            assert ar_lt.get_first() == test_data[0]
            # test if arraylist size() is equal to test_len
            assert (ar_lt.size() == test_len)

    def test_get_last(self):
        """test_get_last test the get_last method of the arraylist with empty
            and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_last method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # test for the arraylist get_last() is equal to test_data
                assert ar_lt.get_last() == test_data[-1]
                # test if arraylist size() is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_get_element(self):
        """test_get_element test the get_element method of the arraylist with
        empty and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.get_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)

                # test get_element with an out-of-range index
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len, test_len*2)
                    ar_lt.get_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # iterate over the test data
                for i in range(len(test_data)):
                    # test for get_element(i) is equal to test_data[i]
                    assert ar_lt.get_element(i) == test_data[i]
                    # test if arraylist size() is equal to test_len
                    assert (ar_lt.size() == test_len)

    def test_remove_first(self):
        """test_remove_first test the remove_first method of the arraylist with
        empty and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.remove_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                for i in range(len(test_data)):
                    t_data = test_data[i]
                    t_elem = ar_lt.remove_first()
                    # test if the removed element is equal to the first
                    assert t_elem == t_data
                    # test if the arraylist size is equal to test_len
                    assert (ar_lt.size() == (test_len - i - 1))

    def test_remove_last(self):
        """test_remove_last test the remove_last method of the arraylist with
        empty and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.remove_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # iterate over the test data
                for i in range(len(test_data)):
                    # get the last element of the test data
                    t_data = test_data[test_len-i-1]
                    # remove the last element of the arraylist
                    t_elem = ar_lt.remove_last()
                    # test if the removed element is equal to the last
                    assert t_elem == t_data
                    # test if the arraylist size is equal to test_len
                    assert (ar_lt.size() == (test_len - i - 1))

    def test_remove_element(self):
        """test_remove_element test the remove_element method of the arraylist
        with empty and non-empty arraylists. Checks for IndexError exceptions.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.remove_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)

                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len*-1, -1)
                    ar_lt.remove_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len-1)
                # get the element in the test data
                t_data = test_data[i]
                # remove the element in the index of the arraylist
                t_elem = ar_lt.remove_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the arraylist size is equal to test_len
                assert (ar_lt.size() == (test_len - 1))

    def test_compare_elements(self):
        """test_compare_elements test the compare_elements method of the
            arraylist with empty and non-empty arraylists. Checks for
            TypeError exceptions. It also checks if the compared elements are
            equal to the index of the arraylist.
        """
        ar_lt = ArrayList()
        # delete the default cmp function
        ar_lt.cmp_function = None
        # delete the default key
        ar_lt.key = None
        # force an exception in the compare_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            j = random.randint(0, 100)
            ar_lt.compare_elements(i, j)
        # test for the exception type
        assert excinfo.type == TypeError
        # test for the exception message
        assert "Undefined compare function" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(elements=test_data,
                                      cmp_function=cmp_test_function)
                # iterate over the test data
                for i in range(len(test_data)):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i-1]
                        ne = test_data[i+1]
                        # test the result with the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = ar_lt.compare_elements(ce, pe) in exp_res
                        res2 = ar_lt.compare_elements(ce, ce) in exp_res
                        res3 = ar_lt.compare_elements(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_is_present(self):
        """test_is_present _summary_
        """
        # TODO add docstring
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                test_len = len(test_data)
                ar_lt = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(elements=test_data,
                                      cmp_function=cmp_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len-1)
                t_data = test_data[i]
                # test if the element is present in the arraylist
                idx = ar_lt.is_present(t_data)
                # test if the index is valid
                assert -1 <= idx <= test_len-1

    def test_change_info(self):
        """test_change_element test the change_element method of the arraylist
            with empty and non-empty arraylists. Checks for IndexError
            exceptions. It also checks if the changed elements are equal to the
            index of the arraylist.
        """
        # TODO add docstring
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.change_info(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(elements=test_data,
                                      cmp_function=cmp_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len-1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the change_info method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len*2, test_len*3)
                    ar_lt.change_info(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len-1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the arraylist
                ar_lt.change_info(t_data, i)
                # get the added element in the index of the arraylist
                t_elem = ar_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the arraylist size is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_exchange(self):
        """test_exchange test the exchange method of the arraylist with empty
            and non-empty arraylists. Checks for IndexError exceptions. It also
            checks if the exchanged elements are equal to the index of the
            arraylist.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the exchange method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            ar_lt.exchange(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(elements=test_data,
                                      cmp_function=cmp_test_function)

                # force an exception in the exchange method
                with pytest.raises(Exception) as excinfo:
                    i, j = random.sample(range(test_len*2, test_len*3), 2)
                    ar_lt.exchange(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i, j = random.sample(range(0, test_len-1), 2)
                # get the elements in the test data
                test_elm1 = test_data[i]
                test_elm2 = test_data[j]

                # exchange the elements in the index of the arraylist
                ar_lt.exchange(i, j)
                # get the exchanged elements in the index of the arraylist
                exch_elm1 = ar_lt.get_element(i)
                exch_elm2 = ar_lt.get_element(j)

                # test if the removed element is equal to the index
                assert exch_elm1 == test_elm2
                assert exch_elm2 == test_elm1
                # test if the arraylist size is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_sublist(self):
        """test_create_sublist test the sublist method of the arraylist with
            empty and non-empty arraylists. Checks for IndexError exceptions.
            It also checks if the sublist is an arraylist and if the elements
            are equal to the sublist of the test data.
        """
        # create a new empty arraylist
        ar_lt = ArrayList()
        # force an exception in the sublist method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            ar_lt.sublist(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new arraylist with the test data
                ar_lt = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(elements=test_data,
                                      cmp_function=cmp_test_function)

                # force an exception in the sublist method
                with pytest.raises(Exception) as excinfo:
                    i, j = random.sample(range(test_len*2, test_len*3), 2)
                    ar_lt.sublist(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "Invalid range: between" in str(excinfo.value)

                # select a random valid a low index in the test data
                low = random.randint(0, test_len-1)
                # select a random valid a high index in the test data
                high = random.randint(low, test_len-1)
                # get the elements in the test data
                sub_lt = list(test_data[low:high])
                # get the elements size in the test data
                sub_lt_size = len(sub_lt)
                # create a sublist with the low and high index
                sub_ar_lt = ar_lt.sublist(low, high)
                # test for the sublist size is an arraylist
                assert isinstance(sub_ar_lt, ArrayList)
                # test for the sublist size is equal to test_len
                assert sub_lt_size == sub_ar_lt.size()
                # test for the sublist elements are equal to sub_lt
                assert sub_lt == sub_ar_lt.elements

    def test_concat(self):
        """test_concat test the concat method of the arraylist with two
            filled arraylists. Checks for TypeError exceptions, it can only
            concatenate with another arraylist, with the same key and cmp
            function.
        """
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                ar_lt1 = ArrayList(elements=test_data)
                # create a python list with the test data
                ar_lt2 = test_data.copy()

                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                err_msg = "Structure is not an ArrayList:"
                assert err_msg in str(excinfo.value)

                # create a new arraylist with the wrong key
                ar_lt2 = ArrayList(elements=test_data,
                                   key="testid")
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid key:" in str(excinfo.value)

                # create a new arraylist with the wrong cmp function
                ar_lt2 = ArrayList(elements=test_data,
                                   cmp_function=cmp_test_function)
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid cmp_function:" in str(excinfo.value)

                # create a new correct arraylist with the test data
                ar_lt1 = ArrayList(elements=test_data)
                ar_lt2 = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt1 = ArrayList(elements=test_data,
                                       cmp_function=cmp_test_function)
                    ar_lt2 = ArrayList(elements=test_data,
                                       cmp_function=cmp_test_function)
                # create the new concatenated arraylist
                ans = ar_lt1.concat(ar_lt2)
                assert isinstance(ans, ArrayList)
                assert ans.size() == ar_lt1.size() + ar_lt2.size()
                assert ans.elements == ar_lt1.elements + ar_lt2.elements
                assert ans.key == ar_lt1.key and ans.key == ar_lt2.key
                assert ans.cmp_function == ar_lt1.cmp_function
                assert ans.cmp_function == ar_lt1.cmp_function

    def test_iterator(self):
        """test_iterator test the iterator method of the arraylist with a
            filled arraylist. Checks for StopIteration exceptions.
        """
        # iterates over global params and create filled arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT", "TEST_AL_LT"):
                # get the test data
                test_data = self.global_params.get(key)
                # create a new arraylist with the test data
                test_len = len(test_data)
                ar_lt = ArrayList(elements=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(elements=test_data,
                                      cmp_function=cmp_test_function)
                # iterates over the arraylist and the test data and compare
                for element, data in zip(ar_lt, test_data):
                    # test for the element is equal to test_data
                    assert element == data
                    # test for the element type is equal to test_data
                    assert type(element) is type(data)
                # test for the iterator is exhausted and the StopIteration
                assert ar_lt.size() == test_len
