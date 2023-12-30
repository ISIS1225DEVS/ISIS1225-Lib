"""
**mock_structs** es un módulo para las pruebas unitarias del módulo que importa dinámicamente otros módulos y estructuras dentro de *DISClib*.

Contiene dos estructuras de datos sencillas y genéricas en python para pruebas unitarias.
"""
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class DataStructA(Generic[T]):
    """**DataStructA** es una estructura de datos genérica para pruebas unitarias.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        DataStructA: Una estructura de datos genérica para pruebas unitarias.
    """
    data: Optional[T] = None

    def get_data(self) -> Optional[T]:
        """**get_data** obtiene los datos de la estructura de datos.

        Returns:
            Optional[T]: Los datos de la estructura de datos.
        """
        return self.data


@dataclass
class DataStructB(Generic[T]):
    """**DataStructB** es una estructura de datos genérica para pruebas unitarias.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        DataStructB: Una estructura de datos genérica para pruebas unitarias.
    """
    data: Optional[T] = None

    def get_data(self) -> Optional[T]:
        """**get_data** obtiene los datos de la estructura de datos.

        Returns:
            Optional[T]: Los datos de la estructura de datos.
        """
        return self.data
