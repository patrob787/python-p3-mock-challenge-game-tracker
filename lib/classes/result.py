from classes.player import Player
from classes.game import Game

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        player.results(self)
        player.games_played(self.game)

        game.results(self)
        game.players(self.player)

        self.all.append(self)

    # def __repr__(self):
    #     return f"""
    #         {self.player}
    #         {self.game}
    #         Score: {self.score}
    #     """

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be a number between 1 and 5000")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if type(player) == Player:
            self._player = player
        else:
            raise Exception("Player is not an object")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if type(game) == Game:
            self._game = game
        else:
            raise Exception("Game is not an object")
