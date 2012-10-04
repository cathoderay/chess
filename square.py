from exception import OutOfBoard


def check_if_is_out(func):
    def decorated(self):
        square = func(self)
        if square.is_out_of_board():
            raise OutOfBoard
        return square
    return decorated


class Square():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tuple = (self.x, self.y)

    def is_out_of_board(self):
        return self.x < 0 or \
               self.x > 7 or \
               self.y < 0 or \
               self.y > 7

    @check_if_is_out
    def up(self):
        return Square(self.x - 1, self.y)

    @check_if_is_out
    def down(self):
        return Square(self.x + 1, self.y) 

    @check_if_is_out
    def left(self):
        return Square(self.x, self.y - 1)

    @check_if_is_out
    def right(self):
        return Square(self.x, self.y + 1)

    @check_if_is_out
    def northeast(self):
        return Square(self.x - 1, self.y + 1)

    @check_if_is_out
    def northwest(self):
        return Square(self.x - 1, self.y - 1)

    @check_if_is_out
    def southeast(self):
        return Square(self.x + 1, self.y + 1)

    @check_if_is_out
    def southwest(self):
        return Square(self.x + 1, self.y - 1)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.x == other.x and \
               self.y == other.y

    def __str__(self):
        return "%s, %s" % (self.x, self.y)
