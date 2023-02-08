import bisect


class RecentCounter:
    def __init__(self):
        self.record = []

        # self.record = collections.deque()

    def ping(self, t: int) -> int:
        self.record.append(t)

        return len(self.record) - bisect.bisect_left(self.record, t - 3000)

        # while self.record and self.record[0] < t - 3000:
        #     self.record.popleft()

        # self.record.append(t)

        # return len(self.record)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
