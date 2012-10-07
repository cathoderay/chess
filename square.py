from functools import wraps


def out(func):
    @wraps(func)
    def decorated(self):
        square = func(self)
        if square.is_out_of_board():
            return None
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

    @out
    def north(self):
        return Square(self.x - 1, self.y)

    @out
    def south(self):
        return Square(self.x + 1, self.y) 

    @out
    def west(self):
        return Square(self.x, self.y - 1)

    @out
    def east(self):
        return Square(self.x, self.y + 1)

    @out
    def northeast(self):
        return Square(self.x - 1, self.y + 1)

    @out
    def northwest(self):
        return Square(self.x - 1, self.y - 1)

    @out
    def southeast(self):
        return Square(self.x + 1, self.y + 1)

    @out
    def southwest(self):
        return Square(self.x + 1, self.y - 1)

    def get_till_out(self, func):
        cur = func()
        l = []
        while cur is not None:
            l.append(cur)
            cur = eval('cur.%s()' % func.func_name)
        return l

    def norths(self):
        return self.get_till_out(self.north)

    def souths(self):
        return self.get_till_out(self.south)

    def wests(self):
        return self.get_till_out(self.west)

    def easts(self):
        return self.get_till_out(self.east)

    def northeasts(self):
        return self.get_till_out(self.northeast)

    def northwests(self):
        return self.get_till_out(self.northwest)

    def southeasts(self):
        return self.get_till_out(self.southeast)

    def southwests(self):
        return self.get_till_out(self.southwest)

    def adjacents(self):
        return filter(lambda square: square,
                       [self.northwest(),
                        self.north(),
                        self.northeast(),
                        self.west(),
                        self.east(),
                        self.southwest(),
                        self.south(),
                        self.southeast()])

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.x == other.x and \
               self.y == other.y

    def __sub__(self, other):
        return Square(self.x - other[0], self.y - other[1])

    def __add__(self, other):
        return Square(self.x + other[0], self.y + other[1])

    def __repr__(self):
        return "Square(%s, %s)" % (self.x, self.y)
