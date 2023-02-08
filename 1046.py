from typing import List


class Solution:
    class PriorityQueue:
        def __init__(self):
            self.queue = []

        def length(self):
            return len(self.queue)

        def isEmpty(self):
            return len(self.queue) == 0

        def insert(self, data):
            self.queue.append(data)

        def delete(self):
            max_val = 0
            for i in range(self.length()):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item

    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = Solution.PriorityQueue()

        for i in stones:
            queue.insert(i)

        while queue.length() > 1:
            y = queue.delete()
            x = queue.delete()

            if x != y:
                queue.insert(y - x)

        if queue.isEmpty():
            return 0
        else:
            return queue.delete()
