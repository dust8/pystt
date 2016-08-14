import unittest
from ..utils import escape_string, unescape_string


class TestEscape(unittest.TestCase):

    def test_forward_slash(self):
        self.assertEqual('key@S', escape_string('key/'))

    def test_at(self):
        self.assertEqual('key@A', escape_string('key@'))


class TestUnescape(unittest.TestCase):

    def test_forward_slash(self):
        self.assertEqual('key/', unescape_string('key@S'))

    def test_at(self):
        self.assertEqual('key@', unescape_string('key@A'))


if __name__ == '__main__':
    unittest.main()
