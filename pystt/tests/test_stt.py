import unittest
from collections import OrderedDict
from .. import loads, dumps


class TestDumps(unittest.TestCase):

    def test_list(self):
        self.assertEqual('value1/value2/value3',
                         dumps(['value1', 'value2', 'value3']))

    def test_dict(self):
        self.assertEqual('key1@=value1/key2@=value2/key3@=value3', dumps(
            OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3',
                                                                  'value3')])))


class TestLoads(unittest.TestCase):

    def test_list(self):
        self.assertEqual(['value1', 'value2', 'value3'],
                         loads('value1/value2/value3'))

    def test_dict(self):
        self.assertEqual({'key1': 'value1',
                          'key2': 'value2',
                          'key3': 'value3'},
                         loads('key1@=value1/key2@=value2/key3@=value3'))


if __name__ == '__main__':
    unittest.main()
