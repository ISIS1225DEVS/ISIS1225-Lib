# importing testing framework
# import unittest
# import pytest

"""
Este módulo contiene datos de prueba para las pruebas unitarias para diferentes estructuras de datos en DISCLib.
"""


def get_node_test_data():
    """*get_node_test_data()* recupera un diccionario con los datos de prueba para la clase *Node*.

    Returns:
        dict: diccionario con los datos de prueba para la clase *Node*.
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


def get_list_test_data():
    """*get_list_test_data()* recupera un diccionario con los datos de prueba para la clase *List*.

    Returns:
        dict: diccionario con los datos de prueba para la clase *List*.
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
    return parameters
