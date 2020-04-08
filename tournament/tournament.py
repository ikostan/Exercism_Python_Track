from team import Team


def tally(rows: list) -> list:
    head = "Team                           | MP |  W |  D |  L |  P"
    return [str(team) for team in ([head] + sorted(data_processor(rows).values()))]


def data_processor(rows: list) -> dict:
    # Process initial data by row
    teams = dict()
    for row in rows:
        team_0, team_1, result = row.split(';')
        add_team(teams, team_0, result, 0)
        add_team(teams, team_1, result, 1)

    return teams


def add_team(teams: dict, team: str, result: str, index: int) -> None:

    result = define_result(result, index)

    if team in teams:
        teams[team].update_team_score(result)
    else:
        teams[team] = Team(team)
        teams[team].update_team_score(result)


def define_result(result: str, index: int) -> str:
    """
    Rather than having the Team decode this, what if we just told it
    whether it had a win, loss, or draw? Then it wouldn't matter how
    we came to know this, we would just have to inform the team.
    The less that the Team knows about how we determine the match results,
    the less likely it will be that the Team will need to be modified if
    we modify how we represent match results.
    :param result: Game Outcome
    :param index: Team Index
    :return:
    """
    # remove spaces and convert chars to lower case
    result = result.strip().lower()

    possible_results = ('win', 'loss', 'draw')

    if result not in possible_results:
        raise ValueError("ERROR: this is invalid game outcome: {}".format(result))

    if result == 'win' and index == 0:
        return possible_results[0]
    elif result == 'win' and index == 1:
        return possible_results[1]
    elif result == 'loss' and index == 0:
        return possible_results[1]
    elif result == 'loss' and index == 1:
        return possible_results[0]
    else:
        return possible_results[2]
