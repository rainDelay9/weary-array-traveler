from collections import deque


class Stack(deque):
    def push(self, item):
        self.append(item)
