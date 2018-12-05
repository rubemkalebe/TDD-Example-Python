import unittest

from src.stack import Stack


class StackTest(unittest.TestCase):
    def test_empty_stack(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertEqual(0, s.size())


if __name__ == '__main__':
    unittest.main()