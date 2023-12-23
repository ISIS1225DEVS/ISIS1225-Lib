"""
*test_dynamic_lists.py* es el módulo que prueba el ADT dinámico y configurable *List* de *DISClib* y sus funciones complementarias *clone()* y *translate()*.
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.lists import List
from DISClib.ADT.lists import clone
from DISClib.ADT.lists import translate


# import the data to test
from Test.Data.test_data import get_dynalist_test_data

# asserting module imports
assert List
assert clone
assert translate
assert get_dynalist_test_data


class TestDynamicList(unittest.TestCase):
    """TestDynamicList _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *List* como un *fixture*.
        """
        self.global_params = get_dynalist_test_data()

    def test_List(self):
        """*test_List()* prueba la creación de una lista dinámica.
        """
        # get the global parameters
        # params = self.global_params

        # create the list
        pass

    def test_clone(self):
        """*test_clone()* prueba la clonación de una lista dinámica.
        """
        # get the global parameters
        # params = self.global_params

        # create the list
        pass

    def test_translate(self):
        """*test_translate()* prueba la traducción de una lista dinámica.
        """
        # get the global parameters
        # params = self.global_params

        # create the list
        pass
