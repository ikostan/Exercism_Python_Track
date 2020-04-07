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
    if team in teams:
        teams[team].update_team_score(index, result)
    else:
        teams[team] = Team(team)
        teams[team].update_team_score(index, result)
