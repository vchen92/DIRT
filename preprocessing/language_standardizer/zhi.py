import jieba


def standardize_line(line):
    words = jieba.cut(line)
    # Remove punctuation?
    return ' '.join(words)