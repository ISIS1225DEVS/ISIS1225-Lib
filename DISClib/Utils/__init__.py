# import python modules
import os
import sys

# import all the modules to package
# error module
from . import error
from .error import error_handler, init_type_checker
# default module
from .default import VALID_DATA_TYPE_LT, lt_default_cmp_funcion, T

# assert import
assert error_handler
assert init_type_checker
assert lt_default_cmp_funcion
assert VALID_DATA_TYPE_LT
assert T

__all__ = ["error"]

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '../..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
# impoting the path to the DISCLib folder
sys.path.insert(0, os.path.abspath(file_path))
