# impoting the path to the DISCLib folder
import os
import sys

# import all the modules in the DataStructures namespaces
# M1
from .arraylist import ArrayList
from .singlelinkedlist import SingleLinked
from .doublelinkedlist import DoubleLinked

# M2
from .mapentry import MapEntry
from .chaininghashtable import SeparateChaining
from .probinghashtable import LinearProbing

# checking modules in M1 namespace
assert ArrayList
assert SingleLinked
assert DoubleLinked

# checking modules in M2 namespace
assert MapEntry
assert SeparateChaining
assert LinearProbing

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '..', '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
# sys.path.insert(0, os.path.abspath(file_path))
sys.path.append(os.path.abspath(file_path))
