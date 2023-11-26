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

   DISClib.T
   DISClib.file_path
   DISClib.file_dir
   DISClib.__version__
   DISClib.__author__
   DISClib.__license__


.. py:class:: DynamicImporter(implementation: str, package: str, **kwargs)


   *DynamicImporter* permite importar dinámicamente módulos y clases de módulos según la configuración de un archivo JSON y las especificaciones del usuario.

   :raises ValueError: no se puede importar el módulo especificado.

   :returns: instancia de la clase dinámica.
   :rtype: DynamicImporter

   .. py:attribute:: package
      :type: str
      :value: ''

      Nombre del paquete en el directorio de compilación.

   .. py:attribute:: implementation
      :type: str
      :value: ''

      Nombre del paquete en el directorio dentro del código fuente.

   .. py:attribute:: _module

      Referencia privada al módulo dinámico.

   .. py:attribute:: _class

      Referencia privada a la clase dinámica seleccionada.

   .. py:attribute:: _instance

      Referencia privada a la instancia de la clase dinámica seleccionada.

   .. py:method:: __post_init__()

      *__post_init__()* función post inicialización. Permite cambiar el nombre de la clase dinámica por el nombre de la clase concreta seleccionada por el usuario.



   .. py:method:: __repr__() -> str

      *__repr__* función de representación. Permite representar la clase dinámica como la clase concreta seleccionada por el usuario.

      :returns: representación de la clase concreta seleccionada.
      :rtype: str


   .. py:method:: start()

      *start()* retorna la instancia de la clase concreta seleccionada por el usuario.

      :returns: instancia de la clase concreta seleccionada.
      :rtype: dataclass


   .. py:method:: __class__() -> type
      :classmethod:

      *__class__* retorna el tipo de la clase concreta seleccionada por el usuario.

      :returns: tipo de la clase concreta seleccionada.
      :rtype: type


   .. py:method:: __instancecheck__(instance) -> bool
      :classmethod:

      *__instancecheck__* permite verificar si una instancia es de la clase concreta seleccionada por el usuario.

      :param instance: instancia a verificar.
      :type instance: T

      :returns: True si la instancia es de la clase concreta seleccionada.
      :rtype: bool



.. py:function:: List(dstruct: str = 'ArrayList', **kwargs) -> DISClib.Utils.default.T

   *List()* Función con patrón de diseño 'factory' que retorna una     instancia del ADT List según el tipo de estructura de datos seleccionada por el usuario.

   :param dstruct: Tipo de estructura de datos a instanciar. Por defecto es "ArrayList". Puende ser "ArrayList", "SingleLinked" o "DoubleLinked".
   :type dstruct: str, optional

   :raises ValueError: error si el tipo de estructura de datos seleccionada no es válida.

   :returns: instancia del ADT List que puede ser "ArrayList", "SingleLinked" o "DoubleLinked".
   :rtype: T


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


.. py:data:: T

   Variable nativa de Python para definir un tipo de @dataclass genérico.

.. py:data:: file_path

   

.. py:data:: file_dir

   

.. py:data:: __version__
   :value: '0.0.3'

   

.. py:data:: __author__
   :value: 'ISIS-1225 Devs EDA Team, DISC, Uniandes'

   

.. py:data:: __license__
   :value: 'GNU 3.0'

   

