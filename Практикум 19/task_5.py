class Game:
    """
    A class representing a game between two teams.

    Attributes:
        team1 (str): Name of the first team.
        team2 (str): Name of the second team.
        team1_score (int): Score of the first team.
        team2_score (int): Score of the second team.
    """

    def __init__(self, teams: dict):
        """
        Initialize a Game object.

        Args:
            teams (dict): Dictionary with keys 'command1' and 'command2' containing team names.
        """
        self.team1 = teams['command1']
        self.team2 = teams['command2']
        self.team1_score = 0
        self.team2_score = 0

    def ball_thrown(self, team, points: int):
        """
        Add points to the specified team's score.

        Args:
            team (int): Team number (1 or 2).
            points (int): Number of points to add.

        Note:
            Points are added only for teams 1 or 2; other inputs are ignored.
        """
        match team:
            case 1:
                self.team1_score += points
            case 2:
                self.team2_score += points

    def get_score(self):
        """
        Get the current scores of both teams.

        Returns:
            tuple: A tuple (team1_score, team2_score).
        """
        return self.team1_score, self.team2_score

    def get_winner(self):
        """
        Determine the winning team based on the higher score.

        Returns:
            str: The name of the team with the higher score.
        """
        players = {self.team1_score: self.team1,
                   self.team2_score: self.team2}
        return players[max(players.keys())]


game_one = Game({'command1' : 'Юта Джаз', 'command2' : 'Майами Хит'})
game_one.ball_thrown(1, 2)
game_one.ball_thrown(1, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 1)
print(game_one.get_score())
game_one.ball_thrown(2, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 2)
print(game_one.get_score())
print(game_one.get_winner())
