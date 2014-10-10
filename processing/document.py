

class Document(object):
    """
    Class for representing a document in memory
    """

    def __init__(self, file_name, metadata=None):
        self.file_name = file_name
        self.metadata = metadata
