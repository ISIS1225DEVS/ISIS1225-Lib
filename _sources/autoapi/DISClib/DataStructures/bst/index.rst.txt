:py:mod:`DISClib.DataStructures.bst`
====================================

.. py:module:: DISClib.DataStructures.bst

.. autoapi-nested-parse::

   * Copyright 2020, Departamento de sistemas y Computación
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

   DISClib.DataStructures.bst.newMap
   DISClib.DataStructures.bst.put
   DISClib.DataStructures.bst.get
   DISClib.DataStructures.bst.remove
   DISClib.DataStructures.bst.contains
   DISClib.DataStructures.bst.size
   DISClib.DataStructures.bst.isEmpty
   DISClib.DataStructures.bst.keySet
   DISClib.DataStructures.bst.valueSet
   DISClib.DataStructures.bst.minKey
   DISClib.DataStructures.bst.maxKey
   DISClib.DataStructures.bst.deleteMin
   DISClib.DataStructures.bst.deleteMax
   DISClib.DataStructures.bst.floor
   DISClib.DataStructures.bst.ceiling
   DISClib.DataStructures.bst.select
   DISClib.DataStructures.bst.rank
   DISClib.DataStructures.bst.height
   DISClib.DataStructures.bst.keys
   DISClib.DataStructures.bst.values
   DISClib.DataStructures.bst.insertNode
   DISClib.DataStructures.bst.getNode
   DISClib.DataStructures.bst.removeNode
   DISClib.DataStructures.bst.sizeTree
   DISClib.DataStructures.bst.valueSetTree
   DISClib.DataStructures.bst.keySetTree
   DISClib.DataStructures.bst.minKeyNode
   DISClib.DataStructures.bst.maxKeyNode
   DISClib.DataStructures.bst.deleteMinTree
   DISClib.DataStructures.bst.deleteMaxTree
   DISClib.DataStructures.bst.floorKey
   DISClib.DataStructures.bst.ceilingKey
   DISClib.DataStructures.bst.selectKey
   DISClib.DataStructures.bst.rankKeys
   DISClib.DataStructures.bst.heightTree
   DISClib.DataStructures.bst.keysRange
   DISClib.DataStructures.bst.valuesRange
   DISClib.DataStructures.bst.defaultfunction



.. py:function:: newMap(omaptype, cmpfunction, datastructure)

   Crea una tabla de simbolos ordenada.
   :param compfunction: La funcion de comparacion

   :returns: La tabla de símbolos ordenada sin elementos

   :raises Exception:


.. py:function:: put(bst, key, value)

   Ingresa una pareja llave,valor. Si la llave ya existe,
   se reemplaza el valor.
   :param bst: El BST
   :param key: La llave asociada a la pareja
   :param value: El valor asociado a la pareja

   :returns: El arbol con la nueva pareja

   :raises Exception:


.. py:function:: get(bst, key)

   Retorna la pareja lleve-valor con llave igual  a key
   :param bst: El arbol de búsqueda
   :param key: La llave asociada a la pareja

   :returns: La pareja llave-valor en caso de que haya sido encontrada

   :raises Exception:


.. py:function:: remove(bst, key)

   Elimina la pareja llave,valor, donde llave == key.
   :param bst: El arbol de búsqueda
   :param key: La llave asociada a la pareja

   :returns: El arbol sin la pareja key-value

   :raises Exception:


.. py:function:: contains(bst, key)

   Informa si la llave key se encuentra en la tabla de hash
   :param bst: El arbol de búsqueda
   :param key: La llave a buscar

   :returns: True si la llave está presente False en caso contrario

   :raises Exception:


.. py:function:: size(bst)

   Retorna el número de entradas en la tabla de simbolos
   :param bst: El arbol de búsqueda

   :returns: El número de elementos en la tabla

   :raises Exception:


.. py:function:: isEmpty(bst)

   Informa si la tabla de simbolos se encuentra vacia
   :param bst: El arbol de búsqueda

   :returns: True si la tabla es vacía, False en caso contrario

   :raises Exception:


.. py:function:: keySet(bst)

   Retorna una lista con todas las llaves de la tabla
   :param bst: La tabla de simbolos

   :returns: Una lista con todas las llaves de la tabla

   :raises Exception:


.. py:function:: valueSet(bst)

   Construye una lista con los valores de la tabla
   :param bst: La tabla con los elementos

   :returns: Una lista con todos los valores

   :raises Exception:


.. py:function:: minKey(bst)

   Retorna la menor llave de la tabla de simbolos
   :param bst: La tabla de simbolos

   :returns: La menor llave de la tabla

   :raises Exception:


.. py:function:: maxKey(bst)

   Retorna la mayor llave de la tabla de simbolos
   :param bst: La tabla de simbolos

   :returns: La mayor llave de la tabla

   :raises Exception:


.. py:function:: deleteMin(bst)

   Encuentra y remueve la menor llave de la tabla de simbolos
   y su valor asociado
   :param bst: La tabla de simbolos

   :returns: La tabla de simbolos sin la menor llave

   :raises Exception:


.. py:function:: deleteMax(bst)

   Encuentra y remueve la mayor llave de la tabla de simbolos
   y su valor asociado
   :param bst: La tabla de simbolos

   :returns: La tabla de simbolos sin la mayor llave

   :raises Exception:


.. py:function:: floor(bst, key)

   Retorna la llave mas grande en la tabla de simbolos,
   menor o igual a la llave key
   :param bst: La tabla de simbolos
   :param key: La llave de búsqueda

   :returns: La llave más grande menor o igual a key

   :raises Exception:


.. py:function:: ceiling(bst, key)

   Retorna la llave mas pequeña en la tabla de simbolos,
   mayor o igual a la llave key
   :param bst: La tabla de simbolos
   :param key: la llave de búsqueda

   :returns: La llave más pequeña mayor o igual a Key

   :raises Exception:


.. py:function:: select(bst, pos)

   Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
   :param bst: La tabla de simbolos
   :param pos: la pos-esima llave mas pequeña

   :returns: La llave más pequeña mayor o igual a Key

   :raises Exception:


.. py:function:: rank(bst, key)

   Retorna el número de llaves en la tabla estrictamente menores que key
   :param bst: La tabla de simbolos
   :param key: La llave de búsqueda

   :returns: El nuemero de llaves encontradas

   :raises Exception:


.. py:function:: height(bst)

   Retorna la altura del arbol de busqueda
   :param bst: La tabla de simbolos

   :returns: La altura del arbol

   :raises Exception:


.. py:function:: keys(bst, keylo, keyhi)

   Retorna todas las llaves del arbol que se encuentren entre
   [keylo, keyhi]

   :param bst: La tabla de simbolos
   :param keylo: limite inferior
   :param keylohi: limite superiorr

   :returns: Las llaves en el rago especificado

   :raises Exception:


.. py:function:: values(bst, keylo, keyhi)

   Retorna todas los valores del arbol que se encuentren entre
   [keylo, keyhi]

   :param bst: La tabla de simbolos
   :param keylo: limite inferior
   :param keylohi: limite superiorr

   :returns: Las llaves en el rago especificado

   :raises Exception:


.. py:function:: insertNode(root, key, value, cmpfunction)

   Ingresa una pareja llave,valor. Si la llave ya existe,
   se reemplaza el valor.
   :param root: La raiz del arbol
   :param key: La llave asociada a la pareja
   :param value: El valor asociado a la pareja
   :param cmpfunction: Función de comparación

   :returns: El arbol con la nueva pareja

   :raises Exception:


.. py:function:: getNode(root, key, cmpfunction)

   Retorna la pareja lleve-valor con llave igual  a key
   :param root: El arbol de búsqueda
   :param key: La llave asociada a la pareja
   :param cmpfunction: Función de comparación

   :returns: El arbol con la nueva pareja

   :raises Exception:


.. py:function:: removeNode(root, key, cmpfunction)

   Elimina la pareja llave,valor, donde llave == key.
   :param bst: El arbol de búsqueda
   :param key: La llave asociada a la pareja

   :returns: El arbol sin la pareja key-value

   :raises Exception:


.. py:function:: sizeTree(root)

   Retornar el número de entradas en la a partir un punto dado
   :param root: El arbol de búsqueda

   :returns: El número de elementos en la tabla

   :raises Exception:


.. py:function:: valueSetTree(root, klist)

   Construye una lista con los valorers de la tabla
   :param root: El arbol con los elementos
   :param klist: La lista de respuesta

   :returns: Una lista con todos los valores

   :raises Exception:


.. py:function:: keySetTree(root, klist)

   Construye una lista con las llaves de la tabla
   :param root: El arbol con los elementos
   :param klist: La lista de respuesta

   :returns: Una lista con todos las llaves

   :raises Exception:


.. py:function:: minKeyNode(root)

   Retorna la menor llave de la tabla de simbolos
   :param root: La raiz del arbol de busqueda

   :returns: El elemento mas izquierdo del arbol

   :raises Exception:


.. py:function:: maxKeyNode(root)

   Retorna la mayor llave de la tabla de simbolos
   :param bst: La tabla de simbolos

   :returns: El elemento mas derecho del árbol

   :raises Exception:


.. py:function:: deleteMinTree(root)

   Encuentra y remueve la menor llave de la tabla de simbolos
   y su valor asociado
   :param root: La raiz del arbol de busqueda

   :returns: El arbol de busqueda

   :raises Excep:


.. py:function:: deleteMaxTree(root)

   Encuentra y remueve la mayor llave de la tabla de simbolos
   y su valor asociado
   :param root: el arbol de busqueda

   :returns: El árbol de búsqueda sin la mayor llave

   :raises Excep:


.. py:function:: floorKey(root, key, cmpfunction)

   Retorna la llave mas grande en la tabla de simbolos,
   menor o igual a la llave key
   :param bst: La tabla de simbolos

   :returns: La tabla de simbolos sin la mayor llave

   :raises Excep:


.. py:function:: ceilingKey(root, key, cmpfunction)

   Retorna la llave mas pequeña en la tabla de simbolos,
   mayor o igual a la llave key
   :param bst: La tabla de simbolos
   :param key: la llave de búsqueda

   :returns: La llave más pequeña mayor o igual a Key

   :raises Excep:


.. py:function:: selectKey(root, key)

   Retorna la k-esima llave mas pequeña de la tabla
   :param bst: La tabla de simbolos
   :param key: la llave de búsqueda

   :returns: La llave más pequeña mayor o igual a Key

   :raises Excep:


.. py:function:: rankKeys(root, key, cmpfunction)

   Retorna el número de llaves en la tabla estrictamente menores que key
   :param bst: La tabla de simbolos
   :param key: la llave de busqueda

   :returns: El numero de llaves

   :raises Exception:


.. py:function:: heightTree(root)

   Retorna la altura del arbol de busqueda
   :param root: La tabla de simbolos

   :returns: La altura del arbol

   :raises Excep:


.. py:function:: keysRange(root, keylo, keyhi, lstkeys, cmpfunction)

   Retorna todas las llaves del arbol en un rango dado
   :param bst: La tabla de simbolos
   :param keylo: limite inferior
   :param keylohi: limite superiorr

   :returns: Las llaves en el rago especificado

   :raises Excep:


.. py:function:: valuesRange(root, keylo, keyhi, lstvalues, cmpfunction)

   Retorna todas los valores del arbol en un rango dado por
   [keylo, keyhi]
   :param bst: La tabla de simbolos
   :param keylo: limite inferior
   :param keylohi: limite superior

   :returns: Las llaves en el rago especificado

   :raises Excep:


.. py:function:: defaultfunction(key1, key2)


