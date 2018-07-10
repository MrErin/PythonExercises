from building import Building


class Outhouse(Building):
    """[summary]

    Arguments:
        Building {[type]} -- [description]
    """

    def __init__(self):
        self.dignity = False
        self.toilets = 1
        super().__init__()
