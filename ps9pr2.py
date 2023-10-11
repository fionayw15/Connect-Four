#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    
    def __init__(self, checker):
        """ constructs a new Player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object
        """
        player = 'Player' + ' ' + str(self.checker)
        return player
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the
            Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        elif self.checker == 'O':
            return 'X'
        
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the column
            where the player wants to make the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            for i in range(b.width):
                if col == i:
                    return col
            print('Try again!')
            print()
            # if valid column index, return that integer
            # else, print 'Try again!' and keep looping
