"""
**test_dynamic_maps** es el módulo que prueba el funcionamiento del ADT dinámico y configurable *Map* de *DISClib* y sus funciones complementarias *clone_mp()* y *translate_mp()*.

*NOTA:* *Map* es auto-configurable gracias a la librería *Dynamic* de *DISClib*.
"""
# import testing package
import unittest
import pytest
from typing import TypeVar

# import the module to test
from Src.DISClib.ADT.maps import Map
from Src.DISClib.ADT.maps import clone_mp
from Src.DISClib.ADT.maps import translate_mp
from Src.DISClib.ADT.maps import STRUCT_PGK_PATH

# import de data structures modules
from Src.DISClib.DataStructures.chaininghashtable import SeparateChaining
from Src.DISClib.DataStructures.probinghashtable import LinearProbing
from Src.DISClib.DataStructures.singlelinkedlist import SingleLinked
from Src.DISClib.DataStructures.mapentry import MapEntry

# import the data to test
from Test.Data.test_data import get_maps_test_data
from Test.Data.test_data import get_hashtable_test_data

# asserting module imports
assert Map
assert clone_mp
assert translate_mp
assert get_maps_test_data
assert get_hashtable_test_data

# Type for the element stored in the list
# :data: T: TypeVar
T = TypeVar("T")
"""
Variable nativa de Python para definir una estructura de datos genérica en los ADTs.
"""

# list oi test dataclasses
# :param MAP_DSTYPE_LT
MAP_DSTYPE_LT = [
    SeparateChaining,
    LinearProbing,
]
"""
Lista de tipos de estructuras de datos para el ADT *Map*. Pueden ser *SeparateChaining* o *LinearProbing*.
"""

# list of tgt test dataclasses
# :param TRANS_DSTYPE_LT
TRANS_DSTYPE_LT = [
    LinearProbing,
    SeparateChaining,
]
"""
Lista de tipos de estructuras de datos para el ADT *Map* objetivo y la función *clone_mp*. Pueden ser *SeparateChaining* o *LinearProbing*.
"""

# list of keys to ignore in the global parameters
# :data: IGNORE_KEYS_LT: list
IGNORE_KEYS_LT = (
    "TEST_NENTRIES",
    "TEST_og_mp_CONFIG",
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


class TestDynamicMaps(unittest.TestCase):
    """**TestDynamicMaps** contiene las pruebas unitarias para el ADT dinámico y configurable *Map* de *DISClib* y sus funciones complementarias *clone_mp()* y *translate_mp()*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para las pruebas unitarias en Python.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Map* como un *fixture*.
        """
        self.global_params = get_maps_test_data()
        self.global_data = get_hashtable_test_data()

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

    def test_Map(self):
        """*test_Map()* prueba como crear un ADT *Map* dinámico con diferentes estructuras de datos.
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

        # iterate over error inducing structures
        for err_imp in err_struct_dict.keys():
            # force an exception in the get_element method
            with pytest.raises(Exception) as excinfo:
                Map(dstruct=err_imp)
            # test for the exception type
            assert excinfo.type == ValueError
            # test for the exception message
            assert "Invalid implementation of" in str(excinfo.value)
            assert f"Map type '{err_imp}' not found" in str(excinfo.value)

        # test for the correct implementations
        for tdsimp, tdstype in zip(struct_dict.keys(), MAP_DSTYPE_LT):
            test_lt = Map(dstruct=tdsimp)
            # test for the correct implementation
            assert test_lt is not None
            assert isinstance(test_lt, tdstype)

    def test_clone_mp(self):
        """*test_clone_mp()* prueba como clonar un ADT *Map* dinámico con diferentes estructuras de datos.
        """
        # getting the global parameters data
        params = self.global_params
        data = self.global_data
        struct_dict = params.get("TEST_STRUCT_DICT")
        struct_key_lt = struct_dict.keys()
        # test data keys
        test_data_lt = data.keys()
        # key type list
        data_ktype_lt = data.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = data.get("CHECK_VALUE_TYPE_LT")

        # zip global params data
        zipped_data_lt = zip(test_data_lt,
                             data_ktype_lt,
                             data_vtype_lt)

        # iterare over the test structures
        for tdsimp, tdstype in zip(struct_key_lt, MAP_DSTYPE_LT):
            # iterate over global param data to create a new Map
            for key, ktype, vtype in zipped_data_lt:
                # ignore some keys from the global params
                if key not in IGNORE_KEYS_LT:
                    # get input test data for current hash table
                    test_data = data.get(key)
                    tkey = "id"
                    # fix custom dict id key to keep test consistency
                    if key == "TEST_CUSTOM_DICT_LT":
                        tkey = "uuid"
                    # create a new Map with the test data
                    og_mp = Map(dstruct=tdsimp,
                                iodata=test_data,
                                cmp_function=cmp_ht_test_function,
                                key=tkey,)

                    # clone the Map
                    cl_mp = clone_mp(og_mp)

                    # test the clone list is not none
                    assert cl_mp is not None
                    # test the clone list is the correct data structure
                    assert isinstance(cl_mp, tdstype)
                    # test the clone list match the size of the test data
                    assert cl_mp.size() == og_mp.size()
                    # test the cmp_function is the same
                    assert og_mp.cmp_function == cl_mp.cmp_function
                    # test the key is the same
                    assert og_mp.key == cl_mp.key

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ival = test_data[i]
                    # get the entry in the Map
                    og_entry = og_mp.get(ikey)
                    og_en_key = og_entry.get_key()
                    og_en_val = og_entry.get_value()

                    cl_entry = cl_mp.get(ikey)
                    cl_en_key = cl_entry.get_key()
                    cl_en_val = cl_entry.get_value()
                    # test if the entry is the same in both Maps
                    assert ikey == og_en_key and ival == og_en_val
                    assert ikey == cl_en_key and ival == cl_en_val

                    # test if the key and value has the same type as test_data
                    dk_inst = isinstance(ikey, ktype)
                    og_ek_inst = isinstance(og_en_key, ktype)
                    cl_ek_inst = isinstance(cl_en_key, ktype)
                    assert dk_inst and og_ek_inst and cl_ek_inst
                    dv_inst = isinstance(ival, vtype)
                    og_ev_inst = isinstance(og_en_val, vtype)
                    cl_ev_inst = isinstance(cl_en_val, vtype)
                    assert dv_inst and og_ev_inst and cl_ev_inst

        # iterate over the test data inside de structures
        for key in test_data_lt:
            # ignore some keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = data.get(key)
                # create the list
                og_mp = test_data
                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    clone_mp(og_mp)
                # test for the exception type
                assert excinfo.type == ValueError
                # test for the exception message
                src_type = type(og_mp).__name__
                err_msg = f"Unable to clone Map, '{src_type}' type not found"
                assert err_msg in str(excinfo.value)

    def test_translate_lt(self):
        """*test_translate()* prueba transformar un ADT *Map* dinámico con diferentes estructuras de datos.
        """
        # get the global parameters
        params = self.global_params
        data = self.global_data
        src_struct_dict = params.get("TEST_STRUCT_DICT")
        tgt_struct_dict = params.get("TEST_TGT_STRUCT_DICT")
        src_struct_key_lt = src_struct_dict.keys()
        tgt_struct_key_lt = tgt_struct_dict.keys()
        # test data keys
        test_data_lt = data.keys()
        # key type list
        data_ktype_lt = data.get("CHECK_KEY_TYPE_LT")
        # value type list
        data_vtype_lt = data.get("CHECK_VALUE_TYPE_LT")
        err_struct_dict = params.get("ERR_STRUCT_DICT")
        err_struct_key_lt = err_struct_dict.keys()

        # iterare over the test structures
        zipped_mp_lt = zip(src_struct_key_lt,
                           tgt_struct_key_lt,
                           MAP_DSTYPE_LT,
                           TRANS_DSTYPE_LT)

        # zip global params data
        zipped_data_lt = zip(test_data_lt,
                             data_ktype_lt,
                             data_vtype_lt)

        # iterate over the test structures
        for src_imp, tgt_imp, dstype, cdstype in zipped_mp_lt:
            # iterate over the test data inside de structures
            # iterate over global param data to create a new Map
            for key, ktype, vtype in zipped_data_lt:
                # ignore some keys from the global params
                if key not in IGNORE_KEYS_LT:
                    # get input test data for current hash table
                    test_data = data.get(key)
                    tkey = "id"
                    # fix custom dict id key to keep test consistency
                    if key == "TEST_CUSTOM_DICT_LT":
                        tkey = "uuid"
                    # create a new Map with the test data
                    src_mp = Map(dstruct=src_imp,
                                 iodata=test_data,
                                 cmp_function=cmp_ht_test_function,
                                 key=tkey,)
                    # translate the Map
                    tgt_mp = translate_mp(src_mp, tgt_imp)
                    # test the map is not none
                    assert src_mp is not None
                    # test the translate map is not none
                    assert tgt_mp is not None

                    # test the map is the correct data structure
                    assert isinstance(src_mp, dstype)
                    # test the translate map is the correct data structure
                    assert isinstance(tgt_mp, cdstype)

                    # test cmp_function is the same
                    assert src_mp.cmp_function == tgt_mp.cmp_function
                    # test key is the same
                    assert src_mp.key == tgt_mp.key

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the new entry (key, value)
                    ikey = test_data[i]
                    ival = test_data[i]
                    # if the entry is a dict, get the proper key
                    if key in ("TEST_CUSTOM_DICT_LT", "TEST_DICT_LT"):
                        ikey = test_data[i].get(tkey)
                        ival = test_data[i]
                    # get the entry of the src map
                    src_entry = src_mp.get(ikey)
                    src_en_key = src_entry.get_key()
                    src_en_val = src_entry.get_value()
                    # gent the entry of the tgt map
                    tgt_entry = tgt_mp.get(ikey)
                    tgt_en_key = tgt_entry.get_key()
                    tgt_en_val = tgt_entry.get_value()
                    # test if the entry is the same in both Maps
                    src_ck = (ikey == src_en_key)
                    src_cv = (ival == src_en_val)
                    tgt_ck = (ikey == tgt_en_key)
                    tgt_cv = (ival == tgt_en_val)
                    all_data = [src_ck,
                                src_cv,
                                tgt_ck,
                                tgt_cv]
                    assert all(all_data)
                    # test if the key and value has the same type as test_data
                    dk_inst = isinstance(ikey, ktype)
                    src_ek_inst = isinstance(src_en_key, ktype)
                    tgt_ek_inst = isinstance(tgt_en_key, ktype)
                    dv_inst = isinstance(ival, vtype)
                    src_ev_inst = isinstance(src_en_val, vtype)
                    tgt_ev_inst = isinstance(tgt_en_val, vtype)
                    all_inst = [dk_inst,
                                src_ek_inst,
                                tgt_ek_inst,
                                dv_inst,
                                src_ev_inst,
                                tgt_ev_inst]
                    assert all(all_inst)

        # error inducing structures
        zipped = zip(src_struct_key_lt,
                     err_struct_key_lt,)
        for src_imp, err_imp in zipped:
            # iterate over the test data inside de structures
            # iterate over global param data to create a new Map
            for key, ktype, vtype in zipped_data_lt:
                # ignore some keys from the global params
                if key not in IGNORE_KEYS_LT:
                    # get input test data for current hash table
                    test_data = data.get(key)
                    tkey = "id"
                    # fix custom dict id key to keep test consistency
                    if key == "TEST_CUSTOM_DICT_LT":
                        tkey = "uuid"
                    # create a new Map with the test data
                    src_mp = Map(dstruct=src_imp,
                                 iodata=test_data,
                                 cmp_function=cmp_ht_test_function,
                                 key=tkey,)
                    # force an exception in the translate_mp method
                    with pytest.raises(Exception) as excinfo:
                        translate_mp(src_mp, err_imp)
                    # test for the exception type
                    assert excinfo.type == ValueError
                    # test for the exception message
                    assert "Invalid implementation of" in str(excinfo.value)
                    err_msg = f"Unable to translate Map '{src_imp}', "
                    err_msg += f"'{err_imp}' Map type not found"
                    assert err_msg in str(excinfo.value)
