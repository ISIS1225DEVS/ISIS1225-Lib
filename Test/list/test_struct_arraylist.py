# impoting testing framework
import unittest
import pytest
# importing the class to be tested
import config
from DISClib.DataStructures.arraylist import array_list as al
# asserting module existence
assert config
assert al


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
        temp_lt = parameters.get("TEST_DICT_LT").copy()
        tal = al(temp_lt)
        TEST_AL_LT.append(tal)
    parameters["TEST_AL_LT"] = TEST_AL_LT
    return parameters


class test_array_list(unittest.TestCase):
    """test_array_list _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, global_params):
        self.global_params = global_params

    def test_basic_init(self):
        """test_init _summary_
        """
        # TODO add docstring

    def test_custom_init(self):
        """test_custom_init _summary_
        """
        # TODO add docstring

    def test_post_init(self):
        """test_post_init _summary_
        """
        # TODO add docstring

    def test_handle_error(self):
        """test_handle_error _summary_
        """
        # TODO add docstring

    def test_size(self):
        """test_get_size _summary_
        """
        # TODO add docstring

    def test_is_empty(self):
        """test_is_empty _summary_
        """
        # TODO add docstring

    def test_get_first(self):
        """test_get_first _summary_
        """
        # TODO add docstring

    def test_get_last(self):
        """test_get_last _summary_
        """
        # TODO add docstring

    def test_get_element(self):
        """test_get_element _summary_
        """
        # TODO add docstring

    def test_get_elements(self):
        """test_get_elements _summary_
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

    def test_remove_first(self):
        """test_remove_first _summary_
        """
        # TODO add docstring

    def test_remove_last(self):
        """test_remove_last _summary_
        """
        # TODO add docstring

    def test_remove_element(self):
        """test_remove_element _summary_
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
