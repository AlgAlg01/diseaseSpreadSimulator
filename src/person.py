import random

class Person:
    def __init__(self, node):
        self.node = node
        self.isInfected = False
        self.hasBeenInfected=False
        self.infectionDaysLeft = 0
        self.willDieFromInfection = False
        self.isDead = False

    def infect(self, kill_prob, min_days, max_days):
        self.isInfected = True
        self.willDieFromInfection = random.random() < kill_prob
        if self.willDieFromInfection:
            self.infectionDaysLeft = random.randint(1, max_days)
        else:
            self.infectionDaysLeft = random.randint(min_days, max_days)

    def progress_disease(self):
        if self.isInfected:
            self.infectionDaysLeft -= 1
            if self.infectionDaysLeft <= 0:
                if self.willDieFromInfection:
                    self.isDead = True
                else:
                    self.isInfected = False
                    self.hasBeenInfected=True
