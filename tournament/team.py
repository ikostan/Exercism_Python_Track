class Team:

    def __init__(self, name: str):
        self.__name = name  # Team Name
        self.__MP = 0  # Matches Played
        self.__W = 0  # Matches Won
        self.__D = 0  # Matches Drawn (Tied)
        self.__L = 0  # Matches Lost
        self.__P = 0  # Points

    @property
    def name(self) -> str:
        """
        Returns Team's name
        :return:
        """
        return self.__name

    def update_team_score(self, result: str) -> None:
        """
        The result of the match refers to the first team listed.
        :param result:
        :return:
        """
        self.__MP += 1

        if result == 'win':
            self.__W += 1

        if result == 'loss':
            self.__L += 1

        if result == 'draw':
            self.__D += 1

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.points() == other.points()

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            if self.points() > other.points():
                return True
            elif self.points() == other.points() and self.name < other.name:
                return True

    def __gt__(self, other):
        return not self.__lt__(other)

    def __str__(self):
        """
        Team | MP |  W |  D |  L |  P
        :return:
        """
        return '{:30} |  {} |  {} |  {} |  {} |  {}'.format(self.__name,
                                                            self.__MP,
                                                            self.__W,
                                                            self.__D,
                                                            self.__L,
                                                            self.points())

    def points(self) -> int:
        """
        Returns points earned by Team.
        A win earns a team 3 points.
        A draw earns 1.
        A loss earns 0.
        :return:
        """
        return (self.__W * 3) + self.__D
