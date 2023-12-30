"""
**test_dynamic_import** es el módulo que prueba la libreria para configurar dinámicamente los ADTs en *DISClib*.
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.dynamic import DynamicImporter

# import the data to test
from Test.Data.test_data import get_dynamic_test_data
from Test.ADT.Mocks.mstructa import DataStructA
from Test.ADT.Mocks.mstructb import DataStructB

# asserting module imports
assert DynamicImporter
assert get_dynamic_test_data
assert DataStructA
assert DataStructB

# global test parameters
struct_type_lt = [
    DataStructA,
    DataStructB
]


class TestDynamicImporter(unittest.TestCase):
    """**TestDynamicImporter** prueba la libreria para configurar dinámicamente los ADTs en *DISClib*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Dynamic* como un *fixture*.
        """
        self.global_params = get_dynamic_test_data()

    def test_dynamic_importer(self):
        """*test_dynamic_importer()* prueba la importación dinámica de un módulo y una clase de un módulo.
        """
        # get the global parameters
        params = self.global_params
        root_package = params.get("TEST_ROOT_PGK_PATH")
        t_struct_dict = params.get("TEST_STRUCT_DICT")
        err_root_package = params.get("ERR_ROOT_PGK_PATH")
        err_struct_dict = params.get("ERR_STRUCT_DICT")

        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            for err_imp in err_struct_dict.keys():
                err_struct = err_struct_dict.get(err_imp)
                err_package = f"{err_root_package}.{err_struct}"
                dynamic = DynamicImporter(package=err_package,
                                          implementation=err_imp)
        # test for the exception type
        assert excinfo.type == ValueError
        # test for the exception message
        assert "Invalid implementation of" in str(excinfo.value)

        # iterate over the test structures
        for dsimp, dstype in zip(t_struct_dict.keys(), struct_type_lt):
            # get the test structure module
            t_struct = t_struct_dict.get(dsimp)
            # complete the package path for the test structure
            t_package = f"{root_package}.{t_struct}"
            # invoke the dynamic importer
            dynamic = DynamicImporter(package=t_package,
                                      implementation=dsimp)
            # test the dynamic importer is filled and the correct type
            assert dynamic is not None
            assert isinstance(dynamic, DynamicImporter)
            assert dynamic._module is not None
            assert dynamic._class is not None
            assert dynamic._instance is not None
            # test the dynamic importer has datastruct instance
            assert isinstance(dynamic._instance, dstype)

    def test_get_instance(self):
        """test_get_instance _summary_
        """
        # get the global parameters
        params = self.global_params
        root_package = params.get("TEST_ROOT_PGK_PATH")
        t_struct_dict = params.get("TEST_STRUCT_DICT")

        for dsimp, dstype in zip(t_struct_dict.keys(), struct_type_lt):
            # get the test structure module
            t_struct = t_struct_dict.get(dsimp)
            # complete the package path for the test structure
            t_package = f"{root_package}.{t_struct}"
            # invoke the dynamic importer
            dynamic = DynamicImporter(package=t_package,
                                      implementation=dsimp)
            tinstance = dynamic.get_instance()
            # test the dynamic importer is filled and the correct type
            assert tinstance is not None
            assert dynamic._module is not None
            assert dynamic._class is not None
            assert dynamic._instance is not None
            # test the dynamic importer has datastruct instance
            assert isinstance(dynamic._instance, dstype)
            assert isinstance(tinstance, dstype)
