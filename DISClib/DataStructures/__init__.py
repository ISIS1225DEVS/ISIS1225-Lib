# native python modules
# import modules for defining the list types
from typing import Union

# custom modules
from DISClib.DataStructures.arraylist import ArrayList
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.DataStructures.doublelinkedlist import DoubleLinked

# sort available list types
# :arg: List: list type
List = Union[ArrayList, SingleLinked, DoubleLinked]
"""
Lista de tipos de estructuras que se pueden ordenar por el algoritmo de ordenamiento (ADT *List* y sus estructuras especificas *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* y *Stack*)
"""
