HEAD = "Team                           | MP |  W |  D |  L |  P"


class Team:
    possible_results = ('loss', 'win', 'draw')

    def __init__(self, name: str):
        self.__name = name  # Team Name
        self.__MP = 0  # Matches Played
        self.__W = 0  # Matches Won
        self.__D = 0  # Matches Drawn (Tied)
        self.__L = 0  # Matches Lost
        self.__P = 0  # Points

    def update_team_score(self, index: int, result: str) -> None:
        """
        The result of the match refers to the first team listed.
        :param result:
        :param index:
        :return:
        """

        self.__MP += 1

        if result == 'loss' and index == 1:
            self.__W += 1

        if result == 'loss' and index == 0:
            self.__L += 1

        if result == 'win' and index == 1:
            self.__L += 1

        if result == 'win' and index == 0:
            self.__W += 1

        if result == 'draw':
            self.__D += 1

        if result not in self.possible_results:
            raise ValueError("ERROR: this is invalid game outcome: {}".format(result))

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
        A win earns a team 3 points.
        A draw earns 1.
        A loss earns 0.
        :return:
        """
        return (self.__W * 3) + self.__D


def tally(rows: list) -> list:
    teams = data_processor(rows)
    results = sort_by_name(teams)
    results = sort_by_points(results)

    return [str(team) for team in ([HEAD] + results)]


def data_processor(rows: list) -> dict:
    # Process initial data by row
    teams = dict()
    for row in rows:
        team_0, team_1, result = row.split(';')
        add_team(teams, team_0, result, 0)
        add_team(teams, team_1, result, 1)

    return teams


def add_team(teams: dict, team: str, result: str, index: int) -> None:
    if team in teams:
        teams[team].update_team_score(index, result)
    else:
        teams[team] = Team(team)
        teams[team].update_team_score(index, result)


def sort_by_name(teams: dict) -> list:
    # Sort by name
    results = list()
    for team in sorted(teams):
        results.append(teams[team])
    return results


def sort_by_points(results: list) -> list:
    # Sort by total points
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i, result in enumerate(results):
            if i + 1 < len(results):
                if result.points() < results[i + 1].points():
                    is_sorted = False
                    results[i], results[i + 1] = results[i + 1], results[i]
    return results
