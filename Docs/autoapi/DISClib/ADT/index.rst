:py:mod:`DISClib.ADT`
=====================

.. py:module:: DISClib.ADT


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   dynamic/index.rst
   graph/index.rst
   indexminpq/index.rst
   lists/index.rst
   maps/index.rst
   minpq/index.rst
   orderedmap/index.rst
   queue/index.rst
   stack/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   DISClib.ADT.DynamicImporter



Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.List



Attributes
~~~~~~~~~~

.. autoapisummary::

   DISClib.ADT.file_path
   DISClib.ADT.file_dir


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


.. py:data:: file_path

   

.. py:data:: file_dir

   

