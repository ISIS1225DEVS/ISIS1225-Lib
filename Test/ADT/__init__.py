# native imports
# import os
# import sys

# importing all the test modules to package
from .test_dynamic_import import TestDynamicImporter
from .test_dynamic_lists import TestDynamicList
from .test_dynamic_maps import TestDynamicMap
from .test_adt_queue import TestQueue
from .test_adt_stack import TestStack

# asserting test classes
assert TestDynamicImporter
assert TestDynamicList
assert TestDynamicMap
assert TestQueue
assert TestStack
