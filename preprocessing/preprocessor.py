import codecs
from os import path


from preprocessing.language_standardizer import eng

PREPROCESS_SUFFIX = '_PRE'


class Preprocessor(object):
    """
    Preprocessor
    """
    def __init__(self, file_name, input_dir, output_dir, standardizer=eng):
        """
        Parameters:
            file_name - name of input file
        """
        self.standardizer = standardizer
        self.input_dir = input_dir
        self.file_name = file_name
        self.output_dir = output_dir

    def process(self):
        output_name = self.file_name + PREPROCESS_SUFFIX
        in_file = path.join(self.input_dir, self.file_name)
        out_file = path.join(self.output_dir, output_name)
        with codecs.open(in_file, encoding='UTF-8') as f:
            with codecs.open(out_file, mode='w+', encoding='UTF-8') as o:
                for line in f:
                    processed_line = self.standardizer.standardize_line(line)
                    o.write(processed_line)
