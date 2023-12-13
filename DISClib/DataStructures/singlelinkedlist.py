"""
Este ADT representa una estructura de datos lineal, específicamente una lista sensillamente enlazada/encadenada (SingleLinked). Esta estructura de datos es una secuencia de nodos enlazados, donde cada nodo contiene un elemento de información y una referencia al siguiente nodo en la secuencia. Esto le permite a la lista un crecimiento y reducción dinámico en la memoria disponible.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect

# custom modules
# node class for the linked list
from DISClib.DataStructures.listnode import SingleNode
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import lt_default_cmp_funcion
from DISClib.Utils.default import T
from DISClib.Utils.default import DEFAULT_DICT_KEY
from DISClib.Utils.default import VALID_IO_TYPE

# checking custom modules
assert error_handler
assert lt_default_cmp_funcion
assert T
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE


@dataclass
class SingleLinked(Generic[T]):
    """**SingleLinked** representa una estructura de datos dinámica de tipo lista sensillamente encadenada (Single Linked List), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        SingleLinked: ADT de tipo SingleLinked o Lista Sensillamente Encadenada.
    """
    # input elements from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.
    """

    # reference to the first node of the list
    # :attr: first
    first: Optional[SingleNode[T]] = None
    """
    Representa el la referencia en memoria al primer nodo del SingleLinked.
    """

    # reference to the last node of the list
    # :attr: last
    last: Optional[SingleNode[T]] = None
    """
    Representa la referencia en memoria al último nodo del SingleLinked.
    """

    # by default, the list is empty
    # FIXME inconsistent use between _size and size()
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación opcional que se utiliza para comparar los elementos del ArrayList, por defecto es None y el *__post_init__()* configura la función por defecto *lt_default_cmp_funcion()*.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del ArrayList, Por defecto es None y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del SingleLinked.
        """
        try:
            # counter for elements in the input list
            # i = 0
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DEFAULT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if the list is empty, the first and last are the same and None
            if self.first is None:
                self.last = self.first
            # if input data is iterable add them to the SingleLinkedList
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """*default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el SingleLinked. Es una función crucial para que la estructura de datos funcione correctamente.

        Args:
            elm1 (Any): primer elemento a comparar.
            elm2 (Any): segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            return lt_default_cmp_funcion(self.key, elm1, elm2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el SingleLinked.

        Si se presenta un error en el SingleLinked, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el SingleLinked.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al SingleLinked sea del mismo tipo contenido dentro de los elementos del SingleLinked.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere
            agregar no es el mismo que el tipo de dato de los elementos que ya contiene el SingleLinked.

        Args:
            element (T): elemento que se quiere procesar en SingleLinked.

        Returns:
            bool: operador que indica si el ADT SingleLinked es del mismo tipo que el elemento que se quiere procesar.
        """
        # TODO check usability of this function
        # if the structure is not empty, check the first element type
        if not self.is_empty():
            # get the type of the first element
            lt_type = type(self.first.get_info())
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for element info: {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el SingleLinked está vacía.

        Returns:
            bool: operador que indica si la estructura SingleLinked está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el número de elementos que actualmente contiene el SingleLinked.

        Returns:
            int: tamaño de la estructura SingleLinked.
        """
        # TODO change the method to @property "size"?
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def add_first(self, element: T) -> None:
        """*add_first()* adiciona un elemento al inicio del SingleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                new_node = SingleNode(element)
                new_node._next = self.first
                self.first = new_node
                if self._size == 0:
                    self.last = self.first
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """*add_last()* adiciona un elemento al final del SingleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                new_node = SingleNode(element)
                if self._size == 0:
                    self.first = new_node
                else:
                    self.last._next = new_node
                self.last = new_node
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """*add_element()* adiciona un elemento en una posición dada del SingleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.
            pos (int): índice en la que se quiere agregar el elemento.

        Raises:
            IndexError: error si la posición es inválida.
            IndexError: error si la estructura está vacía.
        """
        # TODO change the method name to "add_elm()"?
        try:
            if not self.is_empty():
                if self._check_type(element):
                    if pos < 0 or pos > self._size:
                        raise IndexError("Position is out of range")
                    # create a new node
                    new_node = SingleNode(element)
                    # if the list is empty, add the element to the first
                    if self.size() == 0:
                        self.first = new_node
                        self.last = new_node
                    # if the position is the first, add it to the first
                    elif self.size() > 0 and pos == 0:
                        new_node._next = self.first
                        self.first = new_node
                    # if the position is the last, add it to the last
                    elif self.size() > 0 and pos == self.size() - 1:
                        self.last._next = new_node
                        self.last = new_node
                    else:
                        i = 0
                        current = self.first
                        previous = self.first
                        while i < pos + 1:
                            previous = current
                            current = current.next()
                            i += 1
                        new_node._next = current
                        previous._next = new_node
                    self._size += 1
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

    def get_first(self) -> Optional[T]:
        """*get_first()* lee el primer elemento del SingleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el primer elemento del SingleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.first is not None:
                info = self.first.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def get_last(self) -> Optional[T]:
        """*get_last()* lee el último elemento del SingleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el ultimo elemento del SingleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.last is not None:
                info = self.last.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def get_element(self, pos: int) -> Optional[T]:
        """*get_element()* lee un elemento en una posición dada del SingleLinked.

        Args:
            pos (int): índice en la que se quiere agregar el elemento.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición es inválida.

        Returns:
             Optional[T]: el elemento en la posición dada del SingleLinked.
        """
        # TODO change the method name to "get_elm()"?
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size - 1:
                raise IndexError("Index", pos, "is out of range")
            else:
                current = self.first
                i = 0
                # TODO check algorithm with "while i != pos:"
                while i != pos:
                    current = current.next()
                    i += 1
                info = current.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_first(self) -> Optional[T]:
        """*remove_first()* elimina el primer elemento del SingleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el primer elemento eliminado del SingleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._size > 0 and self.first is not None:
                temp = self.first.next()
                node = self.first
                self.first = temp
                self._size -= 1
                if self._size == 0:
                    self.last = None
                    self.first = None
                info = node.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_last(self) -> Optional[T]:
        """*remove_last()* elimina el último elemento del SingleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el ultimo elemento eliminado del SingleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._size > 0 and self.last is not None:
                if self.first == self.last:
                    node = self.first
                    self.last = None
                    self.first = None
                else:
                    temp = self.first
                    while temp.next() != self.last:
                        temp = temp.next()
                    node = self.last
                    self.last = temp
                    self.last._next = None
                self._size -= 1
                info = node.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_element(self, pos: int) -> Optional[T]:
        """*remove_element()* elimina un elemento en una posición dada del SingleLinked.

        Args:
            pos (int): índice del que se quiere eliminar el elemento.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.

        Returns:
            Optional[T]: el elemento eliminado del SingleLinked.
        """
        # TODO change the method name to "remove_elm()"?
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if pos < 0 or pos > self._size - 1:
                raise IndexError(f"Index {pos} is out of range")
            current = self.first
            prev = self.first
            i = 0
            if pos == 0:
                info = self.first.get_info()
                self.first = self.first.next()
            elif pos >= 1:
                # TODO check algorithm with "while i != pos:"
                while i != pos:
                    prev = current
                    current = current.next()
                    i += 1
                prev._next = current.next()
                info = current.get_info()
            self._size -= 1
            return info
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """*compare_elements()* compara dos elementos dentro del SingleLinked según la función de comparación definida por el usuario o la función por defecto.

        Args:
            elem1 (T): Primer elemento a comparar.
            elem2 (T): Segundo elemento a comparar.

        Raises:
            TypeError: error si la función de comparación no está definida.

        Returns:
            int: -1 si elem1 es menor que elem2, 0 si son iguales, 1 si elem1 es mayor que elem2.
        """
        # FIXME with __post_init__ the cmp_function is never None
        try:
            # if the key is defined but the cmp is not, use the default
            if self.key is not None and self.cmp_function is None:
                return self.default_cmp_function(elem1, elem2)
            # otherwise, use the custom cmp function
            if self.cmp_function is not None:
                return self.cmp_function(elem1, elem2)
            # raise an exception if the cmp function is not defined
            raise TypeError("Undefined compare function!!!")
        except Exception as err:
            self._handle_error(err)

    def find(self, element: T) -> int:
        """*find()* revisa si un elemento está en el SingleLinked.

        Args:
            element (T): elemento que se quiere revisar en el SingleLinked.

        Returns:
            int: la posición del elemento en el SingleLinked, -1 si no está.
        """
        # TODO change the method name to "find()"?
        try:
            lt_size = self.size()
            pos = -1
            if lt_size > 0:
                node = self.first
                found = False
                i = 0
                while not found and i < lt_size:
                    data = node.get_info()
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
                    if node.next() is not None:
                        node = node.next()
            return pos
        except Exception as err:
            self._handle_error(err)

    def change_info(self, new_info: T, pos: int) -> None:
        """*change_info()* cambia la información de un elemento en una posición dada.

        Args:
            new_info (T): nueva información que se quiere agregar en el elemento.
            pos (int): posición del elemento que se quiere cambiar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.
        """
        # TODO change the method name to "change_data()" or "update()"?
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError("Index", pos, "is out of range")
            # if not self._check_type(new_info):
            elif self._check_type(new_info):
                # raise TypeError("Invalid element type")
                current = self.first
                i = 0
                while i != pos:
                    current = current.next()
                    i += 1
                current.set_info(new_info)
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def exchange(self, pos1: int, pos2: int) -> None:
        """*exchange()* intercambia la información de dos elementos en dos posiciones dadas.

        Args:
            pos1 (int): posición del primer elemento.
            pos2 (int): posición del segundo elemento.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición del primer elemento es inválida.
            Exception: error si la posición del segundo elemento es inválida.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos1 < 0 or pos1 > self._size - 1:
                raise IndexError("Index", pos1, "is out of range")
            elif pos2 < 0 or pos2 > self._size - 1:
                raise IndexError("Index", pos2, "is out of range")
            info_pos1 = self.get_element(pos1)
            info_pos2 = self.get_element(pos2)
            self.change_info(info_pos2, pos1)
            self.change_info(info_pos1, pos2)
        except Exception as err:
            self._handle_error(err)

    def sublist(self, start: int, end: int) -> "SingleLinked[T]":
        """*sublist()* crea una sublista de la estructura según unas posiciones dentro del SingleLinked original.

        Args:
            start (int): índice inicial de la sublista.
            end (int): índice final de la sublista.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición inicial o final son inválidas.

        Returns:
            SingleLinked[T]: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self._size - 1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = SingleLinked(cmp_function=self.cmp_function,
                                  key=self.key)
            i = 0
            current = self.first
            while i != end + 1:
                if i >= start:
                    sub_lt.add_last(current.get_info())
                current = current.next()
                i += 1
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "SingleLinked[T]") -> "SingleLinked[T]":
        """*concat()* concatena dos estructuras de datos SingleLinked para crear una nueva estructura con los nodos de las dos estructuras.

        Args:
            other (SingleLinked[T]): estructura de datos SingleLinked que se quiere concatenar con la estructura original.

        Raises:
            TypeError: error si la estructura que se quiere concatenar no es un SingleLinked.
            TypeError: error si la llave de la estructura que se quiere unir no es la misma que la llave de la estructura original.
            TypeError: error si la función de comparación de la estructura que se quiere unir no es la misma que la función de comparación de la estructura original.

        Returns:
            SingleLinked[T]: Estructura de datos SingleLinked original que contiene los elementos de las dos estructuras originales.
        """
        try:
            if not isinstance(other, SingleLinked):
                err_msg = f"Structure is not an SingleLinked: {type(other)}"
                raise TypeError(err_msg)
            if self.key != other.key:
                raise TypeError(f"Invalid key: {self.key} != {other.key}")
            # checking functional code of the cmp function

            code1 = self.cmp_function.__code__.co_code
            code2 = other.cmp_function.__code__.co_code
            if code1 != code2:
                err_msg = f"Invalid compare function: {self.cmp_function}"
                err_msg += f" != {other.cmp_function}"
                raise TypeError(err_msg)
            # concatenate the two lists
            self.last._next = other.first
            self.last = other.last
            # update the size
            self._size = self.size() + other.size()
            return self
        except TypeError as err:
            self._handle_error(err)

    def __iter__(self):
        """*__iter__()* iterador nativo de Python intervenida por la estructura de datos para recorrer los elementos del SingleLinked utilizando un ciclo 'for' de python.

        Returns:
            __iter__: iterador sobre los elementos del SingleLinked.
        """
        try:
            # FIXME do I need the try/except block?
            current = self.first
            while current is not None:
                yield current.get_info()
                current = current.next()
        except Exception as err:
            self._handle_error(err)

    def __len__(self) -> int:
        """*__len__()* función nativa de Python intervenida por la estructura de datosv para recuperar el tamaño del SingleLinked.

        Returns:
            int: tamaño del SingleLinked.
        """
        return self.size()
