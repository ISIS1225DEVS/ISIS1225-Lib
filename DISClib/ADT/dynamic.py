"""
Este módulo permite importar dinámicamente otros módulos, funciones y estructuras de datos (ADTs) dentro de *DISClib*. En ves de importar los ADTs de manera estática, se puede importar dinámicamente según la configuración de un diccionario (o archivo JSON) y las especificaciones del usuario.

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
Ruta relativa del paquete principal para las estructuras de datos.
"""

# main package ADT path
# :param ADT_PGK_PATH
ADT_PGK_PATH: str = "DISClib.ADT"
"""
Ruta relativa del paquete principal para crear los ADTs.
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
        """*__init__()* crea la clase dinámica. Permite importar dinámicamente módulos, estructuras (ADTs) y sus funciones según la configuración de un diccionario (o archivo JSON) y las especificaciones del usuario.

        Args:
            implementation (str): implementación de la clase dinámica seleccionada.
            package (str): referencia al paquete de la clase dinámica.

        Raises:
            ValueError: no se puede importar el módulo especificado.
        """
        try:
            self.package = package
            self.implementation = implementation
            self._module = importlib.import_module(self.package)
            self._class = None
            self._instance = None
        except ModuleNotFoundError:
            err_msg = f"Invalid implementation of: {self.implementation}"
            raise ValueError(err_msg)
        # get the class from the module
        self._class = getattr(self._module,
                              self.implementation)
        self._instance = self._class(**kwargs)

    def get_instance(self):
        """*get_instance()* retorna la instancia de la clase concreta seleccionada por el usuario.

        Returns:
            dataclass: instancia de la clase concreta seleccionada.
        """
        # FIXME this is a hack!!!
        return self._instance
