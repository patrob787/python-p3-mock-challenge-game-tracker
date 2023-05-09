class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        self._game_played_count = {}

        self.all.append(self)

    def __repr__(self):
        return f"""
            Player: {self.username}
        """
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be a string and between 2 and 25 characters")
        
    def results(self, new_result=None):
        from classes.result import Result
        
        if type(new_result) == Result:
            self._results.append(new_result)
        
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        
        if type(new_game) == Game:
            if new_game not in self._games_played:
                self._games_played.append(new_game)
                self._game_played_count[new_game] = 1
            else:
                self._game_played_count[new_game] += 1

        return self._games_played
    
    def played_game(self, game):
        if game in self._games_played:
            return True
        else:
            return False
    
    def num_times_played(self, game):
        if game in self._games_played:
            return self._game_played_count[game]
        else:
            return 0
    
    @classmethod
    def highest_scored(cls, game):
        from classes.game import Game
        
        scores_list = []

        if type(game) == Game:
            for player in Player.all:
                scores_list.append(game.average_score(player))
        else:
            raise Exception("game type not valid")
        
        high_score = max(scores_list)
        
        for player in Player.all:
            if game.average_score(player) == high_score:
               return player
        
