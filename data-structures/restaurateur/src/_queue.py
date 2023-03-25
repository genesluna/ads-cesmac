from collections import deque


class Queue:
    """
    A class representing a queue data structure, which follows the First-In-First-Out (FIFO) principle.
    This implementation uses a deque as the underlying data structure and provides the following methods:

    - enqueue(item): adds a new item to the back of the queue.
    - dequeue(): removes and returns the item at the front of the queue.
    - is_empty(): returns True if the queue is empty, False otherwise.
    - size(): returns the number of items currently in the queue.
    """

    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
