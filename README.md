# TDD-Example-Python

Applying TDD steps on a simple Stack solution for educational purposes.

## Tools
* Python 3
* PyCharm

## Iterations

### Iteration I: Empty stack

**Objective:** validate a newly created stack

**Test**:
```
def test_empty_stack(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertEqual(0, s.size())
```

**Initial code**:
```
class Stack(object):
    def is_empty(self):
        pass
    def size(self):
        pass
```

**Final code**:
```
class Stack(object):
    def is_empty(self):
        return True

    def size(self):
        return 0
```


### Iteration II: Push an element to the stack

**Objective:** allow pushing an element to the stack

**Test**:
```
def test_push(self):
        s = Stack()
        s.push("first")
        self.assertFalse(s.is_empty())
        self.assertEqual(1, s.size())
        self.assertTrue("first", s.top())
```

**Initial code**:
```
class Stack(object):
    def is_empty(self):
        return True

    def size(self):
        return 0

    def push(self, element):
        pass

    def top(self):
        pass
```

**Final code**:
```
class Stack(object):
    def __init__(self):
        self.__element = None
        self.__size = 0

    def is_empty(self):
        return self.__element == None

    def size(self):
        return self.__size

    def push(self, element):
        self.__element = element
        self.__size += 1

    def top(self):
        return self.__element
```


### Iteration III: Push and pop from the stack

**Objective:** allow pushing many elements to the stack

**Test**:
```
def test_push_and_pop(self):
        s = Stack()
        s.push("first")
        s.push("second")
        self.assertEqual(2, s.size())
        self.assertTrue("second", s.top())
        
        removed = s.pop()
        self.assertEqual(1, s.size())
        self.assertEqual("first", s.top())
        self.assertEqual("second", removed)
```

**Initial code**:
```
class Stack(object):
    def __init__(self):
        self.__element = None
        self.__size = 0

    def is_empty(self):
        return self.__element == None

    def size(self):
        return self.__size

    def push(self, element):
        self.__element = element
        self.__size += 1

    def top(self):
        return self.__element

    def pop(self):
        pass
```

**Final code**:
```
class Stack(object):
    def __init__(self):
        self.__elements = []

    def is_empty(self):
        return len(self.__elements) == 0

    def size(self):
        return len(self.__elements)

    def push(self, element):
        self.__elements.append(element)

    def top(self):
        return self.__elements[self.size()-1]

    def pop(self):
        element = self.top()
        self.__elements.pop(self.size()-1)
        return element
```


### Iteration IV: Popping from an empty stack

**Objective:** raising an exception when trying to pop from an empty stack

**Test**:
```
def test_pop_empty_stack(self):
        self.assertRaises(EmptyStackException, self.s.pop)
```

**Immediate code**:
```
def pop(self):
        if self.is_empty():
            raise EmptyStackException
        element = self.top()
        self.__elements.pop(self.size()-1)
        return element
```

**Refactored code**:
```
def top(self):
    if self.is_empty():
        raise EmptyStackException
    return self.__elements[self.size()-1]

def pop(self):
    element = self.top()
    self.__elements.pop(self.size()-1)
    return element
```
