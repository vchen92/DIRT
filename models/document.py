

class Document(object):
    """
    Class for representing a document in memory
    """

    def __init__(self, file_name, body, metadata=None):
        self.file_name = file_name
        self.body = body
        self.metadata = metadata
