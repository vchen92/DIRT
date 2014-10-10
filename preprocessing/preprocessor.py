import codecs
import importlib


class Preprocessor(object):
    """
    Preprocessor
    """
    def __init__(self, file_name, language='eng'):
        """
        Parameters:
            file_name - name of input file
        """
        self.language_module = 'language_standardizer.{}'.format(language)
        self.standardizer = importlib.import_module(language_module)
        self.file_name = file_name

    def process():
        processed_lines = []
        with codecs.open(self.file_name) as f:
            for line in f:
                processed_line = self.standardizer.standardize_line(l)
                processed_lines.append(processed_line)
        return '\n'.join(processed_lines)
