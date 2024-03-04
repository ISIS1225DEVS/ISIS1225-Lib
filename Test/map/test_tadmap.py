"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
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
 """

import pytest
import config
from DISClib.ADT import map as ht
from DISClib.ADT.map import switch_module


assert config

capacity = 50
loadfactor = 2


def test_invalid_map():
    """
    Prueba para comprobar que se lanza una excepción cuando se intenta crear un mapa con un tipo de estructura de datos no soportada.
    """

    with pytest.raises(Exception) as excinfo:

        ht.newMap(numelements=capacity, maptype="INVALID", loadfactor=loadfactor)

    assert (
        f"Tipo de estructura de datos no soportada. Solo se soportan: {', '.join(switch_module.keys())}"
        in str(excinfo.value)
    )


def test_create_valid_lists():
    """
    Prueba para comprobar que se crean mapas de manera correcta.
    """
    for datastructure in switch_module.keys():
        mp = ht.newMap(
            numelements=capacity, maptype=datastructure, loadfactor=loadfactor
        )
        assert mp is not None
        assert ht.size(mp) == 0
