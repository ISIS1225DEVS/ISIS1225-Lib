:py:mod:`DISClib.ADT.maps`
==========================

.. py:module:: DISClib.ADT.maps

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

   DISClib.ADT.maps.newMap
   DISClib.ADT.maps.put
   DISClib.ADT.maps.get
   DISClib.ADT.maps.remove
   DISClib.ADT.maps.contains
   DISClib.ADT.maps.size
   DISClib.ADT.maps.isEmpty
   DISClib.ADT.maps.keySet
   DISClib.ADT.maps.valueSet
   DISClib.ADT.maps.mapSelector



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.maps.switch_module


.. py:function:: newMap(numelements=17, prime=109345121, maptype='CHAINING', loadfactor=0.5, cmpfunction=None)

   Crea una tabla de simbolos (map) sin orden

   :param numelements: Tamaño inicial de la tabla
   :param prime: Número primo utilizado en la función MAD
   :param maptype: separate chaining ('CHAINING' ) o linear probing('PROBING')
   :param loadfactor: Factor de carga inicial de la tabla
   :param cmpfunction: Funcion de comparación entre llaves

   :returns: Un nuevo map

   :raises Exception:


.. py:function:: put(map, key, value)

   Ingresa una pareja llave,valor a la tabla de hash.
   Si la llave ya existe en la tabla, se reemplaza el valor

   :param map: El map a donde se guarda la pareja
   :param key: la llave asociada a la pareja
   :param value: el valor asociado a la pareja

   :returns: El map

   :raises Exception:


.. py:function:: get(map, key)

   Retorna la pareja llave, valor, cuya llave sea igual a key
   :param map: El map a donde se guarda la pareja
   :param key: la llave asociada a la pareja

   :returns: Una pareja <llave,valor>

   :raises Exception:


.. py:function:: remove(map, key)

   Elimina la pareja llave,valor, donde llave == key.
   :param map: El map a donde se guarda la pareja
   :param key: la llave asociada a la pareja

   :returns: El map

   :raises Exception:


.. py:function:: contains(map, key)

   Retorna True si la llave key se encuentra en el map
       o False en caso contrario.
   :param map: El map a donde se guarda la pareja
   :param key: la llave asociada a la pareja

   :returns: True / False

   :raises Exception:


.. py:function:: size(map)

   Retorna  el número de entradas en la tabla de hash.
   :param map: El map

   :returns: Tamaño del map

   :raises Exception:


.. py:function:: isEmpty(map)

   Informa si la tabla de hash se encuentra vacia
   :param map: El map

   :returns: El map esta vacio
             False: El map no esta vacio
   :rtype: True

   :raises Exception:


.. py:function:: keySet(map)

   Retorna una lista con todas las llaves de la tabla de hash

   :param map: El map

   :returns: lista de llaves

   :raises Exception:


.. py:function:: valueSet(map)

   Retorna una lista con todos los valores de la tabla de hash

   :param map: El map

   :returns: lista de valores

   :raises Exception:


.. py:data:: switch_module

   

.. py:function:: mapSelector(datastructure)

   Carga dinamicamente el import de la estructura de datos
   seleccionada


