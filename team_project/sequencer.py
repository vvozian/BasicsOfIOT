class Sequencer:
    incermenter = 0
    def __init__(self):
        self.incrementer = 0

    def get_next(self):
        self.incrementer += 1
        return self.incrementer