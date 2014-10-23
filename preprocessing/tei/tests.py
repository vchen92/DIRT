import codecs
import os
import unittest

import cjson

import reader

TEI_ZHI = 'test_data/zhi_tei.xml'
TEI_ENG = 'test_data/eng_tei.xml'

JSON_ZHI = 'test_data/zhi_parsed.json'
JSON_ENG = 'test_data/eng_parsed.json'


class TEIReaderTest(unittest.TestCase):

    # TODO: move three methods to superclass
    #       they are copied from language prep test
    def _get_test_file_name(self, file_name):
        raw_loc = os.path.realpath(__file__)
        my_dir = os.path.dirname(raw_loc)
        real_file_name = os.path.join(my_dir, file_name)
        return real_file_name

    def _read_file(self, file_name):
        real_file_name = self._get_test_file_name(file_name)
        with codecs.open(real_file_name, encoding='utf-8') as f:
            raw_passage = f.read()
        return raw_passage

    def _read_json_file(self, file_name):
        raw = self._read_file(file_name)
        return cjson.decode(raw, all_unicode=True)

    def _test_parse(self, data_file, parsed_json_file):
        """
        Check that an input file is correctly segmented
        :param data_file: utf8 chinese input file
        :param parsed_json_file: uft8 json file of correct segmentation
        """
        real_data_file = self._get_test_file_name(data_file)
        r = reader.TEIReader(real_data_file)
        output = r.parse()
        desired = self._read_json_file(parsed_json_file)
        self.assertEquals(output, desired)

    def test_me(self):
        self._test_parse(TEI_ZHI, JSON_ZHI)
        self._test_parse(TEI_ENG, JSON_ENG)
