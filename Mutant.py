from globals import *

class Mutant:
    def __init__(self, id=None, operator=None, equivalence=None, program=None, difference=None):
        # Each of these represent the values of the dataset
        self.id = id
        self.operator = operator if operator is not None else []
        self.equivalence = equivalence
        self.program = program
        self.difference = difference

    def get_mutated_code(self):
        return 