
from multiprocessing import Queue

class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node



class Queue:
    """Класс для очереди"""


    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []

    @property
    def head(self):
        return self.queue[0]



    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.queue.append(data)


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента - не понятно какой элемет нужно удалить, последний или любой в очереди?
        """
        if len(self.queue) < 1:
            return None
        removed = self.queue.pop(0)
        return removed

    # def dequeue2(self, element):
    #     """
    #     Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
    #
    #     :return: данные удаленного элемента - не понятно какой элемет нужно удалить, последний или любой в очереди?
    #     """
    #     try:
    #         self.queue.remove(element)
    #         return element
    #     except NameError:
    #         return f'Нет такого элемента в очереди'



    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return f'{self.queue}\n'
