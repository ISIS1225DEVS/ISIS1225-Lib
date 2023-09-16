"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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


def handle_error(context: str, func_name: str, err: Exception) -> None:
    """handle_error _summary_

    Args:
        context (str): _description_
        func_name (str): _description_
        err (Exception): _description_

    Raises:
        type: _description_
    """    
    err_msg = f"Error in {context}.{func_name}: {err}"
    raise type(err)(err_msg).with_traceback(err.__traceback__)

# def reraise(excp, *args):
#     """
#     Estructura que contiene la información a guardar en una lista encadenada
#     """
#     excp.args = args + excp.args
#     raise excp.with_traceback(excp.__traceback__)
