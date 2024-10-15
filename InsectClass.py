import random

class Insect:
    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.name = n
        self.flight = 0

    def calc_flight(self):
        self.flight = random.randint(1,10)

    def get_name(self):
        return self.name

    def get_flight(self):
        return self.flight