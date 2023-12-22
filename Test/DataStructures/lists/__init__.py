# impoting the path to the DISCLib folder
import os
import sys

# importing all the test modules to package
from .test_struct_list import TestArrayList
from .test_struct_list import TestSingleLinked
from .test_struct_nodes import TestNode
from .test_struct_nodes import TestSingleNode
from .test_struct_nodes import TestDoubleNode
# asserting test classes
assert TestArrayList
assert TestSingleLinked
assert TestNode
assert TestSingleNode
assert TestDoubleNode

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '..', '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, os.path.abspath(file_path))
data_path = os.path.join(os.path.dirname(__file__), '..', 'Data')