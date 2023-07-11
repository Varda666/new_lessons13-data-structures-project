"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 2})
        self.assertEqual(ll.__str__(), "{'id': 2} -> None")

    def test_insert_beginning2(self):
        ll = LinkedList()
        ll.insert_beginning(2345)
        self.assertEqual(ll.__str__(), '2345 -> None')

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.__str__(),"{'id': 2} -> {'id': 3} -> None")



