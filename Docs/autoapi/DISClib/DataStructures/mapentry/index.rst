:py:mod:`DISClib.DataStructures.mapentry`
=========================================

.. py:module:: DISClib.DataStructures.mapentry

.. autoapi-nested-parse::

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
   *
   * Contribución de:
   *
   * Dario Correal
   *



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.mapentry.newMapEntry
   DISClib.DataStructures.mapentry.setKey
   DISClib.DataStructures.mapentry.setValue
   DISClib.DataStructures.mapentry.getKey
   DISClib.DataStructures.mapentry.getValue



.. py:function:: newMapEntry(key, value)

   Retorna una pareja llave valor para ser guardada
   en un Map
   :param key: llave
   :param value: valor

   :returns: una entrada con la pareja llave-valor

   :raises Exception:


.. py:function:: setKey(entry, key)

   Asigna una llave a una pareja de un Map
   :param entry: la pareja llave valor
   :param key: la nueva llave

   :returns: La pareja modificada

   :raises Exception:


.. py:function:: setValue(entry, value)

   Asigna un nuevo valor a una pareja de un Map
   :param entry: la pareja llave valor
   :param value: el nuevo valor

   :returns: La pareja modificada

   :raises Exception:


.. py:function:: getKey(entry)

   Retorna la llave de una pareja de un Map
   :param entry: la pareja llave valor

   :returns: La llave de la pareja

   :raises Exception:


.. py:function:: getValue(entry)

   Retorna el valor de una pareja de un Map
   :param entry: la pareja llave valor

   :returns: La llave de la pareja

   :raises Exception:


