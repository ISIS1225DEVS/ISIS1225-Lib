:py:mod:`DISClib.DataStructures.rbtnode`
========================================

.. py:module:: DISClib.DataStructures.rbtnode

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

   DISClib.DataStructures.rbtnode.newNode
   DISClib.DataStructures.rbtnode.isRed
   DISClib.DataStructures.rbtnode.getValue
   DISClib.DataStructures.rbtnode.getKey



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.rbtnode.RED
   DISClib.DataStructures.rbtnode.BLACK


.. py:data:: RED
   :value: 0

   

.. py:data:: BLACK
   :value: 1

   

.. py:function:: newNode(key, value, size, color)

   Crea un nuevo nodo para un árbol rojo-negro  y lo retorna.
   color:0 - rojo  color:1 - negro
   :param value: El valor asociado a la llave
   :param key: la llave asociada a la pareja
   :param size: El tamaño del subarbol que cuelga de este nodo
   :param color: El color inicial del nodo

   :returns: Un nodo con la pareja <llave, valor>

   :raises Exception:


.. py:function:: isRed(node)

   Informa si un nodo es rojo
   :param node: El nodo a revisar

   :returns: True si el nodo es rojo, False de lo contrario

   :raises Exception:


.. py:function:: getValue(node)

   Retorna el valor asociado a una pareja llave valor
   :param node: El nodo con la pareja llave-valor

   :returns: El valor almacenado en el nodo

   :raises Exception:


.. py:function:: getKey(node)

   Retorna la llave asociado a una pareja llave valor
   :param node: El nodo con la pareja llave-valor

   :returns: La llave almacenada en el nodo

   :raises Exception:


