# native imports
# import os
# import sys

# importing all the test modules to package
from .test_struct_hashtable import TestSeparateChaining
from .test_struct_hashtable import TestLinearProbing
# TODO create the cuadratic probing test
# from .test_struct_hashtable import testQuadraticProbing
from .test_struct_mapentry import testMapEntry

# asserting test classes
assert TestSeparateChaining
assert TestLinearProbing
# assert testQuadraticProbing
assert testMapEntry
