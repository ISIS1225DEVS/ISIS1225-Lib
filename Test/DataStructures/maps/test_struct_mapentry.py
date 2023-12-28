"""
*test_struct_mapentry* es el módulo que prueba la estructura de datos **MapEntry** (en TestMapEntry) para el ADT dinámico y configurable **Map**.
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
        unittest (TestCase): clase *unittest.TestCase* para pruebas unitarias.
    """
    # TODO add spanish docstring

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *MapEntry* como un *fixture*.
        """
        self.global_params = get_mapentry_test_data()

    def test_new_default_entry(self):
        """*test_new_default_entry()* prueba para crear de un nuevo registro (pareja llave-valor) de mapa con valores por defecto.
        """
        entry = MapEntry()
        assert entry is not None
        assert (entry.get_key()) is None and (entry._key is None)
        assert (entry.get_value() is None) and (entry._value is None)

    def test_new_custom_entry(self):
        """*test_new_custom_entry()* prueba para crear de un nuevo registro (pareja llave-valor) *MapEntry* con valores personalizados.
        """
        # getting the global params
        dtypes_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params and create custom entries
        for key, dtype in zip(self.global_params.keys(), dtypes_lt):
            # ignore 2 keys in the global params
            if key in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a new entry with the test data
                tkey = test_data.get("key")
                tvalue = test_data.get("value")
                entry = MapEntry(tkey, tvalue)
                # test the entry is not None
                assert entry is not None
                # test the key is not None
                assert entry._key is not None
                # test the key is the same as the test data
                assert entry._key == tkey
                # test the value is not None
                assert entry._value is not None
                # test the value is the same as the test data
                assert entry._value == tvalue
                # test the key is the same type as the test data
                assert isinstance(entry._key, dtype)
                # test the value is the same type as the test data
                assert isinstance(entry._value, dtype)

    def test_set_key(self):
        """*test_set_key()* prueba para establecer una nueva llave en el registro (pareja llave-valor) *MapEntry*.
        """
        # getting the global params
        dtypes_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params and create custom entries
        for key, dtype in zip(self.global_params.keys(), dtypes_lt):
            # ignore 2 keys in the global params
            if key in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a new entry with the test data
                tkey = test_data.get("key")
                entry = MapEntry(_key=tkey)
                entry.set_key(tkey)
                # test the key is the same as the test data
                assert entry._key == tkey
                assert entry.get_key() == tkey
                # test the key is the same type as the test data
                assert isinstance(
                    entry._key, dtype) and isinstance(tkey, dtype)
                # test value is still None
                assert entry._value is None

    def test_set_value(self):
        """*test_set_value()* prueba para establecer un nuevo valor en el registro (pareja llave-valor) *MapEntry*.
        """
        # getting the global params
        dtypes_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params and create custom entries
        for key, dtype in zip(self.global_params.keys(), dtypes_lt):
            # ignore 2 keys in the global params
            if key in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a new entry with the test data
                tval = test_data.get("value")
                entry = MapEntry(_value=tval)
                entry.set_value(tval)
                # test the key is the same as the test data
                assert entry._value == tval
                assert entry.get_value() == tval
                # test the key is the same type as the test data
                assert isinstance(entry._value, dtype) and isinstance(tval, dtype)
                # test value is still None
                assert entry._key is None

    def test_get_key(self):
        """*test_get_key()* prueba para obtener la llave del registro (pareja llave-valor) *MapEntry*.
        """
        # getting the global params
        dtypes_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params and create custom entries
        for key, dtype in zip(self.global_params.keys(), dtypes_lt):
            # ignore 2 keys in the global params
            if key in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a new entry with the test data
                tkey = test_data.get("key")
                entry = MapEntry(_key=tkey)
                ckey = entry.get_key()
                # test the key is the same as the test data
                assert entry._key == tkey and tkey == ckey
                # test the key is the same type as the test data
                assert isinstance(
                    entry._key, dtype) and isinstance(ckey, dtype)
                # test value is still None
                assert entry._value is None

    def test_get_value(self):
        """*test_get_value()* prueba para obtener el valor del registro (pareja llave-valor) *MapEntry*.
        """
        # getting the global params
        dtypes_lt = self.global_params.get("CHECK_TYPE_LT")

        # iterate over the global params and create custom entries
        for key, dtype in zip(self.global_params.keys(), dtypes_lt):
            # ignore 2 keys in the global params
            if key in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # create a new entry with the test data
                tval = test_data.get("vaLue")
                entry = MapEntry(_value=tval)
                cval = entry.get_value()
                # test the key is the same as the test data
                assert entry._value == cval and tval == cval
                # test the key is the same type as the test data
                assert isinstance(
                    entry._value, dtype) and isinstance(cval, dtype)
                # test value is still None
                assert entry._key is None

    def test_check_key_type(self):
        """*test_check_key_type()* prueba para verificar que la información de la llave (key) del registro del mapa sea del tipo especificado.
        """
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                tkey = test_data.get("key")
                # create a map entry with test_data
                with pytest.raises(TypeError) as excinfo:
                    entry = MapEntry(_key=tkey)
                    # induce the error by changing the entry key type
                    entry.set_key(err)
                # test the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                assert "for key data" in str(excinfo.value)
                # test the entry key is the same type as tkey
                assert isinstance(tkey, dtype)
                # test the entry key is not the same type as err
                assert dtype != err
                # test the key entry type is valid
                entry = MapEntry(_key=tkey)
                assert entry._key is not None
                assert isinstance(entry.get_key(), dtype)

    def test_check_value_type(self):
        """test_check_value_type _summary_
        """
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 2 keys from the global params
            if key not in ("CHECK_ERR_LT", "CHECK_TYPE_LT"):
                test_data = self.global_params.get(key)
                # tkey = test_data.get("key")
                tvalue = test_data.get("value")
                # create a map entry with test_data
                with pytest.raises(TypeError) as excinfo:
                    entry = MapEntry(_value=tvalue)
                    # induce the error by changing the entry value type
                    entry.set_value(err)
                # test the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                assert "for value data" in str(excinfo.value)
                # test the entry value is the same type as tvalue
                assert isinstance(tvalue, dtype)
                # test the entry value is not the same type as err
                assert dtype != err
                # test the key entry type is valid
                entry = MapEntry(_value=tvalue)
                assert entry._value is not None
                assert isinstance(entry.get_value(), dtype)
