"""
**test_dynamic_lists** es el módulo que prueba el funcionamiento del ADT dinámico y configurable *List* de *DISClib* y sus funciones complementarias *clone()* y *translate()*.

*NOTA:* *List* es auto-configurable gracias a la librería *Dynamic* de *DISClib*.
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.lists import List
from DISClib.ADT.lists import clone_lt
from DISClib.ADT.lists import translate_lt
from DISClib.ADT.lists import STRUCT_PGK_PATH

# import de data structures modules
from DISClib.DataStructures.arraylist import ArrayList
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.doublelinkedlist import DoubleLinked

# import the data to test
from Test.Data.test_data import get_lists_test_data
from Test.Data.test_data import get_list_test_data

# asserting module imports
assert List
assert clone_lt
assert translate_lt
assert get_lists_test_data
assert get_list_test_data

# list oi test dataclasses
# :param LIST_DSTYPE_LT
LIST_DSTYPE_LT = [
    ArrayList,
    SingleLinked,
    DoubleLinked,
]
"""
Lista de tipos de estructuras de datos para el ADT *List*. Pueden ser "ArrayList", "SingleLinked" o "DoubleLinked".
"""

# list of tgt test dataclasses
# :param TRANS_DSTYPE_LT
TRANS_DSTYPE_LT = [
    DoubleLinked,
    ArrayList,
    SingleLinked,
]
"""
Lista de tipos de estructuras de datos para el ADT *Map* objetivo y la función *clone_lt*. Pueden ser "ArrayList", "SingleLinked" o "DoubleLinked".
"""

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


class TestDynamicLists(unittest.TestCase):
    """**TestDynamicLists** es la clase que prueba el funcionamiento del ADT dinámico y configurable *List* de *DISClib* y sus funciones complementarias *clone_lt()* y *translate_lt()*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para las pruebas unitarias en Python.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *List* como un *fixture*.
        """
        self.global_params = get_lists_test_data()
        self.global_data = get_list_test_data()

    def test_List(self):
        """*test_List()* prueba como crear un ADT *List* dinámico con diferentes estructuras de datos.
        """
        # get the global parameters
        params = self.global_params
        root_package = params.get("TEST_ROOT_PGK_PATH")
        struct_dict = params.get("TEST_STRUCT_DICT")
        err_root_package = params.get("ERR_ROOT_PGK_PATH")
        err_struct_dict = params.get("ERR_STRUCT_DICT")

        # test for the correct root folder
        assert root_package == STRUCT_PGK_PATH
        assert err_root_package != STRUCT_PGK_PATH

        # iterate over error inducing structures
        for err_imp in err_struct_dict.keys():
            # force an exception in the get_element method
            with pytest.raises(Exception) as excinfo:
                List(dstruct=err_imp)
            # test for the exception type
            assert excinfo.type == ValueError
            # test for the exception message
            assert "Invalid implementation of" in str(excinfo.value)
            assert f"'{err_imp}' List type not found" in str(excinfo.value)

        # test for the correct implementations
        for tdsimp, tdstype in zip(struct_dict.keys(), LIST_DSTYPE_LT):
            test_lt = List(dstruct=tdsimp)
            # test for the correct implementation
            assert test_lt is not None
            assert isinstance(test_lt, tdstype)

    def test_clone_lt(self):
        """*test_clone()* prueba como clonar un ADT *List* dinámico con diferentes estructuras de datos.
        """
        # get the global parameters
        params = self.global_params
        data = self.global_data
        struct_dict = params.get("TEST_STRUCT_DICT")
        struct_key_lt = struct_dict.keys()
        data_type_lt = data.get("CHECK_TYPE_LT")
        test_data_lt = data.keys()

        # iterare over the test structures
        for tdsimp, tdstype in zip(struct_key_lt, LIST_DSTYPE_LT):
            # test_lt = List(dstruct=tdsimp)
            # iterate over the test data inside de structures
            for key, dtype in zip(test_data_lt, data_type_lt):
                if key not in IGNORE_KEYS_LT:
                    # get the test data
                    test_data = data.get(key)
                    # create the list
                    og_lt = List(dstruct=tdsimp,
                                 iodata=test_data)
                    # test the list is not none
                    assert og_lt is not None
                    # test the list is the correct data structure
                    assert isinstance(og_lt, tdstype)
                    # test the list match the size of the test data
                    assert og_lt.size() == len(test_data)
                    # test the first element of the list
                    assert og_lt.get_first() == test_data[0]
                    # test the first element is the correct type
                    assert isinstance(og_lt.get_first(), dtype)

                    # clone the list
                    cl_lt = clone_lt(og_lt)
                    # test the clone list is not none
                    assert cl_lt is not None
                    # test the clone list is the correct data structure
                    assert isinstance(cl_lt, tdstype)
                    # test the clone list match the size of the test data
                    assert cl_lt.size() == len(test_data)
                    # test the clone list first element
                    assert cl_lt.get_first() == test_data[0]
                    # test the clone list first element is the correct type
                    assert isinstance(cl_lt.get_first(), dtype)

                    # test cmp_function
                    assert og_lt.cmp_function == cl_lt.cmp_function
                    # test key
                    assert og_lt.key == cl_lt.key

                    # iterate both lists
                    for og, cl in zip(og_lt, cl_lt):
                        # test the elements are the same
                        assert og == cl
                        # test the elements are the correct type
                        assert isinstance(og, dtype)
                        assert isinstance(cl, dtype)

        # iterate over the test data inside de structures
        for key in test_data_lt:
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = data.get(key)
                # create the list
                og_lt = list(test_data)
                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    clone_lt(og_lt)
                # test for the exception type
                assert excinfo.type == ValueError
                # test for the exception message
                src_type = type(og_lt).__name__
                err_msg = f"Unable to clone List, '{src_type}' type not found"
                assert err_msg in str(excinfo.value)

    def test_translate_lt(self):
        """*test_translate()* prueba transformar un ADT *List* dinámico con diferentes estructuras de datos. Es decir, de una estructura de datos a otra, ejemplo: de *ArrayList* a *SingleLinked*.
        """
        # get the global parameters
        params = self.global_params
        data = self.global_data
        src_struct_dict = params.get("TEST_STRUCT_DICT")
        tgt_struct_dict = params.get("TEST_TGT_STRUCT_DICT")
        src_struct_key_lt = src_struct_dict.keys()
        tgt_struct_key_lt = tgt_struct_dict.keys()
        data_type_lt = data.get("CHECK_TYPE_LT")
        test_data_lt = data.keys()
        err_struct_dict = params.get("ERR_STRUCT_DICT")
        err_struct_key_lt = err_struct_dict.keys()

        # iterare over the test structures
        zipped_lt = zip(src_struct_key_lt,
                        tgt_struct_key_lt,
                        LIST_DSTYPE_LT,
                        TRANS_DSTYPE_LT)
        # iterate over the test structures
        for src_imp, tgt_imp, dstype, cdstype in zipped_lt:
            # iterate over the test data inside de structures
            for key, dtype in zip(test_data_lt, data_type_lt):
                if key not in IGNORE_KEYS_LT:
                    # get the test data
                    test_data = data.get(key)
                    # create the list
                    src_lt = List(dstruct=src_imp,
                                  iodata=test_data)
                    # translate the list
                    tgt_lt = translate_lt(src_lt, tgt_imp)
                    # test the list is not none
                    assert src_lt is not None
                    # test the translate list is not none
                    assert tgt_lt is not None

                    # test the list is the correct data structure
                    assert isinstance(src_lt, dstype)
                    # test the list match the size of the test data
                    assert src_lt.size() == len(test_data)
                    # test the first element of the list
                    assert src_lt.get_first() == test_data[0]
                    # test the first element is the correct type
                    assert isinstance(src_lt.get_first(), dtype)

                    # test the translate list is the correct data structure
                    assert isinstance(tgt_lt, cdstype)
                    # test the translate list match the size of the test data
                    assert tgt_lt.size() == len(test_data)
                    # test the translate list first element
                    assert tgt_lt.get_first() == test_data[0]
                    # test the translate list first element is the correct type
                    assert isinstance(tgt_lt.get_first(), dtype)

                    # test cmp_function is the same
                    assert src_lt.cmp_function == tgt_lt.cmp_function
                    # test key is the same
                    assert src_lt.key == tgt_lt.key

                    for src, tgt in zip(src_lt, tgt_lt):
                        # test the elements are the same
                        assert src == tgt
                        # test the elements are the correct type
                        assert isinstance(src, dtype)
                        assert isinstance(tgt, dtype)

        # error inducing structures
        zipped = zip(src_struct_key_lt,
                     err_struct_key_lt,)
        for src_imp, err_imp in zipped:
            # iterate over the test data inside de structures
            for key, dtype in zip(test_data_lt, data_type_lt):
                if key not in IGNORE_KEYS_LT:
                    # get the test data
                    test_data = data.get(key)
                    # create the list
                    src_lt = List(dstruct=src_imp,
                                  iodata=test_data)
                    # force an exception in the get_element method
                    with pytest.raises(Exception) as excinfo:
                        translate_lt(src_lt, err_imp)
                    # test for the exception type
                    assert excinfo.type == ValueError
                    # test for the exception message
                    assert "Invalid implementation of" in str(excinfo.value)
                    err_msg = f"Unable to translate List '{src_imp}', "
                    err_msg += f"'{err_imp}' List type not found"
                    assert err_msg in str(excinfo.value)
