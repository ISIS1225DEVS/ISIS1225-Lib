import pytest
import config
from DISClib.ADT import orderedmap as omap
from DISClib.ADT import list as lt
assert config


@pytest.fixture
def tree():
    tree = omap.newMap(omaptype='BST')
    return tree


def test_empty(tree):
    assert omap.isEmpty(tree) is True


def test_put_empty(tree):
    tree = omap.put(tree, 1, 'book1')
    assert omap.size(tree) == 1


def test_put(tree):
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    assert omap.size(tree) == 3


def test_put_deep(tree):
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    assert omap.size(tree) == 6


def test_get(tree):
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    assert omap.size(tree) == 6
    node = omap.get(tree, 3)
    assert node['value'] == 'book3'
    node = omap.get(tree, 34)
    assert node is None


def test_remove(tree):
    tree = omap.put(tree, 21, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.remove(tree, 21)
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 10, 'book10A')
    assert omap.contains(tree, 29) is True
    assert omap.contains(tree, 28) is False
    assert omap.minKey(tree) == 3
    assert omap.maxKey(tree) == 35
    omap.deleteMin(tree)
    assert omap.contains(tree, 3) is False


def test_ceil_floor(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    assert omap.floor(tree, 21) == 20
    assert omap.floor(tree, 25) == 25
    assert omap.floor(tree, 18) == 15
    assert omap.ceiling(tree, 16) == 20
    assert omap.ceiling(tree, 15) == 15
    assert omap.ceiling(tree, 27) == 29


def test_delete_max_min(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    assert omap.contains(tree, 3) is True
    assert omap.size(tree) == 13
    omap.deleteMin(tree)
    assert omap.contains(tree, 3) is False
    assert omap.size(tree) == 12
    assert omap.contains(tree, 35) is True
    assert omap.size(tree) == 12
    omap.deleteMax(tree)
    assert omap.contains(tree, 35) is False
    assert omap.size(tree) == 11


def test_select(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    assert omap.size(tree) == 13
    assert omap.select(tree, 6) == 15


def test_rank(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    assert omap.size(tree) == 13
    assert omap.rank(tree, 15) == 6


def test_height(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    assert omap.size(tree) == 13
    assert omap.height(tree) == 4
    tree = omap.put(tree, 37, 'book11')
    tree = omap.put(tree, 40, 'book15')
    tree = omap.put(tree, 45, 'book10')
    assert omap.size(tree) == 16
    assert omap.height(tree) == 5


def test_keys(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 37, 'book11')
    tree = omap.put(tree, 40, 'book15')
    tree = omap.put(tree, 45, 'book10')
    assert omap.size(tree) == 16
    lst = omap.keys(tree, 10, 40)
    assert lt.size(lst) == 11


def test_values(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 37, 'book11')
    tree = omap.put(tree, 40, 'book15')
    tree = omap.put(tree, 45, 'book10')
    assert omap.size(tree) == 16
    lst = omap.values(tree, 10, 40)
    assert lt.size(lst) == 11


def test_keySet(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 37, 'book11')
    tree = omap.put(tree, 40, 'book15')
    tree = omap.put(tree, 45, 'book10')
    assert omap.size(tree) == 16
    lst = omap.keySet(tree)
    assert lt.size(lst) == 16
    assert lt.isPresent(lst, 11) > 0


def test_valueSet(tree):
    tree = omap.put(tree, 23, 'book21')
    tree = omap.put(tree, 7, 'book7')
    tree = omap.put(tree, 30, 'book30')
    tree = omap.put(tree, 5, 'book5')
    tree = omap.put(tree, 4, 'book4')
    tree = omap.put(tree, 3, 'book3')
    tree = omap.put(tree, 20, 'book20')
    tree = omap.put(tree, 25, 'book25')
    tree = omap.put(tree, 35, 'book35')
    tree = omap.put(tree, 29, 'book29')
    tree = omap.put(tree, 11, 'book11')
    tree = omap.put(tree, 15, 'book15')
    tree = omap.put(tree, 10, 'book10')
    tree = omap.put(tree, 37, 'book11')
    tree = omap.put(tree, 40, 'book15')
    tree = omap.put(tree, 45, 'book10')
    assert omap.size(tree) == 16
    lst = omap.valueSet(tree)
    assert lt.size(lst) == 16
    assert lt.isPresent(lst, 'book20') > 0
