:py:mod:`DISClib.ADT.orderedmap`
================================

.. py:module:: DISClib.ADT.orderedmap

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

   DISClib.ADT.orderedmap.newMap
   DISClib.ADT.orderedmap.put
   DISClib.ADT.orderedmap.get
   DISClib.ADT.orderedmap.remove
   DISClib.ADT.orderedmap.contains
   DISClib.ADT.orderedmap.size
   DISClib.ADT.orderedmap.isEmpty
   DISClib.ADT.orderedmap.keySet
   DISClib.ADT.orderedmap.valueSet
   DISClib.ADT.orderedmap.minKey
   DISClib.ADT.orderedmap.maxKey
   DISClib.ADT.orderedmap.deleteMin
   DISClib.ADT.orderedmap.deleteMax
   DISClib.ADT.orderedmap.floor
   DISClib.ADT.orderedmap.ceiling
   DISClib.ADT.orderedmap.select
   DISClib.ADT.orderedmap.rank
   DISClib.ADT.orderedmap.height
   DISClib.ADT.orderedmap.keys
   DISClib.ADT.orderedmap.values
   DISClib.ADT.orderedmap.mapSelector



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.orderedmap.switch_module


.. py:function:: newMap(omaptype='RBT', cmpfunction=None)

   Crea una tabla de simbolos ordenada.
   :param maptype: El tipo de map ordenado a utilizar
                   'BST' o 'RBT'

   :returns: La tabla de símbolos ordenada sin elementos

   :raises Exception:


.. py:function:: put(map, key, value)

   Ingresa una pareja llave,valor. Si la llave ya existe,
   se reemplaza el valor.
   :param map: La tabla de simbolos ordenada
   :param key: La llave asociada a la pareja
   :param value: El valor asociado a la pareja

   :returns: La tabla de simbolos

   :raises Exception:


.. py:function:: get(map, key)

   Retorna la pareja lleve-valor con llave igual a key
   :param map: La tabla de simbolos
   :param key: La llave asociada a la pareja

   :returns: La tabla de simbolos con la nueva pareja

   :raises Exception:


.. py:function:: remove(map, key)

   Elimina la pareja llave,valor, donde llave == key.
   :param map: La tabla de simbolos
   :param key: La llave asociada a la pareja

   :returns: La tabla de simbolos

   :raises Exception:


.. py:function:: contains(map, key)

   Informa si la llave key se encuentra en la tabla de hash
   :param map: La tabla de simbolos
   :param key: La llave a buscar

   :returns: True si la llave está presente, False en caso contrario

   :raises Exception:


.. py:function:: size(map)

   Retorna el número de entradas en la tabla de simbolos
   :param map: La tabla de simbolos

   :returns: El número de elementos en la tabla

   :raises Exception:


.. py:function:: isEmpty(map)

   Informa si la tabla de simbolos se encuentra vacia
   :param map: La tabla de simbolos

   :returns: True si la tabla es vacía, False en caso contrario

   :raises Exception:


.. py:function:: keySet(map)

   Retorna una lista con todas las llaves de la tabla
   :param map: La tabla de simbolos

   :returns: Una lista con todas las llaves de la tabla

   :raises Exception:


.. py:function:: valueSet(map)

   Construye una lista con los valores de la tabla
   :param map: La tabla con los elementos

   :returns: Una lista con todos los valores

   :raises Exception:


.. py:function:: minKey(map)

   Retorna la menor llave de la tabla de simbolos
   :param map: La tabla de simbolos

   :returns: La menor llave de la tabla

   :raises Exception:


.. py:function:: maxKey(map)

   Retorna la mayor llave de la tabla de simbolos
   :param map: La tabla de simbolos

   :returns: La mayor llave de la tabla

   :raises Exception:


.. py:function:: deleteMin(map)

   Encuentra y remueve la menor llave de la tabla de simbolos
   y su valor asociado
   :param map: La tabla de simbolos

   :returns: La tabla de simbolos sin la menor llave

   :raises Exception:


.. py:function:: deleteMax(map)

   Encuentra y remueve la mayor llave de la tabla de simbolos
   y su valor asociado
   :param map: La tabla de simbolos

   :returns: La tabla de simbolos sin la mayor llave

   :raises Exception:


.. py:function:: floor(map, key)

   Retorna la llave mas grande en la tabla de simbolos,
   menor o igual a la llave key
   :param map: La tabla de simbolos
   :param key: La llave de búsqueda

   :returns: La llave más grande menor o igual a key

   :raises Exception:


.. py:function:: ceiling(map, key)

   Retorna la llave mas pequeña en la tabla de simbolos,
   mayor o igual a la llave key
   :param map: La tabla de simbolos
   :param key: la llave de búsqueda

   :returns: La llave más pequeña mayor o igual a Key

   :raises Exception:


.. py:function:: select(map, k)

   Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
   :param map: La tabla de simbolos
   :param pos: la pos-esima llave mas pequeña

   :returns: La llave más pequeña mayor o igual a Key

   :raises Exception:


.. py:function:: rank(map, key)

   Retorna el número de llaves en la tabla estrictamente menores que key
   :param map: La tabla de simbolos
   :param pos: la pos-esima llave mas pequeña

   :returns: La llave más pequeña mayor o igual a Key

   :raises Exception:


.. py:function:: height(map)

   Retorna la altura del arbol de busqueda
   :param map: La tabla de simbolos

   :returns: La altura del arbol

   :raises Exception:


.. py:function:: keys(map, keylo, keyhi)

   Retorna todas las llaves del arbol que se encuentren entre
   [keylo, keyhi]

   :param map: La tabla de simbolos
   :param keylo: limite inferior
   :param keylohi: limite superiorr

   :returns: Las llaves en el rago especificado

   :raises Exception:


.. py:function:: values(map, keylo, keyhi)

   Retorna todas los valores del arbol que se encuentren entre
   [keylo, keyhi]

   :param map: La tabla de simbolos
   :param keylo: limite inferior
   :param keylohi: limite superiorr

   :returns: Las llaves en el rago especificado

   :raises Exception:


.. py:data:: switch_module

   

.. py:function:: mapSelector(datastructure)

   Carga dinamicamente el import de la estructura de datos
   seleccionada


