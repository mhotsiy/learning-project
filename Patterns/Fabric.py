from abc import ABCMeta, abstractstaticmethod


class Ichair(metaclass=ABCMeta):

    @staticmethod
    def get_dimentions():
        """Chair interface """


class BigChair(Ichair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimentions(self):
        return {'height': self.height, 'width': self.width, 'depth': self.depth}


class ChairFactory():

    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype == 'bigchair':
                return BigChair()
            raise AssertionError('Chair not found')
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    CHAIR = ChairFactory.get_chair('bigchair')
    print(CHAIR.get_dimentions())