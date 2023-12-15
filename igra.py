from random import *


class World:
    def __init__(self):
        self.size = 400
        self.stenki = []
        self.pers = []


class Pers:
    def __init__(self, world):
        self.x = None
        self.y = None
        self.status = True
        self.world = world
        self.speed = 1
        self.napravlenie = 'verh'
        self.ottalknulsa = 0

    def hodit(self):
        print(self.world.stenki)
        if self.napravlenie == 'verh':
            self.y = self.y - self.speed
            if self.stolknovenie():
                if self.world.stenki[0].napravlenie == self.napravlenie:
                    self.napravlenie = 'vniz'
                    self.ottalknulsa += 1
                else:
                    self.status = False
        if self.napravlenie == 'vniz':
            self.y = self.y + self.speed
            if self.stolknovenie():
                if self.world.stenki[0].napravlenie == self.napravlenie:
                    self.napravlenie = 'verh'
                    self.ottalknulsa += 1
                else:
                    self.status = False
        if self.napravlenie == 'vlevo':
            self.x = self.x - self.speed
            if self.stolknovenie():
                if self.world.stenki[0].napravlenie == self.napravlenie:
                    self.napravlenie = 'vpravo'
                    self.ottalknulsa += 1
                else:
                    self.status = False
        if self.napravlenie == 'vpravo':
            self.x = self.x + self.speed
            if self.stolknovenie():
                if self.world.stenki[0].napravlenie == self.napravlenie:
                    self.napravlenie = 'vlevo'
                    self.ottalknulsa += 1
                else:
                    self.status = False

    def stolknovenie(self):
        if 3 < self.y < 400 - 3 and 3 < self.x < 400 - 3:
            return False
        else:
            return True


class Stenki:

    def __init__(self):
        self.world = World
        self.napravlenie = 'verh'
        self.napravlenia = ["verh", 'niz', 'pravo', 'levo']
        self.time = 50
        self.time_now = 0

    def update_stenka(self):
        self.time_now += 1
        if self.time_now >= self.time:
            self.napravlenie = choice(self.napravlenia)
            self.time_now = 0
