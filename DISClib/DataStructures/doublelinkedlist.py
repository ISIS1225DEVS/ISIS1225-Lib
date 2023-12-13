"""
Este ADT representa una estructura de datos lineal, específicamente una lista doblemente enlazada/encadenada (DoubleLinked). Esta estructura de datos es una secuencia de nodos enlazados, donde cada nodo contiene un elemento de información, una referencia al siguiente, y al anterior nodo en la secuencia. Esto le permite a la lista un crecimiento y reducción dinámico en la memoria disponible.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass, field
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect

# custom modules
# node class for the linked list
from DISClib.DataStructures.listnode import DoubleNode
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
class DoubleLinked(Generic[T]):
    """**DoubleLinked** representa una estructura de datos de tipo DoubleLinked con la anotación '@dataclass' de python y el decorador 'Generic[T]' para indicar que es una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        DoubleLinked: ADT de tipo DoubleLinked o Lista Doblemente Encadenada.
    """
    # input elements from python list
    # :param iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.
    """

    # reference to the header node of the list, DoubleNode by default
    # :attr: _header
    _header: Optional[DoubleNode[T]] = field(
        default_factory=lambda: DoubleNode())
    """
    Representa el nodo sentinela de la cabecera de la estructura, por defecto es un DoubleNode vacío.
    """
    # reference to the trailer node of the list, DoubleNode by default
    # :attr: _trailer
    _trailer: Optional[DoubleNode[T]] = field(
        default_factory=lambda: DoubleNode())
    """
    Representa el nodo sentinela del final de la estructura, por defecto es un DoubleNode vacío.
    """

    # by default, the list is empty, -1 for the header and trailer nodes
    # FIXME inconsistent use between _size and size()
    # :attr: _size
    _size: int = -1
    """
    Es el número de elementos que contiene la estructura, por defecto es 0, por defecto es -1 para ajustar por los nodos sentinelas de la estructura.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación opcional que se utiliza para comparar los elementos del ArrayList, por defecto es 'None' y el *__post_init__()* configura la función por defecto *lt_default_cmp_funcion()*.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del ArrayList, Por defecto es 'None' y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del DoubleLinked.
        """
        try:
            # Link sentinel nodes
            self._header._next = self._trailer
            self._trailer._prev = self._header
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DEFAULT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if input data is iterable add them to the DoubleLinkedList
            # TODO sometime strange weird in tests
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """*default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el DoubleLinked. Es una función crucial para que la estructura de datos funcione correctamente.

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
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el DoubleLinked.

        Si se presenta un error en el DoubleLinked, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el DoubleLinked.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al DoubleLinked sea del mismo tipo contenido dentro de los elementos del DoubleLinked.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el DoubleLinked.

        Args:
            element (T): elemento que se quiere procesar en DoubleLinked.

        Returns:
            bool: operador que indica si el ADT DoubleLinked es del mismo tipo que el elemento que se quiere procesar.
        """
        # TODO check usability of this function
        # if the structure is not empty, check the header element type
        if not self.is_empty() and self._header.next().info is not None:
            # get the type of the next element to the header
            lt_type = type(self._header.next().get_info())
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for element info: {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el DoubleLinked está vacía.

        Returns:
            bool: operador que indica si la estructura DoubleLinked está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            if self._size > 0:
                return False
            return True
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el número de elementos que actualmente contiene el DoubleLinked.

        Returns:
            int: tamaño de la estructura DoubleLinked.
        """
        # TODO change the method to @property "size"?
        try:
            if self._size <= 0:
                return 0
            return self._size
        except Exception as err:
            self._handle_error(err)

    def add_first(self, element: T) -> None:
        """*add_first()* adiciona un elemento al inicio del DoubleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                # new double node with the element and sentinel references
                new_node = DoubleNode(element,
                                      _prev=self._header,
                                      _next=self._header.next())
                # completing the references
                self._header._next._prev = new_node
                self._header._next = new_node
                if self._size < 0:
                    self._size = 1
                else:
                    self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """*add_last()* adiciona un elemento al final del DoubleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                new_node = DoubleNode(element,
                                      _prev=self._trailer.prev(),
                                      _next=self._trailer)
                self._trailer._prev._next = new_node
                self._trailer._prev = new_node
                if self._size < 0:
                    self._size = 1
                else:
                    self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """*add_element()* adiciona un elemento en una posición dada del DoubleLinked.

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
                if pos == 0:
                    self.add_first(element)
                elif pos == self._size:
                    self.add_last(element)
                else:
                    i = 0
                    current = self._header.next()
                    while i < pos - 1:
                        current = current.next()
                        i += 1
                    # create a new node
                    new_node = DoubleNode(element,
                                          prev=current,
                                          next=current.next())
                    current._next._prev = new_node
                    current._next = new_node
                    if self._size < 0:
                        self._size = 1
                    else:
                        self._size += 1
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

    def get_first(self) -> Optional[T]:
        """*get_first()* lee el primer elemento del DoubleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el primer elemento del DoubleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._header.next() is not None:
                node = self._header.next()
                info = node.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def get_last(self) -> Optional[T]:
        """*get_last()* lee el último elemento del DoubleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el ultimo elemento del DoubleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._trailer.prev() is not None:
                node = self._trailer.prev()
                info = node.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def get_element(self, pos: int) -> Optional[T]:
        """*get_element()* lee un elemento en una posición dada del DoubleLinked.

        Args:
            pos (int): índice en la que se quiere agregar el elemento.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición es inválida.

        Returns:
             Optional[T]: el elemento en la posición dada del DoubleLinked.
        """
        # TODO change the method name to "get_elm()"?
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size - 1:
                raise IndexError("Index", pos, "is out of range")
            else:
                if pos < self._size // 2:
                    # Start from the beginning
                    i = 0
                    current = self._header.next()
                    while i < pos:
                        current = current.next()
                        i += 1
                else:
                    # Start from the end
                    i = self._size - 1
                    current = self._trailer.prev()
                    while i > pos:
                        current = current.prev()
                        i -= 1
                info = current.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_first(self) -> Optional[T]:
        """*remove_first()* elimina el primer elemento del DoubleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el primer elemento eliminado del DoubleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._size > 0 and self._header.next() is not None:
                first = self._header.next()
                self._header._next = first.next()
                first.next()._prev = self._header
                self._size -= 1
                # if the list is empty, reset the sentinel nodes
                if self._size == 0:
                    self._header.next = self._trailer
                    self._trailer.prev = self._header
                    self._size = -1
                info = first.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_last(self) -> Optional[T]:
        """*remove_last()* elimina el último elemento del DoubleLinked.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el ultimo elemento eliminado del DoubleLinked.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._size > 0 and self._trailer.prev() is not None:
                last = self._trailer.prev()
                self._trailer._prev = last.prev()
                last.prev()._next = self._trailer
                self._size -= 1
                # if the list is empty, reset the sentinel nodes
                if self._size == 0:
                    self._header.next = self._trailer
                    self._trailer.prev = self._header
                    self._size = -1
                info = last.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_element(self, pos: int) -> Optional[T]:
        """*remove_element()* elimina un elemento en una posición dada del DoubleLinked.

        Args:
            pos (int): índice del que se quiere eliminar el elemento.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.

        Returns:
            Optional[T]: el elemento eliminado del DoubleLinked.
        """
        # TODO change the method name to "remove_elm()"?
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if pos < 0 or pos > self._size - 1:
                raise IndexError(f"Index {pos} is out of range")
            # Determine where to start based on the position
            if pos < self._size // 2:
                # Start from the beginning
                i = 0
                current = self._header.next()
                while i != pos:
                    current = current.next()
                    i += 1
            else:
                # Start from the end
                i = self._size - 1
                current = self._trailer.prev()
                while i != pos:
                    current = current.prev()
                    i -= 1
                # removing node by index
                current.prev()._next = current.next()
                current.next()._prev = current.prev()
                self._size -= 1

                # if the list is empty, link the sentinel nodes
                if self._size == 0:
                    self._header.next = self._trailer
                    self._trailer.prev = self._header
                    self._size = -1
                info = current.get_info()
            return info
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """*compare_elements()* compara dos elementos dentro del DoubleLinked según la función de comparación definida por el usuario o la función por defecto.

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
        """*find()* revisa si un elemento está en el DoubleLinked.

        Args:
            element (T): elemento que se quiere revisar en el DoubleLinked.

        Returns:
            int: la posición del elemento en el DoubleLinked, -1 si no está.
        """
        # TODO change the method name to "find()"?
        try:
            lt_size = self.size()
            pos = -1
            if lt_size > 0:
                # setting the current node by the header
                node = self._header.next()
                found = False
                i = 0
                while not found and i < lt_size:
                    data = node.get_info()
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
                    # setting the loop end by the trailer
                    # if all(node.next(), node.next().get_info()):, alt!!!
                    if node.next() is not None:
                        if node.next().get_info() is not None:
                            node = node.next()
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
                if pos < self._size // 2:
                    # start from the beginning
                    current = self._header.next()
                    i = 0
                    while i != pos:
                        current = current.next()
                        i += 1
                else:
                    # start from the end
                    current = self._trailer.prev()
                    i = self._size - 1
                    while i != pos:
                        current = current.prev()
                        i -= 1
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

    def sublist(self, start: int, end: int) -> "DoubleLinked[T]":
        """*sublist()* crea una sublista de la estructura según unas posiciones dentro del DoubleLinked original.

        Args:
            start (int): índice inicial de la sublista.
            end (int): índice final de la sublista.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición inicial o final son inválidas.

        Returns:
            DoubleLinked[T]: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self._size - 1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = DoubleLinked(cmp_function=self.cmp_function,
                                  key=self.key)
            i = 0
            current = self._header.next()
            while i != end + 1:
                if i >= start:
                    sub_lt.add_last(current.get_info())
                current = current.next()
                i += 1
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "DoubleLinked[T]") -> "DoubleLinked[T]":
        """*concat()* concatena dos estructuras de datos DoubleLinked para crear una nueva estructura con los nodos de las dos estructuras.

        Args:
            other (DoubleLinked[T]): estructura de datos DoubleLinked que se
            quiere concatenar con la estructura original.

        Raises:
            TypeError: error si la estructura que se quiere concatenar no es un DoubleLinked.
            TypeError: error si la llave de la estructura que se quiere unir no es la misma que la llave de la estructura original.
            TypeError: error si la función de comparación de la estructura que se quiere unir no es la misma que la función de comparación de lA estructura original.

        Returns:
            DoubleLinked[T]: Estructura de datos DoubleLinked original que contiene los elementos de las dos estructuras originales.
        """
        try:
            if not isinstance(other, DoubleLinked):
                err_msg = f"Structure is not an DoubleLinked: {type(other)}"
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

            # Link the last node with the first node of the other list
            self._trailer._prev._next = other._header.next()
            other._header._next._prev = self._trailer.prev()

            # update the current trailer to the trailer of the other list
            self._trailer = other._trailer

            # Update the size of the current list
            self._size = self.size() + other.size()
            return self
        except TypeError as err:
            self._handle_error(err)

    def __iter__(self):
        """*__iter__* iterador que interviene la función nativa __iter__ para recorrer ascendentemente un DoubleLinked dentro de un ciclo 'for' de python.

        Yields:
            iterator: iterador sobre los elementos del DoubleLinked.
        """
        try:
            # FIXME do I need the try/except block?
            current = self._header.next()
            while current is not self._trailer:
                yield current.get_info()
                current = current.next()
        except Exception as err:
            self._handle_error(err)

    def __reversed__(self):
        """*__reversed__* iterador que interviene la función nativa __reversed__ para recorrer descendentemente un DoubleLinked dentro de un ciclo 'for' de python.

        Yields:
            iterator: iterador sobre los elementos del DoubleLinked.
        """

        current = self._trailer.prev()
        while current is not self._header:
            yield current.get_info()
            current = current.prev()

    def __len__(self) -> int:
        """*__len__()* función nativa intervenida que devuelve el tamaño del DoubleLinked.

        Returns:
            int: tamaño del DoubleLinked.
        """
        return self.size()
