"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

from DISClib.ADT import lists as lt

"""
  Los algoritmos de este libro están basados en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""

# FIXME: pasar a snake_case de python
# FIXME: cambiar pruebas unitarias de acuerdo a los cambios realizados


# FIXME: tipar entradas y salidas de la funcion
# TODO agregar manejo de excepciones a la funcion
# TODO mejorar la descricion de la funcion
def partition(lst, lo, hi, sort_crit):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           lt.getElement(lst, leader), lt.getElement(lst, hi)):
            lt.exchange(lst, follower, leader)
            follower += 1
        leader += 1
    lt.exchange(lst, follower, hi)
    return follower


# FIXME: tipar entradas y salidas de la funcion
# TODO agregar manejo de excepciones a la funcion
# TODO mejorar la descricion de la funcion
def quicksort(lst, lo, hi, sort_crit):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lst, lo, hi, sort_crit)
    quicksort(lst, lo, pivot-1, sort_crit)
    quicksort(lst, pivot+1, hi, sort_crit)


# FIXME: tipar entradas y salidas de la funcion
# TODO agregar manejo de excepciones a la funcion
# TODO mejorar la descricion de la funcion
def sort(lst, sort_crit):
    quicksort(lst, 1, lt.size(lst), sort_crit)
    return lst
