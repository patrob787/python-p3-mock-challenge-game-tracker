class Game:
    def __init__(self, title):
        if len(title) > 0:
            self.title = title
        else:
            raise Exception("Please enter a title")
        self._results = []
        self._players = []

    def __repr__(self):
        return f"""
            title: {self.title}
        """

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise Exception("Title already exists and cannot be changed.")
        else:
            self._title = title
        
    def results(self, new_result=None):
        from classes.result import Result
        
        if type(new_result) == Result:
            self._results.append(new_result)
        
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        
        if type(new_player) == Player and new_player not in self._players:
            self._players.append(new_player)

        return self._players
    
    def average_score(self, player):
        player_results = []
        for result in self._results:
            if result.player == player:
                player_results.append(result.score)
            
        avg_score = (sum(player_results)) / len(player_results)
        return avg_score
        
