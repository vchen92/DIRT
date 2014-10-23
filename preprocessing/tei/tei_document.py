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

    def __init__(self, tree, namespace):
        self.tree = tree
        self.namespace = namespace

    def get_metadata(self):
        return {'title': self.get_element_text(TAG_TITLE),
                'edition': self.get_element_text(TAG_EDITION_STATEMENT),
                'date': self.get_element_text(TAG_DATE),
                'availability': self.get_element_text(TAG_LICENSE),
                'body': self.get_element_text(TAG_BODY),
        }

    def get_element_text(self, tag):
        # TODO: go into p and div to get text
        element = self.get_element(tag)
        if element is not None:
            return element.text
        else:
            return 'No ' + tag

    def get_element(self, tag):
        """

        :param tree:
        :param tag:
        :param namespace:
        :return:
        """
        query = self.get_tag_query(tag)
        return self.tree.find(query)

    def get_tag_query(self, tag):
        return self.query_template.format(namespace=self.namespace,
                                          tag=tag)

    def get_elements(self, tag):
        """
        Return all elements of tag
        :param tree:
        :param tag:
        :param namespace:
        :return:
        """
        query = self.get_tag_query(tag)
        return self.tree.findall(query)
