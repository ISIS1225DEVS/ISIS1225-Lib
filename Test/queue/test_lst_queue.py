"""
 * Copyright 2020, Departamento de sistemas y Computación,
   Universidad de Los Andes
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
 """

import pytest
import config
from DISClib.ADT import queue as q
assert config


@pytest.fixture
def books():
    books = []
    books.append({'book_id': '1', 'title': 'Title 1', 'author': 'author 1'})
    books.append({'book_id': '2', 'title': ' Title 2', 'author': 'author 2'})
    books.append({'book_id': '3', 'title': 'Title 3', 'author': 'author 3'})
    books.append({'book_id': '4', 'title': 'Title 4', 'author': 'author 4'})
    books.append({'book_id': '5', 'title': 'Title 5', 'author': 'author 5'})
    books.append({'book_id': '6', 'title': 'Title 6', 'author': 'author 6'})
    books.append({'book_id': '7', 'title': 'Title 7', 'author': 'author 7'})
    books.append({'book_id': '8', 'title': 'Title 8', 'author': 'author 8'})
    books.append({'book_id': '9', 'title': 'Title 9', 'author': 'author 9'})
    books.append({'book_id': '10', 'title': 'Title 10', 'author': 'author 10'})
    books.append({'book_id': '7', 'title': 'Title 11', 'author': 'author 11'})
    books.append({'book_id': '8', 'title': 'Title 12', 'author': 'author 12'})
    books.append({'book_id': '9', 'title': 'Title 13', 'author': 'author 13'})
    books.append({'book_id': '10', 'title': 'Title 14', 'author': 'author 14'})
    return books


@pytest.fixture
def queue():
    queue = q.newQueue('SINGLE_LINKED')
    return queue


def test_queueElements(queue, books):
    """
    Se prueba la creacion de una nueva cola, se agregan todos los datos
    creados por sistema y se imprime su valor
    """
    q.enqueue(queue, books[5])
    q.enqueue(queue, books[6])
    q.enqueue(queue, books[3])
    q.enqueue(queue, books[10])
    q.enqueue(queue, books[1])
    q.enqueue(queue, books[2])
    q.enqueue(queue, books[8])
    q.enqueue(queue, books[4])
    q.enqueue(queue, books[7])
    q.enqueue(queue, books[9])

    while not q.isEmpty(queue):
        element = q.dequeue(queue)
        result = ("".join(str(key) + ": " + str(value) + ",  "
                  for key, value in element.items()))
        print(result)


def test_sizeQueue(queue, books):
    """
    Se prueba la creacion de una cola y la relacion con el tamaño al
    ingresar datos
    """
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))

    q.enqueue(queue, books[5])
    q.enqueue(queue, books[6])
    q.enqueue(queue, books[3])
    q.enqueue(queue, books[10])
    q.enqueue(queue, books[1])
    q.enqueue(queue, books[2])
    q.enqueue(queue, books[8])
    q.enqueue(queue, books[4])
    q.enqueue(queue, books[7])
    assert q.size(queue) == 9


def test_infoElements(queue, books):
    """
    Este test busca confirmar que los datos se almacenen de forma
    correcta y que sean los valores correctos en el orden apropiado
    de la estructura.
    """
    q.enqueue(queue, books[5])
    q.enqueue(queue, books[6])
    q.enqueue(queue, books[3])
    q.enqueue(queue, books[10])
    q.enqueue(queue, books[1])
    q.enqueue(queue, books[2])
    q.enqueue(queue, books[8])
    q.enqueue(queue, books[4])
    q.enqueue(queue, books[7])

    elem = q.peek(queue)
    assert (elem == books[5])

    elem = q.dequeue(queue)
    assert (elem == books[5])

    elem = q.dequeue(queue)
    assert (q.size(queue) == 7)
    assert (elem == books[6])

    elem = q.peek(queue)
    assert (q.size(queue) == 7)
    assert (elem == books[3])

    q.enqueue(queue, books[9])
    assert (q.size(queue) == 8)
    elem = q.peek(queue)
    assert (elem == books[3])


def test_peek_dequeue(queue, books):
    """
    Este test prueba la creacion de una cola y que el orden de salida
    sea el correcto para la estructura en cuestion, y que el tamaño
    se reduzca para cada salida de objeto
    """

    q.enqueue(queue, books[5])
    q.enqueue(queue, books[6])
    q.enqueue(queue, books[3])
    q.enqueue(queue, books[10])
    q.enqueue(queue, books[1])
    q.enqueue(queue, books[2])
    q.enqueue(queue, books[8])
    q.enqueue(queue, books[4])
    q.enqueue(queue, books[7])

    total = q.size(queue)
    while not (q.isEmpty(queue)):
        peek = q.peek(queue)
        assert(q.dequeue(queue) == peek)
        total -= 1
        assert (total == q.size(queue))


def test_enqueue_dequeue(queue, books):
    """
    Este test prueba que la cola pueda manejar inserciones y eliminaciones
    de forma correcta siguiendo un orden establecido, y que no quede
    referencia al objeto sacado despues de haberlo removido de la
    cola
    """

    q.enqueue(queue, books[5])
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue(queue, books[6])
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue(queue, books[3])
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue(queue, books[10])
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue(queue, books[1])
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue(queue, books[2])
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue(queue, books[8])
    q.enqueue(queue, books[4])
    q.enqueue(queue, books[7])
    q.enqueue(queue, books[9])

    assert (q.size(queue) == 4)
    assert books[8] == q.dequeue(queue)
    assert books[4] == q.dequeue(queue)
    assert books[7] == q.dequeue(queue)
    assert books[9] == q.dequeue(queue)

    assert (q.size(queue) == 0)
