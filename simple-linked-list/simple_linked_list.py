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
        self.__values = list()
        for val in values:
            self.__values.append(Node(val))
            if len(self.__values) > 1:
                self.__values[-1].next_node = self.__values[-2]

        self.max = len(self.__values)

    def __len__(self):
        return len(self.__values)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.__values[-1].value()
            del self.__values[-1]
            self.n += 1
            return result
        else:
            raise StopIteration

    def head(self):
        if len(self.__values) == 0:
            raise EmptyListException("ERROR: the list is empty")
        return self.__values[-1]

    def push(self, value):
        self.__values.append(Node(value=value))
        if len(self.__values) > 1:
            self.__values[-1].next_node = self.__values[-2]
        self.max = len(self.__values)

    def pop(self):
        if len(self.__values) == 0:
            raise EmptyListException("ERROR: the list is empty")
        val = self.__values[-1]
        del self.__values[-1]
        self.max = len(self.__values)
        return val.value()

    def reversed(self):
        if len(self.__values) == 0:
            return LinkedList([])
        elif len(self.__values) == 1:
            return LinkedList([self.__values[0].value()])
        else:
            values: list = list()
            for node in self.__values:
                values.append(node.value())
            values.reverse()
            return LinkedList(values=values)

    def __repr__(self):
        nodes = list()
        for val in self.__values:
            nodes.append(val.value())
        return ''.join(nodes)


class EmptyListException(Exception):
    pass
