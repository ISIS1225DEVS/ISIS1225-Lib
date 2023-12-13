"""
Este ADT representa una estructura de datos lineal, específicamente un arreglo dinámico (ArrayList). El arreglo dinámico es una estructura de datos que permite almacenar un conjunto de elementos del mismo tipo, en la cual se puede acceder y procesar sus elementos utilizando las funciones/métodos propios de la estructura.

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
class ArrayList(Generic[T]):
    """**ArrayList** representa la estructura de datos para arreglos dinamicos (Array List), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        ArrayList: ADT de tipo ArrayList o Arreglo Dinámico.

    """
    # input elements from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python que contiene los elementos de entrada a la estructura, por defecto es None y el usuario puede incluir una lista nativa de python como argumento.
    """

    # using default_factory to generate an empty list
    # :attr: elements
    elements: List[T] = field(default_factory=list)
    """
    Lista nativa de Python que contiene los elementos de la estructura.
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
    Nombre de la llave opcional que se utiliza para comparar los elementos del ArrayList, Por defecto es 'None' y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del ArrayList.
        """
        try:
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DEFAULT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if elements are in a list, add them to the ArrayList
            # TODO sometime strange weird in tests
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """*default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el ArrayList. Es una función crucial para que la estructura de datos funcione correctamente.

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
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el ArrayList.

        Si se presenta un error en ArrayList, se formatea el error según el contexto (paquete/clase), la función que lo generó y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el ArrayList.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al ArrayList sea del mismo tipo contenido dentro de los elementos del ArrayList.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el ArrayList.

        Args:
            element (T): elemento que se quiere procesar en ArrayList.

        Returns:
            bool: operador que indica si el ADT ArrayList es del mismo tipo que el elemento que se quiere procesar.
        """
        # TODO check usability of this function
        # if the structure is not empty, check the first element type
        if not self.is_empty():
            # get the type of the first element
            lt_type = type(self.elements[0])
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for element info: {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el ArrayList está vacía.

        Returns:
            bool: operador que indica si la estructura ArrayList está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el número de elementos que actualmente contiene el ArrayList.

        Returns:
            int: tamaño de la estructura ArrayList.
        """
        # TODO change the method to @property "size"?
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def add_first(self, element: T) -> None:
        """*add_first()* adiciona un elemento al inicio del ArrayList.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                self.elements.insert(0, element)
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """*add_last()* adiciona un elemento al final del ArrayList.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                self.elements.append(element)
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """*add_element()* adiciona un elemento en una posición dada del ArrayList.

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
                        raise IndexError(f"Index {pos} is out of range")
                    self.elements.insert(pos, element)
                    self._size += 1
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

    def get_first(self) -> T:
        """*get_first()* lee el primer elemento del ArrayList.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el primer elemento del ArrayList.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            return self.elements[0]
        except Exception as err:
            self._handle_error(err)

    def get_last(self) -> T:
        """*get_last()* lee el último elemento del ArrayList.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el ultimo elemento del ArrayList.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            return self.elements[self._size - 1]
        except Exception as err:
            self._handle_error(err)

    def get_element(self, pos: int) -> T:
        """*get_element()* lee un elemento en una posición dada del ArrayList.

        Args:
            pos (int): índice en la que se quiere agregar el elemento.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición es inválida.

        Returns:
            T: el elemento en la posición dada del ArrayList.
        """
        # TODO change the method name to "get_elm()"?
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size - 1:
                raise IndexError(f"Index {pos} is out of range")
            return self.elements[pos]
        except Exception as err:
            self._handle_error(err)

    def remove_first(self) -> T:
        """*remove_first()* elimina el primer elemento del ArrayList.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el primer elemento eliminado del ArrayList.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            element = self.elements.pop(0)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def remove_last(self) -> T:
        """*remove_last()* elimina el último elemento del ArrayList.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el ultimo elemento eliminado del ArrayList.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            element = self.elements.pop(self._size - 1)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def remove_element(self, pos: int) -> T:
        """*remove_element()* elimina un elemento en una posición dada del ArrayList.

        Args:
            pos (int): índice del que se quiere eliminar el elemento.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.

        Returns:
            T: el elemento eliminado del ArrayList.
        """
        # TODO change the method name to "remove_elm()"?
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self._size - 1:
                raise IndexError(f"Index {pos} is out of range")
            element = self.elements.pop(pos)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """*compare_elements()* compara dos elementos dentro del ArrayList según la función de comparación definida por el usuario o la función por defecto.

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
        """*find()* revisa si un elemento está en el ArrayList.

        Args:
            element (T): elemento que se quiere revisar en el ArrayList.

        Returns:
            int: la posición del elemento en el ArrayList, -1 si no está.
        """
        # TODO change the method name to "find()"?
        try:
            pos = -1
            lt_size = self.size()
            if lt_size > 0:
                found = False
                i = 0
                while not found and i < lt_size - 1:
                    data = self.get_element(i)
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
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
            elif pos < 0 or pos > self._size - 1:
                raise IndexError(f"Index {pos} is out of range")
            # if not self._check_type(new_info):
            elif self._check_type(new_info):
                # raise TypeError("Invalid element type")
                self.elements[pos] = new_info
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
                raise IndexError(f"Index {pos1} is out of range")
            elif pos2 < 0 or pos2 > self._size - 1:
                raise IndexError(f"Index {pos2} is out of range")
            info_pos1 = self.get_element(pos1)
            info_pos2 = self.get_element(pos2)
            self.change_info(info_pos2, pos1)
            self.change_info(info_pos1, pos2)
        except Exception as err:
            self._handle_error(err)

    def sublist(self, start: int, end: int) -> "ArrayList[T]":
        """*sublist()* crea una sublista de la estructura según unas posiciones dentro del ArrayList original.

        Args:
            start (int): índice inicial de la sublista.
            end (int): índice final de la sublista.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición inicial o final son inválidas.

        Returns:
            ArrayList[T]: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self._size - 1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = ArrayList(cmp_function=self.cmp_function,
                               key=self.key)
            i = start
            while i < end + 1:
                element = self.get_element(i)
                if self._check_type(element):
                    sub_lt.add_last(element)
                i += 1
            # sub_lt._size = len(sub_lt.elements)
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "ArrayList[T]") -> "ArrayList[T]":
        """*concat()* concatena dos estructuras de datos ArrayList para crear una nueva estructura con los elementos de las dos estructuras.

        Args:
            other (ArrayList[T]): estructura de datos ArrayList que se quiere concatenar con la estructura original.

        Raises:
            TypeError: error si la estructura que se quiere concatenar no es un ArrayList.
            TypeError: error si la llave de la estructura que se quiere unir no es la misma que la llave de la estructura original.
            TypeError: error si la función de comparación de la estructura que se quiere unir no es la misma que la función de comparación de la estructura original.

        Returns:
            ArrayList[T]: Estructura de datos original ArrayList que contiene los elementos de las dos estructuras originales.
        """
        try:
            if not isinstance(other, ArrayList):
                err_msg = f"Structure is not an ArrayList: {type(other)}"
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
            # concatenate the elements of the two lists
            self.elements = self.elements + other.elements
            # update the size of the new list
            self._size = self._size + other._size
            return self
        except TypeError as err:
            self._handle_error(err)

    def __iter__(self):
        """*__iter__()* iterador nativo de Python intervenida por la estructura de datos para recorrer los elementos del ArrayList utilizando un ciclo 'for' de python.

        Returns:
            __iter__: iterador Python sobre los elementos del ArrayList.
        """
        try:
            return iter(self.elements)
        except Exception as err:
            self._handle_error(err)

    def __len__(self) -> int:
        """*__len__()* función nativa de Python intervenida por la estructura de datosv para recuperar el tamaño del ArrayList.

        Returns:
            int: tamaño del ArrayList.
        """
        return self._size
