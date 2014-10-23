from lxml import etree

import document


class TEIReader(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        """
        Read TEI xml document into a more useful form
        :return: dictionary of document data
        """
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(self.file_name, parser=parser)
        root = tree.getroot()
        root_tag = root.tag
        ns_index = root_tag.rfind('}') + 1
        namespace = root_tag[:ns_index]

        doc = document.TEIDocument(tree, namespace)
        data_dict = doc.get_data()
        # TODO: return custom object rather than dict
        return data_dict

