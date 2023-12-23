# native imports
# import os
# import sys

# TODO create a test for the graph adjacency matrix
# importing all the test modules to package
from .test_struct_graph import TestGraphAdjacencyList
# from .test_struct_graph import TestGraphAdjacencyMatrix
from .test_struct_graph import TestVertex
from .test_struct_graph import TestEdge

# asserting test classes
assert TestGraphAdjacencyList
# assert TestGraphAdjacencyMatrix
assert TestVertex
assert TestEdge
