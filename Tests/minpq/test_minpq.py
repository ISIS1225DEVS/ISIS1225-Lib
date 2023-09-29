import pytest
import config
from DISClib.ADT import minpq as pq
assert config


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
