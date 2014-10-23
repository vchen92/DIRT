from lxml import etree


class TEIDocument(object):

    def __init__(self, tree, namespace):
        self.tree = tree
        self.namespace = namespace

    def get_element(self, tree, tag, namespace):
        """

        :param tree:
        :param tag:
        :param namespace:
        :return:
        """
        query = self.get_tag_query(namespace, tag)
        return tree.find(query)

    def get_tag_query(self, namespace, tag):
        return self.query_template.format(namespace=namespace,
                                          tag=tag)

    def get_elements(self, tree, tag, namespace):
        """
        Return all elements of tag
        :param tree:
        :param tag:
        :param namespace:
        :return:
        """
        query = self.get_tag_query(namespace, tag)
        return tree.findall(query)
