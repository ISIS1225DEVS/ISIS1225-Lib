""" Esta clase representa una estructura de datos lineal, específicamente
    una lista doblemente enlazada/encadenada (DoubleLinked). Esta
    estructura de datos es una secuencia de nodos enlazados, donde cada
    nodo contiene un elemento de información, una referencia al siguiente,
    y al anterior nodo en la secuencia. Esto le permite a la lista un
    crecimiento y reducción dinámico en la memoria disponible.

    Este código y sus modificaciones para Python está basado en la
    implementación propuesta por los siguientes autores/libros:
        1) Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
        2) Data Structures and Algorithms in Python, Michael T. Goodrich,
            Roberto Tamassia y Michael H. Goldwasser.

Attributes:
    T (type): variable que representa el tipo de dato de los elementos
        contenidos en el DoubleLinked.

Class:
    DoubleLinked(Generic[T]): Esta clase representa una estructura de
        datos de tipo Array List o Arreglo Dinámico.

    Functions:
        - __init__(): inicializa la estructura DoubleLinked (autogenerado).
        - __post_init__(): configura los valores por defecto para el
            DoubleLinked.
        - default_cmp_function(): función de comparación por defecto.
        - _handle_error(): función privada que maneja los errores.
        - _check_type(): función privada que verifica el tipo de dato en el
            DoubleLinked.
        - is_empty(): revisa si la estructura está vacía.
        - size(): devuelve el numero de elementos que contiene la estructura.
        - add_first(): adiciona un elemento al inicio de la estructura.
        - add_last(): adiciona un elemento al final de la estructura.
        - add_element(elem, pos): adiciona un elemento en una posición dada.
        - get_first(): lee el primer elemento de la estructura.
        - get_last(): lee el último elemento de la estructura.
        - get_element(pos): lee un elemento en una posición dada.
        - remove_first(): elimina el primer elemento de la estructura.
        - remove_last(): elimina el último elemento de la estructura.
        - remove_element(pos): elimina un elemento en una posición dada.
        - compare_elements(elem1, elem2): compara dos elementos en dos
            posiciones dadas.
        - is_present(elem): revisa si un elemento está en la estructura.
        - change_info(new_elem, pos): cambia la información de un elemento
            dado.
        - exchange(pos1, pos2): intercambia la información de dos elementos en
            Sdos posiciones dadas.
        - sublist(start, end): crea una sublista de la estructura según unas
            posiciones dadas.
        - concat(other): une dos estructuras de datos DoubleLinked.

Copyrigth:
    Universidad de los Andes, Bogotá - Colombia, South America
    Facultad de Ingeniería,
    Departamento de Ingeniería de Sistemas y Computación DISC
    Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect
# import copy for deepcopy the data structure
import copy

# custom modules
# node class for the linked list
from DISClib.DataStructures.listnode import DoubleNode
# generic error handling and type checking
from DISClib.Utils.error import error_handler
from DISClib.Utils.error import init_type_checker
from DISClib.Utils.default import lt_default_cmp_funcion
from DISClib.Utils.default import T
from DISClib.Utils.default import DEFAULT_DICT_KEY
from DISClib.Utils.default import VALID_IO_TYPE

# checking costum modules
assert error_handler
assert init_type_checker
assert lt_default_cmp_funcion
assert T
assert DEFAULT_DICT_KEY
assert VALID_IO_TYPE


@dataclass
class DoubleLinked(Generic[T]):
    """DoubleLinked Clase que representa una estructura de datos de tipo
        DoubleLinked con la anotación '@dataclass' de python y el decorador
        'Generic[T]' para indicar que es una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type)
            que representa un DoubleLinked o Arreglo Dinámico generico.

    Attributes:
        first (Optional[DoubleNode[T]]): propiedad privada que representa el
            primer nodo del DoubleLinked.
        last (Optional[DoubleNode[T]]): propiedad privada que representa el
            último nodo del DoubleLinked.
        _size (int): propiedad privada que representa el tamaño de la lista.
        cmp_function (Optional[Callable[[T, T], int]]): función de comparación
            opcional que se utiliza para comparar los elementos del ArrayList,
            por defecto es None y el __post_init__ configura la función por
            defecto lt_default_cmp_funcion().
        key (Optional[str]): nombre de la llave opcional que se utiliza para
            comparar los elementos del DoubleLinkedList, Por defecto es None y
            el __post_init__ configura la llave por defecto la llave "id" en
            DEFAULT_DICT_KEY.
        iodata (Optional[List[T]]): lista nativa de python que contiene los
            elementos de la estructura de datos, por defecto es None y el
            usuario puede incluir una lista nativa de python como argumento.

    Returns:
        DoubleLinked: ADT de tipo DoubleLinked o Lista Sensillamente
            Encadenada.
    """
    # input elements from python list
    iodata: Optional[List[T]] = None
    # reference to the head node of the list
    head: Optional[DoubleNode[T]] = None
    # reference to the tail node of the list
    tail: Optional[DoubleNode[T]] = None
    # by default, the list is empty
    _size: int = 0
    # the cmp_function is used to compare elements, not defined by default
    cmp_function: Optional[Callable[[T, T], int]] = None
    # the key is used to compare elements, not defined by default
    key: Optional[str] = None

    def __post_init__(self) -> None:
        """__post_init__ configura los valores por defecto para la llave (key)
                y la función de comparación (cmp_function). Si el usuario
                incluye una lista nativa de python como argumento, se agrega
                a la lista de elementos del DoubleLinked.
        """
        try:
            # counter for elements in the input list
            # i = 0
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DEFAULT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.default_cmp_function
            # if input data is iterable add them to the DoubleLinkedList
            # TODO sometime strange weird in tests
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def default_cmp_function(self, elm1, elm2) -> int:
        """default_cmp_function procesa con algoritmica por defecto la lista
            der elementos que procesa el DoubleLinked. Es una función crucial
            para que la estructura de datos funcione correctamente.

        Args:
            elm1 (Any): primer elemento a comparar.
            elm2 (Any): segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si son
                iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            return lt_default_cmp_funcion(self.key, elm1, elm2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """_handle_error función privada que maneja los errores que se pueden
            presentar en el DoubleLinked.

            Si se presenta un error en el DoubleLinked, se formatea el error
            según el contexto (paquete/clase) y la función que lo generó, y lo
            reenvia al componente superior en la jerarquía de llamados para
            manejarlo segun se considere conveniente.

        Args:
            err (Exception): Excepción que se generó en el DoubleLinked.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """_check_type función privada que verifica que el tipo de dato del
            elemento que se quiere agregar al DoubleLinked sea del mismo tipo
            contenido dentro de los elementos del DoubleLinked.

        Raises:
            TypeError: error si el tipo de dato del elemento que se quiere
                agregar no es el mismo que el tipo de dato de los elementos
                que ya contiene el DoubleLinked.

        Args:
            element (T): elemento que se quiere procesar en DoubleLinked.

        Returns:
            bool: operador que indica si el ADT DoubleLinked es del mismo tipo
                que el elemento que se quiere procesar.
        """
        # TODO check usability of this function
        # if the structure is not empty, check the head element type
        if not self.is_empty():
            # get the type of the head element
            lt_type = type(self.head.get_info())
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for element info: {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """is_empty revisa si el DoubleLinked está vacía.

        Returns:
            bool: operador que indica si la estructura DoubleLinked está vacía.
        """
        # TODO change the method name to "empty" or @property "empty"?
        try:
            return self._size == 0
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """size devuelve el numero de elementos que actualmente contiene el
            DoubleLinked.

        Returns:
            int: tamaño de la estructura DoubleLinked.
        """
        # TODO change the method to @property "size"?
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def add_first(self, element: T) -> None:
        """add_first adiciona un elemento al inicio del SingleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la
                función _handle_error() para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                new_node = DoubleNode(element)

                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """add_last adiciona un elemento al final del SingleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la
                función _handle_error() para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                new_node = DoubleNode(element)

                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """add_element adiciona un elemento en una posición dada del
            SingleLinked.

        Args:
            element (T): elemento que se quiere agregar a la estructura.
            pos (int): índice en la que se quiere agregar el elemento.

        Raises:
            IndexError: error si la posición es inválida.
            IndexError: error si la estructura está vacía.
        """
        # TODO change the method name to "add_elm()"?
        try:
            if not self.is_empty():
                if self._check_type(element):
                    if pos < 0 or pos > self._size:
                        raise IndexError("Position is out of range")
                    # create a new node
                    new_node = DoubleNode(element)

            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)
















# #TODO Mejorar la documentación para especificar el uso del parámetro "key" en listas
# #TODO Eliminar la carga de datos de la función newList
# #FIXME Cambiar el nombre de la funcion para usar snake_case
# def newList(cmpfunction, module,  key, filename, delim):
#     """Crea una lista vacia.

#     Se inicializan los apuntadores a la primera y ultima posicion en None.
#     El tipo de la listase inicializa como SINGLE_LINKED
#     Args:
#         cmpfunction: Función de comparación para los elementos de la lista.
#         Si no se provee una función de comparación, se utilizará la función
#         de comparación por defecto pero se debe suministrar un valor para key

#         key: Identificador que se debe utilizar para la comparación de
#         elementos de la lista

#         filename: Si se provee este valor, se creará una lista a partir de
#         la informacion que se encuentra en el archivo CSV

#         delimiter: Si se provee un archivo para crear la lista, indica el
#         delimitador a usar para separar los campos del archivo CSV

#     Returns:
#         Un diccionario que representa la estructura de datos de una lista
#         encadanada vacia.

#     Raises:

#     """
#     newlist = {'first': None,
#                'last': None,
#                'size': 0,
#                'key': key,
#                'type': 'DOUBLE_LINKED',
#                'datastructure': module
#                }

#     if(cmpfunction is None):
#         newlist['cmpfunction'] = defaultfunction
#     else:
#         newlist['cmpfunction'] = cmpfunction

#     if (filename is not None):
#         input_file = csv.DictReader(open(filename, encoding="utf-8"),
#                                     delimiter=delim)
#         for line in input_file:
#             addLast(newlist, line)
#     return newlist

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos
# #TODO Verificar que el elemento que se esta agregando no sea None
# def addFirst(lst, element):
#     """Agrega un elemento a la lista en la primera posicion.

#     Agrega un elemento en la primera posición de la lista, ajusta el apuntador
#     al primer elemento e incrementa el tamaño de la lista.

#     Args:
#         lst:  La lista don de inserta el elemento
#         element:  El elemento a insertar en la lista

#     Returns:
#         La lista con el nuevo elemento en la primera posición, si el proceso
#         fue exitoso

#     Raises:
#         Exception
#     """
#     try:
#         new_node = Node.newDoubleNode(element)

#         if (lst['size'] == 0):
#             lst['last'] = new_node
#             lst['first'] = new_node
#         else:
#             new_node['next'] = lst['first']
#             lst['first'] = new_node

#         lst['size'] += 1
#         return lst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->addFirst: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos
# #TODO Verificar que el elemento que se esta agregando no sea None
# def addLast(lst, element):
#     """ Agrega un elemento en la última posición de la lista.

#     Se adiciona un elemento en la última posición de la lista y se actualiza
#      el apuntador a la útima posición.
#     Se incrementa el tamaño de la lista en 1
#     Args:
#         lst: La lista en la que se inserta el elemento
#         element: El elemento a insertar

#     Raises:
#         Exception
#     """
#     try:
#         new_node = Node.newDoubleNode(element)

#         if lst['size'] == 0:
#             lst['first'] = new_node
#         else:
#             new_node['prev'] = lst['last']
#             lst['last']['next'] = new_node
#         lst['last'] = new_node
#         lst['size'] += 1
#         return lst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->addLast: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def isEmpty(lst):
#     """ Indica si la lista está vacía
#     Args:
#         lst: La lista a examinar

#     Raises:
#         Exception
#     """
#     try:
#         return lst['size'] == 0
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->isEmpty: ')

# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def size(lst):
#     """ Informa el número de elementos de la lista.
#     Args
#         lst: La lista a examinar

#     Raises:
#         Exception
#     """
#     try:
#         return lst['size']
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->size: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def firstElement(lst):
#     """ Retorna el primer elemento de una lista no vacía.
#      No se elimina el elemento.

#     Args:
#         lst: La lista a examinar

#     Raises:
#         Exception
#     """
#     try:
#         if lst['first'] is not None:
#             return lst['first']['info']
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->fisrtElement: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def lastElement(lst):
#     """ Retorna el último elemento de una  lista no vacia.
#         No se elimina el elemento.

#     Args:
#         lst: La lista a examinar

#     Raises:
#         Exception
#     """
#     try:
#         if lst['last'] is not None:
#             return lst['last']['info']
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->lastElement: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def getElement(lst, pos):
#     """ Retorna el elemento en la posición pos de la lista.

#     Se recorre la lista hasta el elemento pos, el cual  debe ser
#     mayor que cero y menor o igual al tamaño de la lista.
#     Se retorna el elemento en dicha posición sin eleminarlo.
#     La lista no puede ser vacia.

#     Args:
#         lst: La lista a examinar
#         pos: Posición del elemento a retornar

#     Raises:
#         Exception
#     """
#     try:
#         searchpos = 1
#         node = lst['first']
#         while searchpos < pos:
#             searchpos += 1
#             node = node['next']
#         return node['info']
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->getElement: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def deleteElement(lst, pos):
#     """ Elimina el elemento en la posición pos de la lista.

#     Elimina el elemento que se encuentra en la posición pos de la lista.
#     Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
#     Se decrementa en un uno el tamñao de la lista.
#     La lista no puede estar vacia.

#     Args:
#         lst: La lista a retoranr
#         pos: Posición del elemento a eliminar.

#     Raises:
#         Exception
#     """
#     try:
#         if (lst['size'] == 1) and (pos == 1):
#             lst['first'] = None
#             lst['last'] = None

#         node = lst['first']
#         searchpos = 1

#         while searchpos < pos:
#             searchpos += 1
#             node = node['next']
#         prev = node['prev']
#         sig = node['next']

#         if (prev is not None):
#             prev['next'] = sig
#         if (sig is not None):
#             sig['prev'] = prev

#         if(pos == lst['size']):
#             lst['last'] = prev

#         lst['size'] -= 1
#         return lst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->deleteElement: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def removeFirst(lst):
#     """ Remueve el primer elemento de la lista.
#     Elimina y retorna el primer elemento de la lista.
#     El tamaño de la lista se decrementa en uno.  Si la lista
#     es vacía se retorna None.
#     Args:
#         lst: La lista a examinar

#     Raises:
#         Exception
#     """
#     try:
#         if lst['first'] is not None:
#             temp = lst['first']['next']
#             node = lst['first']
#             lst['first'] = temp
#             lst['size'] -= 1
#             if (lst['size'] == 0):
#                 lst['last'] = lst['first']
#             return node['info']
#         else:
#             return None
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->removeFirst: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def removeLast(lst):
#     """ Remueve el último elemento de la lista.

#     Elimina el último elemento de la lista  y lo retorna en caso de existir.
#     El tamaño de la lista se decrementa en 1.
#     Si la lista es vacía  retorna None.

#     Args:
#         lst: La lista a examinar

#     Raises:
#         Exception
#     """
#     try:
#         if lst['size'] > 0:
#             if lst['first'] == lst['last']:
#                 node = lst['first']
#                 lst['last'] = None
#                 lst['first'] = None
#             else:
#                 temp = lst['last']['prev']
#                 node = lst['last']
#                 lst['last'] = temp
#                 if (temp is not None):
#                     lst['last']['next'] = None
#             lst['size'] -= 1
#             return node['info']
#         else:
#             return None
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->remoLast: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos
# #TODO Verificar que el elemento que se esta agregando no sea None
# def insertElement(lst, element, pos):
#     """ Inserta el elemento element en la posición pos de la lista.

#     Inserta el elemento en la posición pos de la lista.
#     La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

#     Args:
#         lst: La lista en la que se va a insertar el elemento
#         element: El elemento a insertar
#         pos: posición en la que se va a insertar el elemento,
#         0 < pos <= size(lst)

#     Raises:
#         Exception
#     """
#     try:
#         new_node = Node.newDoubleNode(element)

#         if (pos == 1):
#             new_node['next'] = lst['first']
#             if (lst['first'] is not None):
#                 lst['first']['prev'] = new_node
#             else:
#                 lst['last'] = new_node
#             lst['first'] = new_node
#         else:
#             searchpos = 1
#             node = lst['first']

#             while searchpos < pos:
#                 searchpos += 1
#                 node = node['next']
#             prev = node['prev']

#             if (prev is not None):
#                 prev['next'] = new_node
#                 new_node['prev'] = prev
#                 new_node['next'] = node

#             if(pos == lst['size']):
#                 lst['last'] = new_node

#         lst['size'] += 1
#         return lst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->insertElement: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def isPresent(lst, element):
#     """ Informa si el elemento element esta presente en la lista.

#     Informa si un elemento está en la lista.  Si esta presente,
#     retorna la posición en la que se encuentra  o cero (0) si no esta presente.
#     Se utiliza la función de comparación utilizada durante la creación
#     de la lista para comparar los elementos.
#     La cual debe retornar cero en caso de que los elementos sean iguales.

#     Args:
#         lst: La lista a examinar
#         element: El elemento a buscar

#     Raises:
#         Exception
#     """
#     try:
#         size = lst['size']
#         if size > 0:
#             node = lst['first']
#             keyexist = False
#             for keypos in range(1, size+1):
#                 if (node is not None):
#                     if (compareElements(lst, element, node['info']) == 0):
#                         keyexist = True
#                         break
#                     node = node['next']
#             if keyexist:
#                 return keypos
#         return 0
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->isPresent: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def changeInfo(lst, pos, newinfo):
#     """ Cambia la informacion contenida en el nodo de la lista que se encuentra
#          en la posicion pos.

#     Args:
#         lst: La lista a examinar
#         pos: la posición de la lista con la información a cambiar
#         newinfo: La nueva información que se debe poner en el nodo de
#         la posición pos

#     Raises:
#         Exception
#     """
#     try:
#         current = lst['first']
#         cont = 1
#         while cont < pos:
#             current = current['next']
#             cont += 1
#         current['info'] = newinfo
#         return lst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->changeInfo: ')

# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def exchange(lst, pos1, pos2):
#     """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

#     Args:
#         lst: La lista a examinar
#         pos1: Posición del primer elemento
#         pos2: Posiocion del segundo elemento

#     Raises:
#         Exception
#     """
#     try:
#         infopos1 = getElement(lst, pos1)
#         infopos2 = getElement(lst, pos2)
#         changeInfo(lst, pos1, infopos2)
#         changeInfo(lst, pos2, infopos1)
#         return lst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->exchange: ')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def subList(lst, pos, numelem):
#     """ Retorna una sublista de la lista lst.

#     Se retorna una lista que contiene los elementos a partir de la
#     posicion pos,con una longitud de numelem elementos.
#     Se crea una copia de dichos elementos y se retorna una lista nueva.

#     Args:
#         lst: La lista a examinar
#         pos: Posición a partir de la que se desea obtener la sublista
#         numelem: Numero de elementos a copiar en la sublista

#     Raises:
#         Exception
#     """
#     try:
#         sublst = {'first': None,
#                   'last': None,
#                   'size': 0,
#                   'type': 'DOUBLE_LINKED',
#                   'key': lst['key'],
#                   'datastructure': lst['datastructure'],
#                   'cmpfunction': lst['cmpfunction']}
#         cont = 1
#         loc = pos
#         while cont <= numelem:
#             elem = getElement(lst, loc)
#             addLast(sublst, elem)
#             loc += 1
#             cont += 1
#         return sublst
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->subList: ')

# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def iterator(lst):
#     """ Retorna un iterador para la lista.
#     Args:
#         lst: La lista a iterar

#     Raises:
#         Exception
#     """
#     try:
#         if(lst is not None):
#             current = lst['first']
#             while current is not None:
#                 yield current['info']
#                 current = current['next']
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->Iterator')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #TODO Implementar manejo más detallado de excepciones con mensajes más especificos

# def compareElements(lst, element, info):
#     """ Compara dos elementos

#     Se utiliza la función de comparación por defecto si key es None
#     o la función provista por el usuario en caso contrario
#     Args:
#         lst: La lista con los elementos
#         element:  El elemento que se esta buscando en la lista
#         info: El elemento de la lista que se está analizando

#     Returns:  0 si los elementos son iguales

#     Raises:
#         Exception
#     """
#     try:
#         if(lst['key'] is not None):
#             return lst['cmpfunction'](element[lst['key']], info[lst['key']])
#         else:
#             return lst['cmpfunction'](element, info)
#     except Exception as exp:
#         error.reraise(exp, 'doublelinkedlist->compareElements')

# #FIXME Cambiar el nombre de la funcion para usar snake_case
# #FIXME Cambiar el nombre de la funcion para que referencie mejor a una compare function

# def defaultfunction(id1, id2):
#     if id1 > id2:
#         return 1
#     elif id1 < id2:
#         return -1
#     return 0
