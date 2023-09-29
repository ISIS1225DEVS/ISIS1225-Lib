"""
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
 """

import pytest
import config
from DISClib.ADT import list as lt
assert config


def cmpfunction(element1, element2):
    if element1['book_id'] == element2['book_id']:
        return 0
    elif element1['book_id'] < element2['book_id']:
        return -1
    else:
        return 1


@pytest.fixture
def alt():
    lst = lt.newList(datastructure='ARRAY_LIST', key='book_id')
    return lst


@pytest.fixture
def altfunc():
    lst = lt.newList(datastructure='ARRAY_LIST',
                     cmpfunction=cmpfunction)
    return lst


@pytest.fixture
def books():
    books = []
    books.append({'book_id': '1', 'book_title': 'Title 1', 'author': 'a1'})
    books.append({'book_id': '2', 'book_title': 'Title 2', 'author': 'a2'})
    books.append({'book_id': '3', 'book_title': 'Title 3', 'author': 'a3'})
    books.append({'book_id': '4', 'book_title': 'Title 4', 'author': 'a4'})
    books.append({'book_id': '5', 'book_title': 'Title 5', 'author': 'a5'})
    books.append({'book_id': '6', 'book_title': 'Title 6', 'author': 'a6'})
    books.append({'book_id': '7', 'book_title': 'Title 7', 'author': 'a7'})
    return books


@pytest.fixture
def altbooks(books):
    lst = lt.newList(datastructure='ARRAY_LIST', key='book_id')
    for i in range(0, 5):
        lt.addLast(lst, books[i])
    return lst


"""Pruebas con Arreglo"""


def test_empty_array(alt):
    assert lt.isEmpty(alt) is True
    assert lt.size(alt) == 0


def test_addFirst_array(alt, books):
    assert lt.isEmpty(alt) is True
    assert lt.size(alt) == 0
    lt.addFirst(alt, books[1])
    assert lt.size(alt) == 1
    lt.addFirst(alt, books[2])
    assert lt.size(alt) == 2
    book = lt.firstElement(alt)
    assert book == books[2]


def test_addLast_array(alt, books):
    assert lt.isEmpty(alt) is True
    assert lt.size(alt) == 0
    lt.addLast(alt, books[1])
    assert lt.size(alt) == 1
    lt.addLast(alt, books[2])
    assert lt.size(alt) == 2
    book = lt.firstElement(alt)
    assert book == books[1]
    book = lt.lastElement(alt)
    assert book == books[2]


def test_getElement_array(altbooks, books):
    book = lt.getElement(altbooks, 1)
    assert book == books[0]
    book = lt.getElement(altbooks, 5)
    assert book == books[4]


def test_removeFirst_array(altbooks, books):
    assert lt.size(altbooks) == 5
    lt.removeFirst(altbooks)
    assert lt.size(altbooks) == 4
    book = lt.getElement(altbooks, 1)
    assert book == books[1]


def test_removeLast_array(altbooks, books):
    assert lt.size(altbooks) == 5
    lt.removeLast(altbooks)
    assert lt.size(altbooks) == 4
    book = lt.getElement(altbooks, 4)
    assert book == books[3]


def test_insertElement_array(alt, books):
    assert lt.isEmpty(alt) is True
    assert lt.size(alt) == 0
    lt.insertElement(alt, books[0], 1)
    assert lt.size(alt) == 1
    lt.insertElement(alt, books[1], 2)
    assert lt.size(alt) == 2
    lt.insertElement(alt, books[2], 1)
    assert lt.size(alt) == 3
    book = lt.getElement(alt, 1)
    assert book == books[2]
    book = lt.getElement(alt, 2)
    assert book == books[0]


def test_isPresent_array(altbooks, books):
    book = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
    assert lt.isPresent(altbooks, books[2]) > 0
    assert lt.isPresent(altbooks, book) == 0


def test_isPresent_func(altfunc, books):
    lt.addLast(altfunc, books[1])
    lt.addLast(altfunc, books[2])
    book = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
    lt.addLast(altfunc, books[3])
    lt.addLast(altfunc, books[4])
    lt.addLast(altfunc, books[5])
    assert lt.isPresent(altfunc, books[3]) > 0
    assert lt.isPresent(altfunc, book) == 0
    assert lt.isPresent(altfunc, books[4]) > 0
    assert lt.isPresent(altfunc, books[6]) == 0


def test_deleteElement_array(altbooks, books):
    pos = lt.isPresent(altbooks, books[2])
    assert pos > 0
    book = lt.getElement(altbooks, pos)
    assert book == books[2]
    lt.deleteElement(altbooks, pos)
    assert lt.size(altbooks) == 4
    book = lt.getElement(altbooks, pos)
    assert book == books[3]


def test_changeInfo_array(altbooks):
    book10 = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
    lt.changeInfo(altbooks, 1, book10)
    book = lt.getElement(altbooks, 1)
    assert book10 == book


def test_exchange_array(altbooks, books):
    book1 = lt.getElement(altbooks, 1)
    book5 = lt.getElement(altbooks, 5)
    lt.exchange(altbooks, 1, 5)
    assert lt.getElement(altbooks, 1) == book5
    assert lt.getElement(altbooks, 5) == book1


def test_iterator(altbooks):
    for element in lt.iterator(altbooks):
        print(element)
