:py:mod:`DISClib.Utils.error`
=============================

.. py:module:: DISClib.Utils.error

.. autoapi-nested-parse::

   Módulo para manejar errores genéricos en los ADTs y todo *DISCLib*.

   *IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

       #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
       #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.Utils.error.error_handler
   DISClib.Utils.error.init_type_checker



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.Utils.error.TYPE_ERR_MSG


.. py:data:: TYPE_ERR_MSG
   :type: str
   :value: 'Invalid data type'

   Contiene el mensaje de error para tipo de dato inválido.

.. py:function:: error_handler(context: str, func_name: str, err: Exception) -> None

   *error_handler()* recibe el contexto, nombre de la función y la excepción para lanzar una excepción con el mensaje de error y el traceback.

   :param context: nombre del contexto donde ocurrió el error.
   :type context: str
   :param func_name: nombre de la función donde ocurrió el error.
   :type func_name: str
   :param err: excepción lanzada.
   :type err: Exception

   :raises type: excepción con el mensaje de error y el traceback.


.. py:function:: init_type_checker(context: str, func_name: str, info: DISClib.Utils.default.T) -> None

   *init_type_checker()* recibe el contexto, nombre de la función y la info
   para verificar su tipo después de la inicialización de la clase.

   :param context: nombre del contexto donde ocurrió el error.
   :type context: str
   :param func_name: nombre de la función donde ocurrió el error.
   :type func_name: str
   :param info: tipo de dato de la información a verificar.
   :type info: T

   :raises TypeError: excepción con el mensaje de error de tipo de dato.


