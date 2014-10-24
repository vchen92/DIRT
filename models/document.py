

class Document(object):
    """
    Class for representing a document in memory
    """

    def __init__(self, file_name, body, metadata=None):
        """
        :param file_name: name of file document represents
        :param body: textual body of document (unicode)
        :param metadata: dict of metadata
        """
        self.file_name = file_name
        self.body = body
        self.metadata = metadata
