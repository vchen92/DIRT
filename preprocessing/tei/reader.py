from lxml import etree

import tei_document


class TEIReader(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(self.file_name, parser=parser)
        root = tree.getroot()
        root_tag = root.tag
        ns_index = root_tag.rfind('}') + 1
        namespace = root_tag[:ns_index]

        doc = tei_document.TEIDocument(tree, namespace)
        metadata = doc.get_metadata()
        return metadata

