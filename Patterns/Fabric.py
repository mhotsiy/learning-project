from abc import ABCMeta, abstractstaticmethod


class IChair(metaclass=ABCMeta):

    @staticmethod
    def get_dimentions():
        """Chair interface """


class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimentions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}


class SmallChair(IChair):

    def __init__(self):
        self.height = 10
        self.width = 10
        self.depth = 10

    def get_dimentions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}


class ChairFactory:

    @staticmethod
    def get_chair(chair_type):
        try:
            if chair_type == 'big chair':
                return BigChair()
            elif chair_type == 'small chair':
                return SmallChair()
            raise AssertionError('Chair not found')
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    small_chair = ChairFactory.get_chair('small chair')
    big_chair = ChairFactory.get_chair('big chair')

    print(small_chair.get_dimentions())
    print(big_chair.get_dimentions())