from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue= self.queue
        queue.append(t)
        start= t-3000

        while start>queue[0] and queue:
            queue.popleft()

        return len(queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)