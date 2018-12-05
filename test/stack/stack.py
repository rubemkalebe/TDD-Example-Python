import unittest

from src.stack import Stack


class StackTest(unittest.TestCase):
    def test_empty_stack(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertEqual(0, s.size())

    def test_push(self):
        s = Stack()
        s.push("first")
        self.assertFalse(s.is_empty())
        self.assertEqual(1, s.size())
        self.assertTrue("first", s.top())


if __name__ == '__main__':
    unittest.main()