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
from DISClib.DataStructures.mapentry import MapEntry

# importing the data to test
from Test.Data.test_data import get_hashtable_test_data

# asserting module imports
assert SeparateChaining
assert LinearProbing
assert MapEntry
assert get_hashtable_test_data

# Type for the element stored in the list
# :data: T: TypeVar
T = TypeVar("T")
"""
Variable nativa de Python para definir una estructura de datos genérica en los ADTs.
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

    def test_new_default_separate_chaining(self):
        """*test_new_default_separate_chaining()* prueba la creación de un ADT *SeparateChaining* con parámetros por defecto.
        """
        ht = SeparateChaining()
        self.assertEqual(ht.size, 0)
        self.assertEqual(ht.capacity, 7)
        self.assertEqual(ht.max_load_factor, 0.75)
        self.assertEqual(ht.cmpfunction, None)
        self.assertEqual(ht.hashfunction, None)

    def test_new_custom_separate_chaining(self):
        """*test_new_custom_separate_chaining()* prueba la creación de un ADT *SeparateChaining* con parámetros personalizados.
        """
        ht = SeparateChaining(13, 0.5, cmp_ht_test_function)
        self.assertEqual(ht.size, 0)
        self.assertEqual(ht.capacity, 13)
        self.assertEqual(ht.max_load_factor, 0.5)
        self.assertEqual(ht.cmpfunction, cmp_ht_test_function)
        self.assertEqual(ht.hashfunction, None)

    def test_custom_key(self):
        """*test_custom_key()* prueba la creación de un ADT *SeparateChaining* con parámetros personalizados y función de comparación.
        """
        ht = SeparateChaining(13, 0.5, cmp_ht_test_function)
        self.assertEqual(ht.cmpfunction, cmp_ht_test_function)

    def test_custom_cmpfunction(self):
        """*test_custom_cmpfunction()* prueba la creación de un ADT *SeparateChaining* con parámetros personalizados y función de comparación.
        """
        ht = SeparateChaining(13, 0.5, cmp_ht_test_function)
        self.assertEqual(ht.cmpfunction, cmp_ht_test_function)

    def test_is_empty(self):
        """*test_is_empty()* prueba la función *is_empty()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        self.assertTrue(ht.is_empty())

    def test_size(self):
        """*test_size()* prueba la función *size()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        self.assertEqual(ht.size, 0)

    def test_put(self):
        """*test_put()* prueba la función *put()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.size, 1)
        self.assertTrue(ht.contains("key"))

    def test_contains(self):
        """*test_contains()* prueba la función *contains()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        self.assertFalse(ht.contains("key"))

    def test_get(self):
        """*test_get()* prueba la función *get()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.get("key"), "value")

    def test_check_bucket(self):
        """*test_check_bucket()* prueba la función *check_bucket()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.check_bucket(0), 1)

    def test_remove(self):
        """*test_remove()* prueba la función *remove()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.remove("key"), "value")
        self.assertEqual(ht.size, 0)

    def test_keys(self):
        """*test_keys()* prueba la función *keys()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.keys(), ["key"])

    def test_values(self):
        """*test_values()* prueba la función *values()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.values(), ["value"])

    def test_entries(self):
        """*test_entries()* prueba la función *entries()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.put("key", "value")
        self.assertEqual(ht.entries(), [("key", "value")])

    def test_rehash(self):
        """*test_rehash()* prueba la función *rehash()* del ADT *SeparateChaining*.
        """
        ht = SeparateChaining()
        ht.rehash(13)
        self.assertEqual(ht.capacity, 13)


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
