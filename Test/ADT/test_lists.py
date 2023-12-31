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

# list test parameters
# :param list_type_lt
list_dstype_lt = [
    ArrayList,
    SingleLinked,
    DoubleLinked
]
"""
Lista de tipos de estructuras de datos para el ADT List. Pueden ser "ArrayList", "SingleLinked" o "DoubleLinked".
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
    """TestDynamicLists _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *List* como un *fixture*.
        """
        self.global_params = get_lists_test_data()
        self.global_data = get_list_test_data()

    def test_List(self):
        """*test_List()* prueba la creación de una lista dinámica.
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

        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            for err_imp in err_struct_dict.keys():
                List(dstruct=err_imp)
        # test for the exception type
        assert excinfo.type == ValueError
        # test for the exception message
        assert "Invalid implementation of" in str(excinfo.value)
        assert f"List type '{err_imp}' not found" in str(excinfo.value)

        # test for the correct implementations
        for tdsimp, tdstype in zip(struct_dict.keys(), list_dstype_lt):
            test_lt = List(dstruct=tdsimp)
            # test for the correct implementation
            assert test_lt is not None
            assert isinstance(test_lt, tdstype)

    def test_clone_lt(self):
        """*test_clone()* prueba la clonación de una lista dinámica.
        """
        # get the global parameters
        params = self.global_params
        data = self.global_data
        struct_dict = params.get("TEST_STRUCT_DICT")
        struct_key_lt = struct_dict.keys()
        data_type_lt = data.get("CHECK_TYPE_LT")
        test_data_lt = data.keys()

        # iterare over the test structures
        for tdsimp, tdstype in zip(struct_key_lt, list_dstype_lt):
            # test_lt = List(dstruct=tdsimp)
            # iterate over the test data inside de structures
            for key, dtype in zip(test_data_lt, data_type_lt):
                if key not in IGNORE_KEYS_LT:
                    # get the test data
                    test_data = data.get(key)
                    # create the list
                    src_lt = List(dstruct=tdsimp,
                                  iodata=test_data)
                    # test the list is not none
                    assert src_lt is not None
                    # test the list is the correct data structure
                    assert isinstance(src_lt, tdstype)
                    # test the list match the size of the test data
                    assert src_lt.size() == len(test_data)
                    # test the first element of the list
                    assert src_lt.get_first() == test_data[0]
                    # test the first element is the correct type
                    assert isinstance(src_lt.get_first(), dtype)

                    # clone the list
                    tgt_lt = clone_lt(src_lt)
                    # test the clone list is not none
                    assert tgt_lt is not None
                    # test the clone list is the correct data structure
                    assert isinstance(tgt_lt, tdstype)
                    # test the clone list match the size of the test data
                    assert tgt_lt.size() == len(test_data)
                    # test the clone list first element
                    assert tgt_lt.get_first() == test_data[0]
                    # test the clone list first element is the correct type
                    assert isinstance(tgt_lt.get_first(), dtype)
                    # iterate both lists
                    for src, tgt in zip(src_lt, tgt_lt):
                        # test the elements are the same
                        assert src == tgt
                        # test the elements are the correct type
                        assert isinstance(src, dtype)
                        assert isinstance(tgt, dtype)

    def test_translate_lt(self):
        """*test_translate()* prueba la traducción de una lista dinámica.
        """
        # get the global parameters
        # params = self.global_params

        # create the list
        pass
