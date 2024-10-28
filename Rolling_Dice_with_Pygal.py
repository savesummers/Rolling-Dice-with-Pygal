from random import randint

class Die():
    '''A class representing a Die.'''
    
    def __init__(self, num_sides=6):
        '''Creates a Die with six sides'''
        self.num_sides = num_sides
    
    def roll(self):
        '''Choose a random number between 1 and 6'''
        return randint(1,self.num_sides)