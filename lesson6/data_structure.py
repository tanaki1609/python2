# types - int, str, bool ....
# structures - list, dict, set
# stack, deque, queue
from collections import deque
class Queue:
    # First In First Out
    arr = []

    def add(self, num):
        x = [num]
        self.arr = x + self.arr

    def pop(self):
        return self.arr.pop()


queue = Queue()
queue.add(1)
queue.add(2)
print(queue.pop())
print(queue.pop())
