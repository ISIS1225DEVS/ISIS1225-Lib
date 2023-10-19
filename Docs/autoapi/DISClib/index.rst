:py:mod:`DISClib`
=================

.. py:module:: DISClib


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   ADT/index.rst
   Algorithms/index.rst
   DataStructures/index.rst
   Utils/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.DynamicImporter
   DISClib.Queue
   DISClib.Stack



Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.List
   DISClib.error_handler
   DISClib.init_type_checker



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.file_path
   DISClib.file_dir
   DISClib.__version__
   DISClib.__author__
   DISClib.__license__


.. py:class:: DynamicImporter(implementation: str, package: str, **kwargs)


   Bases: :py:obj:`object`

   .. py:attribute:: package
      :type: str
      :value: ''

      

   .. py:attribute:: implementation
      :type: str
      :value: ''

      

   .. py:attribute:: _module

      

   .. py:attribute:: _class

      

   .. py:attribute:: _instance

      

   .. py:method:: __post_init__()


   .. py:method:: __repr__() -> str

      Return repr(self).


   .. py:method:: __getattr__(name)


   .. py:method:: start()


   .. py:method:: __class__() -> type
      :classmethod:


   .. py:method:: __instancecheck__(instance) -> bool
      :classmethod:



.. py:function:: List(implementation: str = 'ArrayList', **kwargs)


.. py:class:: Queue


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   ArrayList _summary_

   :param Generic: _description_
   :type Generic: _type_


.. py:class:: Stack


   Bases: :py:obj:`Generic`\ [\ :py:obj:`T`\ ]

   ArrayList _summary_

   :param Generic: _description_
   :type Generic: _type_


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


.. py:data:: file_path

   

.. py:data:: file_dir

   

.. py:data:: __version__
   :value: '0.0.3'

   

.. py:data:: __author__
   :value: 'Uniandes, DISC, EDA team'

   

.. py:data:: __license__
   :value: 'GNU 3.0'

   

