"""
Este ADT representa la registro de un Mapa no Ordenado (MapEntry), el cual es una estructura de datos dinámica que permite almacenar la información en parejas de llave-valor (key-value). La llave (key) es un identificador único para cada valor (value) almacenado en el Mapa no Ordenado (Map). Por su parte, el valor (value) puede ser cualquier tipo de dato.

En el caso de las tablas de Hash, la llave (key) es el resultado de aplicar una función hash al valor (value) almacenado en el Mapa no Ordenado (Map). Esta estructura de datos es fundamental para implementar otros mapas no ordenados como: tablas de símbolos, diccionarios, entre otros.

DISCLib utiliza el MapEntry para guardar la información de las tablas de Hash por Encadenamiento Separado (Separate Chaining) y las tablas por Sondeo Lineal (Linear Probing).

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


# native python modules
# import dataclass for defining the node class
from dataclasses import dataclass
# import modules for defining the MapEntry type
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
class MapEntry(Generic[T]):
    """**MapEntry** representa un registro de un mapa no ordenado. Contiene la llave y el valor del registro del mapa. Donde la llave es única para cada valor y el valor puede ser cualquier tipo de dato.

    Args:
        Generic (T): Tipo de dato genérico dentro del registro del mapa.

    Raises:
        TypeError: error si la información del registro del mapa (llave o valor) no son del tipo adecuado.

    Returns:
        MapEntry: ADT de tipo MapEntry o registro de un mapa.
    """

    # optional key of any type
    # :attr: _key
    _key: Optional[T] = None
    """
    Es la llave del registro del mapa.
    """
    # optional value of any type
    # _value
    _value: Optional[T] = None
    """
    Es el valor del registro del mapa.
    """

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función privada para manejar los errores que se presentan en la clase MapEntry.

        Si se presenta un error en el MapEntry, se formatea el error según el contexto (paquete/clase) y la función que lo generó, y lo reenvia al componente superior en la jerarquía de llamados para manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el MapEntry.
        """
        cur_function = inspect.currentframe().f_code.co_name
        cur_context = self.__class__.__name__
        error_handler(cur_context, cur_function, err)

    def _check_key_type(self, key: T) -> bool:
        """*_check_key_type()* función privada que verifica que la información de la llave (key) del registro del mapa sea del tipo especificado.

        Args:
            key (T): llave que se quiere verificar en el registro del mapa.

        Raises:
            TypeError: error si la información del registro del mapa no es del tipo adecuado.

        Returns:
            bool: operador que indica si el tipo de dato de la llave es el mismo que el tipo de dato de la llave que ya contiene la estructura de datos.
        """
        # TODO check usability of this function
        if not isinstance(key, type(self._key)):
            err_msg = f"Invalid data type: {type(self._key)} "
            err_msg += f"for key data: {type(key)}"
            raise TypeError(err_msg)
        return True

    def _check_value_type(self, value: T) -> bool:
        """*_check_value_type()* función privada que verifica que la información del valor (value) en el registro del mapa sea del tipo especificado.

        Args:
            value (T): valor que se quiere verificar en el registro del mapa.

        Raises:
            TypeError: error si la información del registro del mapa no es del tipo adecuado.

        Returns:
            bool: operador que indica si el tipo de dato del valor es el mismo que el tipo de dato de los elementos que ya contiene la estructura de datos.
        """
        # TODO check usability of this function
        if not isinstance(value, type(self._value)):
            err_msg = f"Invalid data type: {type(self._value)} "
            err_msg += f"for value data: {type(value)}"
            raise TypeError(err_msg)
        return True

    def set_key(self, key: T) -> None:
        """*set_key()* introduce una nueva llave 'key' al registro del mapa.

        Args:
            key (T): la nueva llave del registro del mapa.
        """
        if self._key is not None:
            self._check_key_type(key)
        self._key = key

    def set_value(self, value: T) -> None:
        """*set_value()* introduce un nuevo valor 'value' al registro del mapa.

        Args:
            value (T): el nuevo valor del registro del mapa.
        """
        if self._value is not None:
            self._check_value_type(value)
        self._value = value

    def get_key(self) -> T:
        """*get_key()* recupera la llave 'key' contenida en el registro del mapa.

        Returns:
            T: la llave del registro del mapa.
        """
        return self._key

    def get_value(self) -> T:
        """*get_value()* recupera el valor 'value' contenido en el registro del mapa.

        Returns:
            T: el valor del registro del mapa.
        """
        return self._value
