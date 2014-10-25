import codecs

import cjson

from preprocessing.tei.reader import TEIReader


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
        self.metadata = metadata if metadata else {}

    def clone(self):
        return Document(self.file_name,
                        self.body,
                        self.metadata)

    def to_json(self):
        d = {'file_name': self.file_name,
             'body': self.body,
             'metadata': self.metadata}
        return cjson.encode(d)

    def __eq__(self, other):
        if self.file_name != other.file_name:
            return False
        if self.metadata != other.metadata:
            return False
        if self.body != other.body:
            return False
        return True

    @classmethod
    def from_file(cls, file_name):
        if 'tei' in file_name.lower():
            creator = Document.from_tei
        elif 'json' in file_name.lower():
            creator = Document.from_json
        else:
            creator = Document.from_txt
        return creator(file_name)

    # On the fence about whether or not these belong here
    @classmethod
    def from_txt(cls, file_name):
        with codecs.open(file_name, encoding='UTF-8') as f:
            body = f.read()
        return Document(file_name, body)

    @classmethod
    def from_tei(cls, file_name):
        reader = TEIReader(file_name)
        return reader.read()

    @classmethod
    def from_json(cls, file_name):
        with codecs.open(file_name, encoding='UTF-8') as f:
            raw_json = f.read()
        data = cjson.decode(raw_json)
        return Document(file_name=data['file_name'],
                        body=data['body'],
                        metadata=data['metadata'])