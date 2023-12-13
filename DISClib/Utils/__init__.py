# import python modules
import os
import sys

# import all the modules to package
# error module
# from . import error
from .error import error_handler
# from .error import init_type_checker

# default module
# from . import default
from .default import VALID_DATA_TYPE_LT
from .default import DEFAULT_DICT_KEY
from .default import VALID_IO_TYPE
from .default import DEFAULT_PRIME
from .default import T
from .default import lt_default_cmp_funcion
from .default import ht_default_cmp_funcion

# numbers module
from .numbers import is_prime
from .numbers import next_prime
from .numbers import hash_compress

# assert import
# from error module
assert error_handler
# assert init_type_checker

# from default module
assert VALID_DATA_TYPE_LT
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE
assert DEFAULT_PRIME
assert T
assert lt_default_cmp_funcion
assert ht_default_cmp_funcion

# from the numbers module
assert is_prime
assert next_prime
assert hash_compress

__all__ = ["error"]

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '../..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
# impoting the path to the DISCLib folder
sys.path.insert(0, os.path.abspath(file_path))
