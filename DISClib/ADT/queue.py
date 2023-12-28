"""
Este ADT representa una cola/fila implementada sobre una lista. Esta cola o fila (queue) es una estructura de datos que permite almacenar una colección de elementos y operar sobre ellos en el mismo orden en que fueron agregados (FIFO).

La implementación de la cola se realiza sobre una lista simplemente
encadenada (SingleLinked) para garantizar que las operaciones de agregar y
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
from DISClib.DataStructures.singlelinkedlist import SingleLinked
from DISClib.Utils.default import T

# checking custom modules
assert T


@dataclass
class Queue(SingleLinked):
    """**Queue** representa una cola implementada sobre una lista sencillamente encadenada (SingleLinked), Generic[T] y @dataclass para que sea una estructura de datos genérica. Esta cola o fila (queue) es un Tipo Abstracto de Datos (TAD/ADT) que permite almacenar una colección de elementos y operarlos en el mismo orden en que fueron agregados (FIFO - Firts In First Out).

    *IMPORTANTE:* 'Queue' extiende de la clase 'SingleLinked', por lo que hereda todos sus parametros internos y funciones.

    Args:
        SingleLinked (dataclass): ADT DISClib que implementa las funciones básicas de una lista sencillamente encadenada.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        Queue: ADT de tipo Queue, Cola o Fila, implementado sobre una lista sencillamente encadenada.
    """

    def enqueue(self, element: T) -> None:
        """*enqueue()* agrega un elemento en el final de la cola/fila (Queue).

        Args:
            element (T): elemento que se quiere agregar al Queue.
        """
        try:
            if self._check_type(element):
                self.add_last(element)
        except Exception as exp:
            self._handle_error(exp)

    def dequeue(self) -> T:
        """*dequeue()* elimina y retorna el elemento en la primer posición de la cola/fila Queue.

        Returns:
            T: el elemento en la primera posición de la cola/fila Queue.
        """
        try:
            return self.remove_first()
        except Exception as exp:
            self._handle_error(exp)

    def peek(self) -> Optional[T]:
        """*peek()* lee el primer elemento de la cola/fila Queue sin eliminarlo.

        Returns:
            T: elemento en la primer posición de la cola/fila Queue.
        """
        try:
            return self.get_first()
        except Exception as exp:
            self._handle_error(exp)

    def is_empty(self) -> bool:
        """*is_empty()* informa si la cola/fila Queue esta vacía o no.

        Returns:
            bool: operador que indica si la cola/fila Queue esta vacía.
        """
        # TODO do I need this method?, SingleLinked already has it
        try:
            return self._size == 0
        except Exception as exp:
            self._handle_error(exp)

    def size(self) -> int:
        """*size()* Función que informa el número de elementos en la fila/cola Queue.

        Returns:
            int: número de elementos en el Queue.
        """
        # TODO do I need this method?, SingleLinked already has it
        try:
            return self._size
        except Exception as exp:
            self._handle_error(exp)
