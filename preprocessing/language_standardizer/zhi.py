"""
Module for standarizing Chinese text
"""

import jieba


def standardize_line(line):
    """
    Standardize a line of Chinese text
    :param line: unicode string of Chinese
    :return: standardize form of input line
    """
    words = segment_words(line)
    # Remove punctuation?
    return ' '.join(words)


def segment_words(unsegmented):
    """
    Segment input text into words
    :param unsegmented: raw input text, words unseparated by spaces
    :return: generator of words
    """
    words = jieba.cut(unsegmented)
    return words