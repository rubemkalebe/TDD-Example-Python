import unittest

from src.empty_stack_exception import EmptyStackException
from src.stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.s.is_empty())
        self.assertEqual(0, self.s.size())

    def test_push(self):
        self.s.push("first")
        self.assertFalse(self.s.is_empty())
        self.assertEqual(1, self.s.size())
        self.assertTrue("first", self.s.top())

    def test_push_and_pop(self):
        self.s.push("first")
        self.s.push("second")
        self.assertEqual(2, self.s.size())
        self.assertTrue("second", self.s.top())

        removed = self.s.pop()
        self.assertEqual(1, self.s.size())
        self.assertEqual("first", self.s.top())
        self.assertEqual("second", removed)

    def test_pop_empty_stack(self):
        self.assertRaises(EmptyStackException, self.s.pop)


if __name__ == '__main__':
    unittest.main()