# MAIN __init__ file for the DISCLib Tests
# import python modules
# import os
# import sys

# importing all the test modules to package
# M1
from .DataStructures.lists import test_struct_list
from .DataStructures.lists import test_struct_nodes

# # ADTs based on lists
# from .ADT import test_adt_queue
# from .ADT import test_adt_stack

# # Dynamic imports and ADTs
from .ADT import test_dynamic_import
# from .ADT import test_dynamic_lists
# from .ADT import test_dynamic_maps

# # M2
from .DataStructures.maps import test_struct_mapentry
from .DataStructures.maps import test_struct_hashtable


# asserting test packages
# M1
assert test_struct_list
assert test_struct_nodes
# assert test_adt_queue
# assert test_adt_stack
assert test_dynamic_import
# assert test_dynamic_lists
# assert test_dynamic_maps

# # M2
assert test_struct_mapentry
assert test_struct_hashtable
