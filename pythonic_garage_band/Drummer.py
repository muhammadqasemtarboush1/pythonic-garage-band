from pythonic_garage_band.Musician import Musician


class Drummer(Musician):
    solo = 'rattle boom crash'
    instrument = 'drums'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'



