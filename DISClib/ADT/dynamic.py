"""
 * Copyright 2020, Departamento de sistemas y Computación,
 Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

import importlib


class DynamicImporter(object):
    """DynamicImporter _summary_

    Args:
        object (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """    
    package: str = ""
    implementation: str = ""
    _module = None
    _class = None
    _instance = None

    def __init__(self, implementation: str, package: str, **kwargs):
        """__init__ _summary_

        Args:
            implementation (str): _description_
            package (str): _description_

        Raises:
            ValueError: _description_
        """
        try:
            self.package = package   # __import__(package)
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
        """__post_init__ _summary_
        """
        self.__class__.__name__ = self.implementation

    def __repr__(self) -> str:
        """__repr__ _summary_

        Returns:
            str: _description_
        """
        return self._instance.__repr__()

    def __getattr__(self, name):
        """__getattr__ _summary_

        Args:
            name (_type_): _description_

        Returns:
            _type_: _description_
        """
        # delegate attribute access to the implementation instance
        return getattr(self._instance, name)

    def start(self):
        """start _summary_

        Returns:
            _type_: _description_
        """
        # FIXME this is a hack!!!
        return self._instance

    @classmethod
    def __class__(self) -> type:
        """__class__ _summary_

        Returns:
            type: _description_
        """
        # FIXME this is not working
        # delegate type() to the implementation instance
        return self._instance.__class__

    @classmethod
    def __instancecheck__(self, instance) -> bool:
        """__instancecheck__ _summary_

        Args:
            instance (_type_): _description_

        Returns:
            bool: _description_
        """
        # check if the instance is an instance of the implementation class
        # FIXME this is not working
        return isinstance(instance, self._instance.__class__)
