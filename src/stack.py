from src.empty_stack_exception import EmptyStackException


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
        if self.is_empty():
            raise EmptyStackException
        element = self.top()
        self.__elements.pop(self.size()-1)
        return element