"""
*test_struct_list.py* es el módulo que prueba los ADTs *ArrayList*, *SingleLinked* y *DoubleLinked* con sus respectivas funciones para el ADT dinámico y configurable *List* de *DISCLib*.
"""

# impoting testing framework
import unittest
import pytest
import random

# importing the classes to test
from DISClib.DataStructures.arraylist import ArrayList
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.doublelinkedlist import DoubleLinked

# importing the data to test the classes
from Test.Data.test_data import get_list_test_data

# asserting module existence
assert ArrayList
assert SingleLinked
assert DoubleLinked
assert get_list_test_data

# list of keys to ignore in the global parameters
# :data: IGNORE_KEYS_LT: list
IGNORE_KEYS_LT = (
    "CHECK_ERR_LT",
    "CHECK_TYPE_LT",
    "TEST_AL_LT"
)
"""
Lista de llaves a ignorar en los parámetros globales en las pruebas.
"""


# @pytest.fixture(scope="module")
def cmp_lt_test_function(elm1: dict, elm2: dict) -> int:
    """*cmp_lt_test_function()* compara dos elementos en una lista (ArrayList, SingleLinked, DoubleLinked). Solo funciona con diccionarios con una llave "uuid".

    Args:
        elm1 (dict): primer elemento a comparar.
        elm2 (dict): segundo elemento a comparar.

    Raises:
        Exception: error si la llave no está presente en ambos elementos.
        Exception: error si la comparación es inválida.

    Returns:
        int: devuelve 1 si el primer elemento es mayor que el segundo, -1 si el primer elemento es menor que el segundo, 0 si son iguales.
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
    """*TestArrayList* clase *unittest* para probar la clase *ArrayList* de *DISCLib*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *ArrayList* como un *fixture*.
        """
        self.global_params = get_list_test_data()

        # configure the test data to include ArrayList
        TEST_ARRAY_LIST_LT = list()
        for i in self.global_params.get("TEST_INT_LT"):
            temp_lt = self.global_params.get("TEST_DICT_LT")
            tal = ArrayList(temp_lt)
            TEST_ARRAY_LIST_LT.append(tal)
        self.global_params["TEST_AL_LT"] = TEST_ARRAY_LIST_LT

    def test_default_arraylist(self):
        """*test_default_arraylist()* prueba la inicialización de un *ArrayList* vacío.
        """
        # Test an empty ArrayList
        ar_lt = ArrayList()
        # Test if ArrayList is not None
        assert ar_lt is not None
        # Test if ArrayList is empty
        assert ar_lt._size == 0
        # Test if ArrayList elements is empty
        assert ar_lt.elements == []
        # Test if ArrayList key is "id"
        assert ar_lt.key == "id"
        # Test if ArrayList cmp_function is the default
        assert ar_lt.cmp_function == ar_lt.default_cmp_function
        # Test if ArrayList is an instance of ArrayList
        assert isinstance(ar_lt, ArrayList)

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de comparación predeterminada de *ArrayList* con diferentes tipos de elementos.
        """
        # create a new empty ArrayList with the default cmp function
        ar_lt = ArrayList()
        # iterate over tglobal params and use the default cmp function
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = ar_lt.default_cmp_function(ce, pe) in exp_res
                        res2 = ar_lt.default_cmp_function(ce, ce) in exp_res
                        res3 = ar_lt.default_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_arraylist(self):
        """*test_custom_arraylist()* prueba la inicialización de un *ArrayList* personalizado con elementos de diferentes tipos.
        """
        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(test_data)
                # test for the ArrayList is not None
                assert ar_lt is not None
                # test for the ArrayList elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the ArrayList key is "id"
                assert ar_lt.key == "id"
                # test for the ArrayList cmp_function is the default
                assert ar_lt.cmp_function == ar_lt.default_cmp_function
                # test for the ArrayList is an instance of ArrayList
                assert isinstance(ar_lt, ArrayList)
                # test for the ArrayList elements are of the same type
                assert isinstance(ar_lt.elements[0], data_type)
                # test for the ArrayList size is equal to test_data
                assert ar_lt._size == len(test_data)

    def test_custom_key(self):
        """*test_custom_key()* prueba la inicialización de un *ArrayList* personalizado con elementos de diferentes tipos y una llave personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                ar_lt = ArrayList(iodata=test_data,
                                  key="uuid")
                # test for the ArrayList is not None
                assert ar_lt is not None
                # test for the ArrayList size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the ArrayList elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the ArrayList key is "uuid"
                assert ar_lt.key == "uuid"
                # test for the ArrayList cmp_function is the default
                assert ar_lt.cmp_function == ar_lt.default_cmp_function
                # test for the ArrayList is an instance of ArrayList
                assert isinstance(ar_lt, ArrayList)
                # test for the ArrayList elements are of the same type
                assert isinstance(ar_lt.elements[0], dtype)

    def test_custom_cmp_function(self):
        """*test_custom_cmp_function()* prueba la inicialización de un *ArrayList* personalizado con elementos de diferentes tipos y una función de comparación personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                ar_lt = ArrayList(iodata=test_data,
                                  cmp_function=cmp_lt_test_function)
                # test for the ArrayList is not None
                assert ar_lt is not None
                # test for the ArrayList size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the ArrayList elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the ArrayList key is the default "id"
                assert ar_lt.key == "id"
                # test for the ArrayList cmp_function is the custom function
                assert ar_lt.cmp_function == cmp_lt_test_function
                # test for the ArrayList is an instance of ArrayList
                assert isinstance(ar_lt, ArrayList)
                # test for the ArrayList elements are of the same type
                assert isinstance(ar_lt.elements[0], dtype)

    def test_size(self):
        """*test_size()* prueba el método *size()* de *ArrayList* con estructuras de datos vacías y no vacías.
        """

        # create a new empty ArrayList
        ar_lt = ArrayList()
        # test for the ArrayList size is 0 with size method
        assert ar_lt.size() == 0
        # test for the ArrayList size is 0 with _size attribute
        assert ar_lt._size == 0
        # check if the ArrayList elements is empty
        assert ar_lt.elements == []

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # test for the ArrayList size() is equal to test_data
                assert ar_lt.size() == len(test_data)
                # test for the ArrayList _size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the ArrayList elements is equal to test_data
                assert ar_lt.elements == test_data

    def test_is_empty(self):
        """*test_is_empty()* prueba el método *is_empty()* de *ArrayList* con estructuras de datos vacías y no vacías."""
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # test for the ArrayList is empty
        assert ar_lt.is_empty() is True
        # test for the ArrayList elements is empty
        assert ar_lt.elements == []

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # test for the ArrayList is not empty
                assert ar_lt.is_empty() is False
                # test for the ArrayList elements is equal to test_data
                assert ar_lt.elements == test_data

    def test_add_first(self):
        """*test_add_first()* prueba el método *add_first()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si el elemento añadido es igual al índice de *ArrayList*.
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
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
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
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the ArrayList
                    ar_lt.add_first(t_data)
                    # get the first element of the ArrayList
                    t_elem = ar_lt.get_first()
                    # test for the ArrayList get_first() is equal to test_data
                    assert t_elem == t_data
                    # test if the ArrayList size is equal to test_len
                    assert (ar_lt.size() == i + 1)

    def test_add_last(self):
        """*test_add_last()* prueba el método *add_last()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si el elemento añadido es igual al índice de *ArrayList*.
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
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
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
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the ArrayList
                    ar_lt.add_last(t_data)
                    # get the first element of the ArrayList
                    t_elem = ar_lt.get_last()
                    # test for the ArrayList get_last() is equal to test_data
                    assert t_elem == t_data
                    # test if the ArrayList size is equal to test_len
                    assert (ar_lt.size() == i + 1)

    def test_add_element(self):
        """*test_add_element()* prueba el método *add_element()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento añadido es igual al índice de *ArrayList*.
        """
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.add_element(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the add_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    ar_lt.add_element(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the ArrayList
                ar_lt.add_element(t_data, i)
                # get the added element in the index of the ArrayList
                t_elem = ar_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the ArrayList size is equal to test_len
                assert (ar_lt.size() == (test_len + 1))

    def test_get_first(self):
        """*test_get_first()* prueba el método *get_first()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *ArrayList*.
        """
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # test for the ArrayList get_first() is equal to test_data
                assert ar_lt.get_first() == test_data[0]
                # test if ArrayList size() is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_get_last(self):
        """*test_get_last()* prueba el método *get_last()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *ArrayList*.
        """
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_last method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # test for the ArrayList get_last() is equal to test_data
                assert ar_lt.get_last() == test_data[-1]
                # test if ArrayList size() is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_get_element(self):
        """*test_get_element()* prueba el método *get_element()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *ArrayList*.
        """
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.get_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)

                # test get_element with an out-of-range index
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len, test_len * 2)
                    ar_lt.get_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # test for get_element(i) is equal to test_data[i]
                    assert ar_lt.get_element(i) == test_data[i]
                    # test if ArrayList size() is equal to test_len
                    assert (ar_lt.size() == test_len)

    def test_remove_first(self):
        """*test_remove_first()* prueba el método *remove_first()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice.
        """
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.remove_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                for i in range(0, len(test_data) - 1):
                    t_data = test_data[i]
                    t_elem = ar_lt.remove_first()
                    # test if the removed element is equal to the first
                    assert t_elem == t_data
                    # test if the ArrayList size is equal to test_len
                    assert (ar_lt.size() == (test_len - i - 1))

    def test_remove_last(self):
        """*test_remove_last()* prueba el método *remove_last()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.remove_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the last element of the test data

                    t_data = test_data[test_len - 1 - i]
                    # remove the last element of the ArrayList
                    t_elem = ar_lt.remove_last()
                    # test if the removed element is equal to the last
                    assert t_elem == t_data
                    # test if the ArrayList size is equal to test_len
                    assert (ar_lt.size() == (test_len - i - 1))

    def test_remove_element(self):
        """*test_remove_element()* prueba el método *remove_element()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.remove_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)

                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * -1, -1)
                    ar_lt.remove_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # remove the element in the index of the ArrayList
                t_elem = ar_lt.remove_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the ArrayList size is equal to test_len
                assert (ar_lt.size() == (test_len - 1))

    def test_compare_elements(self):
        """*test_compare_elements()* prueba el método *compare_elements()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos comparados son iguales al índice dentro del *ArrayList*.
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

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result with the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = ar_lt.compare_elements(ce, pe) in exp_res
                        res2 = ar_lt.compare_elements(ce, ce) in exp_res
                        res3 = ar_lt.compare_elements(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_find(self):
        """*test_find()* prueba el método *find()* de *ArrayList* con estructuras de datos no vacías y no vacías. Comprueba que el número entero del indice devuelto sea válido, es decir que esté entre -1 y el tamaño de la estructura de datos menos 1. -1 significa que el elemento no está presente en la estructura de datos y los indices van desde 0 a n-1.
        """
        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                test_len = len(test_data)
                ar_lt = ArrayList(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                t_data = test_data[i]
                # test if the element is present in the ArrayList
                idx = ar_lt.find(t_data)
                # test if the index is valid
                # FIXME check this tokenization assert
                assert -1 <= idx <= test_len - 1

    def test_change_info(self):
        """*test_change_info()* prueba el método *change_info()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento cambiado es igual al índice de *ArrayList* y la estructura de datos no se ha modificado mas allá de la longitud original.
        """
        # create a new empty ArrayList
        ar_lt = ArrayList()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.change_info(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the change_info method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    ar_lt.change_info(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the ArrayList
                ar_lt.change_info(t_data, i)
                # get the added element in the index of the ArrayList
                t_elem = ar_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the ArrayList size is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_exchange(self):
        """*test_exchange()* prueba el método *exchange()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si los elementos intercambiados son iguales al índice de *ArrayList* y que la estructura de datos no se ha modificado más allá de la longitud original."""
        # create a new empty ArrayList
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

        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)

                # force an exception in the exchange method
                with pytest.raises(Exception) as excinfo:
                    i, j = random.sample(range(test_len * 2, test_len * 3), 2)
                    ar_lt.exchange(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i, j = random.sample(range(0, test_len - 1), 2)
                # get the elements in the test data
                test_elm1 = test_data[i]
                test_elm2 = test_data[j]

                # exchange the elements in the index of the ArrayList
                ar_lt.exchange(i, j)
                # get the exchanged elements in the index of the ArrayList
                exch_elm1 = ar_lt.get_element(i)
                exch_elm2 = ar_lt.get_element(j)

                # test if the removed element is equal to the index
                assert exch_elm1 == test_elm2
                assert exch_elm2 == test_elm1
                # test if the ArrayList size is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_sublist(self):
        """*test_sublist()* prueba el método *sublist()* de *ArrayList* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """
        # create a new empty ArrayList
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
        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                ar_lt = ArrayList(iodata=test_data)
                # get the length of the test data
                test_len = len(test_data)
                assert ar_lt.size() == test_len
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                i = random.randint(test_len * -1, -1)
                j = random.randint(test_len + 1, test_len * 2)
                # # sample(range(test_len * 2, test_len * 3), 2)
                # # force an exception in the sublist method
                with pytest.raises(Exception) as excinfo:
                    ar_lt.sublist(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # # test for the exception message
                assert "Invalid range: between" in str(excinfo.value)

                # select a random valid a low index in the test data
                # low = random.randint(0, test_len - 1)
                low = random.randint(0, (test_len - 1) // 2)
                # select a random valid a high index in the test data
                high = random.randint(low, test_len - 1)
                # get the elements in the test data
                sub_lt = list()
                i = low
                while i < high + 1:
                    sub_lt.append(test_data[i])
                    i += 1
                # get the elements size in the test data
                sub_lt_size = len(sub_lt)
                # create a sublist with the low and high index
                sub_ar_lt = ar_lt.sublist(low, high)
                # test for the sublist size is an ArrayList
                assert isinstance(sub_ar_lt, ArrayList)
                # test for the sublist size is equal to test_len
                assert sub_lt_size == sub_ar_lt.size()
                # test for the sublist elements are equal to sub_lt
                assert sub_lt == sub_ar_lt.elements

    def test_concat(self):
        """*test_concat()* prueba el método *concat()* de *ArrayList* con estructuras de datos no vacías. Comprueba las excepciones de *TypeError* para estructuras de datos no compatibles. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """
        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                ar_lt1 = ArrayList(iodata=test_data)
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

                # create a new ArrayList with the wrong key
                ar_lt2 = ArrayList(iodata=test_data,
                                   key="testid")
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid key:" in str(excinfo.value)

                # create a new ArrayList with the wrong cmp function
                ar_lt2 = ArrayList(iodata=test_data,
                                   cmp_function=cmp_lt_test_function)
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid compare function:" in str(excinfo.value)

                # create a new correct ArrayList with the test data
                ar_lt1 = ArrayList(iodata=test_data)
                ar_lt2 = ArrayList(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt1 = ArrayList(iodata=test_data,
                                       cmp_function=cmp_lt_test_function)
                    ar_lt2 = ArrayList(iodata=test_data,
                                       cmp_function=cmp_lt_test_function)
                # get the elements in the test data
                ar_lt1_data = ar_lt1.elements.copy()
                ar_lt2_data = ar_lt2.elements.copy()

                # create the new concatenated ArrayList
                ans = ar_lt1.concat(ar_lt2)
                ans_data = ans.elements.copy()

                assert isinstance(ans, ArrayList)
                assert ans.size() == len(ar_lt1_data) + len(ar_lt2_data)
                assert ans_data == ar_lt1_data + ar_lt2_data
                assert all((ans.key, ar_lt1.key, ar_lt2.key))
                assert all((ans.cmp_function,
                            ar_lt1.cmp_function,
                            ar_lt2.cmp_function))

    def test_iterator(self):
        """*test_iterator()* prueba el iterador *__iter__()* de *ArrayList* con estructuras de datos no vacías. También comprueba si los elementos se pueden iterar en conjunto con los elementos de otras estructuras de datos nativas de Python y que los elementos iterados sean iguales a los de la lista original.
        """
        # iterates over global params and create filled ArrayList
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new ArrayList with the test data
                test_len = len(test_data)
                ar_lt = ArrayList(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = ArrayList(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # iterates over the ArrayList and the test data and compare
                for element, data in zip(ar_lt, test_data):
                    # test for the element is equal to test_data
                    assert element == data
                    # test for the element type is equal to test_data
                    assert type(element) is type(data)
                # test for the iterator is exhausted and the StopIteration
                assert ar_lt.size() == test_len


class TestSingleLinked(unittest.TestCase):
    """*TestSingleLinked* clase *unittest* para probar la clase *SingleLinked* de *DISCLib*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *SingleLinked* como un *fixture*.
        """
        self.global_params = get_list_test_data()
        # FIXME do we need this? is this okey?
        TEST_ARRAY_LIST_LT = list()
        for i in self.global_params.get("TEST_INT_LT"):
            temp_lt = self.global_params.get("TEST_DICT_LT")
            tal = SingleLinked(temp_lt)
            TEST_ARRAY_LIST_LT.append(tal)
        self.global_params["TEST_AL_LT"] = TEST_ARRAY_LIST_LT

    def sll_to_list(self, sl_lt: SingleLinked) -> list:
        """*sll_to_list()* convierte una lista sencillamente encadenada nativa de *DISCLib* en una lista nativa de Python.

        Args:
            sl_lt (SingleLinked): Lista sencillamente encadenada nativa de *DISCLib* a convertir en lista nativa de Python.

        Returns:
            list: lista nativa de Python traducida.
        """
        ans = list()
        for elm in sl_lt:
            ans.append(elm)
        return ans

    def test_default_singlelinked(self):
        """*test_default_singlelinked()* prueba la inicialización de una lista sencillamente encadenada o *SingleLinked* vacía.
        """
        # Test an empty SingleLinked
        sl_lt = SingleLinked()
        # Test if SingleLinked is not None
        assert sl_lt is not None
        # Test if SingleLinked is empty
        assert sl_lt._size == 0
        # Test if the SingleLinked first element is empty
        assert sl_lt.first is None
        # Test if the SingleLinked last element is empty
        assert sl_lt.last is None
        # Test if SingleLinked key is "id"
        assert sl_lt.key == "id"
        # Test if SingleLinked cmp_function is the default
        assert sl_lt.cmp_function == sl_lt.default_cmp_function
        # Test if list is an instance of SingleLinked
        assert isinstance(sl_lt, SingleLinked)

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de comparación predeterminada de *SingleLinked* con diferentes tipos de elementos.
        """
        # create a new empty SingleLinked with the default cmp function
        sl_lt = SingleLinked()
        # iterate over tglobal params and use the default cmp function
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = sl_lt.default_cmp_function(ce, pe) in exp_res
                        res2 = sl_lt.default_cmp_function(ce, ce) in exp_res
                        res3 = sl_lt.default_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_singlelinked(self):
        """*test_custom_singlelinked()* prueba la inicialización de una *SingleLinked* personalizada con elementos de diferentes tipos.
        """

        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # testing SingleLinked is not None
                assert sl_lt is not None
                # testing SingleLinked elements is equal to test_data
                sl_lt_data = self.sll_to_list(sl_lt)
                assert sl_lt_data == test_data
                # testing SingleLinked key is "id"
                assert sl_lt.key == "id"
                # testing SingleLinked cmp_function is the default
                assert sl_lt.cmp_function == sl_lt.default_cmp_function
                # testing SingleLinked is an instance of SingleLinked
                assert isinstance(sl_lt, SingleLinked)
                # testing SingleLinked elements are of the same type
                assert isinstance(sl_lt.first.get_info(), data_type)
                # testing SingleLinked size is equal to test_data
                assert sl_lt._size == len(test_data)

    def test_custom_key(self):
        """*test_custom_key()* prueba la inicialización de una *SingleLinked* personalizada con elementos y una llave personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                sl_lt = SingleLinked(iodata=test_data,
                                     key="uuid")
                # testing SingleLinked is not None
                assert sl_lt is not None
                # testing SingleLinked size is equal to test_data
                assert sl_lt._size == len(test_data)
                # testing SingleLinked elements is equal to test_data
                sl_lt_data = self.sll_to_list(sl_lt)
                assert sl_lt_data == test_data
                # testing SingleLinked key is "uuid"
                assert sl_lt.key == "uuid"
                # testing SingleLinked cmp_function is the default
                assert sl_lt.cmp_function == sl_lt.default_cmp_function
                # testing SingleLinked is an instance of SingleLinked
                assert isinstance(sl_lt, SingleLinked)
                # testing SingleLinked elements are of the same type
                assert isinstance(sl_lt.first.get_info(), dtype)

    def test_custom_cmp_function(self):
        """*test_custom_cmp_function()* prueba la inicialización de una *SingleLinked* personalizada con elementos de diferentes tipos y una función de comparación personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                sl_lt = SingleLinked(iodata=test_data,
                                     cmp_function=cmp_lt_test_function)
                # testing SingleLinked is not None
                assert sl_lt is not None
                # testing SingleLinked size is equal to test_data
                assert sl_lt._size == len(test_data)
                # testing SingleLinked elements is equal to test_data
                sl_lt_data = self.sll_to_list(sl_lt)
                assert sl_lt_data == test_data
                # testing SingleLinked key is the default "id"
                assert sl_lt.key == "id"
                # testing SingleLinked cmp_function is the custom function
                assert sl_lt.cmp_function == cmp_lt_test_function
                # testing SingleLinked is an instance of SingleLinked
                assert isinstance(sl_lt, SingleLinked)
                # testing SingleLinked elements are of the same type
                assert isinstance(sl_lt.first.get_info(), dtype)

    def test_size(self):
        """*test_size()* prueba el método *size()* de *SingleLinked* con estructuras de datos vacías y no vacías.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # testing SingleLinked size is 0 with size method
        assert sl_lt.size() == 0
        # testing SingleLinked size is 0 with _size attribute
        assert sl_lt._size == 0
        # check if the SingleLinked elements is empty
        sl_lt_data = self.sll_to_list(sl_lt)
        assert sl_lt_data == []

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # testing SingleLinked size() is equal to test_data
                assert sl_lt.size() == len(test_data)
                # testing SingleLinked _size is equal to test_data
                assert sl_lt._size == len(test_data)
                # # testing SingleLinked elements is equal to test_data
                sl_lt_data = self.sll_to_list(sl_lt)
                assert sl_lt_data == test_data

    def test_is_empty(self):
        """*test_is_empty()* prueba el método *is_empty()* de *SingleLinked* con estructuras de datos vacías y no vacías.
        """

        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # testing SingleLinked is empty
        assert sl_lt.is_empty() is True
        # testing SingleLinked elements is empty
        sl_lt_data = self.sll_to_list(sl_lt)
        assert sl_lt_data == []

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # testing SingleLinked is not empty
                assert sl_lt.is_empty() is False
                # testing SingleLinked elements is equal to test_data
                sl_lt_data = self.sll_to_list(sl_lt)
                assert sl_lt_data == test_data

    def test_add_first(self):
        """*test_add_first()* prueba el método *add_first()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos agregados son iguales al índice dentro de *SingleLinked*.
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
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                with pytest.raises(TypeError) as excinfo:
                    sl_lt = SingleLinked(test_data)
                    # induce the error by adding an element of a different type
                    sl_lt.add_first(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_first method normal behavior
                sl_lt = SingleLinked()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the SingleLinked
                    sl_lt.add_first(t_data)
                    # get the first element of the SingleLinked
                    t_elem = sl_lt.get_first()
                    # testing SingleLinked get_first() is equal to test_data
                    assert t_elem == t_data
                    # test if the SingleLinked size is equal to test_len
                    assert (sl_lt.size() == i + 1)

    def test_add_last(self):
        """*test_add_last()* prueba el método *add_last()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos agregados son iguales al índice dentro de *SingleLinked*.
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
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                with pytest.raises(TypeError) as excinfo:
                    sl_lt = SingleLinked(test_data)
                    # induce the error by adding an element of a different type
                    sl_lt.add_last(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_lat method normal behavior
                sl_lt = SingleLinked()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the SingleLinked
                    sl_lt.add_last(t_data)
                    # get the first element of the SingleLinked
                    t_elem = sl_lt.get_last()
                    # testing SingleLinked get_last() is equal to test_data
                    assert t_elem == t_data
                    # test if the SingleLinked size is equal to test_len
                    assert (sl_lt.size() == i + 1)

    def test_add_element(self):
        """*test_add_element()* prueba el método *add_element()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento añadido es igual al índice de *SingleLinked*.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            sl_lt.add_element(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the add_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    sl_lt.add_element(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the SingleLinked
                sl_lt.add_element(t_data, i)
                # get the added element in the index of the SingleLinked
                t_elem = sl_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the SingleLinked size is equal to test_len
                assert (sl_lt.size() == (test_len + 1))

    def test_get_first(self):
        """*test_get_first()* prueba el método *get_first()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *SingleLinked*.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            sl_lt.get_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # testing SingleLinked get_first() is equal to test_data
                assert sl_lt.get_first() == test_data[0]
                # test if SingleLinked size() is equal to test_len
                assert (sl_lt.size() == test_len)

    def test_get_last(self):
        """*test_get_last()* prueba el método *get_last()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *SingleLinked*.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_last method
        with pytest.raises(Exception) as excinfo:
            sl_lt.get_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # testing SingleLinked get_last() is equal to test_data
                assert sl_lt.get_last() == test_data[-1]
                # test if SingleLinked size() is equal to test_len
                assert (sl_lt.size() == test_len)

    def test_get_element(self):
        """*test_get_element()* prueba el método *get_element()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *SingleLinked*.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            sl_lt.get_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)

                # test get_element with an out-of-range index
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len, test_len * 2)
                    sl_lt.get_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # test for get_element(i) is equal to test_data[i]
                    assert sl_lt.get_element(i) == test_data[i]
                    # test if SingleLinked size() is equal to test_len
                    assert (sl_lt.size() == test_len)

    def test_remove_first(self):
        """*test_remove_first()* prueba el método *remove_first()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            sl_lt.remove_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                for i in range(0, len(test_data) - 1):
                    t_data = test_data[i]
                    t_elem = sl_lt.remove_first()
                    # test if the removed element is equal to the first
                    assert t_elem == t_data
                    # test if the SingleLinked size is equal to test_len
                    assert (sl_lt.size() == (test_len - i - 1))

    def test_remove_last(self):
        """*test_remove_last()* prueba el método *remove_last()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            sl_lt.remove_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the last element of the test data

                    t_data = test_data[test_len - 1 - i]
                    # remove the last element of the SingleLinked
                    t_elem = sl_lt.remove_last()
                    # test if the removed element is equal to the last
                    assert t_elem == t_data
                    # test if the SingleLinked size is equal to test_len
                    assert (sl_lt.size() == (test_len - i - 1))

    def test_remove_element(self):
        """*test_remove_element()* prueba el método *remove_element()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            sl_lt.remove_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)

                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * -1, -1)
                    sl_lt.remove_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # remove the element in the index of the SingleLinked
                t_elem = sl_lt.remove_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the SingleLinked size is equal to test_len
                assert (sl_lt.size() == (test_len - 1))

    def test_compare_elements(self):
        """*test_compare_elements()* prueba el método *compare_elements()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos comparados son iguales al índice dentro del *SingleLinked*.
        """
        sl_lt = SingleLinked()
        # delete the default cmp function
        sl_lt.cmp_function = None
        # delete the default key
        sl_lt.key = None
        # force an exception in the compare_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            j = random.randint(0, 100)
            sl_lt.compare_elements(i, j)
        # test for the exception type
        assert excinfo.type == TypeError
        # test for the exception message
        assert "Undefined compare function" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt = SingleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result with the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = sl_lt.compare_elements(ce, pe) in exp_res
                        res2 = sl_lt.compare_elements(ce, ce) in exp_res
                        res3 = sl_lt.compare_elements(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_find(self):
        """*test_find()* prueba el método *find()* de *SingleLinked* con estructuras de datos no vacías y no vacías. Comprueba que el número entero del indice devuelto sea válido, es decir que esté entre -1 y el tamaño de la estructura de datos menos 1. -1 significa que el elemento no está presente en la estructura de datos y los indices van desde 0 a n-1.
        """
        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                test_len = len(test_data)
                sl_lt = SingleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt = SingleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                t_data = test_data[i]
                # test if the element is present in the SingleLinked
                idx = sl_lt.find(t_data)
                # test if the index is valid
                assert -1 <= idx <= test_len - 1

    def test_change_info(self):
        """*test_change_info()* prueba el método *change_info()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento cambiado es igual al índice de *SingleLinked* y la estructura de datos no se ha modificado mas allá de la longitud original.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            sl_lt.change_info(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt = SingleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the change_info method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    sl_lt.change_info(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the SingleLinked
                sl_lt.change_info(t_data, i)
                # get the added element in the index of the SingleLinked
                t_elem = sl_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the SingleLinked size is equal to test_len
                assert (sl_lt.size() == test_len)

    def test_exchange(self):
        """*test_exchange()* prueba el método *exchange()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si los elementos intercambiados son iguales al índice de *SingleLinked* y que la estructura de datos no se ha modificado más allá de la longitud original."""
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the exchange method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            sl_lt.exchange(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt = SingleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)

                # force an exception in the exchange method
                with pytest.raises(Exception) as excinfo:
                    i, j = random.sample(range(test_len * 2, test_len * 3), 2)
                    sl_lt.exchange(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i, j = random.sample(range(0, test_len - 1), 2)
                # get the elements in the test data
                test_elm1 = test_data[i]
                test_elm2 = test_data[j]

                # exchange the elements in the index of the SingleLinked
                sl_lt.exchange(i, j)
                # get the exchanged elements in the index of the SingleLinked
                exch_elm1 = sl_lt.get_element(i)
                exch_elm2 = sl_lt.get_element(j)

                # test if the removed element is equal to the index
                assert exch_elm1 == test_elm2
                assert exch_elm2 == test_elm1
                # test if the SingleLinked size is equal to test_len
                assert (sl_lt.size() == test_len)

    def test_sublist(self):
        """*test_sublist()* prueba el método *sublist()* de *SingleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """
        # create a new empty SingleLinked
        sl_lt = SingleLinked()
        # force an exception in the sublist method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            sl_lt.sublist(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                sl_lt = SingleLinked(iodata=test_data)
                # get the length of the test data
                test_len = len(test_data)
                assert sl_lt.size() == test_len
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt = SingleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                i = random.randint(test_len * -1, -1)
                j = random.randint(test_len + 1, test_len * 2)
                # # sample(range(test_len * 2, test_len * 3), 2)
                # # force an exception in the sublist method
                with pytest.raises(Exception) as excinfo:
                    sl_lt.sublist(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # # test for the exception message
                assert "Invalid range: between" in str(excinfo.value)

                # select a random valid a low index in the test data
                # low = random.randint(0, test_len - 1)
                low = random.randint(0, (test_len - 1) // 2)
                # select a random valid a high index in the test data
                high = random.randint(low, test_len - 1)
                # get the elements in the test data
                sub_lt = list()
                i = low
                while i != high + 1:
                    sub_lt.append(test_data[i])
                    i += 1
                # get the elements size in the test data
                sub_lt_size = len(sub_lt)
                # create a sublist with the low and high index
                sub_sl_lt = sl_lt.sublist(low, high)
                # test for the sublist size is an SingleLinked
                assert isinstance(sub_sl_lt, SingleLinked)
                # test for the sublist size is equal to test_len
                assert sub_lt_size == sub_sl_lt.size()
                # test for the sublist elements are equal to sub_lt
                sub_sl_lt_data = self.sll_to_list(sub_sl_lt)
                assert sub_lt == sub_sl_lt_data

    def test_concat(self):
        """*test_concat()* prueba el método *concat()* de *SingleLinked* con estructuras de datos no vacías. Comprueba las excepciones de *TypeError* para estructuras de datos no compatibles. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """

        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                sl_lt1 = SingleLinked(iodata=test_data)
                # create a python list with the test data
                sl_lt2 = test_data.copy()

                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    sl_lt1.concat(sl_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                err_msg = "Structure is not an SingleLinked:"
                assert err_msg in str(excinfo.value)

                # create a new SingleLinked with the wrong key
                sl_lt2 = SingleLinked(iodata=test_data,
                                      key="testid")
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    sl_lt1.concat(sl_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid key:" in str(excinfo.value)

                # create a new SingleLinked with the wrong cmp function
                sl_lt2 = SingleLinked(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    sl_lt1.concat(sl_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid compare function:" in str(excinfo.value)

                # create a new correct SingleLinked with the test data
                sl_lt1 = SingleLinked(iodata=test_data)
                sl_lt2 = SingleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt1 = SingleLinked(iodata=test_data,
                                          cmp_function=cmp_lt_test_function)
                    sl_lt2 = SingleLinked(iodata=test_data,
                                          cmp_function=cmp_lt_test_function)
                # create the new concatenated SingleLinked

                sl_lt1_data = self.sll_to_list(sl_lt1)
                sl_lt2_data = self.sll_to_list(sl_lt2)
                ans = sl_lt1.concat(sl_lt2)
                ans_data = self.sll_to_list(ans)

                assert isinstance(ans, SingleLinked)
                assert ans.size() == len(sl_lt1_data) + len(sl_lt2_data)
                assert ans_data == sl_lt1_data + sl_lt2_data
                assert all((ans.key, sl_lt1.key, sl_lt2.key))
                assert all((ans.cmp_function,
                           sl_lt1.cmp_function,
                           sl_lt2.cmp_function))

    def test_iterator(self):
        """*test_iterator()* prueba el iterador *__iter__()* de *SingleLinked* con estructuras de datos no vacías. También comprueba si los elementos se pueden iterar en conjunto con los elementos de otras estructuras de datos nativas de Python y que los elementos iterados sean iguales a los de la lista original.
        """
        # iterates over global params and create filled SingleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new SingleLinked with the test data
                test_len = len(test_data)
                sl_lt = SingleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    sl_lt = SingleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # iterates over the SingleLinked and the test data and compare
                for element, data in zip(sl_lt, test_data):
                    # test for the element is equal to test_data
                    assert element == data
                    # test for the element type is equal to test_data
                    assert type(element) is type(data)
                # test for the iterator is exhausted and the StopIteration
                assert sl_lt.size() == test_len


class TestDoubleLinked(unittest.TestCase):
    """*TestDoubleLinked* clase *unittest* para probar la clase *DoubleLinked* de *DISCLib*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *DoubleLinked* como un *fixture*.
        """

        self.global_params = get_list_test_data()
        # FIXME do we need this? is this okey?
        TEST_ARRAY_LIST_LT = list()
        for i in self.global_params.get("TEST_INT_LT"):
            temp_lt = self.global_params.get("TEST_DICT_LT")
            tal = DoubleLinked(temp_lt)
            TEST_ARRAY_LIST_LT.append(tal)
        self.global_params["TEST_AL_LT"] = TEST_ARRAY_LIST_LT

    def dll_to_list(self, dl_lt: DoubleLinked) -> list:
        """*dll_to_list()* convierte una lista sencillamente encadenada nativa de *DISCLib* en una lista nativa de Python.

        Args:
            dl_lt (DoubleLinked): Lista sencillamente encadenada nativa de *DISCLib* a convertir en lista nativa de Python.

        Returns:
            list: lista nativa de Python traducida.
        """
        ans = list()
        for elm in dl_lt:
            ans.append(elm)
        return ans

    def test_default_singlelinked(self):
        """*test_default_singlelinked()* prueba la inicialización de una lista sencillamente encadenada o *DoubleLinked* vacía.
        """
        # Test an empty DoubleLinked
        dl_lt = DoubleLinked()
        # Test if DoubleLinked is not None
        assert dl_lt is not None
        # Test if DoubleLinked is empty
        assert dl_lt._size == -1
        # Test if the DoubleLinked first element is empty
        assert dl_lt._header.get_info() is None
        # Test if the DoubleLinked last element is empty
        assert dl_lt._trailer.get_info() is None
        # Test if DoubleLinked key is "id"
        assert dl_lt.key == "id"
        # Test if DoubleLinked cmp_function is the default
        assert dl_lt.cmp_function == dl_lt.default_cmp_function
        # Test if list is an instance of DoubleLinked
        assert isinstance(dl_lt, DoubleLinked)

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de comparación predeterminada de *DoubleLinked* con diferentes tipos de elementos.
        """
        # create a new empty DoubleLinked with the default cmp function
        dl_lt = DoubleLinked()
        # iterate over tglobal params and use the default cmp function
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = dl_lt.default_cmp_function(ce, pe) in exp_res
                        res2 = dl_lt.default_cmp_function(ce, ce) in exp_res
                        res3 = dl_lt.default_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_singlelinked(self):
        """*test_custom_singlelinked()* prueba la inicialización de una *DoubleLinked* personalizada con elementos de diferentes tipos.
        """
        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # testing DoubleLinked is not None
                assert dl_lt is not None
                # testing DoubleLinked elements is equal to test_data
                sl_lt_data = self.dll_to_list(dl_lt)
                assert sl_lt_data == test_data
                # testing DoubleLinked key is "id"
                assert dl_lt.key == "id"
                # testing DoubleLinked cmp_function is the default
                assert dl_lt.cmp_function == dl_lt.default_cmp_function
                # testing DoubleLinked is an instance of DoubleLinked
                assert isinstance(dl_lt, DoubleLinked)
                # testing DoubleLinked elements are of the same type
                assert isinstance(dl_lt._header.next().get_info(), data_type)
                # testing DoubleLinked size is equal to test_data
                assert dl_lt._size == len(test_data)

    def test_custom_key(self):
        """*test_custom_key()* prueba la inicialización de una *DoubleLinked* personalizada con elementos y una llave personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                dl_lt = DoubleLinked(iodata=test_data,
                                     key="uuid")
                # testing DoubleLinked is not None
                assert dl_lt is not None
                # testing DoubleLinked size is equal to test_data
                assert dl_lt._size == len(test_data)
                # testing DoubleLinked elements is equal to test_data
                sl_lt_data = self.dll_to_list(dl_lt)
                assert sl_lt_data == test_data
                # testing DoubleLinked key is "uuid"
                assert dl_lt.key == "uuid"
                # testing DoubleLinked cmp_function is the default
                assert dl_lt.cmp_function == dl_lt.default_cmp_function
                # testing DoubleLinked is an instance of DoubleLinked
                assert isinstance(dl_lt, DoubleLinked)
                # testing DoubleLinked elements are of the same type
                assert isinstance(dl_lt._header.next().get_info(), dtype)

    def test_custom_cmp_function(self):
        """*test_custom_cmp_function()* prueba la inicialización de una *DoubleLinked* personalizada con elementos de diferentes tipos y una función de comparación personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                dl_lt = DoubleLinked(iodata=test_data,
                                     cmp_function=cmp_lt_test_function)
                # testing DoubleLinked is not None
                assert dl_lt is not None
                # testing DoubleLinked size is equal to test_data
                assert dl_lt._size == len(test_data)
                # testing DoubleLinked elements is equal to test_data
                sl_lt_data = self.dll_to_list(dl_lt)
                assert sl_lt_data == test_data
                # testing DoubleLinked key is the default "id"
                assert dl_lt.key == "id"
                # testing DoubleLinked cmp_function is the custom function
                assert dl_lt.cmp_function == cmp_lt_test_function
                # testing DoubleLinked is an instance of DoubleLinked
                assert isinstance(dl_lt, DoubleLinked)
                # testing DoubleLinked elements are of the same type
                assert isinstance(dl_lt._header.next().get_info(), dtype)

    def test_size(self):
        """*test_size()* prueba el método *size()* de *DoubleLinked* con estructuras de datos vacías y no vacías.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # testing DoubleLinked size is 0 with size method
        assert dl_lt.size() == 0
        # testing DoubleLinked size is 0 with _size attribute
        assert dl_lt._size == -1
        # check if the DoubleLinked elements is empty
        sl_lt_data = self.dll_to_list(dl_lt)
        assert sl_lt_data == []

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # testing DoubleLinked size() is equal to test_data
                assert dl_lt.size() == len(test_data)
                # testing DoubleLinked _size is equal to test_data
                assert dl_lt._size == len(test_data)
                # # testing DoubleLinked elements is equal to test_data
                sl_lt_data = self.dll_to_list(dl_lt)
                assert sl_lt_data == test_data

    def test_is_empty(self):
        """*test_is_empty()* prueba el método *is_empty()* de *DoubleLinked* con estructuras de datos vacías y no vacías.
        """

        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # testing DoubleLinked is empty
        assert dl_lt.is_empty() is True
        # testing DoubleLinked elements is empty
        sl_lt_data = self.dll_to_list(dl_lt)
        assert sl_lt_data == []

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # testing DoubleLinked is not empty
                assert dl_lt.is_empty() is False
                # testing DoubleLinked elements is equal to test_data
                sl_lt_data = self.dll_to_list(dl_lt)
                assert sl_lt_data == test_data

    def test_add_first(self):
        """*test_add_first()* prueba el método *add_first()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos agregados son iguales al índice dentro de *DoubleLinked*.
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
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                with pytest.raises(TypeError) as excinfo:
                    dl_lt = DoubleLinked(test_data)
                    # induce the error by adding an element of a different type
                    dl_lt.add_first(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_first method normal behavior
                dl_lt = DoubleLinked()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the DoubleLinked
                    dl_lt.add_first(t_data)
                    # get the first element of the DoubleLinked
                    t_elem = dl_lt.get_first()
                    # testing DoubleLinked get_first() is equal to test_data
                    assert t_elem == t_data
                    # test if the DoubleLinked size is equal to test_len
                    assert (dl_lt.size() == i + 1)

    def test_add_last(self):
        """*test_add_last()* prueba el método *add_last()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos agregados son iguales al índice dentro de *DoubleLinked*.
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
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                with pytest.raises(TypeError) as excinfo:
                    dl_lt = DoubleLinked(test_data)
                    # induce the error by adding an element of a different type
                    dl_lt.add_last(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_lat method normal behavior
                dl_lt = DoubleLinked()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the DoubleLinked
                    dl_lt.add_last(t_data)
                    # get the first element of the DoubleLinked
                    t_elem = dl_lt.get_last()
                    # testing DoubleLinked get_last() is equal to test_data
                    assert t_elem == t_data
                    # test if the DoubleLinked size is equal to test_len
                    assert (dl_lt.size() == i + 1)

    def test_add_element(self):
        """*test_add_element()* prueba el método *add_element()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento añadido es igual al índice de *DoubleLinked*.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            dl_lt.add_element(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the add_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    dl_lt.add_element(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the DoubleLinked
                dl_lt.add_element(t_data, i)
                # get the added element in the index of the DoubleLinked
                t_elem = dl_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the DoubleLinked size is equal to test_len
                assert (dl_lt.size() == (test_len + 1))

    def test_get_first(self):
        """*test_get_first()* prueba el método *get_first()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *DoubleLinked*.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            dl_lt.get_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # testing DoubleLinked get_first() is equal to test_data
                assert dl_lt.get_first() == test_data[0]
                # test if DoubleLinked size() is equal to test_len
                assert (dl_lt.size() == test_len)

    def test_get_last(self):
        """*test_get_last()* prueba el método *get_last()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *DoubleLinked*.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_last method
        with pytest.raises(Exception) as excinfo:
            dl_lt.get_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # testing DoubleLinked get_last() is equal to test_data
                assert dl_lt.get_last() == test_data[-1]
                # test if DoubleLinked size() is equal to test_len
                assert (dl_lt.size() == test_len)

    def test_get_element(self):
        """*test_get_element()* prueba el método *get_element()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *DoubleLinked*.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            dl_lt.get_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)

                # test get_element with an out-of-range index
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len, test_len * 2)
                    dl_lt.get_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # test for get_element(i) is equal to test_data[i]
                    assert dl_lt.get_element(i) == test_data[i]
                    # test if DoubleLinked size() is equal to test_len
                    assert (dl_lt.size() == test_len)

    def test_remove_first(self):
        """*test_remove_first()* prueba el método *remove_first()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            dl_lt.remove_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                for i in range(0, len(test_data) - 1):
                    t_data = test_data[i]
                    t_elem = dl_lt.remove_first()
                    # test if the removed element is equal to the first
                    assert t_elem == t_data
                    # test if the DoubleLinked size is equal to test_len
                    assert (dl_lt.size() == (test_len - i - 1))

    def test_remove_last(self):
        """*test_remove_last()* prueba el método *remove_last()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            dl_lt.remove_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the last element of the test data

                    t_data = test_data[test_len - 1 - i]
                    # remove the last element of the DoubleLinked
                    t_elem = dl_lt.remove_last()
                    # test if the removed element is equal to the last
                    assert t_elem == t_data
                    # test if the DoubleLinked size is equal to test_len
                    assert (dl_lt.size() == (test_len - i - 1))

    def test_remove_element(self):
        """*test_remove_element()* prueba el método *remove_element()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            dl_lt.remove_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)

                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * -1, -1)
                    dl_lt.remove_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # remove the element in the index of the DoubleLinked
                t_elem = dl_lt.remove_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the DoubleLinked size is equal to test_len
                assert (dl_lt.size() == (test_len - 1))

    def test_compare_elements(self):
        """*test_compare_elements()* prueba el método *compare_elements()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos comparados son iguales al índice dentro del *DoubleLinked*.
        """
        dl_lt = DoubleLinked()
        # delete the default cmp function
        dl_lt.cmp_function = None
        # delete the default key
        dl_lt.key = None
        # force an exception in the compare_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            j = random.randint(0, 100)
            dl_lt.compare_elements(i, j)
        # test for the exception type
        assert excinfo.type == TypeError
        # test for the exception message
        assert "Undefined compare function" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result with the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = dl_lt.compare_elements(ce, pe) in exp_res
                        res2 = dl_lt.compare_elements(ce, ce) in exp_res
                        res3 = dl_lt.compare_elements(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_find(self):
        """*test_find()* prueba el método *find()* de *DoubleLinked* con estructuras de datos no vacías y no vacías. Comprueba que el número entero del indice devuelto sea válido, es decir que esté entre -1 y el tamaño de la estructura de datos menos 1. -1 significa que el elemento no está presente en la estructura de datos y los indices van desde 0 a n-1.
        """
        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                test_len = len(test_data)
                dl_lt = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                t_data = test_data[i]
                # test if the element is present in the DoubleLinked
                idx = dl_lt.find(t_data)
                # test if the index is valid
                assert -1 <= idx <= test_len - 1

    def test_change_info(self):
        """*test_change_info()* prueba el método *change_info()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento cambiado es igual al índice de *DoubleLinked* y la estructura de datos no se ha modificado mas allá de la longitud original.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            dl_lt.change_info(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the change_info method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    dl_lt.change_info(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the DoubleLinked
                dl_lt.change_info(t_data, i)
                # get the added element in the index of the DoubleLinked
                t_elem = dl_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the DoubleLinked size is equal to test_len
                assert (dl_lt.size() == test_len)

    def test_exchange(self):
        """*test_exchange()* prueba el método *exchange()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si los elementos intercambiados son iguales al índice de *DoubleLinked* y que la estructura de datos no se ha modificado más allá de la longitud original."""
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the exchange method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            dl_lt.exchange(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)

                # force an exception in the exchange method
                with pytest.raises(Exception) as excinfo:
                    i, j = random.sample(range(test_len * 2, test_len * 3), 2)
                    dl_lt.exchange(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i, j = random.sample(range(0, test_len - 1), 2)
                # get the elements in the test data
                test_elm1 = test_data[i]
                test_elm2 = test_data[j]

                # exchange the elements in the index of the DoubleLinked
                dl_lt.exchange(i, j)
                # get the exchanged elements in the index of the DoubleLinked
                exch_elm1 = dl_lt.get_element(i)
                exch_elm2 = dl_lt.get_element(j)

                # test if the removed element is equal to the index
                assert exch_elm1 == test_elm2
                assert exch_elm2 == test_elm1
                # test if the DoubleLinked size is equal to test_len
                assert (dl_lt.size() == test_len)

    def test_sublist(self):
        """*test_sublist()* prueba el método *sublist()* de *DoubleLinked* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """
        # create a new empty DoubleLinked
        dl_lt = DoubleLinked()
        # force an exception in the sublist method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            dl_lt.sublist(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                dl_lt = DoubleLinked(iodata=test_data)
                # get the length of the test data
                test_len = len(test_data)
                assert dl_lt.size() == test_len
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                i = random.randint(test_len * -1, -1)
                j = random.randint(test_len + 1, test_len * 2)
                # # sample(range(test_len * 2, test_len * 3), 2)
                # # force an exception in the sublist method
                with pytest.raises(Exception) as excinfo:
                    dl_lt.sublist(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # # test for the exception message
                assert "Invalid range: between" in str(excinfo.value)

                # select a random valid a low index in the test data
                # low = random.randint(0, test_len - 1)
                low = random.randint(0, (test_len - 1) // 2)
                # select a random valid a high index in the test data
                high = random.randint(low, test_len - 1)
                # get the elements in the test data
                sub_lt = list()
                i = low
                while i != high + 1:
                    sub_lt.append(test_data[i])
                    i += 1
                # get the elements size in the test data
                sub_lt_size = len(sub_lt)
                # create a sublist with the low and high index
                sub_sl_lt = dl_lt.sublist(low, high)
                # test for the sublist size is an DoubleLinked
                assert isinstance(sub_sl_lt, DoubleLinked)
                # test for the sublist size is equal to test_len
                assert sub_lt_size == sub_sl_lt.size()
                # test for the sublist elements are equal to sub_lt
                sub_sl_lt_data = self.dll_to_list(sub_sl_lt)
                assert sub_lt == sub_sl_lt_data

    def test_concat(self):
        """*test_concat()* prueba el método *concat()* de *DoubleLinked* con estructuras de datos no vacías. Comprueba las excepciones de *TypeError* para estructuras de datos no compatibles. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """

        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                dl_lt1 = DoubleLinked(iodata=test_data)
                # create a python list with the test data
                dl_lt2 = test_data.copy()

                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    dl_lt1.concat(dl_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                err_msg = "Structure is not an DoubleLinked:"
                assert err_msg in str(excinfo.value)

                # create a new DoubleLinked with the wrong key
                dl_lt2 = DoubleLinked(iodata=test_data,
                                      key="testid")
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    dl_lt1.concat(dl_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid key:" in str(excinfo.value)

                # create a new DoubleLinked with the wrong cmp function
                dl_lt2 = DoubleLinked(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    dl_lt1.concat(dl_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid compare function:" in str(excinfo.value)

                # create a new correct DoubleLinked with the test data
                dl_lt1 = DoubleLinked(iodata=test_data)
                dl_lt2 = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt1 = DoubleLinked(iodata=test_data,
                                          cmp_function=cmp_lt_test_function)
                    dl_lt2 = DoubleLinked(iodata=test_data,
                                          cmp_function=cmp_lt_test_function)
                # create the new concatenated DoubleLinked

                sl_lt1_data = self.dll_to_list(dl_lt1)
                sl_lt2_data = self.dll_to_list(dl_lt2)
                ans = dl_lt1.concat(dl_lt2)
                ans_data = self.dll_to_list(ans)

                assert isinstance(ans, DoubleLinked)
                assert ans.size() == len(sl_lt1_data) + len(sl_lt2_data)
                assert ans_data == sl_lt1_data + sl_lt2_data
                assert all((ans.key, dl_lt1.key, dl_lt2.key))
                assert all((ans.cmp_function,
                           dl_lt1.cmp_function,
                           dl_lt2.cmp_function))

    def test_iterator(self):
        """*test_iterator()* prueba el iterador *__iter__()* de *DoubleLinked* con estructuras de datos no vacías. También comprueba si los elementos se pueden iterar en conjunto con los elementos de otras estructuras de datos nativas de Python y que los elementos iterados sean iguales a los de la lista original.
        """
        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                test_len = len(test_data)
                dl_lt = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # iterates over the DoubleLinked and the test data and compare
                for element, data in zip(dl_lt, test_data):
                    # test for the element is equal to test_data
                    assert element == data
                    # test for the element type is equal to test_data
                    assert type(element) is type(data)
                # test for the iterator is exhausted and the StopIteration
                assert dl_lt.size() == test_len

    def test_reversed(self):
        """*test_reversed()* prueba el iterador invertido *__reversed__()* de *DoubleLinked* con estructuras de datos no vacías. También comprueba si los elementos se pueden iterar en conjunto con los elementos de otras estructuras de datos nativas de Python y que los elementos iterados sean iguales a los de la lista original.
        """
        # iterates over global params and create filled DoubleLinked
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new DoubleLinked with the test data
                test_len = len(test_data)
                dl_lt = DoubleLinked(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    dl_lt = DoubleLinked(iodata=test_data,
                                         cmp_function=cmp_lt_test_function)
                # iterates over the DoubleLinked and the test data and compare
                for element, data in zip(reversed(dl_lt), reversed(test_data)):
                    # test for the element is equal to test_data
                    assert element == data
                    # test for the element type is equal to test_data
                    assert type(element) is type(data)
                # test for the iterator is exhausted and the StopIteration
                assert dl_lt.size() == test_len
