class Room(object):
    def __init__(self, length, width):
        self._width = width
        self._length = length

    def area(self):
        return self._length * self._width