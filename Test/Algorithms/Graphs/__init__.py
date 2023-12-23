# impoting the path to the DISCLib folder
import os
import sys

# importing all the test modules to package
from .test_bellman import TestBellmanFord
from .test_bfs import TestBFS
from .test_cycle import TestCycle
from .test_dfo import TestDFO
from .test_dfs import TestDFS
from .test_dijkstra import TestDijkstra
from .test_graph import TestGraph
from .test_ksj import TestKruskal
from .test_prim import TestPrim
from .test_scc import TestSCC
# asserting test classes
assert TestBellmanFord
assert TestBFS
assert TestCycle
assert TestDFO
assert TestDFS
assert TestDijkstra
assert TestGraph
assert TestKruskal
assert TestPrim
assert TestSCC

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '..', '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, os.path.abspath(file_path))
