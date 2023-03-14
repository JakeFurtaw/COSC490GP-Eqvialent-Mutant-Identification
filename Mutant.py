from globals import *

class Mutant:
    def __init__(self, id='', operator=None, equivalence='', program='', difference=''):
        # Each of these represent the values of the dataset
        self.id = id
        self.operator = operator if operator is not None else []
        self.equivalence = equivalence
        self.program = program
        self.difference = difference
        self.type = ''
    
    def calculate_type(self):
        file_extension = self.program.split(".")[-1] 
        if file_extension == "java":
            self.type = "java"
        elif file_extension == "c":
            self.type = "c"