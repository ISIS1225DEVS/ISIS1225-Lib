# impoting the path to the DISCLib folder
import os
import sys

# import all the modules in the DataStructures namespaces
# M1
from .arraylist import ArrayList
from .singlelinkedlist import SingleLinked
from .doublelinkedlist import DoubleLinked

# M2
from .mapentry import MapEntry
from .chaininghashtable import SeparateChaining
from .probinghashtable import LinearProbing

# M3
# search nodes
from .treenode import BSTNode
# from .treenode import KDTNode
# balanced nodes
# from .treenode import AVLNode
from .treenode import RBTNode
# search trees
from .binarysearchtree import BinarySearchTree
# from .binarysearchtree import KDimensionalTree
# balanced trees
from .leftleantree import LeftLeanRedBlackTree
# from .redblacktree import RedBlackTree
# from .avltree import AVLTree

# M4
from .adjcomponents import Vertex
from .adjcomponents import Edge
from .adjlist import AdjacencyList
from .adjmatrix import AdjacencyMatrix

# checking modules in M1 namespace
assert ArrayList
assert SingleLinked
assert DoubleLinked

# checking modules in M2 namespace
assert MapEntry
assert SeparateChaining
assert LinearProbing

# checking modules in M3 namespace
assert BSTNode
# assert KDTNode
# assert AVLNode
assert RBTNode
assert BinarySearchTree
assert LeftLeanRedBlackTree
# assert AVLTree
# assert RedBlackTree
# assert AVLTree

# checking modules in M4 namespace
assert Vertex
assert Edge
assert AdjacencyList
assert AdjacencyMatrix
