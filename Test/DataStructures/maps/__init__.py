# native imports
# import os
# import sys

# importing all the test modules to package
from .test_struct_hashtable import testSeparateChaining
from .test_struct_hashtable import testLinearProbing
# TODO create the cuadratic probing test
# from .test_struct_hashtable import testQuadraticProbing
from .test_struct_mapentry import testMapEntry

# asserting test classes
assert testSeparateChaining
assert testLinearProbing
# assert testQuadraticProbing
assert testMapEntry
