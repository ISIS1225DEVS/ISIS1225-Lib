"""
*test_adt_stack.py* es el módulo que prueba el ADT *Stack* (pila) de *DISClib* basado en una lista sencillamente encadenada (SinglyLinked).
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.stack import Stack

# import the data to test
from Test.Data.test_data import get_list_test_data

# asserting module imports
assert Stack
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
    """*cmp_lt_test_function()* compara dos elementos en una lista (ArrayList, SingleLinked, Stack). Solo funciona con diccionarios con una llave "uuid".

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


class TestStack(unittest.TestCase):
    """*TestStack* clase *unittest* para probar la clase *Stack* de *DISCLib*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Stack* como un *fixture*.
        """

        self.global_params = get_list_test_data()
        # FIXME do we need this? is this okey?
        TEST_ARRAY_LIST_LT = list()
        for i in self.global_params.get("TEST_INT_LT"):
            temp_lt = self.global_params.get("TEST_DICT_LT")
            tal = Stack(temp_lt)
            TEST_ARRAY_LIST_LT.append(tal)
        self.global_params["TEST_AL_LT"] = TEST_ARRAY_LIST_LT

    def dll_to_list(self, st_adt: Stack) -> list:
        """*dll_to_list()* convierte una lista sencillamente encadenada nativa de *DISCLib* en una lista nativa de Python.

        Args:
            st_adt (Stack): Lista sencillamente encadenada nativa de *DISCLib* a convertir en lista nativa de Python.

        Returns:
            list: lista nativa de Python traducida.
        """
        ans = list()
        for elm in st_adt:
            ans.append(elm)
        return ans

    def test_default_stack(self):
        """*test_default_stack()* prueba la inicialización de una lista sencillamente encadenada o *Stack* vacía.
        """
        # Test an empty Stack
        st_adt = Stack()
        # Test if Stack is not None
        assert st_adt is not None
        # Test if Stack is empty
        assert st_adt._size == -1
        # Test if the Stack first element is empty
        assert st_adt._header.get_info() is None
        # Test if the Stack last element is empty
        assert st_adt._trailer.get_info() is None
        # Test if Stack key is "id"
        assert st_adt.key == "id"
        # Test if Stack cmp_function is the default
        assert st_adt.cmp_function == st_adt.default_cmp_function
        # Test if list is an instance of Stack
        assert isinstance(st_adt, Stack)

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de comparación predeterminada de *Stack* con diferentes tipos de elementos.
        """
        # create a new empty Stack with the default cmp function
        st_adt = Stack()
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
                        res1 = st_adt.default_cmp_function(ce, pe) in exp_res
                        res2 = st_adt.default_cmp_function(ce, ce) in exp_res
                        res3 = st_adt.default_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_stack(self):
        """*test_custom_stack()* prueba la inicialización de una *Stack* personalizada con elementos de diferentes tipos.
        """
        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new Stack with the test data
                st_adt = Stack(iodata=test_data)
                # testing Stack is not None
                assert st_adt is not None
                # testing Stack elements is equal to test_data
                sl_lt_data = self.dll_to_list(st_adt)
                assert sl_lt_data == test_data
                # testing Stack key is "id"
                assert st_adt.key == "id"
                # testing Stack cmp_function is the default
                assert st_adt.cmp_function == st_adt.default_cmp_function
                # testing Stack is an instance of Stack
                assert isinstance(st_adt, Stack)
                # testing Stack elements are of the same type
                assert isinstance(st_adt._header.next().get_info(), data_type)
                # testing Stack size is equal to test_data
                assert st_adt._size == len(test_data)

    def test_custom_key(self):
        """*test_custom_key()* prueba la inicialización de una *Stack* personalizada con elementos y una llave personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                st_adt = Stack(iodata=test_data,
                               key="uuid")
                # testing Stack is not None
                assert st_adt is not None
                # testing Stack size is equal to test_data
                assert st_adt._size == len(test_data)
                # testing Stack elements is equal to test_data
                sl_lt_data = self.dll_to_list(st_adt)
                assert sl_lt_data == test_data
                # testing Stack key is "uuid"
                assert st_adt.key == "uuid"
                # testing Stack cmp_function is the default
                assert st_adt.cmp_function == st_adt.default_cmp_function
                # testing Stack is an instance of Stack
                assert isinstance(st_adt, Stack)
                # testing Stack elements are of the same type
                assert isinstance(st_adt._header.next().get_info(), dtype)

    def test_custom_cmp_function(self):
        """*test_custom_cmp_function()* prueba la inicialización de una *Stack* personalizada con elementos de diferentes tipos y una función de comparación personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                st_adt = Stack(iodata=test_data,
                               cmp_function=cmp_lt_test_function)
                # testing Stack is not None
                assert st_adt is not None
                # testing Stack size is equal to test_data
                assert st_adt._size == len(test_data)
                # testing Stack elements is equal to test_data
                sl_lt_data = self.dll_to_list(st_adt)
                assert sl_lt_data == test_data
                # testing Stack key is the default "id"
                assert st_adt.key == "id"
                # testing Stack cmp_function is the custom function
                assert st_adt.cmp_function == cmp_lt_test_function
                # testing Stack is an instance of Stack
                assert isinstance(st_adt, Stack)
                # testing Stack elements are of the same type
                assert isinstance(st_adt._header.next().get_info(), dtype)

    def test_size(self):
        """*test_size()* prueba el método *size()* de *Stack* con estructuras de datos vacías y no vacías.
        """
        # create a new empty Stack
        st_adt = Stack()
        # testing Stack size is 0 with size method
        assert st_adt.size() == 0
        # testing Stack size is 0 with _size attribute
        assert st_adt._size == -1
        # check if the Stack elements is empty
        sl_lt_data = self.dll_to_list(st_adt)
        assert sl_lt_data == []

        # iterates over global params and create filled Stack
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # create a new Stack with the test data
                st_adt = Stack(iodata=test_data)
                # testing Stack size() is equal to test_data
                assert st_adt.size() == len(test_data)
                # testing Stack _size is equal to test_data
                assert st_adt._size == len(test_data)
                # # testing Stack elements is equal to test_data
                sl_lt_data = self.dll_to_list(st_adt)
                assert sl_lt_data == test_data

    def test_is_empty(self):
        """*test_is_empty()* prueba el método *is_empty()* de *Stack* con estructuras de datos vacías y no vacías.
        """

        # create a new empty Stack
        st_adt = Stack()
        # testing Stack is empty
        assert st_adt.is_empty() is True
        # testing Stack elements is empty
        sl_lt_data = self.dll_to_list(st_adt)
        assert sl_lt_data == []

        # iterates over global params and create filled Stack
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Stack with the test data
                st_adt = Stack(iodata=test_data)
                # testing Stack is not empty
                assert st_adt.is_empty() is False
                # testing Stack elements is equal to test_data
                sl_lt_data = self.dll_to_list(st_adt)
                assert sl_lt_data == test_data

    def test_push(self):
        """*test_push()* prueba el método *add_last()* de *Stack* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si los elementos agregados son iguales al índice dentro de *Stack*.
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
                # create a new Stack with the test data
                with pytest.raises(TypeError) as excinfo:
                    st_adt = Stack(test_data)
                    # induce the error by adding an element of a different type
                    st_adt.add_last(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_lat method normal behavior
                st_adt = Stack()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the Stack
                    st_adt.push(t_data)
                    # get the first element of the Stack
                    t_elem1 = st_adt.top()
                    t_elem2 = st_adt._trailer.prev().get_info()
                    # testing Stack top() is equal to test_data
                    assert t_elem1 == t_data and t_elem2 == t_data
                    # test if the Stack size is equal to test_len
                    assert (st_adt.size() == i + 1)

    def test_pop(self):
        """*test_pop()* prueba el método *pop()* de *Stack* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice."""
        # create a new empty Stack
        st_adt = Stack()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            st_adt.pop()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Stack
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Stack with the test data
                st_adt = Stack(iodata=test_data)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the last element of the test data

                    t_data = test_data[test_len - 1 - i]
                    # remove the last element of the Stack
                    t_elem3 = st_adt.get_last()
                    t_elem2 = st_adt._trailer.prev().get_info()
                    t_elem1 = st_adt.pop()
                    # test if the removed element is equal to the last
                    data_elem_lt = (
                        t_elem1 == t_elem2,
                        t_elem2 == t_elem3,
                        t_elem3 == t_data
                    )
                    assert all(data_elem_lt)
                    # test if the Stack size is equal to test_len
                    assert (st_adt.size() == (test_len - i - 1))

    def test_top(self):
        """test_top _summary_
        """
        # get the global parameters
        # params = self.global_params

        """*test_top()* prueba el método *top()* de *Stack* con estructuras de datos vacías y no vacías. Comprueba las excepciones de *IndexError*. También comprueba si el elemento recuperado es igual al índice de *Stack*.
        """
        # create a new empty Stack
        st_adt = Stack()
        # force an exception in the top method
        with pytest.raises(Exception) as excinfo:
            st_adt.top()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Stack
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Stack with the test data
                st_adt = Stack(iodata=test_data)
                # get the last element of the Stack
                t_elem3 = st_adt.get_last()
                t_elem2 = st_adt._trailer.prev().get_info()
                t_elem1 = st_adt.top()
                # test if the removed element is equal to the last
                data_elem_lt = (
                    t_elem1 == t_elem2,
                    t_elem2 == t_elem3,
                    t_elem3 == test_data[-1]
                )
                # testing Stack top() is equal to test_data
                assert all(data_elem_lt)
                # test if Stack size() is equal to test_len
                assert (st_adt.size() == test_len)
