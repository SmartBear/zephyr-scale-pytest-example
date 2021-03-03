import pytest
import unittest

class TestStringMethods(unittest.TestCase):

    @pytest.mark.test_case_key('DEV-123')
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @pytest.mark.test_case_key('DEV-124')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @pytest.mark.test_case_key('DEV-125')
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

