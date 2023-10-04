# MAIN __init__ file for the DISCLib Tests
# import python modules

import os
import sys

# importing all the test modules to package
from .list import test_struct_arraylist
from .list import test_struct_listnode

# asserting test packages
assert test_struct_arraylist
assert test_struct_listnode

# # import all the modules in the Utils namespaces
from .Utils import error
assert error

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '..', '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
# impoting the path to the DISCLib folder
sys.path.insert(0, os.path.abspath(file_path))
