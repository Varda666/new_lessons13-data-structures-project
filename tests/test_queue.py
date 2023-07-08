"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
        def test_dequeue(self):
            q = Queue()
            q.enqueue('first')
            q.enqueue('second')
            q.dequeue()
            self.assertEqual(q.__str__(), "['second']\n")

        def test__str__(self):
            q = Queue()
            q.enqueue('first')
            q.enqueue('second')
            q.enqueue('third')
            self.assertEqual(q.__str__(), "['first', 'second', 'third']\n")

