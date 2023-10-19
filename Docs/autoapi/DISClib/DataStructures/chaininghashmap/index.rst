:py:mod:`DISClib.DataStructures.chaininghashmap`
================================================

.. py:module:: DISClib.DataStructures.chaininghashmap

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

   DISClib.DataStructures.chaininghashmap.newMap
   DISClib.DataStructures.chaininghashmap.contains
   DISClib.DataStructures.chaininghashmap.put
   DISClib.DataStructures.chaininghashmap.get
   DISClib.DataStructures.chaininghashmap.remove
   DISClib.DataStructures.chaininghashmap.size
   DISClib.DataStructures.chaininghashmap.isEmpty
   DISClib.DataStructures.chaininghashmap.keySet
   DISClib.DataStructures.chaininghashmap.valueSet
   DISClib.DataStructures.chaininghashmap.rehash
   DISClib.DataStructures.chaininghashmap.hashValue
   DISClib.DataStructures.chaininghashmap.isPrime
   DISClib.DataStructures.chaininghashmap.nextPrime
   DISClib.DataStructures.chaininghashmap.defaultcompare



.. py:function:: newMap(numelements, prime, loadfactor, cmpfunction, datastructure)

   Crea una tabla de simbolos (map) sin orden

   Crea una tabla de hash con capacidad igual a nuelements
   (primo mas cercano al doble de numelements).
   prime es un número primo utilizado para  el cálculo de los codigos
   de hash, si no es provisto se  utiliza el primo 109345121.

   :param numelements: Tamaño inicial de la tabla
   :param prime: Número primo utilizado en la función MAD
   :param loadfactor: Factor de carga inicial de la tabla
   :param cmpfunc: Funcion de comparación entre llaves

   :returns: Un nuevo map

   :raises Exception:


.. py:function:: contains(map, key)

   Retorna True si la llave key se encuentra en el map
       o False en caso contrario.
   :param map: El map a donde se guarda la pareja
   :param key: la llave asociada a la pareja

   :returns: True / False

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


.. py:function:: rehash(map)

   Se aumenta la capacida de la tabla al doble y se hace
   rehash de todos los elementos de la tabla


.. py:function:: hashValue(table, key)

   Calcula un hash para una llave, utilizando el método
   MAD : hashValue(y) = ((ay + b) % p) % M.
   Donde:
   M es el tamaño de la tabla, primo
   p es un primo mayor a M,
   a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0


.. py:function:: isPrime(n)


.. py:function:: nextPrime(N)


.. py:function:: defaultcompare(key, element)


