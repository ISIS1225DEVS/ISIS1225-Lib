:py:mod:`Src.DISClib.DataStructures.indexheap`
==============================================

.. py:module:: Src.DISClib.DataStructures.indexheap

.. autoapi-nested-parse::

   # TODO cambiar comentarios de lincencia segun estandard del equipo
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



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.DataStructures.indexheap.newIndexHeap
   Src.DISClib.DataStructures.indexheap.insert
   Src.DISClib.DataStructures.indexheap.isEmpty
   Src.DISClib.DataStructures.indexheap.size
   Src.DISClib.DataStructures.indexheap.contains
   Src.DISClib.DataStructures.indexheap.min
   Src.DISClib.DataStructures.indexheap.delMin
   Src.DISClib.DataStructures.indexheap.decreaseKey
   Src.DISClib.DataStructures.indexheap.increaseKey
   Src.DISClib.DataStructures.indexheap.exchange
   Src.DISClib.DataStructures.indexheap.greater
   Src.DISClib.DataStructures.indexheap.swim
   Src.DISClib.DataStructures.indexheap.sink



.. py:function:: newIndexHeap(cmpfunction)

   Crea un cola de prioridad indexada orientada a menor

   :param cmpfunction: La función de comparacion
   :param size: El numero de elementos

   :returns: Una nueva cola de prioridad indexada

   :raises Exception:


.. py:function:: insert(iheap, key, index)

   Inserta la llave key con prioridad index

   :param iheap: El heap indexado

   :returns: El iheap con la nueva paraja indexada

   :raises Exception:


.. py:function:: isEmpty(iheap)

   Informa si una cola de prioridad indexada es vacia

   :param iheap: El heap indexado a revisar

   :returns: True si esta vacia

   :raises Exception:


.. py:function:: size(iheap)

   Retorna el número de elementos en el heap

   :param iheap: El heap a revisar

   :returns: El numero de elementos

   :raises Exception:


.. py:function:: contains(iheap, key)

   Indica si la llave key se encuentra en el heap

   :param iheap: El heap a revisar

   :returns: El numero de elementos

   :raises Exception:


.. py:function:: min(iheap)

   Retorna el primer elemento del heap, es decir el menor elemento

   :param iheap: El heap a revisar

   :returns: El numero de elementos

   :raises Exception:


.. py:function:: delMin(iheap)

   Retorna el menor elemento del heap y lo elimina.
   Se reemplaza con el último elemento y se hace sink.

   :param iheap: El heap a revisar

   :returns: La llave asociada al mayor indice

   :raises Exception:


.. py:function:: decreaseKey(iheap, key, newindex)

   Decrementa el indice de un llave

   :param iheap: El heap a revisar
   :param key: la llave a decrementar
   :param newindex: El nuevo indice de la llave

   :returns: El numero de elementos

   :raises Exception:


.. py:function:: increaseKey(iheap, key, newindex)

   Incrementa el indice de un llave

   :param iheap: El heap a revisar
   :param key: la llave a incrementar
   :param newindex: El nuevo indice de la llave

   :returns: El numero de elementos

   :raises Exception:


.. py:function:: exchange(iheap, i, j)

   Intercambia los elementos en las posiciones i y j del heap


.. py:function:: greater(iheap, parent, element)

   Indica si el index de parent es mayor
   que index de element


.. py:function:: swim(iheap, pos)

   Deja en el lugar indicado un elemento adicionado
   en la última posición

   :param heap: El arreglo con la informacion
   :param pos: posicion en el arreglo a revisar

   :returns: El arreglo en forma de heap

   :raises Exception:


.. py:function:: sink(iheap, pos)

   Deja en la posición correcta un elemento ubicado en la raíz del heap

   :param heap: El arreglo con la informacion
   :param pos: posicion en el arreglo a revisar

   :returns: El arreglo en forma de heap

   :raises Exception:


