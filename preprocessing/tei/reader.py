import models.document
import preprocessing.tei.document as tei_document


class TEIReader(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        """
        Read TEI xml document into a more useful form
        :return: dictionary of document data
        """

        doc = tei_document.TEIDocument(self.file_name)
        data_dict = doc.get_data()
        body = data_dict['body']
        del data_dict['body']
        std_doc = models.document.Document(self.file_name, body, data_dict)
        return std_doc
