from pythonic_garage_band.Musician import Musician


class Bassist(Musician):
    solo = 'bom bom buh bom'
    instrument = 'bass'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
