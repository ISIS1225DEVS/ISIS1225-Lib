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
from DISClib.DataStructures.probinghashtable import LinearProbing
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.mapentry import MapEntry

# importing the data to test
from Test.Data.test_data import get_hashtable_test_data

# asserting module imports
assert SeparateChaining
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
    "CHECK_ERR_LT",
    "CHECK_KEY_TYPE_LT",
    "CHECK_VALUE_TYPE_LT",
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


class testSeparateChaining(unittest.TestCase):
    """testSeparateChaining _summary_

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
                tkey = "uuid"
                custom_id = "uuid"
                # fix default key for dict to keep test consistency
                if key == "TEST_DICT_LT":
                    tkey = "id"
                    custom_id = "id"
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
        sc_ht_keys = sc_ht.keys()
        sc_ht_values = sc_ht.values()
        sc_ht_kdata = self.sll_to_list(sc_ht_keys)
        sc_ht_vdata = self.sll_to_list(sc_ht_values)
        assert sc_ht_kdata == [] and sc_ht_vdata == []

        # iterates over global params and create filled SeparateChaining
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # test_data_set = set(test_data)
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data)
                # testing SeparateChaining is not empty
                assert sc_ht.is_empty() is False
                # testing SeparateChaining keys and values have the same length
                sc_ht_keys = sc_ht.keys()
                sc_ht_values = sc_ht.values()
                sc_ht_kdata = self.sll_to_list(sc_ht_keys)
                sc_ht_vdata = self.sll_to_list(sc_ht_values)
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
        # check if the SeparateChaining elements is empty
        # testing SeparateChaining elements is empty
        sc_ht_keys = sc_ht.keys()
        sc_ht_values = sc_ht.values()
        sc_ht_kdata = self.sll_to_list(sc_ht_keys)
        sc_ht_vdata = self.sll_to_list(sc_ht_values)
        assert sc_ht_kdata == [] and sc_ht_vdata == []

        # iterates over global params and create filled SeparateChaining
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # account for repeated keys in data
                # test_data_set = set(test_data)
                # create a new SeparateChaining with the test data
                sc_ht = SeparateChaining(iodata=test_data)
                # testing SeparateChaining keys and values have the same length
                sc_ht_keys = sc_ht.keys()
                sc_ht_values = sc_ht.values()
                sc_ht_kdata = self.sll_to_list(sc_ht_keys)
                sc_ht_vdata = self.sll_to_list(sc_ht_values)
                # key-value length in hash table is always the same
                assert len(sc_ht_kdata) == len(sc_ht_vdata)
                # testing SeparateChaining size() is equal to test_data
                assert sc_ht.size() == len(sc_ht_kdata) == len(sc_ht_vdata)
                # testing SeparateChaining _size is equal to test_data
                assert sc_ht._size == len(sc_ht_kdata) == len(sc_ht_vdata)

    def test_put(self):
        """*test_put()* prueba la función *put()* del ADT *SeparateChaining*.
        """
        pass

    def test_contains(self):
        """*test_contains()* prueba la función *contains()* del ADT *SeparateChaining*.
        """
        pass

    def test_get(self):
        """*test_get()* prueba la función *get()* del ADT *SeparateChaining*.
        """
        pass

    def test_check_bucket(self):
        """*test_check_bucket()* prueba la función *check_bucket()* del ADT *SeparateChaining*.
        """
        pass

    def test_remove(self):
        """*test_remove()* prueba la función *remove()* del ADT *SeparateChaining*.
        """
        pass

    def test_keys(self):
        """*test_keys()* prueba la función *keys()* del ADT *SeparateChaining*.
        """
        pass

    def test_values(self):
        """*test_values()* prueba la función *values()* del ADT *SeparateChaining*.
        """
        pass

    def test_entries(self):
        """*test_entries()* prueba la función *entries()* del ADT *SeparateChaining*.
        """
        pass

    def test_rehash(self):
        """*test_rehash()* prueba la función *rehash()* del ADT *SeparateChaining*.
        """
        pass


class testLinearProbing(unittest.TestCase):
    """testLinearProbing _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *LinearProbing* como un *fixture*.
        """
        self.global_params = get_hashtable_test_data()

    def test_new_default_separate_chaining(self):
        """*test_new_default_separate_chaining()* prueba la creación de un ADT *LinearProbing* con parámetros por defecto.
        """
        ht = LinearProbing()
        self.assertEqual(ht.size, 0)
        self.assertEqual(ht.capacity, 7)
        self.assertEqual(ht.max_load_factor, 0.75)
        self.assertEqual(ht.cmpfunction, None)
        self.assertEqual(ht.hashfunction, None)

    def test_new_custom_separate_chaining(self):
        """*test_new_custom_separate_chaining()* prueba la creación de un ADT *LinearProbing* con parámetros personalizados.
        """
        ht = LinearProbing(13, 0.5, cmp_ht_test_function)
        self.assertEqual(ht.size, 0)
        self.assertEqual(ht.capacity, 13)
        self.assertEqual(ht.max_load_factor, 0.5)
        self.assertEqual(ht.cmpfunction, cmp_ht_test_function)
        self.assertEqual(ht.hashfunction, None)

    def test_custom_key(self):
        """*test_custom_key()* prueba la creación de un ADT *LinearProbing* con parámetros personalizados y función de comparación.
        """
        ht = LinearProbing(13, 0.5, cmp_ht_test_function)
        self.assertEqual(ht.cmpfunction, cmp_ht_test_function)

    def test_custom_cmpfunction(self):
        """*test_custom_cmpfunction()* prueba la creación de un ADT *LinearProbing* con parámetros personalizados y función de comparación.
        """
        ht = LinearProbing(13, 0.5, cmp_ht_test_function)
        self.assertEqual(ht.cmpfunction, cmp_ht_test_function)

    def test_is_empty(self):
        """*test_is_empty()* prueba la función *is_empty()* del ADT *LinearProbing*.
        """
        ht = LinearProbing()
        self.assertTrue(ht.is_empty())

    def test_size(self):
        """*test_size()* prueba la función *size()* del ADT *LinearProbing*.
        """
        ht = LinearProbing()
        self.assertEqual(ht.size, 0)

    def test_put(self):
        """*test_put()* prueba la función *put()* del ADT *LinearProbing*.
        """
        pass

    def test_contains(self):
        """test_contains _summary_
        """
        pass

    def test_get(self):
        """*test_get()* prueba la función *get()* del ADT *LinearProbing*.
        """
        pass

    def test_check_bucket(self):
        """test_check_bucket _summary_
        """
        pass

    def test_remove(self):
        """test_remove _summary_
        """
        pass

    def test_keys(self):
        """test_keys _summary_
        """
        pass

    def test_values(self):
        """test_values _summary_
        """
        pass

    def test_entries(self):
        """test_entries _summary_
        """
        pass

    def test_rehash(self):
        """*test_rehash()* prueba la función *rehash()* del ADT *LinearProbing*.
        """
        ht = LinearProbing()
        ht.rehash(13)
        self.assertEqual(ht.capacity, 13)

    def test_is_available(self):
        """*test_is_available()* prueba la función *is_available()* del ADT *LinearProbing*.
        """
        pass

    def test_find_slot(self):
        """test_find_slot _summary_
        """
        pass
