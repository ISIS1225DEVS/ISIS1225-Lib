:py:mod:`DISClib.DataStructures.probinghashmap`
===============================================

.. py:module:: DISClib.DataStructures.probinghashmap

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
   * Dario Correal
   *



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.probinghashmap.newList
   DISClib.DataStructures.probinghashmap.addFirst
   DISClib.DataStructures.probinghashmap.addLast
   DISClib.DataStructures.probinghashmap.isEmpty
   DISClib.DataStructures.probinghashmap.size
   DISClib.DataStructures.probinghashmap.firstElement
   DISClib.DataStructures.probinghashmap.lastElement
   DISClib.DataStructures.probinghashmap.getElement
   DISClib.DataStructures.probinghashmap.deleteElement
   DISClib.DataStructures.probinghashmap.removeFirst
   DISClib.DataStructures.probinghashmap.removeLast
   DISClib.DataStructures.probinghashmap.insertElement
   DISClib.DataStructures.probinghashmap.isPresent
   DISClib.DataStructures.probinghashmap.changeInfo
   DISClib.DataStructures.probinghashmap.exchange
   DISClib.DataStructures.probinghashmap.subList
   DISClib.DataStructures.probinghashmap.iterator
   DISClib.DataStructures.probinghashmap.compareElements
   DISClib.DataStructures.probinghashmap.defaultfunction



.. py:function:: newList(cmpfunction, module, key, filename, delim)

   Crea una lista vacia.

   Se inicializan los apuntadores a la primera y ultima posicion en None.
   El tipo de la listase inicializa como SINGLE_LINKED
   :param cmpfunction: Función de comparación para los elementos de la lista.
   :param Si no se provee una función de comparación:
   :param se utilizará la función:
   :param de comparación por defecto pero se debe suministrar un valor para key:
   :param key: Identificador que se debe utilizar para la comparación de
   :param elementos de la lista:
   :param filename: Si se provee este valor, se creará una lista a partir de
   :param la informacion que se encuentra en el archivo CSV:
   :param delimiter: Si se provee un archivo para crear la lista, indica el
   :param delimitador a usar para separar los campos del archivo CSV:

   :returns: Un diccionario que representa la estructura de datos de una lista
             encadanada vacia.

   Raises:



.. py:function:: addFirst(lst, element)

   Agrega un elemento a la lista en la primera posicion.

   Agrega un elemento en la primera posición de la lista, ajusta el apuntador
   al primer elemento e incrementa el tamaño de la lista.

   :param lst: La lista don de inserta el elemento
   :param element: El elemento a insertar en la lista

   :returns: La lista con el nuevo elemento en la primera posición, si el proceso
             fue exitoso

   :raises Exception:


.. py:function:: addLast(lst, element)

   Agrega un elemento en la última posición de la lista.

   Se adiciona un elemento en la última posición de la lista y se actualiza
    el apuntador a la útima posición.
   Se incrementa el tamaño de la lista en 1
   :param lst: La lista en la que se inserta el elemento
   :param element: El elemento a insertar

   :raises Exception:


.. py:function:: isEmpty(lst)

   Indica si la lista está vacía
   :param lst: La lista a examinar

   :raises Exception:


.. py:function:: size(lst)

   Informa el número de elementos de la lista.
   Args
       lst: La lista a examinar

   :raises Exception:


.. py:function:: firstElement(lst)

   Retorna el primer elemento de una lista no vacía.
    No se elimina el elemento.

   :param lst: La lista a examinar

   :raises Exception:


.. py:function:: lastElement(lst)

   Retorna el último elemento de una  lista no vacia.
       No se elimina el elemento.

   :param lst: La lista a examinar

   :raises Exception:


.. py:function:: getElement(lst, pos)

   Retorna el elemento en la posición pos de la lista.

   Se recorre la lista hasta el elemento pos, el cual  debe ser
   mayor que cero y menor o igual al tamaño de la lista.
   Se retorna el elemento en dicha posición sin eleminarlo.
   La lista no puede ser vacia.

   :param lst: La lista a examinar
   :param pos: Posición del elemento a retornar

   :raises Exception:


.. py:function:: deleteElement(lst, pos)

   Elimina el elemento en la posición pos de la lista.

   Elimina el elemento que se encuentra en la posición pos de la lista.
   Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
   Se decrementa en un uno el tamñao de la lista.
   La lista no puede estar vacia.

   :param lst: La lista a retoranr
   :param pos: Posición del elemento a eliminar.

   :raises Exception:


.. py:function:: removeFirst(lst)

   Remueve el primer elemento de la lista.
   Elimina y retorna el primer elemento de la lista.
   El tamaño de la lista se decrementa en uno.  Si la lista
   es vacía se retorna None.
   :param lst: La lista a examinar

   :raises Exception:


.. py:function:: removeLast(lst)

   Remueve el último elemento de la lista.

   Elimina el último elemento de la lista  y lo retorna en caso de existir.
   El tamaño de la lista se decrementa en 1.
   Si la lista es vacía  retorna None.

   :param lst: La lista a examinar

   :raises Exception:


.. py:function:: insertElement(lst, element, pos)

   Inserta el elemento element en la posición pos de la lista.

   Inserta el elemento en la posición pos de la lista.
   La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

   :param lst: La lista en la que se va a insertar el elemento
   :param element: El elemento a insertar
   :param pos: posición en la que se va a insertar el elemento,
   :param 0 < pos <= size:
   :type 0 < pos <= size: lst

   :raises Exception:


.. py:function:: isPresent(lst, element)

   Informa si el elemento element esta presente en la lista.

   Informa si un elemento está en la lista.  Si esta presente,
   retorna la posición en la que se encuentra  o cero (0) si no esta presente.
   Se utiliza la función de comparación utilizada durante la creación
   de la lista para comparar los elementos.
   La cual debe retornar cero en caso de que los elementos sean iguales.

   :param lst: La lista a examinar
   :param element: El elemento a buscar

   :raises Exception:


.. py:function:: changeInfo(lst, pos, newinfo)

   Cambia la informacion contenida en el nodo de la lista que se encuentra
        en la posicion pos.

   :param lst: La lista a examinar
   :param pos: la posición de la lista con la información a cambiar
   :param newinfo: La nueva información que se debe poner en el nodo de
   :param la posición pos:

   :raises Exception:


.. py:function:: exchange(lst, pos1, pos2)

   Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

   :param lst: La lista a examinar
   :param pos1: Posición del primer elemento
   :param pos2: Posiocion del segundo elemento

   :raises Exception:


.. py:function:: subList(lst, pos, numelem)

   Retorna una sublista de la lista lst.

   Se retorna una lista que contiene los elementos a partir de la
   posicion pos,con una longitud de numelem elementos.
   Se crea una copia de dichos elementos y se retorna una lista nueva.

   :param lst: La lista a examinar
   :param pos: Posición a partir de la que se desea obtener la sublista
   :param numelem: Numero de elementos a copiar en la sublista

   :raises Exception:


.. py:function:: iterator(lst)

   Retorna un iterador para la lista.
   :param lst: La lista a iterar

   :raises Exception:


.. py:function:: compareElements(lst, element, info)

   Compara dos elementos

   Se utiliza la función de comparación por defecto si key es None
   o la función provista por el usuario en caso contrario
   :param lst: La lista con los elementos
   :param element: El elemento que se esta buscando en la lista
   :param info: El elemento de la lista que se está analizando

   Returns:  0 si los elementos son iguales

   :raises Exception:


.. py:function:: defaultfunction(id1, id2)


