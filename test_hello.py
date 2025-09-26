import unittest
from hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        say_hello()

if __name__ == "__main__":
    unittest.main()
