# 
import pytest
# import Test.map as map
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import maps as ht
from DISClib.ADT import lists as lt
# assert map


@pytest.fixture
def map():
    capacity = 4
    map = ht.newMap(capacity, maptype='PROBING',
                    loadfactor=0.5)

    ht.put(map, '1', 'title 1')
    ht.put(map, '2', 'title 2')
    ht.put(map, '3', 'title 3')
    ht.put(map, '4', 'title 4')
    ht.put(map, '5', 'title 5')
    ht.put(map, '6', 'title 6')
    ht.put(map, '7', 'title 7')
    ht.put(map, '8', 'title 8')
    ht.put(map, '9', 'title 9')
    ht.put(map, '10', 'title 10')
    ht.put(map, '11', 'title 11')
    ht.put(map, '12', 'title 12')
    return map


@pytest.fixture
def map2():
    capacity = 4
    map = ht.newMap(capacity,
                    maptype='PROBING',
                    loadfactor=0.5,
                    cmpfunction=cmpkeys)
    ht.put(map, '1', 'title 1')
    ht.put(map, '2', 'title 2')
    ht.put(map, '3', 'title 3')
    ht.put(map, '4', 'title 4')
    ht.put(map, '5', 'title 5')
    ht.put(map, '6', 'title 6')
    ht.put(map, '7', 'title 7')
    ht.put(map, '8', 'title 8')
    ht.put(map, '9', 'title 9')
    ht.put(map, '10', 'title 10')
    ht.put(map, '11', 'title 11')
    ht.put(map, '12', 'title 12')
    return map


def test_contains(map):
    assert ht.contains(map, '1') is True
    assert ht.contains(map, '15') is False
    assert ht.contains(map, '11') is True
    assert ht.contains(map, '50') is False
    assert ht.contains(map, '15') is False
    assert ht.contains(map, '12') is True


def test_get(map):
    entry = ht.get(map, '5')
    assert me.getKey(entry) == '5'
    me.getValue(entry)
    assert me.getValue(entry) == 'title 5'
    entry = ht.get(map, '110')
    assert entry is None
    ht.put(map, '110', 'title 110')
    ht.put(map, '120', 'title 120')
    entry = ht.get(map, '110')
    assert entry is not None
    me.getValue(entry)
    assert me.getValue(entry) == 'title 110'


def test_remove(map):
    assert ht.size(map) == 12
    assert ht.contains(map, '3') is True
    ht.remove(map, '3')
    assert ht.size(map) == 11
    assert ht.contains(map, '3') is False
    entry = ht.get(map, '110')
    assert entry is None
    ht.put(map, '110', 'title 110')
    ht.put(map, '111', 'title 111')
    ht.put(map, '112', 'title 112')
    ht.put(map, '113', 'title 113')
    ht.put(map, '114', 'title 114')
    ht.put(map, '115', 'title 115')
    assert ht.size(map) == 17
    ht.put(map, '110', 'title 110-new')
    ht.put(map, '111', 'title 111-new')
    ht.put(map, '112', 'title 112-new')
    ht.put(map, '113', 'title 113-new')
    ht.put(map, '114', 'title 114-new')
    ht.put(map, '115', 'title 115-new')
    assert ht.size(map) == 17
    entry = ht.get(map, '110')
    assert me.getValue(entry) == 'title 110-new'
    entry = ht.remove(map, '110')
    entry = ht.remove(map, '111')
    entry = ht.remove(map, '112')
    entry = ht.remove(map, '113')
    entry = ht.remove(map, '114')
    entry = ht.remove(map, '115')
    assert ht.size(map) == 11


def test_remove2(map2):
    assert ht.size(map2) == 12
    assert ht.contains(map2, '3') is True
    ht.remove(map2, '3')
    assert ht.size(map2) == 11
    assert ht.contains(map2, '3') is False
    entry = ht.get(map2, '110')
    assert entry is None
    ht.put(map2, '110', 'title 110')
    ht.put(map2, '111', 'title 111')
    ht.put(map2, '112', 'title 112')
    ht.put(map2, '113', 'title 113')
    ht.put(map2, '114', 'title 114')
    ht.put(map2, '115', 'title 115')
    assert ht.size(map2) == 17
    ht.put(map2, '110', 'title 110-new')
    ht.put(map2, '111', 'title 111-new')
    ht.put(map2, '112', 'title 112-new')
    ht.put(map2, '113', 'title 113-new')
    ht.put(map2, '114', 'title 114-new')
    ht.put(map2, '115', 'title 115-new')
    assert ht.size(map2) == 17
    entry = ht.get(map2, '110')
    assert me.getValue(entry) == 'title 110-new'
    entry = ht.remove(map2, '110')
    entry = ht.remove(map2, '111')
    entry = ht.remove(map2, '112')
    entry = ht.remove(map2, '113')
    entry = ht.remove(map2, '114')
    entry = ht.remove(map2, '115')
    assert ht.size(map2) == 11


def test_getkeys(map):
    ltset = ht.keySet(map)
    assert lt.size(ltset) == 12
    element = lt.getElement(ltset, 1)
    assert element is not None
    for element in lt.iterator(ltset):
        print(element)


def test_getvalues(map):
    ltset = ht.valueSet(map)
    assert lt.size(ltset) == 12
    for element in lt.iterator(ltset):
        print(element)


def cmpkeys(key, element):
    if (key == element['key']):
        return 0
    elif (key > element['key']):
        return 1
    return -1
