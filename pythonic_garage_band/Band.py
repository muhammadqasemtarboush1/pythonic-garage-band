from pythonic_garage_band.Musician import Musician
from pythonic_garage_band.Guitarist import Guitarist
from pythonic_garage_band.Bassist import Bassist
from pythonic_garage_band.Drummer import Drummer


class Band(Musician):
    instances = []

    def __init__(self, name, members=[]):
        self.members = members
        self.instances.append(self)
        super(Band, self).__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def play_solos(self):
        output = []
        for member in self.members:
            output.append(member.play_solo())
        return output

    @classmethod
    def to_list(cls):
        output = []
        for current_band in cls.instances:
            output.append(current_band)

        return output
