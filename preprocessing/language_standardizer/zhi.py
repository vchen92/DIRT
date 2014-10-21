import jieba


def standardize_line(line):
    words = jieba.cut(line)
    # Remove punctiation?
    return ' '.jin(words)