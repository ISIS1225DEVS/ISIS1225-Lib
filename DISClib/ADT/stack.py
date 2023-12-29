"""
Este ADT representa una pila implementada sobre una lista doblemente encadenada. Esta pila (Stack) es un Tipo Abstracto de Datos (TAD/ADT) que permite almacenar una colección de elementos y operarlos en el mismo orden en que fueron agregados (LIFO - Last In First Out).

La implementación de la cola se realiza sobre una lista doblemente
encadenada (DoubleLinked) para garantizar que las operaciones de agregar y
eliminar elementos se realicen en tiempo constante y no consumir memoria
innecesaria.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# native python modules
# import dataclass to define the array list
from dataclasses import dataclass
# import modules for defining the element's type in the array
from typing import Optional

# custom modules
# base datastructure for the queue
from DISClib.DataStructures.doublelinkedlist import DoubleLinked
from DISClib.Utils.default import T

# checking custom modules
assert T


@dataclass
class Stack(DoubleLinked):
    """**Stack** representa una pila implementada sobre una lista doblemente encadenada (*DoubleLinked*) y @dataclass para que sea una estructura de datos genérica. Esta pila (*Stack*) es un Tipo Abstracto de Datos (TAD/ADT) que permite almacenar una colección de elementos y operarlos en el mismo orden en que fueron agregados (LIFO - Last In First Out).

    **IMPORTANTE:** *Stack* extiende de la clase *DoubleLinked*, por lo que hereda todos sus parametros internos y funciones.

    Args:
        DoubleLinked (dataclass): ADT *DISClib* que implementa las funciones básicas de una lista doblemente encadenada.

    Returns:
        Stack: ADT de tipo *Stack* o Pila, implementado sobre una lista doblemente encadenada.
    """

    def push(self, element: T) -> None:
        """*push()* inserta o agrega un elemento en el tope del *Stack*.

        Args:
            element (T): el elemento que se quiere agregar al *Stack*.
        """
        try:
            if self._check_type(element):
                self.add_last(element)
        except Exception as exp:
            self._handle_error(exp)

    def pop(self) -> T:
        """*pop()* elimina o remueve el elemento en tope del ADT *Stack*.

        Returns:
            T: el elemento de la posición más alta (tope) del ADT *Stack*.
        """
        try:
            return self.remove_last()
        except Exception as exp:
            self._handle_error(exp)

    def top(self) -> Optional[T]:
        """*top()* lee el elemento ubicado en el tope del ADT *Stack* sin eliminarlo.

        Returns:
            T: el elemento en la posición más alta (tope) del ADT *Stack*.
        """
        try:
            return self.get_last()
        except Exception as exp:
            self._handle_error(exp)
