from pythonic_garage_band.Musician import Musician


class Guitarist(Musician):

    solo = 'face melting guitar solo'
    instrument = 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'