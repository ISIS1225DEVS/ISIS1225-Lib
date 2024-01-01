"""
*test_struct_hashtable.py* es el módulo que prueba los ADTs *SeparateChaining* y *LinearProbing* con sus respectivas funciones para el ADT dinámico y configurable *Map* de *DISClib*.
"""

# impoting testing framework
import unittest
import pytest
import random
from typing import TypeVar


# importing the classes to test
from DISClib.DataStructures.chaininghashtable import SeparateChaining
from DISClib.DataStructures.chaininghashtable import Bucket
from DISClib.DataStructures.probinghashtable import LinearProbing
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.mapentry import MapEntry

# importing the data to test
from Test.Data.test_data import get_hashtable_test_data

# asserting module imports
assert SeparateChaining
assert Bucket
assert LinearProbing
assert SingleLinked
assert MapEntry
assert get_hashtable_test_data

# Type for the element stored in the list
# :data: T: TypeVar
T = TypeVar("T")
"""
Variable nativa de Python para definir una estructura de datos genérica en los ADTs.
"""

# list of keys to ignore in the global parameters
# :data: IGNORE_KEYS_LT: list
IGNORE_KEYS_LT = (
    "TEST_NENTRIES",
    "TEST_SC_HT_CONFIG",
    "TEST_LP_HT_CONFIG",
    "CHECK_KEY_TYPE_LT",
    "CHECK_VALUE_TYPE_LT",
    "CHECK_KEY_ERR_LT",
    "CHECK_VALUE_ERR_LT"
)
"""
Lista de llaves a ignorar en los parámetros globales en las pruebas.
"""


def cmp_ht_test_function(key1: T, entry2: MapEntry) -> int:
    """*ht_default_cmp_funcion()* función de comparación por defecto para los elementos del ADT Map (HashTable). pueden ser de tipo nativo o definido por el usuario.

    Args:
        key1 (T): llave (key) de la primera entrada (pareja llave-valor) a comparar.
        entry2 (MapEntry): segunda entrada (pareja llave-valor) a comparar de tipo *MapEntry*. puede contener cualquier tipo de estructura, dato o ADT.

    Raises:
        TypeError: error de tipo de dato si las llaves no son comparables.

    Returns:
        int: retorna -1 si key1 es menor que la llave de entry2, 0 si las llaves son iguales y 1 si la llave key1 es mayor que la llave de entry2.
    """
    key2 = entry2.get_key()
    if type(key1) is not type(key2):
        err_msg = f"Invalid comparison between {type(key1)} and "
        err_msg += f"{type(key2)} keys"
        raise TypeError(err_msg)
    if (key1 == key2):
        return 0
    elif (key1 > key2):
        return 1
    return -1


class TestSeparateChaining(unittest.TestCase):
    """TestSeparateChaining _summary_

    Args:
        unittest (_type_): _description_
    """
    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *SeparateChaining* como un *fixture*.
        """
        self.global_params = get_hashtable_test_data()

    def sll_to_list(self, sl_lt: SingleLinked) -> list:
        """*sll_to_list()* convierte una lista sencillamente encadenada nativa de *DISCLib* en una lista nativa de Python.

        Args:
            sl_lt (SingleLinked): Lista sencillamente encadenada nativa de *DISCLib* a convertir en lista nativa de Python.

        Returns:
            list: lista nativa de Python traducida.
        """
        ans = list()
        for elm in sl_lt:
            ans.append(elm)
        return ans

    def test_default_separate_chaining(self):
        """*test_default_separate_chaining()* prueba para crear una estructura *SeparateChaining* con parámetros por defecto.
        """
        # create a new SeparateChaining
        sc_ht = SeparateChaining()
        # Test if the SeparateChaining not is None
        assert sc_ht is not None
        # Test if the SeparateChaining is rehashable
        assert sc_ht.rehashable is True
        # Test if the SeparateChaining has the default number of elements
        assert sc_ht.nentries == 1
        # Test if the SeparateChaining has the default capacity
        assert sc_ht.mcapacity == 2
        # Test if the SeparateChaining has the default load factor
        assert sc_ht.alpha == 4.0
        # Test if the SeparateChaining has the default hash function
        assert sc_ht.cmp_function == sc_ht.default_cmp_function
        # Test if the SeparateChaining has the default key
        assert sc_ht.key == "id"
        # Test if the SeparateChaining has the default prime number
        assert sc_ht.prime == 109345121
        # Test if the SeparateChaining has the default min load factor
        assert sc_ht.min_alpha == 2.0
        # Test if the SeparateChaining has the default max load factor
        assert sc_ht.max_alpha == 8.0
        # Test if the SeparateChaining is empty
        assert sc_ht._size == 0
        # Test if the SeparateChaining has no collisions
        assert sc_ht._collisions == 0
        # Test if the SeparateChaining has not define key type
        assert sc_ht._key_type is None
        # Test if the SeparateChaining has not define value type
        assert sc_ht._value_type is None

    def test_custom_separate_chaining(self):
        """*test_custom_separate_chaining()* prueba para crear una estructura *SeparateChaining* con parámetros personalizados.
        """
        # getting the global parameters data
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # test data keys
        param_lt = self.global_params.keys()
        # hash table base number of elements (n)
        test_nelements = self.global_params.get("TEST_NENTRIES")
        # dict for the hash table configuration parameters
        test_sc_ht_config = self.global_params.get("TEST_SC_HT_CONFIG")
        # iterate over global param data to create a new SeparateChaining
        for key, ktype, vtype in zip(param_lt, data_ktype_lt, data_vtype_lt):
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                for config in test_sc_ht_config.keys():
                    # custom dict id key
                    custom_id = "uuid"
                    # get SeparateChaining config for current test
                    tconfig = test_sc_ht_config.get(config)
                    talpha = tconfig.get("alpha")
                    tmin = tconfig.get("_min_alpha")
                    tmax = tconfig.get("_max_alpha")
                    trehash = tconfig.get("rehashable")
                    tkey = tconfig.get("key")
                    # get input test data for current hash table
                    test_data = self.global_params.get(key)
                    # fix default key for dict to keep test consistency
                    if key == "TEST_DICT_LT":
                        tkey = "id"
                        custom_id = "id"
                    # create a new SeparateChaining with the test data
                    sc_ht = SeparateChaining(iodata=test_data,
                                             nentries=test_nelements,
                                             alpha=talpha,
                                             min_alpha=tmin,
                                             max_alpha=tmax,
                                             key=tkey,
                                             rehashable=trehash,)
                    # Test SeparateChaining is not None
                    assert sc_ht is not None
                    # Test SeparateChaining data type
                    assert isinstance(sc_ht, SeparateChaining)
                    # testing SeparateChaining key is "uuid"
                    assert sc_ht.key == custom_id
                    # testing SeparateChaining cmp_function is the default
                    assert sc_ht.cmp_function == sc_ht.default_cmp_function
                    # Test SeparateChaining alpha is the one defined
                    assert sc_ht.alpha == talpha
                    # Test SeparateChaining min_alpha is the one defined
                    assert sc_ht.min_alpha == tmin
                    # Test SeparateChaining max_alpha is the one defined
                    assert sc_ht.max_alpha == tmax
                    # Test SeparateChaining rehashable is the one defined
                    assert sc_ht.rehashable == trehash
                    # Test SeparateChaining value type is consistent
                    assert sc_ht._value_type == vtype
                    # Test SeparateChaining key type is consistent
                    assert sc_ht._key_type == ktype

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de crear un ADT *SeparateChaining* con parámetros personalizados, junto con datos de inicialización nativos de Python y definidos por el usuario.
        """
        # create a new SeparateChaining with default cmp function
        sc_ht = SeparateChaining()

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
                        # get current data, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # create the MapEntry for the data
                        cme = MapEntry(ce, ce)
                        pme = MapEntry(pe, pe)
                        nme = MapEntry(ne, ne)
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = sc_ht.default_cmp_function(ce, pme) in exp_res
                        res2 = sc_ht.default_cmp_function(ce, cme) in exp_res
                        res3 = sc_ht.default_cmp_function(ce, nme) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de comparación por defecto para las entradas (pareka llave-valor) del ADT Map (HashTable). pueden ser de tipo nativo o definido por el usuario.
        """
        # getting the global parameters data
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # test data keys
        param_lt = self.global_params.keys()
        # iterate over global param data to create a new SeparateChaining
        for key, ktype, vtype in zip(param_lt, data_ktype_lt, data_vtype_lt):
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                custom_id = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                    custom_id = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         cmp_function=cmp_ht_test_function,
                                         key=tkey,)
                # Test SeparateChaining is not None
                assert sc_ht is not None
                # Test SeparateChaining data type
                assert isinstance(sc_ht, SeparateChaining)
                # testing SeparateChaining key is "uuid"
                assert sc_ht.key == custom_id
                # testing SeparateChaining cmp_function is the custome one
                assert sc_ht.cmp_function == cmp_ht_test_function
                # Test SeparateChaining value type is consistent
                assert sc_ht._value_type == vtype
                # Test SeparateChaining key type is consistent
                assert sc_ht._key_type == ktype

    def test_is_empty(self):
        """*test_is_empty()* prueba la función *is_empty()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining is empty
        assert sc_ht.is_empty() is True
        # testing SeparateChaining elements is empty
        sc_ht_kdata = self.sll_to_list(sc_ht.keys())
        sc_ht_vdata = self.sll_to_list(sc_ht.values())
        assert sc_ht_kdata == [] and sc_ht_vdata == []

        # iterates over global params and create filled SeparateChaining
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         cmp_function=cmp_ht_test_function,
                                         key=tkey,)
                # testing SeparateChaining is not empty
                assert sc_ht.is_empty() is False
                # testing SeparateChaining keys and values have the same length
                sc_ht_kdata = self.sll_to_list(sc_ht.keys())
                sc_ht_vdata = self.sll_to_list(sc_ht.values())
                # key-value length in hash table is always the same
                assert len(sc_ht_kdata) == len(sc_ht_vdata)

    def test_size(self):
        """*test_size()* prueba la función *size()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining size is 0 with size method
        assert sc_ht.size() == 0
        # testing SeparateChaining size is 0 with _size attribute
        assert sc_ht._size == 0
        # testing SeparateChaining elements is empty
        sc_ht_kdata = self.sll_to_list(sc_ht.keys())
        sc_ht_vdata = self.sll_to_list(sc_ht.values())
        assert sc_ht_kdata == [] and sc_ht_vdata == []

        # iterates over global params and create filled SeparateChaining
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         cmp_function=cmp_ht_test_function,
                                         key=tkey,)
                # testing SeparateChaining keys and values have the same length
                sc_ht_kdata = self.sll_to_list(sc_ht.keys())
                sc_ht_vdata = self.sll_to_list(sc_ht.values())
                # key-value length in hash table is always the same
                assert len(sc_ht_kdata) == len(sc_ht_vdata)
                # testing SeparateChaining size() is equal to test_data
                assert sc_ht.size() == len(sc_ht_kdata) == len(sc_ht_vdata)
                # testing SeparateChaining _size is equal to test_data
                assert sc_ht._size == len(sc_ht_kdata) == len(sc_ht_vdata)

    def test_put(self):
        """*test_put()* prueba la función *put()* del ADT *SeparateChaining*.
        """
        # getting the global parameters data
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # key type error test data list
        type_kerr_lt = self.global_params.get("CHECK_KEY_ERR_LT")
        # value type error test data list
        type_verr_lt = self.global_params.get("CHECK_VALUE_ERR_LT")
        # test data keys
        param_lt = self.global_params.keys()
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt,
                     type_kerr_lt,
                     type_verr_lt)
        # iterate over global param data to create a new SeparateChaining
        for key, ktype, vtype, kerr, verr in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)

                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                with pytest.raises(TypeError) as excinfo:
                    sc_ht = SeparateChaining(iodata=test_data,
                                             key=tkey,)
                    # induce the error by adding an entry of other type
                    sc_ht.put(kerr, verr)
                # test for the exception type
                assert excinfo.type == TypeError
                # assert the type error is raised
                key_err = "Invalid key type" in str(excinfo.value)
                val_err = "Invalid value type" in str(excinfo.value)
                assert key_err or val_err
                # assert the entry value is the same type as test_data
                assert isinstance(test_data[0], vtype)
                # assert the key-value type anre not the same as the errors
                assert ktype != kerr or vtype != verr

                # create a new custom SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         cmp_function=cmp_ht_test_function,
                                         key=tkey,)

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ivalue = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ivalue = test_data[i]
                    # put the new entry in the SeparateChaining
                    sc_ht.put(ikey, ivalue)
                    # recover the entry from the SeparateChaining
                    t_entry = sc_ht.get(ikey)
                    # test the entry equals the new entry
                    t_mentry = MapEntry(ikey, ivalue)
                    assert t_entry == t_mentry
                    # test if the SeparateChaining size is the same as keys
                    assert sc_ht.size() == sc_ht.keys().size()

    def test_contains(self):
        """*test_contains()* prueba la función *contains()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining size is 0 with size method
        assert sc_ht.size() == 0
        # testing SeparateChaining size is 0 with _size attribute
        assert sc_ht._size == 0

        # test if empty SeparateChaining raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            sc_ht.contains(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,)
        # iterate over global param data to create a new SeparateChaining
        for key, ktype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                    # put the new entry in the SeparateChaining
                    con = sc_ht.contains(ikey)
                    # recover the keys from the SeparateChaining
                    sc_ht_keys_lt = self.sll_to_list(sc_ht.keys())
                    # test if the key is in the SeparateChaining
                    con_key = [s for s in sc_ht_keys_lt if s == ikey][-1]
                    # test if the key is in the SeparateChaining
                    assert con is True
                    # test if the key is in the SeparateChaining keys
                    assert ikey == con_key
                    # # test key type is consistent
                    key_inst = isinstance(ikey, ktype)
                    val_inst = isinstance(con_key, ktype)
                    assert key_inst and val_inst

    def test_get(self):
        """*test_get()* prueba la función *get()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining size is 0 with size method
        assert sc_ht.size() == 0
        # testing SeparateChaining size is 0 with _size attribute
        assert sc_ht._size == 0

        # test if empty SeparateChaining raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            sc_ht.get(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt)
        # iterate over global param data to create a new SeparateChaining
        for key, ktype, vtype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ival = test_data[i]
                    # get the entry in the SeparateChaining
                    entry = sc_ht.get(ikey)
                    entry_key = entry.get_key()
                    entry_val = entry.get_value()
                    # test if the key and value is the same as the entry
                    assert ikey == entry_key and ival == entry_val
                    # test if the key and value has the same type as test_data
                    dk_inst = isinstance(ikey, ktype)
                    ek_inst = isinstance(entry_key, ktype)
                    assert dk_inst and ek_inst
                    dv_inst = isinstance(ival, vtype)
                    ev_inst = isinstance(entry_val, vtype)
                    assert dv_inst and ev_inst

    def test_check_bucket(self):
        """*test_check_bucket()* prueba la función *check_bucket()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining size is 0 with size method
        assert sc_ht.size() == 0
        # testing SeparateChaining size is 0 with _size attribute
        assert sc_ht._size == 0

        # test if empty SeparateChaining raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            sc_ht.check_bucket(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt)
        # iterate over global param data to create a new SeparateChaining
        for key, ktype, vtype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    # ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                    # get the bucket in the SeparateChaining
                    ibucket = sc_ht.check_bucket(ikey)
                    # test if bucket is actually type Bucket
                    assert isinstance(ibucket, Bucket)
                    # iterating bucket to check if data is reacheble by .get()
                    for buck in ibucket:
                        bkey = buck.get_key()
                        entry = sc_ht.get(bkey)
                        # test for entry consistency
                        assert buck == entry

                    # this is double check!!!
                    # iterating test data to check if data is consistent
                    for j in range(0, len(test_data) - 1):
                        # get the new entry (key, value)
                        jkey = test_data[j]
                        jval = test_data[j]
                        # if the entry is a dict, get the proper key
                        if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                            jkey = test_data[j].get(tkey)
                            jval = test_data[j]
                        # looking into the bucket for the entry
                        jidx = ibucket.find(jkey)
                        if jidx > -1:
                            entry = ibucket.get_element(jidx)
                            entry_key = entry.get_key()
                            entry_val = entry.get_value()

                            # test if the key-value is the same as the entry
                            assert jkey == entry_key and jval == entry_val
                            # test if the key-value has the same type as test_data
                            dk_inst = isinstance(jkey, ktype)
                            ek_inst = isinstance(entry_key, ktype)
                            assert dk_inst and ek_inst
                            dv_inst = isinstance(jval, vtype)
                            ev_inst = isinstance(entry_val, vtype)
                            assert dv_inst and ev_inst

    def test_remove(self):
        """*test_remove()* prueba la función *remove()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining size is 0 with size method
        assert sc_ht.size() == 0
        # testing SeparateChaining size is 0 with _size attribute
        assert sc_ht._size == 0

        # test if empty SeparateChaining raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            sc_ht.remove(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt)
        # iterate over global param data to create a new SeparateChaining
        for key, ktype, vtype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ival = test_data[i]
                    # getting OG hash table size
                    ht_size = sc_ht.size()
                    # if map not empty remove the entry in the SeparateChaining
                    if sc_ht.is_empty() is False:
                        entry = sc_ht.remove(ikey)
                        entry_key = entry.get_key()
                        entry_val = entry.get_value()
                        # test if the key-value has the same type as test_data
                        dk_inst = isinstance(ikey, ktype)
                        ek_inst = isinstance(entry_key, ktype)
                        assert dk_inst and ek_inst
                        dv_inst = isinstance(ival, vtype)
                        ev_inst = isinstance(entry_val, vtype)
                        assert dv_inst and ev_inst

                        # check if tha hash table size is reduced by 1
                        assert ht_size - 1 == sc_ht.size()
                        # update hash table size
                        ht_size -= 1
                        # check the removed entry is not in the hash table
                        if not sc_ht.is_empty():
                            assert sc_ht.contains(entry_key) is False

    def test_keys(self):
        """*test_keys()* prueba la función *keys()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining is empty
        assert sc_ht.is_empty() is True
        # testing SeparateChaining keys() is empty
        sc_ht_kdata = self.sll_to_list(sc_ht.keys())
        assert sc_ht_kdata == [] and sc_ht.size() == 0

        # iterates over global params and create filled SeparateChaining
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom SeparateChaining with test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         cmp_function=cmp_ht_test_function,
                                         key=tkey,)

                sc_keys = self.sll_to_list(sc_ht.keys())
                # test that the keys() method is consistent
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the test key
                    ikey = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                    # test each test key is in the recovered keys
                    assert ikey in sc_keys
                # test the length of the keys is the same as the hash table
                assert len(sc_keys) == sc_ht.size()

    def test_values(self):
        """*test_values()* prueba la función *values()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining is empty
        assert sc_ht.is_empty() is True
        # testing SeparateChaining keys() is empty
        sc_ht_vdata = self.sll_to_list(sc_ht.values())
        assert sc_ht_vdata == [] and sc_ht.size() == 0

        # iterates over global params and create filled SeparateChaining
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom SeparateChaining with test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         cmp_function=cmp_ht_test_function,
                                         key=tkey,)
                sc_values = self.sll_to_list(sc_ht.values())
                # test that the values() method is consistent
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the test key
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        # get the proper id key
                        ikey = test_data[i].get(tkey)
                        # find the exact entry values when dict is used
                        ival = [sc_val for sc_val in sc_values if sc_val[tkey] == ikey][0]
                        # test each dict is exactly the same
                        assert ival == test_data[i]
                    # otherwise, test the value is in the recovered values
                    else:
                        assert ival in sc_values
                # test the length of the values is the same as the hash table
                assert len(sc_values) == sc_ht.size()

    def test_entries(self):
        """*test_entries()* prueba la función *entries()* del ADT *SeparateChaining*.
        """
        # create a new empty SeparateChaining
        sc_ht = SeparateChaining()
        # testing SeparateChaining size is 0 with size method
        assert sc_ht.size() == 0
        # testing SeparateChaining size is 0 with _size attribute
        assert sc_ht._size == 0
        # testing SeparateChaining elements is empty
        sc_ht_edata = self.sll_to_list(sc_ht.entries())
        assert sc_ht_edata == []

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()

        # iterate over global param data to create a new SeparateChaining
        for key in param_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function)
                sc_ht_edata = self.sll_to_list(sc_ht.entries())
                sc_ht_kdata = [k[0] for k in sc_ht_edata]
                sc_ht_vdata = [v[1] for v in sc_ht_edata]

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        # get the proper id key
                        ikey = test_data[i].get(tkey)
                        # find the exact entry values when dict is used
                        ival = [
                            sc_val for sc_val in sc_ht_vdata if sc_val[tkey] == ikey][0]
                        assert ival == test_data[i]
                    # otherwise, test the value is in the recovered values
                    else:
                        assert ival in sc_ht_vdata
                    # test each dict is exactly the same
                    assert ikey in sc_ht_kdata
                # test the length of the values is the same as the hash table
                assert len(sc_ht_edata) == sc_ht.size()

    def test_rehash(self):
        """*test_rehash()* prueba la función *rehash()* del ADT *SeparateChaining*.
        """
        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()

        # iterate over global param data to create a new SeparateChaining
        for key in param_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function,
                                         min_alpha=3.0,
                                         max_alpha=4.0,
                                         rehashable=False)
                # test the hash table is not rehashable
                assert sc_ht.rehashable is False

                # setting to increase hash table with rehash()
                # get current hash table properties
                cur_size = sc_ht.size()
                cur_mcapacity = sc_ht.mcapacity
                cur_nentries = sc_ht.nentries
                cur_collisions = sc_ht._collisions
                cur_alpha = sc_ht._cur_alpha

                # rehash the table
                sc_ht.rehashable = True
                sc_ht.rehash()

                # get the new hash table properties
                new_size = sc_ht.size()
                new_mcapacity = sc_ht.mcapacity
                new_nentries = sc_ht.nentries
                new_collisions = sc_ht._collisions
                new_alpha = sc_ht._cur_alpha

                # compare the new and old hash table properties
                assert new_size == cur_size
                assert new_mcapacity >= cur_mcapacity
                assert new_nentries == cur_nentries
                assert new_collisions <= cur_collisions
                assert new_alpha <= cur_alpha

                # setting for decrease hash table with rehash()
                # freezing the hash table
                sc_ht.rehashable = False
                # test the hash table is not rehashable
                assert sc_ht.rehashable is False

                # 50% of the entries will be deleted
                n_remove = int(sc_ht.size() * 0.5)
                # select random entries to delete
                rmv_entry_lt = random.sample(test_data, n_remove)
                # iterating and entries to delete
                for rmv_entry in rmv_entry_lt:
                    # selecting key
                    ikey = rmv_entry
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        # get the proper id key
                        ikey = rmv_entry.get(tkey)
                    sc_ht.remove(ikey)

                # get current hash table properties
                cur_size = sc_ht.size()
                cur_mcapacity = sc_ht.mcapacity
                cur_nentries = sc_ht.nentries
                cur_collisions = sc_ht._collisions
                cur_alpha = sc_ht._cur_alpha

                # rehash the table
                sc_ht.rehashable = True
                sc_ht.rehash()

                # get the new hash table properties
                new_size = sc_ht.size()
                new_mcapacity = sc_ht.mcapacity
                new_nentries = sc_ht.nentries
                new_collisions = sc_ht._collisions
                new_alpha = sc_ht._cur_alpha

                # compare the new and old hash table properties
                assert new_size == cur_size
                assert new_mcapacity <= cur_mcapacity
                assert new_nentries == cur_nentries
                assert new_collisions <= cur_collisions
                assert new_alpha >= cur_alpha


class TestLinearProbing(unittest.TestCase):
    """TestLinearProbing _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *LinearProbing* como un *fixture*.
        """
        self.global_params = get_hashtable_test_data()

    def sll_to_list(self, sl_lt: SingleLinked) -> list:
        """*sll_to_list()* convierte una lista sencillamente encadenada nativa de *DISCLib* en una lista nativa de Python.

        Args:
            sl_lt (SingleLinked): Lista sencillamente encadenada nativa de *DISCLib* a convertir en lista nativa de Python.

        Returns:
            list: lista nativa de Python traducida.
        """
        ans = list()
        for elm in sl_lt:
            ans.append(elm)
        return ans

    def test_default_linear_probing(self):
        """*test_default_linear_probing()* prueba la creación de un ADT *LinearProbing* con parámetros por defecto.
        """
        # create a new LinearProbing
        lp_ht = LinearProbing()
        # Test if the LinearProbing not is None
        assert lp_ht is not None
        # Test if the LinearProbing is rehashable
        assert lp_ht.rehashable is True
        # Test if the LinearProbing has the default number of elements
        assert lp_ht.nentries == 1
        # Test if the LinearProbing has the default capacity
        assert lp_ht.mcapacity == 3
        # Test if the LinearProbing has the default load factor
        assert lp_ht.alpha == 0.5
        # Test if the LinearProbing has the default hash function
        assert lp_ht.cmp_function == lp_ht.default_cmp_function
        # Test if the LinearProbing has the default key
        assert lp_ht.key == "id"
        # Test if the LinearProbing has the default prime number
        assert lp_ht.prime == 109345121
        # Test if the LinearProbing has the default min load factor
        assert lp_ht.min_alpha == 0.2
        # Test if the LinearProbing has the default max load factor
        assert lp_ht.max_alpha == 0.8
        # Test if the LinearProbing is empty
        assert lp_ht._size == 0
        # Test if the LinearProbing has no collisions
        assert lp_ht._collisions == 0
        # Test if the LinearProbing has not define key type
        assert lp_ht._key_type is None
        # Test if the LinearProbing has not define value type
        assert lp_ht._value_type is None

    def test_custom_linear_probing(self):
        """*test_custom_linear_probing()* prueba la creación de un ADT *LinearProbing* con parámetros personalizados.
        """
        # getting the global parameters data
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # test data keys
        param_lt = self.global_params.keys()
        # hash table base number of elements (n)
        test_nelements = self.global_params.get("TEST_NENTRIES")
        # dict for the hash table configuration parameters
        test_lp_ht_config = self.global_params.get("TEST_LP_HT_CONFIG")
        # iterate over global param data to create a new LinearProbing
        for key, ktype, vtype in zip(param_lt, data_ktype_lt, data_vtype_lt):
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                for config in test_lp_ht_config.keys():
                    # custom dict id key
                    custom_id = "uuid"
                    # get LinearProbing config for current test
                    tconfig = test_lp_ht_config.get(config)
                    talpha = tconfig.get("alpha")
                    tmin = tconfig.get("_min_alpha")
                    tmax = tconfig.get("_max_alpha")
                    trehash = tconfig.get("rehashable")
                    tkey = tconfig.get("key")
                    # get input test data for current hash table
                    test_data = self.global_params.get(key)
                    # fix default key for dict to keep test consistency
                    if key == "TEST_DICT_LT":
                        tkey = "id"
                        custom_id = "id"
                    # create a new LinearProbing with the test data
                    sc_ht = LinearProbing(iodata=test_data,
                                          nentries=test_nelements,
                                          alpha=talpha,
                                          min_alpha=tmin,
                                          max_alpha=tmax,
                                          key=tkey,
                                          rehashable=trehash,)
                    # Test LinearProbing is not None
                    assert sc_ht is not None
                    # Test LinearProbing data type
                    assert isinstance(sc_ht, LinearProbing)
                    # testing LinearProbing key is "uuid"
                    assert sc_ht.key == custom_id
                    # testing LinearProbing cmp_function is the default
                    assert sc_ht.cmp_function == sc_ht.default_cmp_function
                    # Test LinearProbing alpha is the one defined
                    assert sc_ht.alpha == talpha
                    # Test LinearProbing min_alpha is the one defined
                    assert sc_ht.min_alpha == tmin
                    # Test LinearProbing max_alpha is the one defined
                    assert sc_ht.max_alpha == tmax
                    # Test LinearProbing rehashable is the one defined
                    assert sc_ht.rehashable == trehash
                    # Test LinearProbing value type is consistent
                    assert sc_ht._value_type == vtype
                    # Test LinearProbing key type is consistent
                    assert sc_ht._key_type == ktype

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba la creación de un ADT *LinearProbing* con parámetros personalizados y función de comparación.
        """
        # create a new LinearProbing with default cmp function
        lp_ht = LinearProbing()

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
                        # get current data, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # create the MapEntry for the data
                        cme = MapEntry(ce, ce)
                        pme = MapEntry(pe, pe)
                        nme = MapEntry(ne, ne)
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = lp_ht.default_cmp_function(ce, pme) in exp_res
                        res2 = lp_ht.default_cmp_function(ce, cme) in exp_res
                        res3 = lp_ht.default_cmp_function(ce, nme) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_cmp_function(self):
        """*test_default_cmp_function()* prueba la función de comparación por defecto para las entradas (pareka llave-valor) del ADT Map (HashTable). pueden ser de tipo nativo o definido por el usuario.
        """
        # getting the global parameters data
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # test data keys
        param_lt = self.global_params.keys()
        # iterate over global param data to create a new LinearProbing
        for key, ktype, vtype in zip(param_lt, data_ktype_lt, data_vtype_lt):
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                custom_id = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                    custom_id = "uuid"
                # create a new LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      cmp_function=cmp_ht_test_function,
                                      key=tkey,)
                # Test LinearProbing is not None
                assert lp_ht is not None
                # Test LinearProbing data type
                assert isinstance(lp_ht, LinearProbing)
                # testing LinearProbing key is "uuid"
                assert lp_ht.key == custom_id
                # testing LinearProbing cmp_function is the custome one
                assert lp_ht.cmp_function == cmp_ht_test_function
                # Test LinearProbing value type is consistent
                assert lp_ht._value_type == vtype
                # Test LinearProbing key type is consistent
                assert lp_ht._key_type == ktype

    def test_is_empty(self):
        """*test_is_empty()* prueba la función *is_empty()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing is empty
        assert lp_ht.is_empty() is True
        # testing LinearProbing elements is empty
        lp_ht_kdata = self.sll_to_list(lp_ht.keys())
        lp_ht_vdata = self.sll_to_list(lp_ht.values())
        assert lp_ht_kdata == [] and lp_ht_vdata == []

        # iterates over global params and create filled LinearProbing
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      cmp_function=cmp_ht_test_function,
                                      key=tkey,)
                # testing LinearProbing is not empty
                assert lp_ht.is_empty() is False
                # testing LinearProbing keys and values have the same length
                lp_ht_kdata = self.sll_to_list(lp_ht.keys())
                lp_ht_vdata = self.sll_to_list(lp_ht.values())
                # key-value length in hash table is always the same
                assert len(lp_ht_kdata) == len(lp_ht_vdata)

    def test_size(self):
        """*test_size()* prueba la función *size()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing size is 0 with size method
        assert lp_ht.size() == 0
        # testing LinearProbing size is 0 with _size attribute
        assert lp_ht._size == 0
        # testing LinearProbing elements is empty
        lp_ht_kdata = self.sll_to_list(lp_ht.keys())
        lp_ht_vdata = self.sll_to_list(lp_ht.values())
        assert lp_ht_kdata == [] and lp_ht_vdata == []

        # iterates over global params and create filled LinearProbing
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      cmp_function=cmp_ht_test_function,
                                      key=tkey,)
                # testing LinearProbing keys and values have the same length
                lp_ht_kdata = self.sll_to_list(lp_ht.keys())
                lp_ht_vdata = self.sll_to_list(lp_ht.values())
                # key-value length in hash table is always the same
                print(lp_ht_kdata, "\n", lp_ht_vdata)
                assert len(lp_ht_kdata) == len(lp_ht_vdata)
                # testing LinearProbing size() is equal to test_data
                assert lp_ht.size() == len(lp_ht_kdata) == len(lp_ht_vdata)
                # testing LinearProbing _size is equal to test_data
                assert lp_ht._size == len(lp_ht_kdata) == len(lp_ht_vdata)

    def test_put(self):
        """*test_put()* prueba la función *put()* del ADT *LinearProbing*.
        """
        # getting the global parameters data
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # key type error test data list
        type_kerr_lt = self.global_params.get("CHECK_KEY_ERR_LT")
        # value type error test data list
        type_verr_lt = self.global_params.get("CHECK_VALUE_ERR_LT")
        # test data keys
        param_lt = self.global_params.keys()
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt,
                     type_kerr_lt,
                     type_verr_lt)
        # iterate over global param data to create a new LinearProbing
        for key, ktype, vtype, kerr, verr in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)

                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new LinearProbing with the test data
                with pytest.raises(TypeError) as excinfo:
                    lp_ht = LinearProbing(iodata=test_data,
                                          key=tkey,)
                    # induce the error by adding an entry of other type
                    lp_ht.put(kerr, verr)
                # test for the exception type
                assert excinfo.type == TypeError
                # assert the type error is raised
                key_err = "Invalid key type" in str(excinfo.value)
                val_err = "Invalid value type" in str(excinfo.value)
                assert key_err or val_err
                # assert the entry value is the same type as test_data
                assert isinstance(test_data[0], vtype)
                # assert the key-value type anre not the same as the errors
                assert ktype != kerr or vtype != verr

                # create a new custom LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      cmp_function=cmp_ht_test_function,
                                      key=tkey,)

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ivalue = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ivalue = test_data[i]
                    # put the new entry in the LinearProbing
                    lp_ht.put(ikey, ivalue)
                    # recover the entry from the LinearProbing
                    t_entry = lp_ht.get(ikey)
                    # test the entry equals the new entry
                    t_mentry = MapEntry(ikey, ivalue)
                    assert t_entry == t_mentry
                    # test if the LinearProbing size is the same as keys
                    assert lp_ht.size() == lp_ht.keys().size()

    def test_contains(self):
        """*test_contains()* prueba la función *contains()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing size is 0 with size method
        assert lp_ht.size() == 0
        # testing LinearProbing size is 0 with _size attribute
        assert lp_ht._size == 0

        # test if empty LinearProbing raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            lp_ht.contains(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,)
        # iterate over global param data to create a new LinearProbing
        for key, ktype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      key=tkey,
                                      cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                    # put the new entry in the LinearProbing
                    con = lp_ht.contains(ikey)
                    # recover the keys from the LinearProbing
                    lp_ht_keys_lt = self.sll_to_list(lp_ht.keys())
                    # test if the key is in the LinearProbing
                    con_key = [s for s in lp_ht_keys_lt if s == ikey][-1]
                    # test if the key is in the LinearProbing
                    assert con is True
                    # test if the key is in the LinearProbing keys
                    assert ikey == con_key
                    # # test key type is consistent
                    key_inst = isinstance(ikey, ktype)
                    val_inst = isinstance(con_key, ktype)
                    assert key_inst and val_inst

    def test_get(self):
        """*test_get()* prueba la función *get()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing size is 0 with size method
        assert lp_ht.size() == 0
        # testing LinearProbing size is 0 with _size attribute
        assert lp_ht._size == 0

        # test if empty LinearProbing raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            lp_ht.get(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt)
        # iterate over global param data to create a new LinearProbing
        for key, ktype, vtype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      key=tkey,
                                      cmp_function=cmp_ht_test_function)
                # iterate over the test data

                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ival = test_data[i]
                    # get the entry in the LinearProbing
                    entry = lp_ht.get(ikey)
                    entry_key = entry.get_key()
                    entry_val = entry.get_value()
                    # test if the key and value is the same as the entry
                    assert ikey == entry_key and ival == entry_val
                    # test if the key and value has the same type as test_data
                    dk_inst = isinstance(ikey, ktype)
                    ek_inst = isinstance(entry_key, ktype)
                    assert dk_inst and ek_inst
                    dv_inst = isinstance(ival, vtype)
                    ev_inst = isinstance(entry_val, vtype)
                    assert dv_inst and ev_inst

    def test_check_slots(self):
        """*test_check_slots()* prueba la función *check_slots()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing size is 0 with size method
        assert lp_ht.size() == 0
        # testing LinearProbing size is 0 with _size attribute
        assert lp_ht._size == 0

        # test if empty LinearProbing raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            lp_ht.check_slots(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt)
        # iterate over global param data to create a new LinearProbing
        for key, ktype, vtype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      key=tkey,
                                      rehashable=False,
                                      cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the current entry (key, value)
                    ikey = test_data[i]
                    # check the slot for the key
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)

                    # check the slot for the key
                    lp_ht_slots = self.sll_to_list(lp_ht.check_slots(ikey))
                    lp_ht_keys = self.sll_to_list(lp_ht.keys())
                    lp_ht_values = self.sll_to_list(lp_ht.values())
                    # test for a linked list non empty
                    assert len(lp_ht_slots) > 0

                    for slot in lp_ht_slots:
                        # test if the key is in the LinearProbing
                        slotk = slot.get_key()
                        slotv = slot.get_value()
                        assert slotk in lp_ht_keys
                        assert slotv in lp_ht_values
                        assert type(slotk) is ktype
                        assert type(slotv) is vtype

    def test_remove(self):
        """*test_remove()* prueba la función *remove()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing size is 0 with size method
        assert lp_ht.size() == 0
        # testing LinearProbing size is 0 with _size attribute
        assert lp_ht._size == 0

        # test if empty LinearProbing raise the proper error
        with pytest.raises(Exception) as excinfo:
            # create a random entry
            rkey = random.randint(0, 100)
            lp_ht.remove(rkey)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()
        # key type list
        data_ktype_lt = self.global_params.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = self.global_params.get("CHECK_VALUE_TYPE_LT")
        # zip global params data
        zip_lt = zip(param_lt,
                     data_ktype_lt,
                     data_vtype_lt)
        # iterate over global param data to create a new LinearProbing
        for key, ktype, vtype in zip_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      key=tkey,
                                      cmp_function=cmp_ht_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ival = test_data[i]
                    # getting OG hash table size
                    ht_size = lp_ht.size()
                    # if map not empty remove the entry in the LinearProbing
                    if lp_ht.is_empty() is False:
                        entry = lp_ht.remove(ikey)
                        entry_key = entry.get_key()
                        entry_val = entry.get_value()
                        print(entry_key, entry_val)
                        # test if the key-value has the same type as test_data
                        dk_inst = isinstance(ikey, ktype)
                        ek_inst = isinstance(entry_key, ktype)
                        assert dk_inst and ek_inst
                        dv_inst = isinstance(ival, vtype)
                        ev_inst = isinstance(entry_val, vtype)
                        assert dv_inst and ev_inst

                        # check if tha hash table size is reduced by 1
                        assert ht_size - 1 == lp_ht.size()
                        # update hash table size
                        ht_size -= 1
                        # check the removed entry is not in the hash table
                        if not lp_ht.is_empty():
                            assert lp_ht.contains(entry_key) is False

    def test_keys(self):
        """*test_keys()* prueba la función *keys()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing is empty
        assert lp_ht.is_empty() is True
        # testing LinearProbing keys() is empty
        lp_ht_kdata = self.sll_to_list(lp_ht.keys())
        assert lp_ht_kdata == [] and lp_ht.size() == 0

        # iterates over global params and create filled LinearProbing
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom LinearProbing with test data
                lp_ht = LinearProbing(iodata=test_data,
                                      cmp_function=cmp_ht_test_function,
                                      key=tkey,)

                sc_keys = self.sll_to_list(lp_ht.keys())
                # test that the keys() method is consistent
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the test key
                    ikey = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                    # test each test key is in the recovered keys
                    assert ikey in sc_keys
                # test the length of the keys is the same as the hash table
                assert len(sc_keys) == lp_ht.size()

    def test_values(self):
        """*test_values()* prueba la función *values()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing is empty
        assert lp_ht.is_empty() is True
        # testing LinearProbing keys() is empty
        lp_ht_vdata = self.sll_to_list(lp_ht.values())
        assert lp_ht_vdata == [] and lp_ht.size() == 0

        # iterates over global params and create filled LinearProbing
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # configure the key for the test data
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new custom LinearProbing with test data
                lp_ht = LinearProbing(iodata=test_data,
                                      cmp_function=cmp_ht_test_function,
                                      key=tkey,)
                sc_values = self.sll_to_list(lp_ht.values())
                # test that the values() method is consistent
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the test key
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        # get the proper id key
                        ikey = test_data[i].get(tkey)
                        # find the exact entry values when dict is used
                        ival = [
                            sc_val for sc_val in sc_values if sc_val[tkey] == ikey][0]
                        # test each dict is exactly the same
                        assert ival == test_data[i]
                    # otherwise, test the value is in the recovered values
                    else:
                        assert ival in sc_values
                # test the length of the values is the same as the hash table
                assert len(sc_values) == lp_ht.size()

    def test_entries(self):
        """*test_entries()* prueba la función *entries()* del ADT *LinearProbing*.
        """
        # create a new empty LinearProbing
        lp_ht = LinearProbing()
        # testing LinearProbing size is 0 with size method
        assert lp_ht.size() == 0
        # testing LinearProbing size is 0 with _size attribute
        assert lp_ht._size == 0
        # testing LinearProbing elements is empty
        lp_ht_edata = self.sll_to_list(lp_ht.entries())
        assert lp_ht_edata == []

        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()

        # iterate over global param data to create a new LinearProbing
        for key in param_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new LinearProbing with the test data
                lp_ht = LinearProbing(iodata=test_data,
                                      key=tkey,
                                      cmp_function=cmp_ht_test_function)
                lp_ht_edata = self.sll_to_list(lp_ht.entries())
                lp_ht_kdata = [k[0] for k in lp_ht_edata]
                lp_ht_vdata = [v[1] for v in lp_ht_edata]

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        # get the proper id key
                        ikey = test_data[i].get(tkey)
                        # find the exact entry values when dict is used
                        ival = [
                            sc_val for sc_val in lp_ht_vdata if sc_val[tkey] == ikey][0]
                        assert ival == test_data[i]
                    # otherwise, test the value is in the recovered values
                    else:
                        assert ival in lp_ht_vdata
                    # test each dict is exactly the same
                    assert ikey in lp_ht_kdata
                # test the length of the values is the same as the hash table
                assert len(lp_ht_edata) == lp_ht.size()

    def test_rehash(self):
        """*test_rehash()* prueba la función *rehash()* del ADT *LinearProbing*.
        """
        # getting the global parameters data
        # test data keys
        param_lt = self.global_params.keys()

        # iterate over global param data to create a new SeparateChaining
        for key in param_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get input test data for current hash table
                test_data = self.global_params.get(key)
                tkey = "id"
                # fix custom dict id key to keep test consistency
                if key == "TEST_CUSTOM_DICT_LT":
                    tkey = "uuid"
                # create a new SeparateChaining with the test data
                lp_ht = SeparateChaining(iodata=test_data,
                                         key=tkey,
                                         cmp_function=cmp_ht_test_function,
                                         min_alpha=3.0,
                                         max_alpha=4.0,
                                         rehashable=False)
                # test the hash table is not rehashable
                assert lp_ht.rehashable is False

                # setting to increase hash table with rehash()
                # get current hash table properties
                cur_size = lp_ht.size()
                cur_mcapacity = lp_ht.mcapacity
                cur_nentries = lp_ht.nentries
                cur_collisions = lp_ht._collisions
                cur_alpha = lp_ht._cur_alpha

                # rehash the table
                lp_ht.rehashable = True
                lp_ht.rehash()

                # get the new hash table properties
                new_size = lp_ht.size()
                new_mcapacity = lp_ht.mcapacity
                new_nentries = lp_ht.nentries
                new_collisions = lp_ht._collisions
                new_alpha = lp_ht._cur_alpha

                # compare the new and old hash table properties
                assert new_size == cur_size
                assert new_mcapacity >= cur_mcapacity
                assert new_nentries == cur_nentries
                assert new_collisions <= cur_collisions
                assert new_alpha <= cur_alpha

                # setting for decrease hash table with rehash()
                # freezing the hash table
                lp_ht.rehashable = False
                # test the hash table is not rehashable
                assert lp_ht.rehashable is False

                # 50% of the entries will be deleted
                n_remove = int(lp_ht.size() * 0.5)
                # select random entries to delete
                rmv_entry_lt = random.sample(test_data, n_remove)
                # iterating and entries to delete
                for rmv_entry in rmv_entry_lt:
                    # selecting key
                    ikey = rmv_entry
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        # get the proper id key
                        ikey = rmv_entry.get(tkey)
                    lp_ht.remove(ikey)

                # get current hash table properties
                cur_size = lp_ht.size()
                cur_mcapacity = lp_ht.mcapacity
                cur_nentries = lp_ht.nentries
                cur_collisions = lp_ht._collisions
                cur_alpha = lp_ht._cur_alpha

                # rehash the table
                lp_ht.rehashable = True
                lp_ht.rehash()

                # get the new hash table properties
                new_size = lp_ht.size()
                new_mcapacity = lp_ht.mcapacity
                new_nentries = lp_ht.nentries
                new_collisions = lp_ht._collisions
                new_alpha = lp_ht._cur_alpha

                # compare the new and old hash table properties
                assert new_size == cur_size
                assert new_mcapacity <= cur_mcapacity
                assert new_nentries == cur_nentries
                assert new_collisions <= cur_collisions
                assert new_alpha >= cur_alpha
