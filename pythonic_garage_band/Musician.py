class Musician:
    solo = 'N/A'
    instrument = 'N/A'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def play_solo(self):
        return self.__class__.solo

    def get_instrument(self):
        return self.__class__.instrument
