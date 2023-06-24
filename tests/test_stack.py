"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

import pytest

from src.stack import Node, Stack


# s = Stack()

class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push('data1')
        self.assertEqual(s.push('data3'), ['data1', 'data3'])

    def test_push2(self):
        with self.assertRaises(TypeError):
            s = Stack()
            s.push('data1')
            s.push('data2')
            s.push('data3')
            self.assertIn('data3', s)



    def test_pop(self):
        s = Stack()
        # s.pop()
        s.push('data1')
        s.push('data2')
        s.push('data3')
        self.assertEqual(s.pop(), 'data3')

    def test_pop2(self):
        s = Stack()
        # s.pop()
        self.assertEqual(s.pop(), None)







if __name__ == '__main__':
    unittest.main()

    # with self.assertRaises(ZeroDivisionError):
    #     calc.divide(10, 0)