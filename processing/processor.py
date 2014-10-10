import importlib


class Processor(object):
    """
    Processor
    """
    def __init__(self, comparator_name='simple'):
        comparator_module = 'comparators.{}'.format(comparator_name)
        self.comparator = importlib.import_module(comparator_module)

