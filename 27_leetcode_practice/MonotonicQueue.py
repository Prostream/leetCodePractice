from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.q = deque()

    def maxq(self):
        return self.q[0]

    def push(self, n):
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)

