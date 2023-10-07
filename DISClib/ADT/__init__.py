# import python modules
import os
import sys

# import all the modules to package
# M1
from .dynamic import DynamicImporter
from .lists import List
from . import queue
from . import stack
# M2
# from . import maps
# # M3
# from . import orderedmap
# from . import indexminpq
# from . import minpq
# # M4
# from . import graph

assert DynamicImporter
assert List
assert queue
assert stack

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '../..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
# impoting the path to the DISCLib folder
sys.path.insert(0, os.path.abspath(file_path))
