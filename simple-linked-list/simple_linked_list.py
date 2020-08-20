class Node:
    def __init__(self, value):
        self.__value = value
        self.next_node = None

    def value(self):
        return self.__value

    def next(self):
        return self.next_node


class LinkedList:
    """
    This variant of linked lists is often used to
    represent sequences or push-down stacks
    (also called a LIFO stack; Last In, First Out).
    """

    def __init__(self, values=[]):
        self.__head = None
        self.__len = 0
        for val in values:
            self.push(val)

    def __len__(self):
        return self.__len

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.pop()
        except EmptyListException:
            raise StopIteration

    def head(self):
        if not self.__head:
            raise EmptyListException('ERROR: the list is empty')
        return self.__head

    def push(self, value):
        node = Node(value=value)
        self.__len += 1
        node.next_node, self.__head = self.__head, node

    def pop(self):
        if self.head():
            self.__len -= 1
            val = self.head().value()
            self.__head = self.head().next()
            return val
        else:
            raise EmptyListException("ERROR: the list is empty")

    def reversed(self):
        return LinkedList(list(self))


class EmptyListException(Exception):
    pass
