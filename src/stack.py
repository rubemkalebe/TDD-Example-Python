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