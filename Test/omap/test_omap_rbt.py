import pytest
import config
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
from DISClib.Algorithms.Trees import traversal as tv
assert config


@pytest.fixture
def tree():
    tree = om.newMap(omaptype='RBT')
    return tree


def test_empty(tree):
    assert om.isEmpty(tree) is True


def test_root(tree):
    om.put(tree, 100, "100")
    om.put(tree, 50, "50")
    assert om.size(tree) == 2


def test_put_empty(tree):
    tree = om.put(tree, 1, 'book1')
    assert om.size(tree) == 1


def test_put(tree):
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    assert om.size(tree) == 3


def test_put_deep(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    assert om.height(tree) == 4


def test_get(tree):
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    assert om.size(tree) == 6
    assert om.contains(tree, 3) is True
    node = om.get(tree, 3)
    assert node['value'] == 'book3'
    assert om.contains(tree, 34) is False
    node = om.get(tree, 35)
    assert node is None


def test_contains(tree):
    tree = om.put(tree, 21, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 10, 'book10A')
    assert om.contains(tree, 29) is True
    assert om.contains(tree, 50) is False
    assert om.minKey(tree) == 3
    assert om.maxKey(tree) == 35
    tree = om.put(tree, 50, 'book50')
    assert om.contains(tree, 50) is True
    assert om.maxKey(tree) == 50


def test_ceil_floor(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    assert om.floor(tree, 21) == 20
    assert om.floor(tree, 25) == 25
    assert om.floor(tree, 18) == 15
    assert om.ceiling(tree, 16) == 20
    assert om.ceiling(tree, 15) == 15
    assert om.ceiling(tree, 27) == 29


def test_delete_max_min(tree):
    tree = om.put(tree, 23, 'book23')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    assert om.contains(tree, 3) is True
    assert om.size(tree) == 13
    om.deleteMin(tree)
    assert om.contains(tree, 3) is False
    assert om.size(tree) == 12
    assert om.contains(tree, 35) is True
    assert om.size(tree) == 12
    om.deleteMax(tree)
    assert om.contains(tree, 35) is False
    assert om.size(tree) == 11


def test_select(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    assert om.size(tree) == 13
    assert om.select(tree, 6) == 15


def test_rank(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    assert om.size(tree) == 13
    assert om.rank(tree, 15) == 6


def test_height(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    assert om.size(tree) == 13
    assert om.height(tree) == 4
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    assert om.height(tree) == 4


def test_keys(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    lst = om.keys(tree, 10, 40)
    assert lt.size(lst) == 11


def test_values(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    lst = om.values(tree, 10, 40)
    assert lt.size(lst) == 11


def test_remove(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    assert om.contains(tree, 11) is True
    tree = om.remove(tree, 11)
    assert om.size(tree) == 15
    assert om.contains(tree, 11) is False


def test_traversal(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    lstin = tv.inorder(tree)
    lstpre = tv.preorder(tree)
    lstpost = tv.postorder(tree)
    assert lt.size(lstin) == 16
    assert lt.size(lstpre) == 16
    assert lt.size(lstpost) == 16


def test_keySet(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    lst = om.keySet(tree)
    assert lt.size(lst) == 16
    assert lt.isPresent(lst, 11) > 0


def test_valueSet(tree):
    tree = om.put(tree, 23, 'book21')
    tree = om.put(tree, 7, 'book7')
    tree = om.put(tree, 30, 'book30')
    tree = om.put(tree, 5, 'book5')
    tree = om.put(tree, 4, 'book4')
    tree = om.put(tree, 3, 'book3')
    tree = om.put(tree, 20, 'book20')
    tree = om.put(tree, 25, 'book25')
    tree = om.put(tree, 35, 'book35')
    tree = om.put(tree, 29, 'book29')
    tree = om.put(tree, 11, 'book11')
    tree = om.put(tree, 15, 'book15')
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 37, 'book11')
    tree = om.put(tree, 40, 'book15')
    tree = om.put(tree, 45, 'book10')
    assert om.size(tree) == 16
    lst = om.valueSet(tree)
    assert lt.size(lst) == 16
    assert lt.isPresent(lst, 'book20') > 0
