class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __repr__(self):
        return f"[{self.start}, {self.end}]"

class Solution:
    def insert(self, intervals, new_interval):
        result = []
        i = 0
        n = len(intervals)

        # 1) Add intervals that come before new interval
        while i < n and intervals[i].end < new_interval.start:
            result.append(intervals[i])
            i += 1

        # 2) Merge overlaps
        while i < n and intervals[i].start <= new_interval.end:
            new_interval.start = min(new_interval.start, intervals[i].start)
            new_interval.end = max(new_interval.end, intervals[i].end)
            i += 1

        # Add merged interval
        result.append(new_interval)

        # 3) Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


intervals = [Interval(1,3), Interval(6,9)]
new_interval = Interval(2,5)

sol = Solution()
print(sol.insert(intervals, new_interval))
