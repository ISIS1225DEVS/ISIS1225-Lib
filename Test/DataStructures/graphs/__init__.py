# native imports
# import os
# import sys

# TODO create a test for the graph adjacency matrix
# importing all the test modules to package
from .test_struct_graph import TestAdjacencyList
from .test_struct_graph import TestAdjacencyMatrix
from .test_struct_adjacency import TestVertex
from .test_struct_adjacency import TestEdge

# asserting test classes
assert TestAdjacencyList
assert TestAdjacencyMatrix
assert TestVertex
assert TestEdge
