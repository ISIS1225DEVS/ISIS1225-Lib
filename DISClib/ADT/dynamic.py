"""
Este módulo permite importar dinámicamente módulos, funciones y estructuras de datos (ADTs) de módulos dentro de DISClib según las especificaciones del usuario.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import for dytamic module support
import importlib

# main package data structure path
# :param STRUCT_PGK_PATH
STRUCT_PGK_PATH: str = "DISClib.DataStructures"
"""
Ruta relativa del paquete principal para instanciar el ADT List.
"""


class DynamicImporter:
    """ **DynamicImporter** permite importar dinámicamente módulos y clases de módulos según la configuración de un archivo JSON y las especificaciones del usuario.

    Raises:
        ValueError: no se puede importar el módulo especificado.

    Returns:
        DynamicImporter: instancia de la clase dinámica.
    """
    # package name in build directory
    # :param package
    package: str = ""
    """
    Nombre del paquete en el directorio de compilación.
    """

    # package name in src directory
    # :param implementation
    implementation: str = ""
    """
    Nombre del paquete en el directorio dentro del código fuente.
    """

    # private dynamic module reference
    # :param _module
    _module = None
    """
    Referencia privada al módulo dinámico.
    """
    # private dynamic class reference
    # :param _class
    _class = None
    """
    Referencia privada a la clase dinámica seleccionada.
    """
    # private dynamic class instance reference
    # :param _instance
    _instance = None
    """
    Referencia privada a la instancia de la clase dinámica seleccionada.
    """

    def __init__(self, implementation: str, package: str, **kwargs):
        """*__init__()* Constructor de la clase dinámica. Permite importar dinámicamente módulos y clases de módulos según la configuración de un archivo JSON y las especificaciones del usuario.

        Args:
            implementation (str): implementación de la clase dinámicA seleccionada.
            package (str): referencia al paquete de la clase dinámica.

        Raises:
            ValueError: no se puede importar el módulo especificado.
        """
        # TODO add docstring
        try:
            self.package = package
            self.implementation = implementation
            self._module = importlib.import_module(self.package)
            self._class = None
            self._instance = None
        except ModuleNotFoundError:
            err_msg = f"Invalid implementation: {self.implementation}"
            raise ValueError(err_msg)
        self._class = getattr(self._module,
                              self.implementation)
        self._instance = self._class(**kwargs)

    def __post_init__(self):
        """*__post_init__()* función post inicialización. Permite cambiar el nombre de la clase dinámica por el nombre de la clase concreta seleccionada por el usuario.
        """
        self.__class__.__name__ = self.implementation

    def __repr__(self) -> str:
        """*__repr__* función de representación. Permite representar la clase dinámica como la clase concreta seleccionada por el usuario.

        Returns:
            str: representación de la clase concreta seleccionada.
        """
        return self._instance.__repr__()

    def get_instance(self):
        """*get_instance()* retorna la instancia de la clase concreta seleccionada por el usuario.

        Returns:
            dataclass: instancia de la clase concreta seleccionada.
        """
        # FIXME this is a hack!!!
        return self._instance

    @classmethod
    def __class__(self) -> type:
        """*__class__* retorna el tipo de la clase concreta seleccionada por el usuario.

        Returns:
            type: tipo de la clase concreta seleccionada.
        """
        # FIXME this is not working
        # delegate type() to the implementation instance
        return self._instance.__class__

    @classmethod
    def __instancecheck__(self, instance) -> bool:
        """*__instancecheck__* permite verificar si una instancia es de la clase concreta seleccionada por el usuario.

        Args:
            instance (T): instancia a verificar.

        Returns:
            bool: True si la instancia es de la clase concreta seleccionada.
        """
        # FIXME this is not working
        # check if the instance is an instance of the implementation class
        return isinstance(instance, self._instance.__class__)
