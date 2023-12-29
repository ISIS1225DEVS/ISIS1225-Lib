"""
**test_adt_queue** es el módulo que prueba el ADT *Queue* (cola) de *DISClib* basado en una lista doblemente encadenada (DoubleLinked).
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.queue import Queue

# import the data to test
from Test.Data.test_data import get_list_test_data

# asserting module imports
assert Queue
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
    """*cmp_lt_test_function()* función de comparación personalizada para probar la función de las estructuras de tipo listas (*ArrayList*, *SingleLinked*, *DoubleLinked*). Solo funciona con diccionarios con una llave "uuid".

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


class TestQueue(unittest.TestCase):
    """**TestQueue** implementa las pruebas unitarias para el ADT *Queue* (cola) de *DISClib* basado en una lista doblemente encadenada (*DoubleLinked*).

    Args:
        unittest (TestCase): clase *unittest.TestCase* para las pruebas unitarias en Python.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Queue* como un *fixture*.
        """
        self.global_params = get_list_test_data()
        TEST_ARRAY_LIST_LT = list()
        for i in self.global_params.get("TEST_INT_LT"):
            temp_lt = self.global_params.get("TEST_DICT_LT")
            tal = Queue(temp_lt)
            TEST_ARRAY_LIST_LT.append(tal)
        self.global_params["TEST_AL_LT"] = TEST_ARRAY_LIST_LT

    def sll_to_list(self, qu_adt: Queue) -> list:
        """*sll_to_list()* convierte una lista sencillamente encadenada nativa de *DISCLib* en una lista nativa de Python.

        Args:
            sl_lt (SingleLinked): Lista sencillamente encadenada nativa de *DISCLib* para convertir en lista nativa de Python.

        Returns:
            list: lista nativa de Python traducida.
        """
        ans = list()
        for elm in qu_adt:
            ans.append(elm)
        return ans

    def test_default_queue(self):
        """*test_default_queue()* prueba para crear una cola vacía con los valores predeterminados de *Queue*.
        """
        # Test an empty Queue
        qu_adt = Queue()
        # Test if Queue is not None
        assert qu_adt is not None
        # Test if Queue is empty
        assert qu_adt._size == 0
        # Test if the Queue first element is empty
        assert qu_adt.first is None
        # Test if the Queue last element is empty
        assert qu_adt.last is None
        # Test if Queue key is "id"
        assert qu_adt.key == "id"
        # Test if Queue cmp_function is the default
        assert qu_adt.cmp_function == qu_adt.default_cmp_function
        # Test if list is an instance of Queue
        assert isinstance(qu_adt, Queue)

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba para la función de comparación predeterminada de *Queue* con diferentes tipos de datos.
        """
        # create a new empty Queue with the default cmp function
        qu_adt = Queue()
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
                        res1 = qu_adt.default_cmp_function(ce, pe) in exp_res
                        res2 = qu_adt.default_cmp_function(ce, ce) in exp_res
                        res3 = qu_adt.default_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_queue(self):
        """*test_custom_queue()* prueba para crear un *Queue* personalizado con elementos y valores predeterminados.
        """
        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new Queue with the test data
                qu_adt = Queue(iodata=test_data)
                # testing Queue is not None
                assert qu_adt is not None
                # testing Queue elements is equal to test_data
                qu_adt_data = self.sll_to_list(qu_adt)
                assert qu_adt_data == test_data
                # testing Queue key is "id"
                assert qu_adt.key == "id"
                # testing Queue cmp_function is the default
                assert qu_adt.cmp_function == qu_adt.default_cmp_function
                # testing Queue is an instance of Queue
                assert isinstance(qu_adt, Queue)
                # testing Queue elements are of the same type
                assert isinstance(qu_adt.first.get_info(), data_type)
                # testing Queue size is equal to test_data
                assert qu_adt._size == len(test_data)

    def test_custom_key(self):
        """*test_custom_key()* prueba para crear un *Queue* con elementos y una llave personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                qu_adt = Queue(iodata=test_data,
                               key="uuid")
                # testing Queue is not None
                assert qu_adt is not None
                # testing Queue size is equal to test_data
                assert qu_adt._size == len(test_data)
                # testing Queue elements is equal to test_data
                qu_adt_data = self.sll_to_list(qu_adt)
                assert qu_adt_data == test_data
                # testing Queue key is "uuid"
                assert qu_adt.key == "uuid"
                # testing Queue cmp_function is the default
                assert qu_adt.cmp_function == qu_adt.default_cmp_function
                # testing Queue is an instance of Queue
                assert isinstance(qu_adt, Queue)
                # testing Queue elements are of the same type
                assert isinstance(qu_adt.first.get_info(), dtype)

    def test_custom_cmp_function(self):
        """*test_custom_cmp_function()* prueba para crear un *Queue* con elementos y una función de comparación personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                qu_adt = Queue(iodata=test_data,
                               cmp_function=cmp_lt_test_function)
                # testing Queue is not None
                assert qu_adt is not None
                # testing Queue size is equal to test_data
                assert qu_adt._size == len(test_data)
                # testing Queue elements is equal to test_data
                qu_adt_data = self.sll_to_list(qu_adt)
                assert qu_adt_data == test_data
                # testing Queue key is the default "id"
                assert qu_adt.key == "id"
                # testing Queue cmp_function is the custom function
                assert qu_adt.cmp_function == cmp_lt_test_function
                # testing Queue is an instance of Queue
                assert isinstance(qu_adt, Queue)
                # testing Queue elements are of the same type
                assert isinstance(qu_adt.first.get_info(), dtype)

    def test_enqueue(self):
        """*test_enqueue()* prueba para encolar o agregar elementos al ADT *Queue* utilizando la funcion *enqueue()*.
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
                # create a new Queue with the test data
                with pytest.raises(TypeError) as excinfo:
                    qu_adt = Queue(test_data)
                    # induce the error by adding an element of a different type
                    qu_adt.enqueue(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_lat method normal behavior
                qu_adt = Queue()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the Queue
                    qu_adt.enqueue(t_data)
                    # get the first element of the Queue
                    t_elem1 = qu_adt.get_last()
                    t_elem2 = qu_adt.last.get_info()
                    # test if the removed element is equal to the last
                    c1 = (t_elem1 == t_elem2)
                    c2 = (t_elem2 == t_data)
                    # testing Queue enqueue() is equal to test_data
                    assert c1 and c2
                    # test if the Queue size is equal to test_len
                    assert (qu_adt.size() == i + 1)

    def test_dequeue(self):
        """*test_dequeue()* prueba para desencolar o remover elementos de la cola *Queue* utilizando la función *dequeue()*.
        """
        # create a new empty Queue
        qu_adt = Queue()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            qu_adt.dequeue()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Queue
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Queue with the test data
                qu_adt = Queue(iodata=test_data)
                for i in range(0, len(test_data) - 1):
                    t_data = test_data[i]
                    # get the last element of the Queue
                    t_elem3 = qu_adt.get_first()
                    t_elem2 = qu_adt.first.get_info()
                    t_elem1 = qu_adt.dequeue()
                    # test if the removed element is equal to the last
                    c1 = (t_elem1 == t_elem2)
                    c2 = (t_elem2 == t_elem3)
                    c3 = (t_elem3 == t_data)
                    # testing Queue dequeue() is equal to test_data
                    assert c1 and c2 and c3
                    # test if the Queue size is equal to test_len
                    assert (qu_adt.size() == (test_len - i - 1))

    def test_peek(self):
        """*test_peek()* prueba para leer el primer elemento de la cola *Queue* utilizando la función *peek()*.
        """
        # create a new empty Queue
        qu_adt = Queue()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            qu_adt.peek()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Queue
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Queue with the test data
                qu_adt = Queue(iodata=test_data)
                # get the last element of the Queue
                t_elem3 = qu_adt.get_first()
                t_elem2 = qu_adt.first.get_info()
                t_elem1 = qu_adt.peek()
                # test if the removed element is equal to the last
                c1 = (t_elem1 == t_elem2)
                c2 = (t_elem2 == t_elem3)
                c3 = (t_elem3 == test_data[0])
                # testing Queue peek() is equal to test_data
                assert c1 and c2 and c3
                # test if Queue size() is equal to test_len
                assert (qu_adt.size() == test_len)
