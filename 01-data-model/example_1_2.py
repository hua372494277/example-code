from math import hypot

class Vector:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)


    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # only support: right multiple(vector * scalar)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def zero_vector(v0):
    if v0:
        print('Not Zero vector')
    else:
        print('Zero vector')

if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)
    v3 = v1 + v2
    print(v3)
    v4 = v1 * 8
    print(v4)

    v5 = 5 * v2
    print(v5)

    v0 = Vector(0, 0)
    print("v0")
    zero_vector(v0)
    print("v1")
    zero_vector(v1)







