# native python modules
# import modules for defining the list types
from typing import Union

# custom modules
# M1
from DISClib.DataStructures.arraylist import ArrayList
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.doublelinkedlist import DoubleLinked

# M2
from DISClib.DataStructures.chaininghashtable import SeparateChaining
from DISClib.DataStructures.probinghashtable import LinearProbing

# union of available list types for sorting
# :arg: List: list type
List = Union[ArrayList, SingleLinked, DoubleLinked]
"""
Lista de estructuras que se pueden ordenar por el algoritmo de ordenamiento (ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*)
"""

# union of available hash table types for hashing
# :arg: HashTable: hash table type
HashTable = Union[SeparateChaining, LinearProbing]
"""
Lista de tipos de estructuras que pueden cambiar su mecánica de hashing (ADT *HashTable* y sus estructuras especificas *SeparateChaining* y *LinearProbing*)
"""
