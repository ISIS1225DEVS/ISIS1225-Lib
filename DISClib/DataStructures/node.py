"""
Este ADT representa un nodo **Node** de información de una estructura de datos dinámica, las cuales pueden ser: listas sencillas, listas doblemente encadenadas, pilas, colas, BST, RBT, entre otras.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


# native python modules
# import dataclass for defining the node class
from dataclasses import dataclass
# import modules for defining the Node type
from typing import Generic, Optional
# import inspect for getting the name of the current function
import inspect

# custom modules
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.default import T

# checking custom modules
assert error_handler
assert T


@dataclass
class Node(Generic[T]):
    """**Node** Es el ADT que representar la información de un nodo de una estructura de datos dinámica y las funciones basicas para acceder a ella. Puede utilizarse para representar un nodo de una lista sencilla o doblemente encadenada.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        Node: ADT de tipo *Node* o nodo de información.
    """
    # optional information of any type
    # :attr: info
    info: Optional[T] = None
    """
    Es la información contenida en el nodo.
    """

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *Node*.

        Si se presenta un error en *SingleLinked*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DISCLib* para manejarlo segun se considere conveniente el usuario.

        Args:
            err (Exception): Excepción que se generó en el *Node*.
        """
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función propia de la estructura que verifica que la información de *Node* sea del tipo adecuado.

        Args:
            element (T): elemento que se desea procesar en *Node*.

        Raises:
            TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *Node*.

        Returns:
            bool: operador que indica si el ADT *Node* es del mismo tipo que el elemento que se desea procesar.
        """
        if not isinstance(element, type(self.info)):
            err_msg = f"Invalid data type: {type(self.info)} "
            err_msg += f"for element info: {type(element)}"
            raise TypeError(err_msg)
        return True

    def set_info(self, info: T) -> None:
        """*set_info()* establece la información de *Node*.

        Args:
            info (T): información que se desea actualizar en *Node*.
        """
        if self.info is not None:
            self._check_type(info)
        self.info = info

    def get_info(self) -> T:
        """*get_info()* recupera la información de *Node*.

        Returns:
            T: información de *Node*.
        """
        return self.info
