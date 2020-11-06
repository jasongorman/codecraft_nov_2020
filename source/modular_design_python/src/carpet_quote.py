from math import ceil


class CarpetQuote(object):
    def __init__(self, price_per_sqr_mtr, round_up, room):
        self.room = room
        self.round_up = round_up
        self.price_per_sqr_mtr = price_per_sqr_mtr

    def quote(self):
        area = self.room.area()
        if self.round_up:
            area = ceil(area)
        return area * self.price_per_sqr_mtr

