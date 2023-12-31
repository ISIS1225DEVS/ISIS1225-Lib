"""
# TODO: agregar descripción del módulo

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
from DISClib.DataStructures.treenode import BSTNode
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import lt_default_cmp_funcion
from DISClib.Utils.default import T
from DISClib.Utils.default import DEFAULT_DICT_KEY
from DISClib.Utils.default import VALID_IO_TYPE

# checking custom modules
assert BSTNode
assert error_handler
assert lt_default_cmp_funcion
assert T
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE


@dataclass
class BinarySearchTree(Generic[T]):
    """**BinarySearchTree** representa la estructura de datos para arreglos dinamicos (Array List), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        BinarySearchTree: ADT de tipo BinarySearchTree o Arreglo Dinámico.

    """
    # input elements from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación personalizable por el usuario para reconocer los elementos dentro de la estructura. Es un argumento configurable al crear la estructura. Por defecto es la función *lt_default_cmp_funcion()* propia de *DISClib*.
    """

    # using default_factory to generate an empty list
    # :attr: elements
    elements: List[T] = field(default_factory=list)
    """
    Lista nativa de Python que contiene los elementos de la estructura.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave opcional que se utiliza para comparar los elementos del BinarySearchTree, Por defecto es *None* y el *__post_init__()* configura la llave por defecto la llave 'id' en *DEFAULT_DICT_KEY*.
    """

    # by default, the list is empty
    # FIXME inconsistent use between _size and size()
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los valores por defecto para la llave ('key') y la función de comparación ('cmp_function'). Si el usuario incluye una lista nativa de python como argumento, se agrega a la lista de elementos del BinarySearchTree.
        """
        try:
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DEFAULT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if elements are in a list, add them to the BinarySearchTree
            # TODO sometime strange weird in tests
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """*default_cmp_function()* procesa con algoritmica por defecto la lista de elementos que procesa el BinarySearchTree. Es una función crucial para que la estructura de datos funcione correctamente.

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
        """*_handle_error()* función privada que maneja los errores que se pueden presentar en el BinarySearchTree.

        Si se presenta un error en BinarySearchTree, se formatea el error según el contexto (paquete/clase), la función que lo generó y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el BinarySearchTree.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función privada que verifica que el tipo de dato del elemento que se quiere agregar al BinarySearchTree sea del mismo tipo contenido dentro de los elementos del BinarySearchTree.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere agregar no es el mismo que el tipo de dato de los elementos que ya contiene el BinarySearchTree.

        Args:
            element (T): elemento que se quiere procesar en BinarySearchTree.

        Returns:
            bool: operador que indica si el ADT BinarySearchTree es del mismo tipo que el elemento que se quiere procesar.
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
