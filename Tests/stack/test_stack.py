"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
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
from DISClib.ADT import stack as st
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
def stack():
    stack = st.newStack('ARRAY_LIST')
    return stack


def test_pushElements(stack, books):
    assert st.size(stack) == 0
    st.push(stack, books[5])
    assert st.size(stack) == 1
    assert st.top(stack) == books[5]
    st.push(stack, books[6])
    st.push(stack, books[3])
    st.push(stack, books[10])
    st.push(stack, books[1])
    st.push(stack, books[2])
    st.push(stack, books[8])
    st.push(stack, books[4])
    st.push(stack, books[7])
    st.push(stack, books[9])
    assert st.size(stack) == 10
    assert st.top(stack) == books[9]
    while not st.isEmpty(stack):
        element = st.pop(stack)
        print(element)


def test_infoElements(stack, books):
    assert (st.size(stack) == 0)
    assert (st.isEmpty(stack))
    st.push(stack, books[5])
    st.push(stack, books[6])
    st.push(stack, books[3])
    st.push(stack, books[10])
    st.push(stack, books[1])
    st.push(stack, books[2])
    st.push(stack, books[8])
    st.push(stack, books[4])
    st.push(stack, books[7])
    st.push(stack, books[9])

    elem = st.top(stack)
    assert (st.size(stack) == 10)
    assert (elem == books[9])

    elem = st.pop(stack)
    assert (st.size(stack) == 9)
    assert (elem == books[9])

    elem = st.pop(stack)
    assert (st.size(stack) == 8)
    assert (elem == books[7])

    elem = st.top(stack)
    assert (st.size(stack) == 8)
    assert (elem == books[4])

    st.push(stack, books[9])
    assert (st.size(stack) == 9)
    elem = st.top(stack)
    assert (elem == books[9])


def test_top_pop(stack, books):
    assert st.size(stack) == 0
    assert st.isEmpty(stack)
    st.push(stack, books[5])
    st.push(stack, books[6])
    st.push(stack, books[3])
    st.push(stack, books[10])
    st.push(stack, books[1])
    st.push(stack, books[2])
    st.push(stack, books[8])
    st.push(stack, books[4])
    st.push(stack, books[7])
    st.push(stack, books[9])
    total = st.size(stack)
    while not (st.isEmpty(stack)):
        top = st.top(stack)
        assert(st.pop(stack) == top)
        total -= 1
        assert (total == st.size(stack))


def test_push_pop(stack, books):
    assert (st.size(stack) == 0)
    assert (st.isEmpty(stack))

    st.push(stack, books[5])
    assert(st.size(stack) == 1)
    assert(st.top(stack) == st.pop(stack))
    assert(st.size(stack) == 0)

    st.push(stack, books[6])
    assert(st.size(stack) == 1)
    assert(st.top(stack) == st.pop(stack))
    assert(st.size(stack) == 0)

    st.push(stack, books[3])
    assert(st.size(stack) == 1)
    assert(st.top(stack) == st.pop(stack))
    assert(st.size(stack) == 0)

    st.push(stack, books[10])
    assert(st.size(stack) == 1)
    assert(st.top(stack) == st.pop(stack))
    assert(st.size(stack) == 0)

    st.push(stack, books[1])
    assert(st.size(stack) == 1)
    assert(st.top(stack) == st.pop(stack))
    assert(st.size(stack) == 0)

    st.push(stack, books[2])
    assert(st.size(stack) == 1)
    assert(st.top(stack) == st.pop(stack))
    assert(st.size(stack) == 0)

    st.push(stack, books[8])
    st.push(stack, books[4])
    st.push(stack, books[7])
    st.push(stack, books[9])

    assert (st.size(stack) == 4)
    assert books[9] == st.pop(stack)
    assert books[7] == st.pop(stack)
    assert books[4] == st.pop(stack)
    assert books[8] == st.pop(stack)

    assert (st.size(stack) == 0)


def test_error_pop(stack):
    assert (st.size(stack) == 0)
    assert(st.isEmpty(stack))

    with pytest.raises(Exception):
        st.pop(stack)
