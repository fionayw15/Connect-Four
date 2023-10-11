#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        inh_repr = super().__repr__()
        return inh_repr + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the
            board, and that returns the index of the column with the maximum
            score. If one or more columns are tied for the maximum score, the
            method should apply the called AIPlayer‘s tiebreaking strategy to
            break the tie
        """
        score_ind = [x for x in range(len(scores)) if scores[x] == max(scores)]
        if self.tiebreak == 'RANDOM':
            return random.choice(score_ind)
        elif self.tiebreak == 'LEFT':
            return score_ind[0]
        elif self.tiebreak == 'RIGHT':
            return score_ind[-1]
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores
            for the columns in b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col]
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if opp_scores[col] == 0:
                    scores[col] = 100
                elif opp_scores[col] == 100:
                    scores[col] = 0
                elif opponent.tiebreak == 0:
                    scores[col] = 50
                b.remove_checker(col)
                    
        return scores
    
    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is inherited
            from Player. Rather than asking the user for the next move, this
            version of next_move should return the called AIPlayer‘s judgment
            of its best possible move
        """
        super().next_move(b)