:py:mod:`DISClib.ADT.queue`
===========================

.. py:module:: DISClib.ADT.queue

.. autoapi-nested-parse::

   * Copyright 2020, Departamento de sistemas y Computación,
   * Universidad de Los Andes
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

Classes
~~~~~~~

.. autoapisummary::

   DISClib.ADT.queue.Queue



Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.queue.newQueue
   DISClib.ADT.queue.enqueue
   DISClib.ADT.queue.dequeue
   DISClib.ADT.queue.peek
   DISClib.ADT.queue.isEmpty
   DISClib.ADT.queue.size



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.queue.T


.. py:data:: T

   

.. py:class:: Queue


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   ArrayList _summary_

   :param Generic: _description_
   :type Generic: _type_


.. py:function:: newQueue(datastructure='SINGLE_LINKED')

   Crea una cola vacia basada en una lista.
   :param datastructure: Indica el tipo de estructura de datos a utilizar
                         para implementar la cola

   :returns: Una cola vacia

   :raises Exception:


.. py:function:: enqueue(queue, element)

   Agrega el elemento element en el tope de la pila
   :param queue: La cola donde se insertará el elemento
   :param element: El elemento a insertar

   :returns: La cola modificada

   :raises Exception:


.. py:function:: dequeue(queue)

   Retorna el elemento en la primer posición de la cola, y lo elimina.
    Args:
       queue: La cola donde se eliminará el elemento

   :returns: El primer elemento de la cola

   :raises Exception:


.. py:function:: peek(queue)

   Retorna el elemento en la primer posición de la cola sin eliminarlo
   :param queue: La cola  a examinar

   :returns: True el primer elemento de cola sin eliminarlo

   :raises Exception:


.. py:function:: isEmpty(queue)

   Informa si la cola es vacía o no
   :param queue: La cola  a examinar

   :returns: True si la cola es vacia, False de lo contrario

   :raises Exception:


.. py:function:: size(queue)

   Informa el número de elementos en la cola
   :param queue: La cola  a examinar

   :returns: Retorna el tamaño de la cola

   :raises Exception:


