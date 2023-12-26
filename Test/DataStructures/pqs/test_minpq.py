from DISClib.ADT import indexminpq as pq
import pytest
# import Test.minpq as minpq
from DISClib.ADT import minpq as pq
# assert minpq


def greater(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


@pytest.fixture
def minpq():
    minpq = pq.newMinPQ(greater)
    return minpq


def test_empty(minpq):
    assert pq.isEmpty(minpq) is True


def test_insert(minpq):
    minpq = pq.insert(minpq, 23)
    minpq = pq.insert(minpq, 7)
    minpq = pq.insert(minpq, 30)
    minpq = pq.insert(minpq, 5)
    minpq = pq.insert(minpq, 15)
    minpq = pq.insert(minpq, 1)
    key = pq.min(minpq)
    assert key == 1


def test_delete(minpq):
    minpq = pq.insert(minpq, 23)
    minpq = pq.insert(minpq, 7)
    minpq = pq.insert(minpq, 30)
    minpq = pq.insert(minpq, 5)
    minpq = pq.insert(minpq, 15)
    minpq = pq.insert(minpq, 1)
    key = pq.min(minpq)
    assert key == 1
    key = pq.delMin(minpq)
    assert key == 1
    key = pq.min(minpq)
    assert key == 5
    key = pq.delMin(minpq)
    assert key == 5
    key = pq.min(minpq)
    assert key == 7
    minpq = pq.insert(minpq, 4)
    minpq = pq.insert(minpq, 3)
    minpq = pq.insert(minpq, 2)
    key = pq.min(minpq)
    assert key == 2
    key = pq.delMin(minpq)
    assert key == 2
    key = pq.delMin(minpq)
    assert key == 3
    key = pq.delMin(minpq)
    assert key == 4


# INDEX MINPQ LEGACY CODE
# import Test.minpq as minpq
# assert minpq


def greater(key1, entry):
    if key1 == entry['key']:
        return 0
    elif key1 < entry['key']:
        return -1
    else:
        return 1


@pytest.fixture
def iminpq():
    iminpq = pq.newIndexMinPQ(greater)
    iminpq = pq.insert(iminpq, 'A', 23)
    iminpq = pq.insert(iminpq, 'B', 7)
    iminpq = pq.insert(iminpq, 'C', 30)
    iminpq = pq.insert(iminpq, 'D', 5)
    iminpq = pq.insert(iminpq, 'E', 15)
    return iminpq


def test_empty(iminpq):
    assert pq.isEmpty(iminpq) is False


def test_insert(iminpq):
    iminpq = pq.decreaseKey(iminpq, 'A', 1)
    key = pq.min(iminpq)
    assert key == 'A'
    iminpq = pq.increaseKey(iminpq, 'A', 12)
    key = pq.min(iminpq)
    assert key == 'D'


def test_delMin(iminpq):
    iminpq = pq.decreaseKey(iminpq, 'A', 1)
    key = pq.min(iminpq)
    assert key == 'A'
    iminpq = pq.increaseKey(iminpq, 'A', 12)
    key = pq.min(iminpq)
    assert key == 'D'
    pq.delMin(iminpq)
    key = pq.min(iminpq)
    assert key == 'B'
