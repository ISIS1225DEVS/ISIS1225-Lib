"""
**test_dynamic_maps** es el módulo que prueba el funcionamiento del ADT dinámico y configurable *Map* de *DISClib* y sus funciones complementarias *clone_mp()* y *translate_mp()*.

*NOTA:* *List* es auto-configurable gracias a la librería *Dynamic* de *DISClib*.
"""
# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.maps import Map
from DISClib.ADT.maps import clone_mp
from DISClib.ADT.maps import translate_mp

# import de data structures modules
from DISClib.DataStructures.chaininghashtable import SeparateChaining
from DISClib.DataStructures.probinghashtable import LinearProbing

# import the data to test
from Test.Data.test_data import get_graphs_test_data

# asserting module imports
assert Map
assert clone_mp
assert translate_mp
assert get_graphs_test_data


class TestDynamicMaps(unittest.TestCase):
    """TestDynamicMaps _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Map* como un *fixture*.
        """
        self.global_params = get_graphs_test_data()

    def test_Map(self):
        """*test_Map()* prueba la creación de un mapa dinámico.
        """
        # get the global parameters
        # params = self.global_params

        # create the map
        pass

    def test_clone_mp(self):
        """*test_clone_mp()* prueba la clonación de un mapa dinámico.
        """
        # get the global parameters
        # params = self.global_params

        # create the map
        pass

    def test_translate_mp(self):
        """*test_translate_mp()* prueba la traducción de un mapa dinámico.
        """
        # get the global parameters
        # params = self.global_params

        # create the map
        pass
