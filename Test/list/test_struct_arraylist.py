# impoting testing framework
import unittest
import pytest
import random
# importing the class to be tested
import config
from DISClib.DataStructures.arraylist import array_list
# as al
# asserting module existence
assert config
# assert al
assert array_list


@pytest.fixture(scope="module")
def global_params():
    """global_params _summary_

    Returns:
        _type_: _description_
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
    )
    TEST_AL_LT = list()
    for i in parameters.get("TEST_INT_LT"):
        temp_lt = parameters.get("TEST_DICT_LT")
        tal = array_list(temp_lt)
        TEST_AL_LT.append(tal)
    parameters["TEST_AL_LT"] = TEST_AL_LT
    return parameters


# @pytest.fixture(scope="module")
def cmp_test_function(elm1, elm2):
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


class test_array_list(unittest.TestCase):
    """test_array_list _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        """inject_fixtures _summary_

        Args:
            global_param (_type_): _description_
        """
        # TODO add docstring
        self.global_params = global_params

    def test_empty_init(self):
        """test_init _summary_
        """
        # TODO add docstring
        test_al = array_list()
        assert test_al is not None
        assert test_al._size == 0
        assert test_al.elements == []

    def test_fill_init(self):
        """test_init _summary_
        """
        # TODO add docstring
        test_data = self.global_params.get("TEST_DICT_LT")
        test_al = array_list(test_data)
        assert test_al is not None
        assert test_al._size == len(test_data)
        assert test_al.elements == test_data

    def test_custom_key_init(self):
        """test_custom_init _summary_
        """
        # TODO add docstring
        test_data = self.global_params.get("TEST_CUSTOM_DICT_LT")
        test_al = array_list(elements=test_data,
                             key="uuid")
        assert test_al is not None
        assert test_al._size == len(test_data)
        assert test_al.elements == test_data
        assert test_al.key == "uuid"

    def test_custom_cmp_init(self):
        """test_custom_init _summary_
        """
        # TODO add docstring
        test_data = self.global_params.get("TEST_CUSTOM_DICT_LT")
        test_al = array_list(elements=test_data,
                             cmp_function=cmp_test_function)
        assert test_al is not None
        assert test_al._size == len(test_data)
        assert test_al.elements == test_data
        assert test_al.cmp_function == cmp_test_function

    def test_post_init(self):
        """test_post_init _summary_
        """
        # TODO add docstring
        # FIXME do we need this?

    def test_handle_error(self):
        """test_handle_error _summary_
        """
        # TODO add docstring
        # FIXME do we need this?

    def test_size(self):
        """test_get_size _summary_
        """
        # TODO add docstring
        test_al = array_list()
        assert test_al.size() == 0
        assert test_al._size == 0
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_al = array_list(elements=test_data)
            # assert test_al.size() == len(test_data)
            # assert test_al._size == len(test_data)

    def test_is_empty(self):
        """test_is_empty _summary_
        """
        # TODO add docstring
        test_al = array_list()
        assert test_al.is_empty() is True
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_al = array_list(elements=test_data)
            assert test_al.is_empty() is False
            assert test_al._size == len(test_data)

    def test_get_first(self):
        """test_get_first _summary_
        """
        # TODO add docstring
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_len = len(test_data)
            test_al = array_list(elements=test_data)
            assert test_al.get_first() == test_data[0]
            a = (test_al._size == test_len)
            b = (test_al.size() == test_len)
            assert all([a, b])

    def test_get_last(self):
        """test_get_last _summary_
        """
        # TODO add docstring
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_len = len(test_data)
            test_al = array_list(elements=test_data)
            assert test_al.get_last() == test_data[-1]
            a = (test_al._size == test_len)
            b = (test_al.size() == test_len)
            assert all([a, b])


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































        """test_get_element _summary_
        """
        # TODO add docstring
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_al = array_list(elements=test_data)
            for i in range(len(test_data)):
                assert test_al.get_element(i) == test_data[i]

    def test_remove_first(self):
        """test_remove_first _summary_
        """
        # TODO add docstring
        for key in self.global_params.keys():
            test_data = self.global_params.get(key)
            test_len = len(test_data)
            test_al = array_list(elements=test_data)
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
