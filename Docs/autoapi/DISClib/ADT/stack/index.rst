:py:mod:`DISClib.ADT.stack`
===========================

.. py:module:: DISClib.ADT.stack

.. autoapi-nested-parse::

   * Copyright 2020, Departamento de sistemas y Computación,
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

Classes
~~~~~~~

.. autoapisummary::

   DISClib.ADT.stack.Stack



Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.stack.newStack
   DISClib.ADT.stack.push
   DISClib.ADT.stack.pop
   DISClib.ADT.stack.isEmpty
   DISClib.ADT.stack.top
   DISClib.ADT.stack.size



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.stack.T


.. py:data:: T

   

.. py:class:: Stack


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   ArrayList _summary_

   :param Generic: _description_
   :type Generic: _type_


.. py:function:: newStack(datastructure='DOUBLE_LINKED')

   Crea una pila vacia.

   :param datastructure: Indica el tipo de estructura de datos a utilizar
                         para implementar la pila

   :returns: Una pila vacia

   :raises Exception:


.. py:function:: push(stack, element)

   Agrega el elemento element en el tope de la pila.

   :param stack: La pila donde se insetará el elemento
   :param element: El elemento a insertar

   :returns: La pila modificada

   :raises Exception:


.. py:function:: pop(stack)

   Retorna el elemento  presente en el tope de la pila.

    Args:
       stack:  La pila de donde se retirara el elemento

   :returns: El elemento del tope de la pila

   :raises Exception:


.. py:function:: isEmpty(stack)

   Informa si la pila es vacía o no
    Args:
       stack:  La pila a examinar

   :returns: True si la pila es vacia
             False de lo contrario

   :raises Exception:


.. py:function:: top(stack)

   Retorna el elemento en tope de la pila, sin eliminarlo de la pila

   :param stack: La pila a examinar

   :returns: El primer elemento de la pila, sin eliminarlo

   :raises Exception:


.. py:function:: size(stack)

   Informa el número de elementos en la pila
   :param stack: La pila a examinar

   :returns: Retorna el tamaño de la pila

   :raises Exception:


