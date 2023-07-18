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

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        self.assertEqual(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_1s'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_2s'})

        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_1s'})


