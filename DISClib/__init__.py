# MAIN __init__ file for the DISCLib package
# import python modules
# import os
# import sys

# import all the modules to package
# M1
from .ADT.dynamic import DynamicImporter
from .ADT.dynamic import STRUCT_PGK_PATH
from .ADT.lists import List
from .ADT.queue import Queue
from .ADT.stack import Stack

# M2
from .ADT.maps import Map

# M3
# from .ADT import orderedmap
# from .ADT import indexminpq
# from .ADT import minpq

# M4
# from .ADT import graph

# import ADT.maps as maps
# # M3
# import ADT.orderedmap as orderedmap
# import ADT.indexminpq as indexminpq
# import ADT.minpq as minpq
# # M4
# import ADT.graph as graph

# import all the modules in the Algorithms namespaces
# # M1
# import Algorithms.Sorting.selectionsort as selectionsort
# import Algorithms.Sorting.insertionsort as insertionsort
# import Algorithms.Sorting.shellsort as shellsort
# import Algorithms.Sorting.mergesort as mergesort
# import Algorithms.Sorting.quicksort as quicksort
# # M3
# import Algorithms.Trees.traversal as traversal
# # M4
# import Algorithms.Graphs.dfs as dfs
# import Algorithms.Graphs.bfs as bfs
# import Algorithms.Graphs.dfo as dfo
# import Algorithms.Graphs.cycles as cycles
# import Algorithms.Graphs.scc as scc
# import Algorithms.Graphs.prim as prim
# import Algorithms.Graphs.dijsktra as dijsktra
# import Algorithms.Graphs.bellmanford as bellmanford

# # import all the modules in the DataStructures namespaces
# # M1
# import DataStructures.arraylist as arraylist
# import DataStructures.singlelinkedlist as singlelinkedlist
# import DataStructures.doublelinkedlist as doublelinkedlist
# import DataStructures.listnode as listnode
# # M2
# import DataStructures.chaininghashmap as chaininghashmap
# import DataStructures.probinghashmap as probinghashmap
# import DataStructures.mapentry as mapentry
# # M3
# import DataStructures.redblacktree as redblacktree
# import DataStructures.binarysearchtree as binarysearchtree
# import DataStructures.nodetree as nodetree
# import DataStructures.heap as heap
# import DataStructures.indexheap as indexheap
# import DataStructures.iminpqnode as iminpqnode
# # M4
# import DataStructures.adjlist as adjlist
# import DataStructures.adjmatrix as adjmatrix
# import DataStructures.edge as edge

# import all the modules in the Utils namespaces
from .Utils.error import error_handler
# from .Utils.error import init_type_checker

# import all the modules in the Default namespaces
from .Utils.default import T

# import all the modules in the Numbers namespaces
from .Utils.numbers import is_prime
from .Utils.numbers import next_prime
from .Utils.numbers import hash_compress

# asserting modules
# M1
assert DynamicImporter
assert STRUCT_PGK_PATH
assert List
assert Queue
assert Stack

# M2
assert Map

# M3
# assert orderedmap
# assert indexminpq
# assert minpq

# M4
# assert graph

# Utils
assert error_handler
# assert init_type_checker

# Default
assert T

# Numbers
assert is_prime
assert next_prime
assert hash_compress


# config the path to the DISCLib folder

# __path__ = sys.path
# # print(__path__)
# # print(__name__)

# # add namespace packages
# __path__ = extend_path(__path__, __name__)

# package details
__version__ = "0.0.3"
__author__ = "ISIS-1225 Devs EDA Team, DISC, Uniandes"
__license__ = "GNU 3.0"
