import pytest
import config
from DISClib.ADT import indexminpq as pq
assert config


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
