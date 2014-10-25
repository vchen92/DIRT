"""
Module for standarizing Chinese text
"""

import jieba


BLACKLIST = [u' ',
             u'\n']


def standardize(text):
    """
    Standardize a line of Chinese text
    :param text: unicode string of Chinese
    :return: standardize form of input line
    """
    words = segment_words(text)
    # Remove punctuation?
    return ' '.join(words)


def segment_words(unsegmented):
    """
    Segment input text into words, removing blacklisted segments
    :param unsegmented: raw input text, words unseparated by spaces
    :return: generator of words
    """
    words = jieba.cut(unsegmented)
    return (word for word in words if word not in BLACKLIST)