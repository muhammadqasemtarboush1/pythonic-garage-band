class Musician:
    solo = 'N/A'
    instrument = 'N/A'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{type(self).__name__} instance. Name = {self.name}'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def play_solo(self):
        return self.__class__.solo

    def get_instrument(self):
        return self.__class__.instrument
