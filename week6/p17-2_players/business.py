class Player():
    def __init__(self,name,wins,losses,ties):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties

    @property
    def games(self):
        return self.wins + self.losses + self.ties