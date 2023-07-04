class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
                """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле """
                self.data = data
                self.next_node = next_node



class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack = []

    def __str__(self):
        return f'{self.stack}'

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        self.stack.append(data)
        return self.stack

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def top(self):
        """
                Метод для возвращения верхнего элемента с вершины стека

                :return: данные верхенго(последнего добавленного) элемента
                """
        return self.stack[-1]

