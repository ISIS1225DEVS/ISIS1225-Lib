"""
*test_adt_queue.py* es el módulo que prueba el ADT *Queue* (cola) de *DISClib* basado en una lista doblemente encadenada (DoubleLinked).
"""

# import testing package
import unittest
import pytest

# import the module to test
from DISClib.ADT.queue import Queue

# import the data to test
from Test.Data.test_data import get_list_test_data

# asserting module imports
assert Queue
assert get_list_test_data

class TestQueue(unittest.TestCase):
    """TestQueue _summary_

    Args:
        unittest (_type_): _description_
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Queue* como un *fixture*.
        """
        self.global_params = get_list_test_data()

    def test_new_default_queue(self):
        """*test_default_queue()* prueba la creación de una cola por defecto.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None

    def test_new_custom_queue(self):
        """*test_custom_queue()* prueba la creación de una cola personalizada.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None

    def test_enqueue(self):
        """*test_enqueue()* prueba la adición de elementos a la cola.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None

    def test_dequeue(self):
        """*test_dequeue()* prueba la eliminación de elementos a la cola.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None

    def test_peek(self):
        """*test_peek()* prueba la lectura de elementos a la cola.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None

    def test_is_empty(self):
        """*test_is_empty()* prueba la verificación de si la cola esta vacía.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None

    def test_size(self):
        """*test_size()* prueba la lectura del tamaño de la cola.
        """
        # get the global parameters
        # params = self.global_params

        # create the queue
        queue = Queue()
        assert queue is not None
