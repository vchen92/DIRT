"""
Base comparator
"""

class BaseComparator(object):
    """
    Base comparator class
    """
    def __init__(self, alpha, beta, match_length=10, gap_length=3):
        self.alpha = alpha
        self.beta = beta
        self.match_length = match_length
        self.gap_length = gap_length
