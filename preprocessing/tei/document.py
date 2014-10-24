from lxml import etree

TAG_HEADER = 'teiHeader'
TAG_FILE_DESC = 'fileDesc'
TAG_TITLE_STATEMENT = 'titleStmt'
TAG_TITLE = 'title'
TAG_PRINCIPAL = 'principal'
TAG_EDITION_STATEMENT = 'editionStmt'
TAG_PUB_STATEMENT = 'publicationStmt'
TAG_DATE = 'date'
TAG_DISTRIBUTOR = 'distributor'
TAG_LICENSE = 'availability'
TAG_TEXT = 'text'
TAG_FRONT = 'front'
TAG_BODY = 'body'


class TEIDocument(object):

    query_template = '//{namespace}{tag}'
    no_tag_error_template = 'Could not find <{tag}>'

    def __init__(self, file_name):
        """
        :param file_naem: file name
        """
        self.file_name = file_name
        self.namespace = ''
        self.tree = None

    def get_data(self):
        """
        Get document meta/data
        :return: dictionary of data
        """
        parser = etree.XMLParser(remove_blank_text=True)
        self.tree = etree.parse(self.file_name, parser=parser)
        root = self.tree.getroot()
        root_tag = root.tag
        ns_index = root_tag.rfind('}') + 1

        self.namespace = root_tag[:ns_index]
        raw_body = self.get_element_text(TAG_BODY)
        stripped_body = ' '.join(raw_body.split())
        return {'title': self.get_element_text(TAG_TITLE),
                'edition': self.get_element_text(TAG_EDITION_STATEMENT),
                'date': self.get_element_text(TAG_DATE),
                'availability': self.get_element_text(TAG_LICENSE),
                'body': stripped_body,
                }

    def get_element_text(self, tag):
        """
        Get text from element in document
        :param tag: name of tag
        :return: text within tag
        """
        element = self.get_element(tag)
        if element is not None:
            return element.xpath('string()')
        else:
            return self.no_tag_error_template.format(tag=tag)

    def get_element(self, tag):
        """
        Get a single element from the xml document
        :param tag: tag of the element in the document
        :return: element node
        """
        query = self.get_tag_query(tag)
        return self.tree.find(query)

    def get_tag_query(self, tag):
        """
        Get xpath query for tag
        """
        return self.query_template.format(namespace=self.namespace,
                                          tag=tag)
