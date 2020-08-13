class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    """
    A circular buffer, cyclic buffer or ring buffer is a
    data structure that uses a single, fixed-size buffer
    as if it were connected end-to-end.
    """

    # A circular buffer first starts empty
    # and of some predefined length.
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__buffer = None
        self.clear()

    def __is_empty(self):
        for element in self.__buffer:
            if element:
                return False
        return True

    def __empty_cell_available(self):
        for element in self.__buffer:
            if not element:
                return True
        return False

    def read(self):
        """
        Reading empty buffer should fail.
        Read frees up capacity for another write.
        Read position is maintained even across multiple writes.
        :return:
        """

        # If buffer has no elements -> raise error
        if self.__is_empty():
            raise BufferEmptyException("ERROR: the buffer is empty!")

        # Read position is maintained even across multiple writes
        min_i = 0
        for i, element in enumerate(self.__buffer):

            if not self.__buffer[min_i] and element:
                min_i = i

            if element and element < self.__buffer[min_i]:
                min_i = i

        # Read frees up capacity for another write
        result = self.__buffer[min_i]
        self.__buffer[min_i] = []
        return result[0]

    def write(self, data):
        """
        Write operation.
        Exact starting location does not matter in a circular buffer.
        :param data:
        :return:
        """
        # When the buffer is full an error will be raised,
        # alerting the client that further writes are
        # blocked until a slot becomes free.
        if not self.__empty_cell_available():
            raise BufferFullException("ERROR: the buffer has no empty cells!")

        for i, element in enumerate(self.__buffer):
            if not element:
                self.__buffer[i] = [data]
                break

    def overwrite(self, data):
        """
        When the buffer is full, the client can opt to
        overwrite the oldest data with a forced write.
        :param data:
        :return:
        """
        try:
            self.write(data)
        except BufferFullException:
            self.read()
            self.write(data)

    def clear(self):
        """
        Set all buffer elements as "EMPTY"
        :return:
        """
        self.__buffer = [[] for i in range(self.__capacity)]
