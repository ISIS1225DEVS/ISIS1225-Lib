"""
*test_dynamic_import.py* es el módulo que prueba la libreria para configurar dinámicamente los ADTs de *DISClib*.
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.dynamic import DynamicImporter

# import the data to test
from Test.Data.test_data import get_dynamic_test_data

# asserting module imports
assert DynamicImporter
assert get_dynamic_test_data


class TestDynamicImporter(unittest.TestCase):
    """TestDynamicImporter _summary_

    Args:
        unittest (_type_): _description_
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

        # get the dynamic importer
        dynamic_importer = DynamicImporter(
            implementation=params["implementation"],
            package=params["package"]
        )

        # assert the dynamic importer
        assert dynamic_importer
        assert dynamic_importer.package == params["package"]
        assert dynamic_importer.implementation == params["implementation"]

    def test_repr(self):
        """test_repr _summary_
        """
        pass

    def test_get_instance(self):
        """test_get_instance _summary_
        """
        pass

    def test_class(self):
        """test_class _summary_
        """
        pass

    def test_instance_check(self):
        """test_instancecheck _summary_
        """
        pass
