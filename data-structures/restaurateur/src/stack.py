class Stack:
    """
    A class representing a stack data structure, which follows the Last-In-First-Out (LIFO) principle.
    This implementation uses a list as the underlying data structure and provides the following methods:

    - push(item): adds a new item to the top of the stack.
    - pop(): removes and returns the item at the top of the stack.
    - is_empty(): returns True if the stack is empty, False otherwise.
    - size(): returns the number of items currently in the stack.
    """

    def __init__(self):
        # Create an empty list to store the elements of the stack.
        self.stack = []

    def push(self, item):
        # Adds a new item to the top of the stack.
        self.stack.append(item)

    def pop(self):
        # Removes and returns the item at the top of the stack.
        return self.stack.pop()

    def is_empty(self):
        # Returns True if the stack is empty, False otherwise.
        return len(self.stack) == 0

    def size(self):
        # returns the number of items currently in the stack.
        return len(self.stack)
