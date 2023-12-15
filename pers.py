from random import randint
from math import sqrt


class Unit:
    def __init__(self):
        self.i = None
        self.j = None
        self.team = None  # принадлежн к команде
        self.hp = 100

    def move(self, new_j, new_i):
        shag = sqrt((self.i - new_i)**2 + (self.j - new_j)**2)
        if shag <= 3.5:
            self.i = new_i
            self.j = new_j

    def hit(self, strenth_of_hit):
        pass


    def dead(self):
        pass


class Team1(Unit):
    def __init__(self):
        super().__init__()




class Team2(Unit):
    def __init__(self):
        super().__init__()

