""" Esta clase representa un nodo de información de una estructura de datos
    dinámica, las cuales pueden ser: listas sencillas, listas doblemente
    encadenadas, pilas, colas, BST, RBT, entre otras.

    Este código está basado en la implementación propuesta por los libros
    con algunas modificaciones para adaptarlo a Python.
        1) Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
        2) Data Structures and Algorithms in Python, Michael T. Goodrich,
            Roberto Tamassia y Michael H. Goldwasser.

Attributes:
    T (type): variable que representa el tipo de dato de los elementos
        contenidos en el Node, SingleNode o DoubleNode.

Class:
    Node(Generic[T]): representa un nodo de una lista sencilla o doblemente
        encadenada.

    Funciones:
        - __post_init__: inicializa el nodo con la información recibida
            como argumento.
        - _handle_error: maneja el error recibido como argumento.
        - _check_type: verifica el tipo de la información recibida como
            argumento.
        - set_info: establece la información del nodo.
        - get_info: retorna la información del nodo.

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería,
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
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
from DISClib.Utils.error import init_type_checker
from DISClib.Utils.default import T

# checking costum modules
assert error_handler
assert init_type_checker
assert T


@dataclass
class Node(Generic[T]):
    """Node Clase que representa un nodo de una lista sencilla o doblemente
        encadenada. Contiene la información del nodo y las funciones
        basicas para acceder a ella.

    Args:
        Generic (T): TAD/ADT que representa el tipo de dato de la
        información dentro del nodo.

    Attributes:
        info (T): información del nodo.

    Raises:
        TypeError: error si la información del nodo no es del tipo
            especificado.

    Returns:
        Node: ADT de tipo Node o nodo de información.
    """
    # optional information of any type
    info: Optional[T] = None

    def __post_init__(self):
        """__post_init__ revisa que la información del nodo sea de un tipo
            válido.
        """
        try:
            # if the info attribute is not None, check its type
            if self.info is not None:
                cur_function = inspect.currentframe().f_code.co_name
                cur_context = self.__class__.__name__
                init_type_checker(cur_context, cur_function, self.info)
        # if an error occurs, handle it
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error función privada que maneja los errores que se
            presentan en la clase Node.

            Si se presenta un error en el Node, se formatea el error según
            el contexto (paquete/clase) y la función que lo generó, y lo
            reenvia al componente superior en la jerarquía de llamados para
            manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el Node.
        """
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> None:
        """_check_type función privada que verifica que la información del
            nodo sea del tipo especificado.

        Args:
            element (T): elemento que se quiere verificaren el nodo.

        Raises:
            TypeError: error si la información del nodo no es del tipo
                especificado.

        Returns:
            _type_: operador que indica si el tipo de dato del elemento
                es el mismo que el tipo de dato de los elementos que ya
                contiene la estructura de datos.
        """
        if element is not None and not isinstance(element, type(self.info)):
            err_msg = f"Invalid data type: {type(self.info)} "
            err_msg += f"for element info: {type(element)}"
            raise TypeError(err_msg)
        return True

    def set_info(self, info: T) -> None:
        """set_info introduce la información al nodo.

        Args:
            info (T): información que se quiere introducir al nodo.
        """
        if self.info is not None:
            self._check_type(info)
        self.info = info

    def get_info(self) -> T:
        """get_info recupera la información del nodo.

        Returns:
            T: información del nodo.
        """
        return self.info
