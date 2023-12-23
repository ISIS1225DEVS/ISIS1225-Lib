"""
*test_struct_mapentry.py* es el módulo que prueba la estructura de datos *MapEntry* para el ADT dinámico y configurable *Map*.
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.DataStructures.mapentry import MapEntry

# import the data to test
from Test.Data.test_data import get_mapentry_test_data

# asserting module imports
assert MapEntry
assert get_mapentry_test_data


class testMapEntry(unittest.TestCase):
    """TestMapEntry _summary_

    Args:
        unittest (_type_): _description_
    """
    # TODO add spanish docstring

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """inject_fixtures _summary_

        Args:
            capsys (_type_): _description_
        """
        # TODO add spanish docstring
        self.global_params = get_mapentry_test_data()

    def test_new_default_entry(self):
        """test_new_default_entry _summary_
        """
        entry = MapEntry()
        assert entry is not None
        assert entry.get_key() is None
        assert entry.get_value() is None

    def test_new_custom_entry(self):
        """test_new_custom_entry _summary_
        """
        entry = MapEntry(self.global_params["key"], self.global_params["value"])
        assert entry is not None
        assert entry.get_key() == self.global_params["key"]
        assert entry.get_value() == self.global_params["value"]

    def test_set_key(self):
        """test_set_key _summary_
        """
        entry = MapEntry()
        entry.set_key(self.global_params["key"])
        assert entry.get_key() == self.global_params["key"] 
    
    def test_set_value(self):
        """test_set_value _summary_
        """
        entry = MapEntry()
        entry.set_value(self.global_params["value"])
        assert entry.get_value() == self.global_params["value"]
    
    def test_get_key(self):
        """test_get_key _summary_
        """
        entry = MapEntry()
        entry.set_key(self.global_params["key"])
        assert entry.get_key() == self.global_params["key"]
    
    def test_get_value(self):
        """test_get_value _summary_
        """
        entry = MapEntry()
        entry.set_value(self.global_params["value"])
        assert entry.get_value() == self.global_params["value"]
    
    def test_check_key_type(self):
        """test_check_key_type _summary_
        """
        entry = MapEntry()
        assert entry._check_key_type(self.global_params["key"]) == True
    
    def test_check_value_type(self):
        """test_check_value_type _summary_
        """
        entry = MapEntry()
        assert entry._check_value_type(self.global_params["value"]) == True
        
        