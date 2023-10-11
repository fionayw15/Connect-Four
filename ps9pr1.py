#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """ constructs a new Board object
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-' * (self.width * 2 + 1)
        s += '\n'
        for i in range(self.width):
            s += ' ' + str(i % 10)
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        self.checker = checker
        self.col = col
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                row -= 1
                break
        self.slots[row][col] = checker
        

    
    ### add your reset method here ###
    def reset(self):
        """ should reset the Board object on which it is called by setting all
            slots to contain a space character
        """
        for row in range(self.height):
            for col in range(self.width): 
                if self.slots[row][col] != ' ': 
                    self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col on
            the calling Board object. Otherwise, it should return False
        """
        self.col = col
        if col < 0:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
        
    def is_full(self):
        """ returns True if the called Board object is completely full of
            checkers, and returns False otherwise
        """
        for col in range(self.width): 
            if self.can_add_to(col) == True:
                return False
        return True
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing
        """
        row = 0
        while self.slots[row][col] == ' ' and row < self.height:
            row += 1
        self.slots[row][col] = ' '
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
                
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonals that go down win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
                
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonals that go up win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
                
        return False
        
    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O', and returns
            True if there are four consecutive slots containing checker on the
            board. Otherwise, it should return False
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        if self.is_horizontal_win(checker) == True:
            return True
        if self.is_vertical_win(checker) == True:
            return True
        if self.is_down_diagonal_win(checker) == True:
            return True
        if self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
