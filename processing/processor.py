import importlib
import codecs
import os

REPORT_NAME = '{}__{}__CMP.json'


class Processor(object):
    """
    Processor
    """
    def __init__(self, alpha_name, beta_name, input_dir, output_dir, comparator_name='simple'):
        comparator_module = 'processing.comparators.{}'.format(comparator_name)
        self.comparator = importlib.import_module(comparator_module)
        self.alpha_name = alpha_name
        self.beta_name = beta_name
        self.input_dir = input_dir
        self.output_dir = output_dir

    def read_file_from_input(self, file_name):
        a_name = os.path.join(self.input_dir, file_name)
        with codecs.open(a_name) as alpha_f:
            alpha = alpha_f.read()
        return alpha

    def process(self):
        alpha = self.read_file_from_input(self.alpha_name)
        beta = self.read_file_from_input(self.beta_name)
        comparator = self.comparator.Comparator(alpha=alpha,
                                                beta=beta)
        out_name = REPORT_NAME.format(self.alpha_name,
                                      self.beta_name)
        compared = comparator.compare()
        str_compared = str(compared)
        uni_compared = str_compared.encode('utf8')
        out_file = os.path.join(self.output_dir, out_name)
        with codecs.open(out_file, 'w+', 'UTF-8') as o:
            o.write(uni_compared)
