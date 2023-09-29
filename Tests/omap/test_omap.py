import pytest
import config
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
from DISClib.Algorithms.Trees import traversal as tr
assert config


@pytest.fixture
def tree():
    tree = om.newMap(omaptype='BST')
    return tree


def test_empty(tree):
    assert om.isEmpty(tree) is True


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
    assert om.height(tree) == 5


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
    node = om.get(tree, 34)
    assert om.contains(tree, 34) is False
    assert node is None


def test_remove(tree):
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
    tree = om.remove(tree, 21)
    tree = om.put(tree, 10, 'book10')
    tree = om.put(tree, 10, 'book10A')
    assert om.contains(tree, 29) is True
    assert om.contains(tree, 28) is False
    assert om.minKey(tree) == 3
    assert om.maxKey(tree) == 35
    om.deleteMin(tree)
    assert om.contains(tree, 3) is False


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
    assert om.height(tree) == 5


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


def test_inorder(tree):
    tree = om.put(tree, 2, 'book2')
    tree = om.put(tree, 1, 'book1')
    tree = om.put(tree, 3, 'book3')
    lst = tr.inorder(tree)
    for element in lt.iterator(lst):
        print(element)


def test_preorder(tree):
    tree = om.put(tree, 2, 'book2')
    tree = om.put(tree, 1, 'book1')
    tree = om.put(tree, 3, 'book3')
    lst = tr.preorder(tree)
    for element in lt.iterator(lst):
        print(element)


def test_postorder(tree):
    tree = om.put(tree, 2, 'book2')
    tree = om.put(tree, 1, 'book1')
    tree = om.put(tree, 3, 'book3')
    lst = tr.postorder(tree)
    for element in lt.iterator(lst):
        print(element)
