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
from typing import Generic, Optional

# custom modules
# base datastructure for the queue
from DISClib.DataStructures.doublelinkedlist import DoubleLinked
from DISClib.Utils.default import T

# checking custom modules
assert T


@dataclass
class Stack(DoubleLinked, Generic[T]):
    """**Stack** representa una pila implementada sobre una lista doblemente encadenada (DoubleLinked), Generic[T] y @dataclass para que sea una estructura de datos genérica. Esta pila (Stack) es un Tipo Abstracto de Datos (TAD/ADT) que permite almacenar una colección de elementos y operarlos en el mismo orden en que fueron agregados (LIFO - Last In First Out).

    **IMPORTANTE:** *Stack* extiende de la clase *DoubleLinked*, por lo que hereda todos sus parametros internos y funciones.

    Args:
        DoubleLinked (dataclass): ADT DISClib que implementa las funciones básicas de una lista doblemente encadenada.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        Stack: ADT de tipo Stack o Pila, implementado sobre una lista doblemente encadenada.
    """

    def push(self, element: T) -> None:
        """*push()* agrega un elemento en el tope de la pila (Stack).

        Args:
            element (T): elemento que se quiere agregar al Stack.
        """
        try:
            if self._check_type(element):
                self.add_last(element)
        except Exception as exp:
            self._handle_error(exp)

    def pop(self) -> T:
        """*pop()* elimina y retorna el elemento en tope de la pila (Stack).

        Returns:
            T: el elemento en en el tope de la pila (Stack).
        """
        try:
            return self.remove_last()
        except Exception as exp:
            self._handle_error(exp)

    def top(self) -> Optional[T]:
        """*top()* retorna el elemento en el tope de la pila (Stack).

        Returns:
            T: el elemento en la primera posición de la pila (Stack).
        """
        try:
            return self.last_element()
        except Exception as exp:
            self._handle_error(exp)

    def is_empty(self) -> bool:
        """*is_empty()* informa si la pila Stack esta vacía o no.

        Returns:
            bool: operador que indica si la pila Stack esta vacía.
        """
        # TODO do I need this method?, DoubleLinked already has it
        try:
            return self._size == 0
        except Exception as exp:
            self._handle_error(exp)

    def size(self) -> int:
        """*size()* Función que informa el número de elementos en la pila Stack.

        Returns:
            int: número de elementos en el Stack.
        """
        # TODO do I need this method?, DoubleLinked already has it
        try:
            return self._size
        except Exception as exp:
            self._handle_error(exp)
