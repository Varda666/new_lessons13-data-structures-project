class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        """ Конструктор класса Node"""
        self.data = data
        self.next_node = None


class LinkedList(Node):
    """Класс для односвязного списка"""
    def __init__(self):
        """Конструктор класса односвязного списка"""
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        n = self.head
        while n.next_node is not None:
            n = n.next_node
        n.next_node = new_node


    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        data_list = []
        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, id):
        for item in LinkedList.to_list(self):
            try:
                if id == item['id']:
                    return item
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')


