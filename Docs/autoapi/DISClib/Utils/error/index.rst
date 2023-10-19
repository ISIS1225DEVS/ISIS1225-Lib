:py:mod:`DISClib.Utils.error`
=============================

.. py:module:: DISClib.Utils.error

.. autoapi-nested-parse::

   _summary_
   # TODO add summary

   .. attribute:: T

      _description_

      :type: type

   .. attribute:: TYPE_ERR_MSG

      _description_

      :type: str

   .. attribute:: VALID_DATA_TYPE_LT

      _description_

      :type: tuple

   Functions:
       error_handler(context: str, func_name: str, err: Exception) -> None:
           error_handler receives the context, function name and error to raise.
       init_type_checker(context: str, func_name: str, info: T) -> None:
           init_type_checker receives the context, function name and info to check
               its type after class initialization.

   Copyrigth:
       Universidad de los Andes, Bogotá - Colombia, South America
       Facultad de Ingeniería, 2023
       Departamento de Ingeniería de Sistemas y Computación DISC
       Developed by: Data Structures & Algorithms Group - EDA - ISIS-1225



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

   DISClib.Utils.error.T
   DISClib.Utils.error.VALID_DATA_TYPE_LT
   DISClib.Utils.error.TYPE_ERR_MSG


.. py:data:: T

   

.. py:data:: VALID_DATA_TYPE_LT
   :value: ()

   

.. py:data:: TYPE_ERR_MSG
   :value: 'Invalid data type'

   

.. py:function:: error_handler(context: str, func_name: str, err: Exception) -> None

   error_handler receives the context, function name and error to raise.

   :param context: name of the class where the error occurred.
   :type context: str
   :param func_name: name of the function where the error occurred.
   :type func_name: str
   :param err: exception raised.
   :type err: Exception

   :raises type: exception with the error message and traceback.


.. py:function:: init_type_checker(context: str, func_name: str, info: T) -> None

   init_type_checker receives the context, function name and info to check
       its type after class initialization.

   :param context: name of the class where the check is performed.
   :type context: str
   :param func_name: name of the function where the check is performed.
   :type func_name: str
   :param info: info to check its type.
   :type info: T

   :raises TypeError: exception with the type error message.


