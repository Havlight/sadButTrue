class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = dict()
        max_len = 0
        first_index = 0
        for i, data in enumerate(s):
            if data not in table:
                table[data] = i
                max_len = max(max_len, len(table))
            else:
                tmp = table[data]
                for j in range(first_index, tmp):
                    table.pop(s[j], None)
                first_index = tmp + 1
        return max_len
