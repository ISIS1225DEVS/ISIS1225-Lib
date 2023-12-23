# native imports
# import os
# import sys

# TODO create the other types of tree tests
# importing all the test modules to package
from .test_struct_searchtree import TestBST
# from .test_struct_searchtree import TestKDTree
# from .test_struct_balancedtree import TestRBT
from .test_struct_balancedtree import TestLLRBT
# from .test_struct_balancedtree import TestAVL
from .test_struct_treenode import TestBSTNode
# from .test_struct_treenode import TestKDTreeNode
from .test_struct_treenode import TestRBTNode
# from .test_struct_treenode import TestLLRBTNode
# from .test_struct_treenode import TestAVLNode

assert TestBST
# assert TestKDTree
# assert TestRBT
assert TestLLRBT
# assert TestAVL
assert TestBSTNode
# assert TestKDTreeNode
assert TestRBTNode
# assert TestLLRBTNode
# assert TestAVLNode
