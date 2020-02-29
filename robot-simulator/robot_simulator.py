# Globals for the directions
# Change the values as you see fit
EAST = ('x', '+')
NORTH = ('y', '+')
WEST = ('x', '-')
SOUTH = ('y', '-')


class Robot:
    """
    A robot simulator.

    A robot factory's test facility needs a program to verify robot movements.

    Robots are placed on a hypothetical infinite grid, facing a particular
    direction (north, east, south, or west) at a set of {x,y} coordinates,
    e.g., {3,8}, with coordinates increasing to the north and east.
    """

    __valid_directions = (EAST, NORTH, WEST, SOUTH)

    def __init__(self, direction=NORTH, x=0, y=0):

        self.__set_direction(direction)
        self.__set_coordinates(x, y)

    def __set_coordinates(self, x: int, y: int) -> None:
        """
        Set initial x and y coordinates.
        Includes data type check.
        :param x:
        :param y:
        :return:
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Invalid coordinates: x={}, y={}".format(x, y))
        self.__coordinates = {
            'x': x,
            'y': y
        }
        return None

    def __set_direction(self, direction) -> None:
        """
        Set initial direction.
        Includes data type check.
        :param direction:
        :return:
        """
        if direction not in self.__valid_directions:
            raise ValueError("Invalid direction: {}".format(direction))
        self.__direction = direction
        return None

    @property
    def direction(self) -> tuple:
        """
        Returns current direction as a tuple.
        The direction represented by:
         EAST -> x+
         WEST -> x-
         NORTH -> y+
         SOUTH -> y-
        :return:
        """
        return self.__direction

    @property
    def coordinates(self) -> tuple:
        """
        Returns X, Y coordinates a s a tuple
        :return:
        """
        return self.__coordinates['x'], \
               self.__coordinates['y']

    def move(self, movement: str) -> None:
        """
        Turn left or right or advance.

        The robots have three possible movements:
            turn right
            turn left
            advance

        The letter-string "RAALAL" means:
            Turn right
            Advance twice
            Turn left
            Advance once
            Turn left yet again

        :param movement:
        :return:
        """
        for m in movement.upper():
            # Movement check
            if m not in "LRA":
                raise ValueError("Invalid movement: {}".format(m))

            # Turn RIGHT
            if m == 'R':
                if self.direction == EAST:
                    self.__direction = SOUTH
                elif self.direction == SOUTH:
                    self.__direction = WEST
                elif self.direction == WEST:
                    self.__direction = NORTH
                else:
                    self.__direction = EAST

            # Turn LEFT
            if m == 'L':
                if self.direction == EAST:
                    self.__direction = NORTH
                elif self.direction == NORTH:
                    self.__direction = WEST
                elif self.direction == WEST:
                    self.__direction = SOUTH
                else:
                    self.__direction = EAST

            # Advance
            if m == 'A':
                self.__coordinates[self.direction[0]] = eval("{}{}1".format(self.__coordinates[self.direction[0]],
                                                                            self.direction[1]))

        return None
