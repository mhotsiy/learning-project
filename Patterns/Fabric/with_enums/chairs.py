from abc import ABCMeta
from enum import Enum, auto


class IChair(metaclass=ABCMeta):

    @staticmethod
    def get_dimentions():
        """Chair interface """


class Chair(Enum):
    SMALL = auto()
    BIG = auto()

class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimentions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}


class SmallChair(IChair):

    def __init__(self):
        self.height = 40
        self.width = 150
        self.depth = 106

    def get_dimentions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}


class ChairFactory:

    @staticmethod
    def get_chair(chair_type: Chair):
        try:
            if chair_type == Chair.BIG:
                return BigChair()
            elif chair_type == Chair.SMALL:
                return SmallChair()
            raise AssertionError('Chair not found')
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    small = ChairFactory.get_chair(Chair.SMALL)
    print(small.get_dimentions())

    small = ChairFactory.get_chair(Chair.BIG)
    print(small.get_dimentions())

    print(Chair.BIG.value)
    print(Chair.SMALL.value)


