__author__ = 'Sindbad the Sailor'


class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.coin_number = 0

    def can_add(self, v):
        if self.coin_number + v > self.capacity:
            return False
        return True

    def add(self, v):
        self.coin_number += v
