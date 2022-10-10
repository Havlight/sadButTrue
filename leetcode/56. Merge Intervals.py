class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []

        for item in intervals:
            if ans and ans[-1][1] >= item[0]:
                ans[-1][1] = max(item[1], ans[-1][1])
            else:
                ans += [item]

        return ans
