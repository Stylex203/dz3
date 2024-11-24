import unittest
from io import StringIO
from main import *

class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.parser = ConfigParser()

    def test_simple_key_value(self):
        data = ["server: nginx"]
        result = self.parser.parse(data)
        self.assertEqual(result, {"server": "nginx"})

    def test_constant_definition(self):
        data = ["def port := 8080", "port: @{port}"]
        result = self.parser.parse(data)
        self.assertEqual(result, {"port": 8080})

    def test_array(self):
        data = ["def workers := #(2 4 8)", "workers: @{workers}"]
        result = self.parser.parse(data)
        self.assertEqual(result, {"workers": [2, 4, 8]})

    def test_invalid_syntax(self):
        data = ["def port : 8080"]
        with self.assertRaises(SyntaxError):
            self.parser.parse(data)

if __name__ == "__main__":
    unittest.main()
